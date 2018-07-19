import re
import sys
from datetime import date

from invoke import task
from invoke.context import Context

# Docker
IMAGE_NAME = f'europython/workshop'
DOCKER_SERVICE = 'web'

# Tox
DEV_ENV = 'dev'
ACTIVATE_DEV = f'.tox/{DEV_ENV}/bin/activate'
PYTHON_TESTS = 'py36'
LOCAL_ENV = 'local'

# Python
SETUP_FILE = 'setup.py'


# Commands

build_help = {
    'erase': "Overwritte previously created container with the same tag.",
}


@task
def build(ctx, erase=False):
    """Build a new Docker container."""
    today = date.today().strftime('%Y.%m.%d')

    # Build the Docker container.
    if erase:
        print("Erasing existing Docker image")
        command = f'docker rmi {IMAGE_NAME}:{today}'
        run(command)

    print("Building new Docker image")
    command = f'docker build -t {IMAGE_NAME}:{today} -t {IMAGE_NAME}:latest .'
    run(command)

    # Update application version.
    print(f"Updating version in {SETUP_FILE}")
    to_replace = [(r"version='\d+.\d+.\d+'", f"version='{today}'")]
    replace(to_replace, SETUP_FILE)


demo_help = {
    'debug': "Execute a shell inside the Docker container instead.",
}


@task(help=demo_help)
def demo(ctx, debug=False):
    """Launch the demo web API in foreground."""
    raise NotImplementedError


test_help = {
    'debug': "Execute a shell inside the Docker container instead.",
}


@task(help=test_help)
def test(ctx, debug=False):
    """Execute the test suite."""
    raise NotImplementedError


@task
def virtualenv(ctx):
    """Install web application and its dependencies locally."""
    raise NotImplementedError


# Helpers

def run(command):
    """Execute a command with Invoke."""
    ctx = Context()
    ctx.run(
        command,
        echo=True,  # To improve User eXperience
        pty=True,  # To get colors in output
    )


def docker_run(command):
    """Execute a command inside a standalone running Docker container."""
    cmdline = f'docker run {IMAGE_NAME}:latest {command}'
    run(cmdline)


def docker_compose_run(command):
    """Execute a command inside a fully running Docker Compose stack."""
    cmdline = (
        f'docker-compose run '
        f'--entrypoint "sh -c" '  # To run any command
        f'--service-ports '  # To expose container's ports on host machine
        f'{DOCKER_SERVICE} "{command}"'
    )
    run(cmdline)


def replace(lines, in_file):
    """Replace lines in a file.

    Terminate script execution if lines are not found.

    :param lines:
        list of string tuples,
        with regex expressions to look for and their substitutes.
    """
    with open(in_file, 'r+') as f:
        content = f.read()

        for regex, string in lines:
            content, has_been_changed = re.subn(regex, string, content)
            if not has_been_changed:
                sys.exit(f"Regex not found in {in_file}: {regex}")

        f.seek(0)
        f.write(content)
        f.truncate()
