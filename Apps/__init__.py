from flask import Flask
from Apps.config import config
from Apps.ext import init_ext
from .main.views import main_blue


def create_app(env='dev'):
    app = Flask(__name__)
    app.config.from_object(config[env])
    init_ext(app)
    app.register_blueprint(main_blue)
    return app