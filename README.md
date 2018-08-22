[![Build Status](https://travis-ci.org/Jay54520/tornado-structure.svg?branch=master)](https://travis-ci.org/Jay54520/tornado-structure)
[![Coverage Status](https://coveralls.io/repos/github/Jay54520/tornado-structure/badge.svg?branch=master)](https://coveralls.io/github/Jay54520/tornado-structure?branch=master)

# tornado-structure
Python tornado project structure

## Create Virtualenv and Install requirements

* Create virtualenv: `python3 -m venv env`
* Activate virtualenv: `source env/bin/activate`
* Install requirements: `pip install requirements.txt`

## Run sever

`python app.py`

Set port using command line:

`python app.py --port=8000`

Enable DEBUG by set environment variable:

`export DEBUG=1`

## Run tests

`python -m unittest`

## Run scripts

`python -m sample.scripts.hello`

## Reference

1. [Repository Structure and Python](https://www.kennethreitz.org/essays/repository-structure-and-python)
1. [Django Project Structure](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)