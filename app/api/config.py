import os


class Config(object):
    DEBUG = os.getenv("DEBUG", default=True)
    TESTING = (
        False  # False by default. When using the below TestingConfig we switch this one
    )
    CSRF_ENABLED = True  # Enable CSRF protection. We will discuss this more later
    SECRET_KEY = "change-in-prod"  # Our default SECRET_KEY we will use for debug, dev. test environments


class TestingConfig(Config):
    TESTING = True
