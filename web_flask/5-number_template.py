#!/usr/bin/python3
# A script that starts a Flask web application

from flask import render_template, Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Function that prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index_hbnb():
    """Function that prints HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def index_c(text):
    """Function that displays C with variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def index_python(text):
    """Function that displays Python with variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def index_number(n):
    """Function that checks for number"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def index_number_template(n):
    """Function that checks for number"""
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
