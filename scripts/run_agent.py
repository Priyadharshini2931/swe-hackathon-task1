import os
import anthropic

api_key = os.environ.get("ANTHROPIC_API_KEY")

if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is not set")

client = anthropic.Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=200,
    messages=[
        {
            "role": "user",
            "content": "Say hello from Claude"
        }
    ]
)

print(message.content[0].text)
