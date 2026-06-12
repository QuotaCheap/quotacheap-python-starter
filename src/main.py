import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("QUOTACHEAP_API_KEY")
base_url = os.environ.get("QUOTACHEAP_BASE_URL", "https://api.quota.cheap/v1")
model = os.environ.get("QUOTACHEAP_MODEL", "gpt-5.4-mini")

if not api_key:
    raise SystemExit("Set QUOTACHEAP_API_KEY in .env first.")

client = OpenAI(api_key=api_key, base_url=base_url)

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a concise developer assistant."},
        {"role": "user", "content": "Write one sentence about why API usage logs matter."},
    ],
)

print(response.choices[0].message.content)
