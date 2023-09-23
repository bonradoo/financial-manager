from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify

from blueprints.login.login import login_bp

home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')
home_bp.register_blueprint(login_bp, url_prefix='/login')


@home_bp.route('/')
def home():
    return render_template('home.html')

@home_bp.route('/home_logged_in')
def home_logged_in():
    return render_template('home_logged_in.html')