from flask import Flask
from .users.routes import user
from .routes import main
from .api.routes import api
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(16)
    app.register_blueprint(user)
    app.register_blueprint(main)
    app.register_blueprint(api)    
    return app
