#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, abort, render_template
from models.state import State
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    This function retrieves all State objects from
    the storage and renders them in a HTML page.
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)



@app.teardown_appcontext
def teardown_db(exception):
    """ display a HTML page: (inside the tag BODY)
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
