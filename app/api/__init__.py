from flask import Flask


def create_app(test_config=None) -> Flask:
    """App factory pattern with context manager"""
    app = Flask(__name__, instance_relative_config=True)

    return app
