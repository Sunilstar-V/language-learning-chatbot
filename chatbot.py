import openai
import config

#set the OpenAI API key
openai.api_key = config.OPENAI_API_KEY

#function to get a response from the OpenAI API
def chat_with_bot(user_input):
    try:
        client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI that assists in language learning."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
while True:
    user_text = input("You: ")
    if user_text.lower() in ['exit', 'quit']:
        print("Exiting the chat.")
        break
    
    bot_response = chat_with_bot(user_text)
    print(f"Bot: {bot_response}")
# This script uses the OpenAI API to create a simple chatbot that can assist with language learning.