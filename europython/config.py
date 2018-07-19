import os


class DefaultConfig:
    """Application configuration.

    Default values are defined as class attributes. If you want to override
    them, you MUST instantiate the config class, and:

    - define new values during instantiation (as keyword arguments),
    - define new values as environment variables.

    Setting values are processed in this order of importance:

    1. instance attributes,
    2. environment variables,
    3. class attributes.
    """

    #: How to connect to the database.
    DATABASE_URL = 'sqlite:///:memory:'

    def __init__(self, **kwargs):
        for setting, default_value in self.__class__.__dict__.items():
            if setting.isupper():  # Filter configuration settings only
                value = os.environ.get(setting, default_value)
                setattr(self, setting, value)

        self.__dict__.update(**kwargs)
