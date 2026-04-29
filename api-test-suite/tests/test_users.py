from utils.api_client import APIClient
from utils.schemas import USER_SCHEMA
from jsonschema import validate

def test_get_users():
    response = APIClient.get("/users")

    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)

    # Validate each user against schema
    for user in users:
        validate(instance=user, schema=USER_SCHEMA)