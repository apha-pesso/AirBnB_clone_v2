#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import *
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
    """Function that display C with variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def index_python(text):
    """Function that display python with variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def index_number(n):
    """Method to check for number"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
