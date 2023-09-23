from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify

dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')

@dashboard_bp.route('/')
def dashboard():
    return render_template('dashboard.html')