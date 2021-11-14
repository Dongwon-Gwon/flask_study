import pytest

from run import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_admin_all(client):
    response = client.get("/admin/name")
    assert response.status_code == 200

def test_get_admin_by_id(client):
    response = client.get("/admin/name/1")
    assert response.status_code == 200
    assert response.data == b'[{"admin_id":1,"admin_name":"Seongha"}]\n'
