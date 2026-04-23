from core.http_client import HttpClient


def test_api_is_alive():
    client = HttpClient()

    response = client.get("/users?page=2")

    assert response.status_code == 200