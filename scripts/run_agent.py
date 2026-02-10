import os
from anthropic import Anthropic

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is not set")

client = Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Say hello from Claude"}
    ]
)

print(response.content[0].text)
