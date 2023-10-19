from unittest import mock

from chalice.test import Client
from app import app
from chalicelib.otameshi.app_otameshi import url_prefix_otameshi

...


def test_get_index():
    """Testing the index route"""
    with Client(app) as client:
        response = client.http.get(f"{url_prefix_otameshi}/")
        assert response.json_body == {"hello": "world"}


@mock.patch("chalicelib.otameshi.app_otameshi.requests.get")
def test_get_posts(mock_get: mock.MagicMock):
    """Mocking with the patch decorator to get posts from an JsonPlaceholder API"""
    # Mocking the response from the JsonPlaceholder API
    mock_get.return_value.ok = True
    mock_get.return_value.json.return_value = [
        {"id": 1, "title": "foo"},
        {"id": 2, "title": "bar"},
    ]
    # Testing the route
    with Client(app) as client:
        response = client.http.get(f"{url_prefix_otameshi}/jsonplaceholder/posts")
        assert response.status_code == 200
