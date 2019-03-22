"""Initialize the flask backend, and describes routes for serving HTML.

Flask basics: http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# App initialization must happen first.
app = Flask(__name__)

#-----------------
# ROUTE DECORATORS
#-----------------
## Create route decorators which maps URL route to corresponding HTML template
## to serve thr user.

@app.route('/')
def index():
    """Routes to the index page of the site."""
    return render_template('index.html')

@app.route('/data')
def example():
    """Routes to a sample data page."""
    return render_template('datapage.html')

#------------------------
# END ROUTE DECORATORS
#------------------------


# Debug provides live updates without restarting;
# this is a development only argument.
if __name__ == "__main__":
    app.run(debug=True)
