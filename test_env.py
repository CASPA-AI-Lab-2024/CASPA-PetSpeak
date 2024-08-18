import openai

from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "You are a comedian."},
    {"role": "user", "content": "Tell me a 20 word joke"}
]


response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=messages,
    max_tokens=50
)

print(response['choices'][0]['message']['content'].strip())