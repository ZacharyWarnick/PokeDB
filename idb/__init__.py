"""Initialize the flask backend, and describes routes for serving HTML.

Flask basics: http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
"""

from flask import Flask, render_template
from pathlib import Path

loader_path = Path(__file__).parent / 'frontend' / 'dist'

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """Routes to the index page of the site."""
    return render_template('gen/index.html')


@app.route('/data')
def example():
    """Routes to a sample data page."""
    return render_template('datapage.html')


@app.route('/entity')
def entity():
    """Routes to a specific entity. This will be an API_get"""
    return render_template('entity.html')


@app.route('/indv')
def indv():
    """Individual view will return a page that gets its name from the API"""
    return render_template('individual_view.html')


if __name__ == "__main__":
    # Debug provides live updates without restarting;
    # this is a development only argument.
    app.run(debug=True)
