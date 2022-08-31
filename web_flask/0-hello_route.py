from flask import Flask

# Creando una instancia de flask con el nombre del archivo nuestro
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Function hello, that return a prompt saying: Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """
    Set host IP addres and port
    Info: https://www.codegrepper.com/code-examples/python/flask+set+listen+
    address+port
    """
    app.run(host="0.0.0.0", port=5000)
