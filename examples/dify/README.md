# Dify

When adding an OpenAI-compatible provider in Dify, use:

- Base URL: `http://127.0.0.1:9000/v1`
- API Key: your upstream-compatible token

If your upstream requires special headers or auth translation, add that logic in `proxy.py`.
