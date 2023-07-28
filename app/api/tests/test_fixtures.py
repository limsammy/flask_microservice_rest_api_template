import pytest


def test_create_app_fixture(app):
    breakpoint()
    assert app is not None
    assert app.name == "api"
