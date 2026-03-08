from openai import OpenAI

client = OpenAI(
    api_key="your-token",
    base_url="http://127.0.0.1:9000/v1",
)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "hello"}],
)

print(resp)
