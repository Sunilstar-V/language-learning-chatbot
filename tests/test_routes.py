import pytest
from app import app, initialize_db

@pytest.fixture
def client():
    """Creates a test client for Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            initialize_db()
        yield client

def test_homepage(client):
    """Test if the homepage loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<!doctype html>" in response.data

def test_chat_route(client):
    """Test the chat endpoint."""
    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json
