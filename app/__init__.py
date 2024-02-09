# app/__init__.py

from dotenv import load_dotenv
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from .models import db
from routes import rts

debug = DebugToolbarExtension()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)  # Load configuration from the Config class
    db.init_app(app)
    app.register_blueprint(rts)
    return app

