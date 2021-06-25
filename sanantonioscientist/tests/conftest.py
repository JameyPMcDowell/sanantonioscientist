import pytest

from sanantonioscientist.app import create_app


@pytest.fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    Yields
    -------
    flask.app.Flask
        An instance of our flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    Parameters
    ----------
    app : flask.app.Flask
        Pytest fixture

    Yields
    -------
    flask.testing.FlaskClient
        Flask app client
    """
    yield app.test_client()
