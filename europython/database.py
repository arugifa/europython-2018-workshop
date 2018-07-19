from apistar_sqlalchemy.database import Base
from sqlalchemy import create_engine


def connect_db(url):
    """Connect to the database.

    :param str url:
        database's URL
        (e.g., ``postgresql://user:password@localhost/database``).
    :return:
        connection to the database.
    :rtype:
        sqlalchemy.engine.Engine
    """
    return create_engine(url)


def init_db(engine):
    """Create all model tables into database.

    :param connection: connection to the database.
    :type connection: sqlalchemy.engine.Engine
    """
    Base.metadata.create_all(engine)


def clean_db(engine):
    """Drop all model tables from the database.

    :param connection: connection to the database.
    :type connection: sqlalchemy.engine.Engine
    """
    Base.metadata.drop_all(engine)
