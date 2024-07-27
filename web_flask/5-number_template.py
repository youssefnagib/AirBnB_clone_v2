#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ simple displaying Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hb():
    """ simple displaying HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def py(text):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    try:
        int_n = int(n)
        return "{} is a number".format(int_n)
    except ValueError:
        abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
