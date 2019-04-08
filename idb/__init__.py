"""Initialize the flask backend, and describes routes for serving HTML.

Flask basics: http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
"""

import sys

from pathlib import Path
from flask import Flask, render_template
from flask_cors import CORS

# Need to place local files in module search path.
sys.path.append(str(Path(__file__).parent.absolute()))

# Local Imports
from api import api  # noqa: E402
from config import DefaultConfig  # noqa: E402
from models import db  # noqa: E402


app = Flask(__name__)
app.config.from_object(DefaultConfig)

db.init_app(app)
app.register_blueprint(api)

cors = CORS(app, resources={r'/api/*': {"origins": "*"}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """Routes to the index page of the site."""
    return render_template('gen/index.html')


@app.cli.command('reset_db')
def reset_db():
    for table in ['pokemon', 'type', 'evolution', 'form', 'base_stats']:
        db.engine.execute('DROP TABLE if exists {} cascade;'.format(table))
    db.create_all()


@app.cli.command('create_db')
def create_db():
    from create_db import initialize
    initialize()


if __name__ == "__main__":
    # Debug provides live updates without restarting;
    # this is a development only argument.
    app.run(debug=True)
