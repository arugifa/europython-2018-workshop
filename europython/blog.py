from apistar import App
from apistar.exceptions import NotFound
from sqlalchemy.orm import Session

from europython import models


def home(app: App, session: Session):
    """Blog homepage."""
    articles = models.Article.all()
    return app.render_template('home.html', articles=articles)


def article(app: App, article_id: int, session: Session):
    """Article page."""
    article = models.Article.find(id=article_id)

    if not article:
        raise NotFound

    return app.render_template('article.html', article=article)
