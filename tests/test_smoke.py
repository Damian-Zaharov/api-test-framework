from core.http_client import HttpClient


def test_users_endpoint():
    client = HttpClient()

    response = client.get("/users")

    assert response.status_code == 200