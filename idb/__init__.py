
#-----------
#__init__.py
#-----------
# Initializes the backend flask runtime. Contains routes which return the rendered
# HTML templates.

from flask import Flask, render_template

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

#------------------------
# END ROUTE DECORATORS
#------------------------



if __name__ == "__main__":
    app.run()