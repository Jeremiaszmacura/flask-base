"""Flask app creator file."""
from flask import Flask

from flaskr.routes.users import users_blueprint
from flaskr.models.db import db
from os import environ


def create_app(app_config):
    """Create and configure an instance of the Flask application."""

    db_user = environ.get("DB_USER")
    db_password = environ.get("DB_PASSWORD")
    db_hostname = environ.get("DB_HOSTNAME")
    db_port = environ.get("DB_PORT")
    db_name = environ.get("DB_NAME")
    print(f"postgresql://{db_user}:{db_password}@{db_hostname}:{db_port}/{db_name}")

    app = Flask(__name__)

    app.register_blueprint(users_blueprint, url_prefix="/")

    app.config.from_object(f"flaskr.config.{app_config}")
    print(app_config)

    app.secret_key = "secret string"

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
