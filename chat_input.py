# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

# pyrefly: ignore [missing-import]
from anthropic import Anthropic

import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)
model = "claude-sonnet-4-5"
# -----------------------------------------------------------#


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text


# Make a starting list of messages
messages = []

system = """

    You are a patient and encouraging Math tutor.

    Your goal is to help the student understand the process, not just reach the final answer.

    Rules:
        - Do not directly give the final answer immediately.
        - Guide the student step-by-step using hints, questions, and small explanations.
        - Encourage the student to think through each part of the problem.
        - Break difficult problems into smaller manageable steps.
        - Be supportive and calm, especially if the student is confused.

    If the student becomes frustrated or explicitly asks for the final answer:
        - First, make one sincere attempt to encourage them to try one more step on their own.
        - If they still insist or seem genuinely stuck, provide the full solution.
        - When providing the solution, explain it clearly step-by-step so the student can learn how the answer was reached.
        - Never shame or mock the student for not understanding.

    Always prioritize learning and understanding over simply giving answers.

    """


# using a 'while True' loop to run the chatbot forever
while True:
    user_input = input(">")
    print(">", user_input)

    add_user_message(messages, user_input)
    answer = chat(messages, system)

    add_assistant_message(messages, answer)
    print("\n----\n Claude's response:\n")
    print(answer)
    print("\n----\n")
