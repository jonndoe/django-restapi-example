import json

from django.urls import reverse


def test_hello_world():
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"

# Follow Given_when_then framework to write tests
def test_sayhi(client):
    # Given - the state of the application before the test runs
    # client

    # When   - the behavior/logic being tested
    url = reverse("sayhi")
    response = client.get(url)
    content = json.loads(response.content)

    # Then   -  the expected changes based on the behavior
    assert response.status_code == 200
    assert content["sayhi"] == "hihihi!"
