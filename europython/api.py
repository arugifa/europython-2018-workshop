from typing import List

from apistar.http import QueryParam, QueryParams
from sqlalchemy.orm import Session

from europython import models, schemas


def articles(
        title: QueryParam, query: QueryParams,
        session: Session) -> List[schemas.Article]:
    """Return list of articles."""
    articles = models.Article.filter(**query)
    return [schemas.Article(article) for article in articles]
