# blueprints/dashboard/routes.py

from flask import render_template, session, redirect, url_for, flash
from . import dashboard_bp
from currency_utils import get_exchange_rate
import os
from blueprints.profile.routes import load_encrypted_profile

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('auth_bp.login'))

    username = session['username']

    # Fetch user's profile data
    profile_data = get_user_profile_data(username)
    default_currency = profile_data.get('default_currency', 'USD')
    api_key = profile_data.get('api_key', None)

    exchange_rate = None

    if api_key and default_currency and default_currency != 'USD':
        exchange_rate = get_exchange_rate(api_key, 'USD', default_currency)
        if exchange_rate is None:
            flash('Unable to retrieve exchange rate. Please check your API key and internet connection.', 'error')
    elif not api_key:
        flash('API key not set. Please update your profile.', 'error')
        return redirect(url_for('profile_bp.profile'))

    return render_template(
        'dashboard/dashboard.html',
        username=username,
        default_currency=default_currency,
        exchange_rate=exchange_rate
    )

def get_user_profile_data(username):
    user_dir = os.path.join(DATA_DIR, 'users', username)
    profile_dir = os.path.join(user_dir, 'profile')
    config_file = os.path.join(profile_dir, 'config.json')
    key_file = os.path.join(user_dir, 'encryption_key.key')

    if not os.path.exists(key_file):
        return {}

    with open(key_file, 'rb') as f:
        encryption_key = f.read()

    if os.path.exists(config_file):
        profile_data = load_encrypted_profile(config_file, encryption_key)
        return profile_data
    else:
        return {}
