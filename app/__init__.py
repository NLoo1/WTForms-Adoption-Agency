# app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from models import db

debug = DebugToolbarExtension()

def create_app(config_class='config.Config'):

    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    return app
