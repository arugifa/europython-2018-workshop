from apistar_sqlalchemy.database import Session
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from europython import models


class ArticleFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.Article
        sqlalchemy_session = Session
        # We commit objects, in order to make them visible
        # between different sessions (e.g., test and codebase sessions).
        sqlalchemy_session_persistence = 'commit'

    title = Sequence(lambda n: f'Article {n}')
    content = "This is a great article about a super cool technology."
