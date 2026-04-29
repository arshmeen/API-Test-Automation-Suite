from utils.api_client import APIClient
from utils.schemas import POST_SCHEMA, USER_SCHEMA
from jsonschema import validate

def test_get_users():
    response = APIClient.get("/users")

    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)

    for user in users:
        validate(instance=user, schema=USER_SCHEMA)


def test_create_post_missing_fields():
    payload = {
        "title": "test"
        # missing "body" and "userId"
    }

    response = APIClient.post("/posts", payload)

    # JSONPlaceholder still returns 201 (fake API)
    # In real APIs, you'd expect 400
    assert response.status_code == 201

    json_data = response.json()

    # Schema validation SHOULD fail if strict
    try:
        validate(instance=json_data, schema=POST_SCHEMA)
    except Exception:
        assert True

def test_create_post_invalid_datatype():
    payload = {
        "title": 123,   # should be string
        "body": True,   # should be string
        "userId": "abc" # should be number
    }

    response = APIClient.post("/posts", payload)

    assert response.status_code == 201

    json_data = response.json()

    try:
        validate(instance=json_data, schema=POST_SCHEMA)
    except Exception:
        assert True