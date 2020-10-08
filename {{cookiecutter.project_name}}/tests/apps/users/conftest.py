import pytest


@pytest.fixture
def user_data():
    return {
        "id": "a72fcbe5-1103-4acc-a77b-954b46bc7ba8",
        "email": "user1@email.com",
        "is_active": True,
        "username": "username",
        "password": "supersecret",
    }
