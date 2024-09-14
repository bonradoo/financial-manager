# blueprints/auth/routes.py

from flask import render_template, request, redirect, url_for, session, flash
from . import auth_bp
import os
import csv
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet

# Path to the login.csv file
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
LOGIN_FILE = os.path.join(DATA_DIR, 'login.csv')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'login' in request.form:
            # Handle login form submission
            username = request.form['username']
            password = request.form['password']

            # Check credentials
            if authenticate_user(username, password):
                session['username'] = username
                return redirect(url_for('dashboard_bp.dashboard'))
            else:
                flash('Invalid username or password', 'error')
                return redirect(url_for('auth_bp.login'))

        elif 'register' in request.form:
            # Handle registration form submission
            username = request.form['reg_username']
            password = request.form['reg_password']

            if register_user(username, password):
                flash('Registration successful! You can now log in.', 'success')
                return redirect(url_for('auth_bp.login'))
            else:
                flash('Username already exists.', 'error')
                return redirect(url_for('auth_bp.login'))
    else:
        return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home_bp.index'))

def authenticate_user(username, password):
    try:
        with open(LOGIN_FILE, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['username'] == username:
                    password_hash = row['password_hash']
                    if check_password_hash(password_hash, password):
                        return True
        return False
    except FileNotFoundError:
        return False

def register_user(username, password):
    # Check if username already exists
    if user_exists(username):
        return False

    # Hash the password
    password_hash = generate_password_hash(password)

    # Ensure data directories exist
    os.makedirs(DATA_DIR, exist_ok=True)
    users_dir = os.path.join(DATA_DIR, 'users')
    os.makedirs(users_dir, exist_ok=True)

    # Append the new user to login.csv
    fieldnames = ['username', 'password_hash']
    file_exists = os.path.isfile(LOGIN_FILE)

    with open(LOGIN_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if file is new
        if not file_exists or os.stat(LOGIN_FILE).st_size == 0:
            writer.writeheader()

        writer.writerow({'username': username, 'password_hash': password_hash})

    # Create user data directory
    user_dir = os.path.join(users_dir, username)
    os.makedirs(user_dir, exist_ok=True)

    # Generate and store the encryption key
    encryption_key = Fernet.generate_key()
    key_file = os.path.join(user_dir, 'encryption_key.key')
    with open(key_file, 'wb') as f:
        f.write(encryption_key)

    return True


def user_exists(username):
    if not os.path.isfile(LOGIN_FILE):
        return False

    with open(LOGIN_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username:
                return True
    return False
