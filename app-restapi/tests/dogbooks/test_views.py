import json

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
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "Kavkazskaya Ovcharka"

    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 1


@pytest.mark.django_db
def test_add_dogbook_invalid_json(client):
    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 0

    resp = client.post(
        "/api/dogbooks/",
        {},
        content_type="application/json"
    )
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
        content_type="application/json"
    )
    assert resp.status_code == 400

    dogbooks = Dogbook.objects.all()
    assert len(dogbooks) == 0
