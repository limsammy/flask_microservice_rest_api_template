import pytest


def test_create_app_fixture(app):
    assert app is not None
    assert app.name == "api"
    # These config vars are set in app/api/__init__.py
    assert app.config["API_TITLE"] == "Flask API"
    assert app.config["API_VERSION"] == "0.1.0"


def test_app_client_fixture(client):
    assert client is not None
    assert client.application.name == "api"
