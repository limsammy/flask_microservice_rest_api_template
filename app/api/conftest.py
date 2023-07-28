import pytest

from api import create_app


@pytest.fixture
# TODO: Add typing hint (flask.Flask ?)
def app():
    """Fixture for creating Flask app"""
    app = create_app(test_config="api.config.TestingConfig")
    yield app


@pytest.fixture
def client(app):
    """Fixture for accessing client instance in tests"""
    return app.test_client()
