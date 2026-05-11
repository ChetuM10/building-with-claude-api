# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# pyrefly: ignore [missing-import]
from anthropic import Anthropic

import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)
model = "claude-sonnet-4-5"


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages):
    message = client.messages.create(model=model, max_tokens=1000, messages=messages)
    return message.content[0].text


# Make a starting list of messages
messages = []

# Add in the initial user question
add_user_message(messages, "Tell me about Naruto Uzumaki in one sentence.")

# Pass the list of messages into 'chat' to get an answer
answer = chat(messages)
print("\n Answer 1:", answer)


# ------------------------------------------------------------------#


# Take the answer and add it as an assistant message into our list
add_assistant_message(messages, answer)

# Add in the user's follow-up question
add_user_message(
    messages, "List me top 3 quotes from Naruto, including one of his own."
)

# Call chat again with the list of messages to get a final answer
answer = chat(messages)

# Final answer
print("\n Answer 2:", answer)
