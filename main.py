from flask import Flask, redirect, url_for

from blueprints.dashboard.dashboard import dashboard_bp

app = Flask(__name__)
app.secret_key = 'secret_key'

MONGO_USER = 'localhost'
MONGO_PASS = 'vEBCUt1N8mJ0g4ky'
MONGO_URI = f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@main.aqvtfli.mongodb.net/?retryWrites=true&w=majority'

app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route('/')
def home():
    return redirect(url_for('dashboard.dashboard'))

if __name__ == '__main__':
    app.run(debug=True)