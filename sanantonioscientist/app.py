from flask import Flask
from celery import Celery

from sanantonioscientist.blueprints.page import page
from sanantonioscientist.blueprints.contact import contact
from sanantonioscientist.blueprints.data_upload import data_upload
from sanantonioscientist.extensions import debug_toolbar, mail, csrf

CELERY_TASK_LIST = [
    'sanantonioscientist.blueprints.contact.tasks',
]


def create_celery_app(app=None):
    app = app or create_app()

    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        include=CELERY_TASK_LIST
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


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
    app.register_blueprint(contact)
    app.register_blueprint(data_upload)
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
    mail.init_app(app)
    csrf.init_app(app)

    return None
