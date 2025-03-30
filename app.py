from flask import Flask, render_template, request, jsonify, session
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback_secret_key")

# Load API Key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Initialize Chat Model
chat_model = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=OPENAI_API_KEY)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=chat_model, memory=memory)

DB_NAME = "mistakes.db"

# Initialize the database
def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_mistakes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            native_language TEXT NOT NULL,
            target_language TEXT NOT NULL,
            proficiency TEXT NOT NULL,
            user_input TEXT NOT NULL,
            bot_feedback TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Store user mistakes in the database
def store_user_mistakes(user_id, native_language, target_language, proficiency, user_input, ai_feedback):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO user_mistakes (user_id, native_language, target_language, proficiency, user_input, bot_feedback, timestamp) 
           VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (user_id, native_language, target_language, proficiency, user_input, ai_feedback, datetime.now())
    )
    conn.commit()
    conn.close()

# Fetch all mistakes
def fetch_mistakes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_mistakes ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "user_id": row[1],
            "native_language": row[2],
            "target_language": row[3],
            "proficiency": row[4],
            "user_input": row[5],
            "bot_feedback": row[6],
            "timestamp": row[7]
        }
        for row in rows
    ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_preferences', methods=['POST'])
def set_preferences():
    data = request.json
    session['user_id'] = data.get('user_id', 'anonymous')  # Assign a default user ID if not provided
    session['native_language'] = data.get('native_language', 'English')
    session['target_language'] = data.get('target_language', 'English')
    session['proficiency'] = data.get('proficiency', 'Beginner')
    return jsonify({"message": "Preferences saved!"})

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    user_id = session.get('user_id', 'anonymous')
    native_language = session.get('native_language', 'English')
    target_language = session.get('target_language', 'English')
    proficiency = session.get('proficiency', 'Beginner')

    if not memory.buffer:
        memory.save_context({"system": ""}, {"response": f"You are a language tutor. The user speaks {native_language} and wants to learn {target_language}. Their level is {proficiency}. Speak to them only in {target_language}. Correct their mistakes politely."})
    
    try:
        response = conversation.predict(input=user_input)
        store_user_mistakes(user_id, native_language, target_language, proficiency, user_input, response)
    except Exception as e:
        response = f"Error: {str(e)}"

    return jsonify({"response": response})

@app.route('/get_mistakes', methods=['GET'])
def get_mistakes():
    mistakes = fetch_mistakes()
    if not mistakes:
        return jsonify({"message": "No mistakes found"}), 404
    return jsonify(mistakes)

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)
