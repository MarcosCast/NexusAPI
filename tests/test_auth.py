from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/auth/login", json={"username": "johndoe", "password": "secret123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure():
    response = client.post("/auth/login", json={"username": "johndoe", "password": "wrongpass"})
    assert response.status_code == 401
