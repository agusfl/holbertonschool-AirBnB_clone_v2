#!/usr/bin/python3
"""
Script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
- You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

# Creando una instancia de flask con el nombre del archivo nuestro
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Function hello, that return a prompt saying: Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Function, that return a prompt saying: HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function, that return a prompt saying: C and text passed"""
    replace = text.replace("_", " ")
    return f"C {replace}"


if __name__ == '__main__':
    """
    Set host IP addres and port
    """
    app.run(host="0.0.0.0", port=5000)
