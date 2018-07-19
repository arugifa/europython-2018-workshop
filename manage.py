#!/usr/bin/env python3

"""Command-line utility for administrative tasks."""

import os

import click

from europython import create_app
from europython.config import DefaultConfig
from europython.database import connect_db, init_db
from europython.factories import ArticleFactory
from europython.models import Article


# Settings retrieved from environment variables.
DATABASE_URL = 'DATABASE_URL'
SERVER_PORT = 'SERVER_PORT'


@click.group()
def cli():  # noqa: D401
    """Base command-line group.

    To be used for decorating any other command.
    """


@cli.command()
@click.option(
    '--port', envvar=SERVER_PORT,
    required=True, type=int, help="Demo server's port.")
@click.option(
    '--db_url', envvar=DATABASE_URL,
    required=True, help="How to connect to the database.")
def demo(port, db_url):
    """Launch a demo server."""
    config = DefaultConfig(DATABASE_URL=db_url)
    app = create_app(config)

    db = connect_db(config.DATABASE_URL)
    init_db(db)

    if not Article.all():  # Not reusing previous demo database
        ArticleFactory.create_batch(10)

    app.serve('0.0.0.0', port, debug=True)


if __name__ == '__main__':
    cli()
