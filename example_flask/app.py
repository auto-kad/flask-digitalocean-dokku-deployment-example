import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return '<h1> Hello World! </h1>'

    @app.route('/b')
    def bruh():
        return '<h1> is this working </h1>'

    return app



