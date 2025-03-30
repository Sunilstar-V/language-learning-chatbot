import sqlite3
from datetime import datetime

DB_NAME = 'mistakes.db'

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_mistakes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            language TEXT NOT NULL,
            proficiency_level TEXT NOT NULL,
            user_input TEXT NOT NULL,
            bot_feedback TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def store_user_mistakes(user_id, language, proficiency_level, user_input, ai_feedback):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_mistakes (user_id, language, proficiency_level, user_input, bot_feedback, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, language, proficiency_level, user_input, ai_feedback, datetime.now())
    )
    conn.commit()
    conn.close()

# Initialize the database
initialize_db()
