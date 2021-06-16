import pytest

from dogbooks.models import Dogbook


@pytest.fixture(scope="function")
def add_dogbook():
    def _add_dogbook(title, field, year):
        dogbook = Dogbook.objects.create(title=title, field=field, year=year)
        return dogbook

    return _add_dogbook
