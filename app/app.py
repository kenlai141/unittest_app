import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
