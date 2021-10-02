import json


def test_create_user(client):
    data = {
        "username": "test_user_1",
        "email": "test@test.com",
        "password": "1234",
    }
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"
    assert response.json()["is_active"] is True
