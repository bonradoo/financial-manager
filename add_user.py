# add_user.py

import csv
import os
from werkzeug.security import generate_password_hash

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
LOGIN_FILE = os.path.join(DATA_DIR, 'login.csv')
USERS_DIR = os.path.join(DATA_DIR, 'users')

def add_user(username, password):
    # Hash the password
    password_hash = generate_password_hash(password)

    # Ensure data directories exist
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(USERS_DIR, exist_ok=True)

    # Check if user already exists
    if os.path.exists(LOGIN_FILE):
        with open(LOGIN_FILE, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['username'] == username:
                    print('User already exists.')
                    return

    # Append the new user to login.csv
    with open(LOGIN_FILE, 'a', newline='') as csvfile:
        fieldnames = ['username', 'password_hash']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if file is new
        if os.stat(LOGIN_FILE).st_size == 0:
            writer.writeheader()

        writer.writerow({'username': username, 'password_hash': password_hash})

    # Create user data directory
    user_dir = os.path.join(USERS_DIR, username)
    os.makedirs(user_dir, exist_ok=True)
    print(f'User {username} added successfully.')

if __name__ == '__main__':
    import getpass
    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    add_user(username, password)
