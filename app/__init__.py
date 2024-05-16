import logging

from flask import Flask

from app.config import Config


app = Flask(__name__)

app.config.from_object(Config)

# Set up logging
# logging.basicConfig(filename="app.log", level=logging.DEBUG)

from app.extensions import (
    login_manager,
    cors,
    db,
    limiter,
    mail,
)

cors.init_app(app)
db.init_app(app)
limiter.init_app(app)
mail.init_app(app)
login_manager.init_app(app)

# app.jinja_env.globals.update(decrypt_text=decrypt_text)

# Create tables
from app import models

with app.app_context():
    print("Creating tables")
    db.create_all()

# Register blueprints
from app import routes

app.register_blueprint(routes.api_blueprint)
app.register_blueprint(routes.auth_blueprint)
app.register_blueprint(routes.health_check_blueprint)
