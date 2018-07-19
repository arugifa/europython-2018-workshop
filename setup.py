from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent

with (here / 'README.rst').open() as f:
    long_description = f.read()

setup(
    name='europython',
    version='2018.07.19',
    description="Material for my EuroPython 2018 workshop.",
    long_description=long_description,
    author="Alexandre Figura",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'apistar>=0.5',
        'apistar-sqlalchemy>=0.3',
        'click>=6.7',
        'factory-boy>=2.11',
        'sqlalchemy>=1.2',
    ],
)
