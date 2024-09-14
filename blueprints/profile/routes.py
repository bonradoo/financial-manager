# blueprints/profile/routes.py

from flask import render_template, request, redirect, url_for, session, flash
from . import profile_bp
import os
import csv
from cryptography.fernet import Fernet, InvalidToken
from werkzeug.security import generate_password_hash
import base64
from currency_utils import get_currency_list
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# Path to the data directory
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
USERS_DIR = os.path.join(DATA_DIR, 'users')

@profile_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('auth_bp.login'))

    username = session['username']
    user_dir = os.path.join(USERS_DIR, username)
    profile_dir = os.path.join(user_dir, 'profile')
    config_file = os.path.join(profile_dir, 'config.json')
    key_file = os.path.join(user_dir, 'encryption_key.key')

    # Load the encryption key
    if not os.path.exists(key_file):
        flash('Encryption key not found. Please contact support.', 'error')
        return redirect(url_for('dashboard_bp.dashboard'))

    with open(key_file, 'rb') as f:
        encryption_key = f.read()

    if request.method == 'POST':
        # Collect profile data from the form
        profile_data = {
            'full_name': request.form.get('full_name', ''),
            'email': request.form.get('email', ''),
            'age': request.form.get('age', ''),
            'default_currency': request.form.get('default_currency', ''),
            'api_key': request.form.get('api_key', ''),
        }

        # Encrypt and save profile data
        os.makedirs(profile_dir, exist_ok=True)
        save_encrypted_profile(config_file, profile_data, encryption_key)
        flash('Profile updated successfully.', 'success')
        return redirect(url_for('profile_bp.profile'))
    else:
        # Load and decrypt profile data
        if os.path.exists(config_file):
            profile_data = load_encrypted_profile(config_file, encryption_key)
            if profile_data is None:
                flash('Failed to decrypt profile data. Please update your profile.', 'error')
                profile_data = {}
        else:
            profile_data = {}

    # Load currency list using the user's API key
    api_key = profile_data.get('api_key')
    currency_list = None
    if api_key:
        currency_list = get_currency_list(api_key)
        if not currency_list:
            flash('Invalid API key or unable to load currency list. Please check your API key.', 'error')

    return render_template('profile/profile.html', profile_data=profile_data, currency_list=currency_list)


def generate_encryption_key(username, password):
    # Generate a key from the password
    salt = username.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    password_key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))

    # Check if an encryption key already exists
    user_dir = os.path.join(USERS_DIR, username)
    key_file = os.path.join(user_dir, 'encryption_key.key')

    if os.path.exists(key_file):
        # Load and decrypt the encryption key
        with open(key_file, 'rb') as f:
            encrypted_key = f.read()
        fernet = Fernet(password_key)
        encryption_key = fernet.decrypt(encrypted_key)
    else:
        # Generate a new encryption key
        encryption_key = Fernet.generate_key()
        # Encrypt and save the encryption key
        fernet = Fernet(password_key)
        encrypted_key = fernet.encrypt(encryption_key)
        with open(key_file, 'wb') as f:
            f.write(encrypted_key)

    return encryption_key


def get_password_hash(username):
    # Retrieve the password hash from login.csv
    LOGIN_FILE = os.path.join(DATA_DIR, 'login.csv')
    try:
        with open(LOGIN_FILE, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['username'] == username:
                    return row['password_hash']
    except FileNotFoundError:
        return None
    return None

def save_encrypted_profile(file_path, data, key):
    fernet = Fernet(key)
    # Convert data to CSV format
    fieldnames = ['full_name', 'email', 'age', 'default_currency']
    csv_data = ','.join([data.get(field, '') for field in fieldnames])
    # Encrypt data
    encrypted_data = fernet.encrypt(csv_data.encode('utf-8'))
    # Save to file
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def load_encrypted_profile(file_path, key):
    fernet = Fernet(key)
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        # Decrypt data
        decrypted_data = fernet.decrypt(encrypted_data).decode('utf-8')
        # Parse CSV data
        fieldnames = ['full_name', 'email', 'age', 'default_currency']
        values = decrypted_data.split(',')
        return dict(zip(fieldnames, values))
    except (InvalidToken, FileNotFoundError):
        return None
