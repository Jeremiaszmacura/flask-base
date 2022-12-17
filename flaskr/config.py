"""App configuration file."""
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, "../.env"))


class Config(object):
    """Base config."""

    db_user = environ.get("DB_USER")
    db_password = environ.get("DB_PASSWORD")
    db_hostname = environ.get("DB_HOSTNAME")
    db_port = environ.get("DB_PORT")
    db_name = environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_hostname}:{db_port}/{db_name}"
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Uses production PostgreSQL database container."""

    pass

class DevelopmentConfig(Config):
    """Uses PostgreSQL in docker container."""

    pass


class TestingConfig(Config):
    """Uses sqlite in memory."""

    TESTING = True
