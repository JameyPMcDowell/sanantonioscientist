from flask import Flask

from sanantonioscientist.blueprints.page import page
from sanantonioscientist.extensions import debug_toolbar


def create_app(settings_override=None):
    """Generate a Flask application using the app factory pattern.

    Parameters
    ----------
    settings_override : dict, optional
        Config override settings, by default None

    Returns
    -------
    flask.app.Flask
        An instance of our flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    extensions(app)

    return app


def extensions(app):
    """Register 0 or more extensions (mutates the app passed in).

    Parameters
    ----------
    app : flask.app.Flask
        Flask application instance

    Returns
    -------
    None
    """
    debug_toolbar.init_app(app)

    return None
