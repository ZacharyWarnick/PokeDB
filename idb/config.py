
import os

_DEFAULT_DB_STRING = 'postgres://postgres@localhost:5432/pokedb'


class DefaultConfig(object):
    DEBUG = False
    TESTING = False


class DatabaseConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_STRING', _DEFAULT_DB_STRING)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
