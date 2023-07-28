# Flask API Microserver Template

## Goal

Create a template for my picky favorite design patterns and libraries/frameworks for a microservice. Will be using example models and mock data for testing

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