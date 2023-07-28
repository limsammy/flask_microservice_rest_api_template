import pytest

from api import create_app


@pytest.fixture
# TODO: Add typing hint (flask.Flask ?)
def app():
    app = create_app(test_config="api.config.TestingConfig")
    yield app
