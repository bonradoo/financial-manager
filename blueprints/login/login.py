from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
from google.cloud import datastore

login_bp = Blueprint('login', __name__, template_folder='templates', static_folder='static')

@login_bp.route('/')
def login():
    return render_template('login.html')

@login_bp.route('/verify_login', methods=['POST'])
def verify_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == 'admin':
        return redirect(url_for('home.home_logged_in'))
    else:
        error = 'Invalid credentials. Please try again'
        return render_template('login.html', error=error)
    
@login_bp.route('/signup')
def signup():
    return render_template('signup.html')

@login_bp.route('/verify_signup', methods=['POST'])
def verify_signup():
    try:
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
    except:
        error = 'There was an error retreiving your information. Please try again.'
        return render_template('signup.html', error=error)

    try:
        client = datastore.Client(project='financial-manager-399912')
        table = datastore.Entity(client.key('users'))
        
        table['name'] = name
        table['username'] = username
        table['email'] = email
        table['password'] = password
        client.put(table)
        message = 'Your account has been created. Please login.'
        return render_template('login.html', message=message)
    except Exception as e:
        print(e)
        error = 'There was an error creating your account. Please try again.'
        return render_template('signup.html', error=error)