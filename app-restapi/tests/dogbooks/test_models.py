import pytest

from dogbooks.models import Dogbook

@pytest.mark.django_db
def test_dogbook_model():
    dogbook = Dogbook(title="Kavkaskaya Ovcharka", field="vospitanie", year="2003")
    dogbook.save()
    assert dogbook.title == "Kavkaskaya Ovcharka"
    assert dogbook.field == "vospitanie"
    assert dogbook.year == "2003"
    assert dogbook.created_date
    assert dogbook.updated_date
    assert str(dogbook) == dogbook.title