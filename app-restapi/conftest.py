# This is file to set test databases to use with pytest
# Check out All You Need to Know to Start Using Fixtures in Your pytest Code
import os

from django.conf import settings

import pytest


DEFAULT_ENGINE = "django.db.backends.postgresql_psycopg2"


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
        "HOST": os.environ["DB_TEST_HOST"],
        "NAME": os.environ["DB_TEST_NAME"],
        "PORT": os.environ["DB_TEST_PORT"],
        "USER": os.environ["DB_TEST_USER"],
        "PASSWORD": os.environ["DB_TEST_PASSWORD"],
    }
