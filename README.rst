===================================
Writing and Running Tests in Docker
===================================

Material for my workshop at EuroPython 2018.

.. image:: https://travis-ci.org/arugifa/ep2018-workshop.svg?branch=master
    :target: https://travis-ci.org/arugifa/ep2018-workshop

Getting Started
===============

To install Python dependencies::

    virtualenv -p python3.6 venv
    . venv/bin/activate
    pip install -r requirements.txt

To run tests::

    python -m pytest tests/

To run the demo server::

    ./manage.py demo --port 5000 --db_url "sqlite:////tmp/europython.sqlite"


Useful Links
============

To write tests:

- Pytest: https://docs.pytest.org/
- Pytest-BDD: https://github.com/pytest-dev/pytest-bdd
- Pytest-Splinter: https://github.com/pytest-dev/pytest-splinter
- Splinter: https://splinter.readthedocs.io/
- Pytest-SQLAlchemy: https://github.com/toirl/pytest-sqlalchemy
- SQLAlchemy: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
- Pytest-LocalServer: https://bitbucket.org/pytest-dev/pytest-localserver
- Webtest: http://webtest.pythonpaste.org/

To run and automate tests:

- Tox: https://tox.readthedocs.io/
- Docker: https://docs.docker.com/engine/reference/builder/
- Docker Compose: https://docs.docker.com/compose/
- Invoke: http://www.pyinvoke.org/
