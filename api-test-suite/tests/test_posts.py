from utils.api_client import APIClient

def test_get_posts():
    response = APIClient.get("/posts")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_post():
    payload = {
        "title": "test",
        "body": "data",
        "userId": 1
    }

    response = APIClient.post("/posts", payload)

    assert response.status_code == 201
    json_data = response.json()

    assert json_data["title"] == payload["title"]
    assert json_data["body"] == payload["body"]
    assert json_data["userId"] == payload["userId"]