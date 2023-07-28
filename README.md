# Flask API Microserver Template

## Goal

Create a template for my picky favorite design patterns and libraries/frameworks for a microservice. Will be using example models and mock data for testing

## Prereqs

* Postgres
* Python (using version `Python 3.10.5`)
* Pyenv (reccomended)
* Virtualenv (reccomended)

1. Create a new python virtual environment for this project: `pyenv virtualenv flask-api-project`
2. Activate the environment: `pyenv activate flask-api-project`

### Iterations

#### Iteration 1

![Basic table set up for Users, Group, Projects](./img/user_auth_tables.png)

This is a basic visualization of our relational models we will be implementing as our first step. The goal will be for teach of these to offer CRUD functionality via REST API. Relevant tests should be included

First, we create our `.flaskenv` and give flask some information about our app.

```
FLASK_ENV=development
FLASK_APP=app/api
FLASK_RUN_PORT=8000
```

* We set our environment to development -- this will give debug information and stack traces for debugging purposes
* We set `FLASK_APP` to the `./app/api` module (this is where the flask app actually "lives")
* Set port for debug server (8000) `FLASK_RUN_PORT=8000`

Now, install `flask` and `python-dotenv`: `pip install flask python-dotenv` (Or if you've already downloaded the project's dependecies, you can skip this step (`pip install -r requirements`))

Next, we create the api module under the app directory: `touch app/api/__init__.py`. This tells python that the `api` directory is a python *module*

We are using an [app factory](https://flask.palletsprojects.com/en/2.3.x/patterns/appfactories/) building pattern, so we want to define our `api` module with the following:

```python
from flask import Flask


def create_app(test_config=None) -> Flask:
    """App factory pattern with context manager"""
    app = Flask(__name__, instance_relative_config=True)

    return app
```

Let's see if we can start a server, run the following in your terminal: `flask run`

You should see the following output:

```shell
flask run
 * Serving Flask app 'app/api'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
```

If we send a GET request to the dev server from our browser (naviage to the URL) runnong on: `http://127.0.0.1:8000`, you should see the following output in your terminal:

```shell
127.0.0.1 - - [27/Jul/2023 17:46:52] "GET / HTTP/1.1" 404 -
```

*Note:* We are getting a 404 as we have not implemented any routes to handle requests to the index (`/`)

---

Now that we have a very early app actually running, let's implement our testing framework.

Install pytest: `pip install pytest`

Create an testing configuration file where we will define fixtures: `touch app/conftest.py`

We will now create a fixture for our app factory. We will import our `create_app()` function and use it to create an app instance; we `yield` the instance to introduce the object into the individual test's scope

```python
import pytest

from api import create_app


@pytest.fixture
# TODO: Add typing hint (flask.Flask ?)
def app():
    app = create_app(test_config="api.config.TestingConfig")
    yield app
```
