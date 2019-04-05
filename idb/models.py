
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import DatabaseConfig

app = Flask(__name__)
app.config.from_object(DatabaseConfig)

db = SQLAlchemy(app)


class Pokemon(db.Model):
    pass
