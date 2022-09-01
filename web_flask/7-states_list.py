#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage  # use storage for fetching data

# Creando una instancia de flask con el nombre del archivo nuestro
app = Flask(__name__)


@app.teardown_appcontext
def teardon_appcontext(self):
    """
    After each request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Import data from storage
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    """
    Set host IP addres and port
    """
    app.run(host='0.0.0.0', port=5000)
