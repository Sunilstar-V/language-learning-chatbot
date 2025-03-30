import pytest

@pytest.fixture

def client():
    """Creates a test client for Flask app."""
    from app import app
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
        
def test_set_preferences(client):
    """Test setting user preferences."""
    response = client.post("/set_preferences", json={
        "native_language": "English",
        "target_language": "French",
        "proficiency": "Intermediate"
    })
    assert response.status_code == 200
    assert response.json == {"message": "Preferences saved!"}