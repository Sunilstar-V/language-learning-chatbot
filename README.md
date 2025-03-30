# Language Learning Chatbot

## Overview
The **Language Learning Chatbot** is an AI-powered conversational assistant designed to help users learn new languages interactively. By engaging users in real-time conversations, the chatbot corrects mistakes, tracks progress, and provides detailed feedback to improve language skills.

## Features
- **Multi-language Support**: Learn various languages based on your preferences.
- **Real-time Error Correction**: Detects and corrects user mistakes during conversations.
- **Progress Tracking**: Logs user mistakes in a local SQLite database for review.
- **Detailed Feedback**: Provides a summary of mistakes and suggestions for improvement at the end of each session.
- **AI-Powered Conversations**: Uses OpenAI models with LangChain for natural and engaging interactions.

## Technologies Used
- **Programming Language**: Python
- **AI Model**: OpenAI GPT (via API)
- **AI Wrapper Library**: LangChain
- **Database**: SQLite
- **Frameworks & Libraries**:
  - OpenAI API
  - LangChain
  - SQLite3
  - Flask (optional, for web deployment)

## System Architecture
1. **User Input Handling**:
   - The chatbot asks users for their target language, native language, and proficiency level.
2. **Scenario Setup**:
   - Creates a learning scenario tailored to the user's preferences.
3. **Conversational Interaction**:
   - Engages the user in a conversation in the target language.
   - Corrects mistakes and logs them in the database.
4. **Mistake Analysis**:
   - Retrieves logged mistakes and generates an improvement report.
5. **Final Feedback**:
   - Provides a summary of mistakes and actionable suggestions for improvement.

## Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/language-learning-chatbot.git
cd language-learning-chatbot
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r [requirements.txt](http://_vscodecontentref_/1)
```

### 4. Set Up OpenAI API Key
1. Create a .env file in the project directory.
2. Add your OpenAI API key:
    ```bash
    python [chatbot.py](http://_vscodecontentref_/2)
    ```
### 5. Run the Chatbot
``` bash
python [chatbot.py](http://_vscodecontentref_/2)
```

## Database Structure
The chatbot uses SQLite to store user mistakes. Below is the database schema:

| Column Name | Data Type | Description                          |
|-------------|-----------|--------------------------------------|
| `id`        | INTEGER   | Unique ID (Primary Key)             |
| `user_id`   | TEXT      | Identifier for the user             |
| `language`  | TEXT      | Target language user is learning    |
| `mistake`   | TEXT      | Incorrect phrase or sentence        |
| `correction`| TEXT      | Suggested correction                |
| `timestamp` | DATETIME  | Time of mistake                     |

## Example Conversation Flow
```plaintext
Bot: "What language would you like to learn?"
User: "French"

Bot: "What is your native language?"
User: "English"

Bot: "What is your current proficiency level? (Beginner, Intermediate, Advanced)"
User: "Beginner"

Bot: "Let's start! Imagine you're ordering food at a French restaurant..."
User: "Je veux une pizza avec fromage."

Bot: "Great! But a more natural way to say it is: 'Je voudrais une pizza au fromage.'"

[Conversation Continues]

Final Report: "Here are the common mistakes you made and how to improve..."
```
## Deliverables
- **Project Code**: Includes `chatbot.py`, supporting scripts, and database setup.
- **Documentation**: This `README.md` file explaining the architecture and usage.
- **Screen Recorded Video**: Explanation of code, architecture, and logic.

## Future Enhancements
- Add voice recognition and speech synthesis for spoken language learning.
- Expand support for additional languages.
- Deploy as a web-based or mobile application.

## Contributors
- **Your Name** - AI Engineer & Developer

## License
This project is licensed under the [MIT License](LICENSE).