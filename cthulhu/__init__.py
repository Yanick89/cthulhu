import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

"""
 Logging configuration
"""
__version__ = "0.0.1"
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

db = SQLA()
appbuilder = AppBuilder()


def rise(config):
    return create_app(config)


def create_app(config):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config)
        db.init_app(app)
        appbuilder.init_app(app, db.session)
        from . import views  # noqa

        db.create_all()
        appbuilder.post_init()
    return app
