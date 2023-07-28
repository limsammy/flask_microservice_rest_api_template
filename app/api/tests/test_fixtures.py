import pytest


def test_create_app_fixture(app):
    assert app is not None
    assert app.name == "api"


def test_app_client_fixture(client):
    assert client is not None
    assert client.application.name == "api"
