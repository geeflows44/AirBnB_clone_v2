#!/usr/bin/python3
"""flask we app starts
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """prints "Hello HBNB!"
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """prints “HBNB”
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """prints "C" followed by the value of variable text
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
