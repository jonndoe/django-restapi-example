import pytest

from dogbooks.models import Dogbook


@pytest.mark.django_db
def test_add_dogbook(client):
    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 0

    resp = client.post(
        "/api/dogbooks/",
        {
            "title": "Kavkazskaya Ovcharka",
            "field": "vospitanie sobaki",
            "year": "2004",
        },
        content_type="application/json",
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "Kavkazskaya Ovcharka"

    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 1


@pytest.mark.django_db
def test_add_dogbook_invalid_json(client):
    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 0

    resp = client.post("/api/dogbooks/", {}, content_type="application/json")
    assert resp.status_code == 400

    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 0


@pytest.mark.django_db
def test_add_dogbook_invalid_json_keys(client):
    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 0

    resp = client.post(
        "/api/dogbooks/",
        {
            "title": "Taksa",
            "field": "kormlenie",
        },
        content_type="application/json",
    )
    assert resp.status_code == 400

    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 0


@pytest.mark.django_db
def test_get_single_dogbook(client, add_dogbook):
    dogbook = add_dogbook(title="Sibirskaya Taksa", field="pravilniy uhod", year="2005")
    resp = client.get(f"/api/dogbooks/{dogbook.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "Sibirskaya Taksa"


def test_get_single_dogbook_incorrect_id(client):
    resp = client.get(f'{"/api/dogbooks/gogogo/"}')
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_dogbooks(client, add_dogbook):
    dogbook_one = add_dogbook(title="Spanielle", field="kormlenie", year="2005")
    dogbook_two = add_dogbook("Pudel", "vospitanie", "2013")
    resp = client.get(f"{'/api/dogbooks/'}")
    assert resp.status_code == 200
    assert resp.data[0]["title"] == dogbook_one.title
    assert resp.data[1]["title"] == dogbook_two.title
