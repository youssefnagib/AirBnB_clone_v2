#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, abort, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    This function retrieves all State objects from
    the storage and renders them in a HTML page.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ display a HTML page: (inside the tag BODY
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
