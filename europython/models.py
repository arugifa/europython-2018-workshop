from apistar_sqlalchemy.database import Base, Session
from sqlalchemy import Column, Integer, String, Text


class Article(Base):
    """Article model."""

    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)

    @classmethod
    def all(cls):
        """Return all articles.

        :rtype: list
        """
        return Session.query(cls).all()

    @classmethod
    def filter(cls, **kwargs):
        """Filter articles.

        Fields to filter on can be given as keyword arguments.

        :rtype: list
        """
        return Session.query(cls).filter_by(**kwargs).all()

    @classmethod
    def find(cls, **kwargs):
        """Find a specific article.

        Fields to filter on can be given as keyword arguments.

        :return: the article if found; ``None`` otherwise.
        :rtype: Article
        """
        return Session.query(cls).filter_by(**kwargs).one_or_none()
