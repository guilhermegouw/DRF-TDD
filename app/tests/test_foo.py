import json

from django.urls import reverse


def test_hello_world():
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"


def test_ping(client):
    url = reverse("ping")
    response = client.get(url)
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data["ping"] == "pong"
