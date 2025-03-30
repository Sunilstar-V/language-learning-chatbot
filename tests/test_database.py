import pytest
import sqlite3
from app import DB_NAME, initialize_db

@pytest.fixture
def setup_db():
    """Setup test database."""
    initialize_db()
    
def test_database_connection(setup_db):
    """Test if the database connection is established."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_mistakes';")
    table = cursor.fetchone() is not None
    conn.close()
    assert table is not None, "Database table 'user_mistakes' does not exist."
    
def test_insert_mistake(setup_db):
    """Test if a mistake can be inserted into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_mistakes (user_id, language, proficiency_level, user_input, bot_feedback) VALUES (?, ?, ?, ?, ?)",
        ("test_user", "English", "Intermediate", "Hello", "Goodbye")
    )
    conn.commit()
    
    cursor.execute("INSERT INTO user_mistakes (user_input, bot_feedback) VALUES (?, ?)", 
                   ("Helo", "Did you mean 'Hello'?"))
    conn.commit()
    
    cursor.execute("SELECT * FROM user_mistakes WHERE user_input = 'Helo'")
    result = cursor.fetchone()
    conn.close()
    
    assert result is not None, "Inserted mistake should be retrievable."