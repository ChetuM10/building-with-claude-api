from dotenv import load_dotenv
from anthropic import Anthropic
import os
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)
model = "claude-sonnet-4-5"

def add_user_message(messages, text):
    user_message = { "role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = { "role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages):
    message = client.messages.create(
        model = model,
        max_tokens = 1000,
        messages = messages
    )
    return message.content[0].text



# Make a starting list of messages
messages = []

#using a 'while True' loop to run the chatbot forever
while True:
    user_input = input(">")
    print(">", user_input)

    add_user_message(messages, user_input)
    answer = chat(messages)

    add_assistant_message(messages, answer)
    print("\n----\n Claude's response:\n")
    print(answer)
    print("\n----\n")