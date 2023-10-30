from chalice.test import Client

from app import app
from src.todo.app_todo import URL_PREFIX


def test_get_index(testuser_id_token):
    """Testing the index route"""
    with Client(app) as client:
        response = client.http.get(f"{URL_PREFIX}/", headers={"Authorization": testuser_id_token})
        assert response.json_body == {"success": True}
