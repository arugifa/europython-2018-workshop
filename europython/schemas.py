from apistar import types, validators


class Article(types.Type):
    """Schema for :class:`europython.models.Article`."""

    id = validators.Integer(description="Article's identifier.")
    title = validators.String(description="Article's title.")
    content = validators.String(description="Article's content.")
