from flask import Flask
from .login_system.routes import user
from .routes import main
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(16)
    app.register_blueprint(user)
    app.register_blueprint(main)    
    return app
