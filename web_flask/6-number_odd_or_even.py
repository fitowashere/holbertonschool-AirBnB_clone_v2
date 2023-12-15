#!/usr/bin/python3
""" Script that start Flask """
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Create a route for home"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Create a route of /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Create a route of /c"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)  
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    " Create a route of /python"
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """creates a route of /Number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """creates a route of /number_template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """creates a route of /number_odd_or_even"""
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=o_e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
