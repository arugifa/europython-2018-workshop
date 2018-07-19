import inspect
from pathlib import Path

from apistar import App, Route
from apistar_sqlalchemy.components import SQLAlchemySessionComponent
from apistar_sqlalchemy.event_hooks import SQLAlchemyTransactionHook

from europython import api, blog
from europython.config import DefaultConfig

TEMPLATES_DIR = Path(__file__).parent / 'templates'

routes = [
    # Blog
    Route('/', method='GET', handler=blog.home),
    Route('/articles/{article_id}/', method='GET', handler=blog.article),

    # API
    Route('/api/articles/', method='GET', handler=api.articles),
]


def create_app(config=DefaultConfig):
    """Set-up the web API.

    :rtype: apistar.App
    """
    if inspect.isclass(config):
        config = config()  # To load configuration from environment variables

    database_url = f'{config.DATABASE_URL}'
    components = [SQLAlchemySessionComponent(url=database_url)]
    event_hooks = [SQLAlchemyTransactionHook()]

    return App(
        routes=routes, template_dir=str(TEMPLATES_DIR),
        components=components, event_hooks=event_hooks,
    )
