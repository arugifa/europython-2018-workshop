from factory.alchemy import SQLAlchemyModelFactory


def reset_factories_session(session):
    """Reset database session used by all factories.

    By default, factories use :data:``apistar_sqlalchemy.database.Session``.
    But this session is closed after every request made to the web application.
    The result is that objects created with factories before making a request,
    are detached from the session after the request, and it becomes impossible
    to access to their attributes afterwards.

    For example, this code snippet would fail without using this helper::

        item = factories.MyFactory()
        response = client.get('/items/').json
        assert item.id in response.keys()

    :param session: the new session to used.
    :type session: sqlalchemy.orm.session.Session
    """
    for cls in SQLAlchemyModelFactory.__subclasses__():
        cls._meta.sqlalchemy_session = session
