#!/usr/bin/python3
"""
Script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
* /c/<text>: display “C ”, followed by the value of the text variable (replace
underscore _ symbols with a space )
* /python/(<text>): display “Python ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
- The default value of text is “is cool”
* /number/<n>: display “n is a number” only if n is an integer
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
    return "C {}".format(replace)


@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Function, that return a prompt tha display a message
    Info default varaibles:
    https://stackoverflow.com/questions/14032066/can-flask-have-optional-url
    -parameters
    """
    replace = text.replace("_", " ")
    return "Python {}".format(replace)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Function, that display “n is a number” only if n is an integer
    Info: https://uniwebsidad.com/libros/explore-flask/chapter-6/url-converters
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    """
    Set host IP addres and port
    """
    app.run(host="0.0.0.0", port=5000)
