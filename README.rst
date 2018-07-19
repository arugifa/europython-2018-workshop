===================================
Writing and Running Tests in Docker
===================================

Material for my workshop at EuroPython 2018.

Every commit of the repository corresponds to a different step of the workshop.

.. image:: https://travis-ci.org/arugifa/ep2018-workshop.svg?branch=master
    :target: https://travis-ci.org/arugifa/ep2018-workshop


Getting Started
===============

First, go back in time::

    git checkout -b workshop setup

You will start to work from this commit, in a new ``workshop`` branch.
From there, you can have a look into ``master`` if you are blocked and don't know what to do next.

Then, **install requirements**:

- `VirtualBox`_: to run the workshop inside a virtual machine (Ubuntu),
- `Vagrant`_: to set-up the virtual machine,

.. _Vagrant: https://www.vagrantup.com/downloads.html
.. _VirtualBox: https://www.virtualbox.org/wiki/Downloads

By using **VirtualBox**, we are sure to all have the same environment. Which will save us time!

Now that you are ready to start, let's **create a virtual machine**::

    vagrant up  # Create the VM
    vagrant ssh  # Connect to the VM

Inside the virtual machine, you can now **set-up the demo project**::

    cd /vagrant  # Local repository is shared with the VM in /vagrant
    virtualenv -p python3.6 venv
    . venv/bin/activate
    pip install -r requirements-test.txt

Finally, you can check that everything is working, by running the demo server::

    ./manage.py demo --port 5000 --db_url "sqlite:////tmp/europython.sqlite"

And access to the demo blog on `http://192.168.50.4:5000/ <http://192.168.50.4:5000/>`_,
using your favorite browser on your local machine.


Writing Tests (with Pytest)
===========================

First step of the workshop is to write tests.

If you try to run them now, you will only get failures::

    python -m pytest tests/

By looking at error messages, you will see ``NotImplementedError`` exceptions.
It's because you have to implement yourself:

- **acceptance tests** for the demo blog (using `Pytest-BDD`_) in ``tests/test_blog.py``,
- **end-to-end tests** for the demo web API (using `WebTest`_) in ``tests/test_api.py``,
- `Pytest fixtures`_, in ``tests/conftest.py``.

.. _WebTest: http://webtest.pythonpaste.org/
.. _Pytest-BDD: https://github.com/pytest-dev/pytest-bdd
.. _Pytest fixtures: https://docs.pytest.org/en/latest/fixture.html

To implement the tests:

#. **Execute** them one by one:

   - for the blog: ``python -m pytest tests/test_blog.py::test_read_article``
   - for the web API: ``python -m pytest tests/test_api.py::test_get_articles``

#. **Read** the error message,
#. **Let you guide** by the error message to find a solution,
#. **Implement** the solution.
#. **Do it again**, until you fix all errors.

Hints:

- there are **factories** in ``europython/factories.py``
  to create objects in database from the tests,
- **test helpers** are available in ``europython/database.py`` and ``europython/test.py``,
- look at **Pytest extensions** we use in ``requirements-test.txt``:
  they already provide fixtures, that our own fixtures or tests are depending on.

Useful links:

- Pytest: https://docs.pytest.org/
- Pytest-BDD: https://github.com/pytest-dev/pytest-bdd
- Pytest-Splinter: https://github.com/pytest-dev/pytest-splinter
- Splinter: https://splinter.readthedocs.io/
- Pytest-SQLAlchemy: https://github.com/toirl/pytest-sqlalchemy
- SQLAlchemy: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
- Pytest-LocalServer: https://bitbucket.org/pytest-dev/pytest-localserver
- Webtest: http://webtest.pythonpaste.org/


Automating Tests (with Tox)
===========================

Now that our tests are **GREEN**, an important step is still missing:
how to be sure that our project is packaged correctly?
Because if you update a broken package to `PyPI`_, people will not be able to use it...

For this purpose, we will use `Tox`_, to run our tests inside a virtual environment,
automatically updated every time you change a dependency or the project's packaging.
In fact, we will need several environments:

- one for **running the tests**,
- another one for **running lint checking** with `Flake8`_,
- and two **development environments**:

  - the first one to be used **locally** *(e.g., to get auto-completion in your IDE)*,
  - the second one to be used in **Docker** later on.

- as a bonus, you can also create one for **checking security issues**
  in dependencies (with `Safety`_).

.. _Coverage.py: https://coverage.readthedocs.io/
.. _Flake8: http://flake8.pycqa.org/
.. _PyPI: https://pypi.org/
.. _Safety: https://github.com/pyupio/safety
.. _Tox: https://tox.readthedocs.io/

Hints:

- now that we are using **Tox**, you can move test dependencies
  from ``requirements-test.txt`` into ``tox.ini``,
- you can get **test coverage** for free with `Coverage.py`_.


Running Tests (in Docker)
=========================

Running tests locally is nice. But only when you work alone!

As soon as you work with other persons, using **different operating systems**,
things start to be complicated. People will probably have different versions
of **system dependencies**, and most of the time, installing the needed version
will not be straightforward.

That's where `Docker`_ comes to the rescue!

With **Docker**, the only system dependency people will have to install is **Docker** itself. Period.

For our workshop, we will need two **Docker** images:

1. one for running on **production**,
2. another one to use for **tests**, based on the PROD image (to not dupplicate *Dockerfiles*),
   and including all test dependencies like **Tox**, **Pytest** and others.

Finally, to simulate a real use case, with a project depending on external systems,
we will also replace with `PostgreSQL`_ the **SQLite** in-memory database
we were using until now. For this purpose, we will set-up our testing stack with `Docker Compose`_.

.. _Docker: https://docs.docker.com/engine/reference/builder/
.. _Docker Compose: https://docs.docker.com/compose/
.. _PostgreSQL: https://hub.docker.com/_/postgres/

Hints:

- Use **Alpine images**, for a smaller image footprint.
- **Configure** the application container using **environment variables** (see ``europython/config.py``).
- You will have to:

  - add ``psycopg2`` to the application's dependencies,
    and install ``gcc``, ``libc-dev`` and ``postgresql-dev`` in the PROD application container,
    in order to interact with **PostgreSQL**,
  - install ``chromium`` and ``chromium-chromedriver`` in the TEST application container,
    in order to run the acceptance tests.

- You already run tests locally with **Tox**. So do the same inside Docker 😃
  Just don't forget to forward environment variables (used to configure containers)
  to Pytest, with the `passenv directive`_.
- Run the tests directly inside the application container in order to:

  - share your local code with the container,
  - take advantage of using `PDB`_ when debugging tests.

.. _passenv directive: https://tox.readthedocs.io/en/latest/config.html?#confval-passenv=SPACE-SEPARATED-GLOBNAMES
.. _PDB: https://docs.python.org/3/library/pdb.html


Automating Workflow (with Invoke)
=================================

TODO: explain what to do next.

.. _Invoke: http://www.pyinvoke.org/


Adding Continuous Integration (on Travis CI)
============================================

TODO: explain what to do next.
