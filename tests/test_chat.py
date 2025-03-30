import pytest
from app import conversation

def test_chatbot_response():
    """test chatbot response format"""
    user_message = "Bonjour"
    response = conversation.predict(input=user_message)
    assert isinstance(response, str), "Response should be a string."
    assert len(response) > 0, "Response should not be empty."