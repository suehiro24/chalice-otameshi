# from unittest.mock import patch

from chalice.test import Client
from chalicelib.app import app
from chalicelib.otameshi.app_otameshi import url_prefix_otameshi

...


def test_get_index():
    """Testing the index route"""
    with Client(app) as client:
        response = client.http.get(f"{url_prefix_otameshi}/")
        assert response.json_body == {"hello": "world"}
