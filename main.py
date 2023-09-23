from flask import Flask, redirect, url_for

from blueprints.home.home import home_bp
# from blueprints.api.api import api_bp
from blueprints.login.login import login_bp
from blueprints.dashboard.dashboard import dashboard_bp

app = Flask(__name__)
app.secret_key = 'secret_key'


app.register_blueprint(home_bp, url_prefix='/home')
# app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(login_bp, url_prefix='/login')

@app.route('/')
def home():
    return redirect(url_for('home.home'))

if __name__ == '__main__':
    app.run(debug=True)