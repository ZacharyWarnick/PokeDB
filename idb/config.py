"""Module for describing different execution environment configurations."""

import os

from pathlib import Path

_DEFAULT_DB_STRING = 'postgresql://postgres@localhost:5432/pokedb'


def load(name):
    options = {
        'development': Development,
        'testing': Testing,
        'production': DefaultConfig
        }

    if name not in options:
        print('Invalid app configuration was specified:', name)
        print('Using development environment by default.')

    return options.get(name, Development)


def _get_data_dir():
    this_dir = Path(__file__).parent
    default_data_path = this_dir.parent / 'data'
    return str(default_data_path.absolute())


class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_STRING', _DEFAULT_DB_STRING)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TABLE_DATA_DIR = _get_data_dir()


class Development(DefaultConfig):
    DEBUG = True


class Testing(DefaultConfig):
    TESTING = True
