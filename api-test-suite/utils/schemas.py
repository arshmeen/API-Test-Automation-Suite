# Schema for a single user object
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["id", "name", "username", "email"]
}

# Schema for a post
POST_SCHEMA = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["userId", "title", "body"]
}
