from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "CI/CD Demo App is running"

def test_users():
    client = app.test_client()
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

def test_single_user():
    client = app.test_client()
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json["name"] == "Aparna"

def test_user_not_found():
    client = app.test_client()
    response = client.get("/users/999")
    assert response.status_code == 404
    assert b"User not found" in response.data