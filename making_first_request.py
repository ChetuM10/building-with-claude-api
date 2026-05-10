from dotenv import load_dotenv
from anthropic import Anthropic
import os
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(api_key=api_key)
model = "claude-sonnet-4-6"

response = client.messages.create(
    model = model,
    max_tokens = 1000,
    messages = [
        {
            "role": "user",
            "content": "Who is Naruto Uzumaki? Answer in one sentence."
        }
    ]
)

print(response.model_dump_json(indent=2))
