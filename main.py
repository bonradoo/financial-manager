# main.py

from flask import Flask
from blueprints.home import home_bp
from blueprints.dashboard import dashboard_bp
from blueprints.auth import auth_bp
from blueprints.profile import profile_bp  # Add this line

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)  # Add this line

if __name__ == '__main__':
    app.run(debug=True)
