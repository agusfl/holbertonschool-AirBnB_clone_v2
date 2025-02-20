#!/usr/bin/python3
"""
Script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- You must use storage for fetching data from the storage engine (FileStorage
or DBStorage) => from models import storage and storage.all(...)
- To load all cities of a State:
* If your storage engine is DBStorage, you must use cities relationship
* Otherwise, use the public getter method cities
- After each request you must remove the current SQLAlchemy Session:
* Declare a method to handle @app.teardown_appcontext
* Call in this method storage.close()
- Routes:
* /hbnb_filters: display a HTML page like 6-index.html, which was done during
the project 0x01. AirBnB clone - Web static
* * Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css from
web_static/styles/ to the folder web_flask/static/styles
* * Copy files icon.png and logo.png from web_static/images/ to the folder
web_flask/static/images
* * Update .popover class in 6-filters.css to allow scrolling in the popover
and a max height of 300 pixels.
* * Use 6-index.html content as source code for the template
10-hbnb_filters.html:
* * * Replace the content of the H4 tag under each filter title (H3 States and
H3 Amenities) by &nbsp;
* * State, City and Amenity objects must be loaded from DBStorage and sorted by
name (A->Z)
"""

from flask import Flask, render_template
from models import storage  # use storage for fetching data
from models import State  # Importo state para poder usar la clase
from models.amenity import Amenity
from models.place import Place

# Creando una instancia de flask con el nombre del archivo nuestro
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """
    After each request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def states_list():
    """Import data from storage"""
    # Importamos los estados (States)
    states = storage.all(State).values()
    # Importamos los amenities
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


if __name__ == "__main__":
    """
    Set host IP addres and port
    """
    app.run(host='0.0.0.0', port=5000)
