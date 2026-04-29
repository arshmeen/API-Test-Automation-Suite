from utils.api_client import APIClient

def test_get_users():
    response = APIClient.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0