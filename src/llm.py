import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

def ask_bot(message):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(message)
    return response.text


if __name__ == "__main__":
    print('Welcome to chatbot')
    print(ask_bot('WHats the capital of India?'))     

