from pathlib import PurePath

import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions

from europython.config import DefaultConfig


@pytest.fixture(scope='session')
def app(config):
    """Return the web application.

    :rtype: apistar.App
    """
    raise NotImplementedError


@pytest.fixture(scope='session')
def client(app):
    """Return a client query the web application.

    :rtype: webtest.TestApp
    """
    raise NotImplementedError


@pytest.fixture(scope='session')
def config(tmpdir_factory):
    """Return applicaton's configuration.

    :rtype: europython.config.DefaultConfig
    """
    config = DefaultConfig()  # Read config from environment variables

    if 'sqlite' in config.DATABASE_URL:
        tmp_db = tmpdir_factory.mktemp('database').join('test.sqlite')
        config.DATABASE_URL = f'sqlite:///{tmp_db}'

    return config


@pytest.fixture
def db(dbsession, engine):
    """Return database session.

    All tables are recreated between tests execution.

    :rtype: sqlalchemy.orm.session.Session
    """
    raise NotImplementedError


@pytest.fixture(scope='session')
def server(app):
    """Return an HTTP server hosting the web application.

    :rtype: pytest_localserver.http.WSGIServer
    """
    raise NotImplementedError


@pytest.fixture(scope='session')
def sqlalchemy_connect_url(config):
    """Return database's connection URL.

    Used by :mod:`pytest_sqlalchemy`.
    """
    return f'{config.DATABASE_URL}'


@pytest.fixture(scope='session')
def splinter_driver_kwargs():
    """Launch Chrome with the sandbox disabled.

    Otherwise, Chrome refuses to start inside Docker::

        Failed to move to new namespace:
        PID namespaces supported, Network namespace supported,
        but failed: errno = Operation not permitted

    For an overwiew of supported options by the Chrome WebDriver,
    see https://sites.google.com/a/chromium.org/chromedriver/capabilities
    """
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    return {'options': options}


@pytest.fixture(scope='session')
def splinter_headless():
    """Run Chrome in headless mode, for faster tests."""
    return True


@pytest.fixture(scope='session')
def splinter_screenshot_dir():
    """Store screenshots near the tests.

    Used by :mod:`pytest_splinter`.
    """
    return str(PurePath(__file__).parent / 'screenshots')


@pytest.fixture(scope='session')
def splinter_webdriver():
    """Use Chrome, which is simpler to launch in headless mode.

    Firefox needs the Gecko driver to be manually installed first.
    Moreover, as of 22/07/2018, Firefox in headless mode is not yet
    available in python:3.6-alpine3.7 (version 52).
    """
    return 'chrome'
