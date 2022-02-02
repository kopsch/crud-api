from flask import Flask
from flask_cors import CORS
from app import routes

def create_app():

    app = Flask(__name__, static_folder=None)
    CORS(app)
    routes.init_app(app)

    return app