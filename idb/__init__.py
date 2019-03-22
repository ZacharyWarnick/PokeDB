
#-----------
#__init__.py
#-----------
# Initializes the backend flask runtime. Contains routes which return the rendered
# HTML templates.

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# create flask object
app = Flask(__name__)

#-----------------
# ROUTE DECORATORS
#-----------------
## Create route decorators which maps URL route to corresponding HTML template
## to serve thr user.

## Home page, or no specification
## may route to splash, home page, or main index
@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/data')
def example():
    return render_template('datapage.html')

#------------------------
# END ROUTE DECORATORS
#------------------------


# Debug provides live updates without restarting;
# this is a development only argument.
if __name__ == "__main__":
    app.run(debug=True)