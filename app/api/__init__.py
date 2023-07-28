from flask import Flask


def create_app(test_config=None) -> Flask:
    """App factory pattern with context manager"""
    app = Flask(__name__, instance_relative_config=True)

    # Check for correct config
    if test_config is None:
        if app.config["ENV"] == "production":
            app.config.from_object("api.config.ProductionConfig")
        else:
            app.config.from_object("api.config.ProductionConfig")
    else:
        app.config.from_object(test_config)

    app.config["API_TITLE"] = "Flask API"
    app.config["API_VERSION"] = "0.1.0"

    return app
