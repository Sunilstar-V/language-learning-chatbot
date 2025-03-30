import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

#openai api key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#database file path
#DB_PATH = os.getenv("DB_FILE")
DB_PATH = "data/chatbot.db"

print("Loaded API Key:", OPENAI_API_KEY)