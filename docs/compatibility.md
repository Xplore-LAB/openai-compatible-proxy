# Compatibility

## Supported Endpoints

Current implementation supports:

- `GET /v1/models`
- `GET /v1/{path}`
- `POST /v1/{path}`

## Behavior Notes

- Requests are forwarded to `{REAL_BASE}/{path}`
- Query parameters are preserved
- Most incoming headers are forwarded
- `host` and `content-length` are removed before proxying
- `chat/completions` can be forced to `stream=true`

## Compatible Clients

These clients should work when they support custom API base URLs:

- OpenAI Python SDK
- OpenAI Node SDK
- Cherry Studio
- Open WebUI
- Dify
- Other OpenAI-compatible SDK consumers

## Caveats

- This project does not yet rewrite model ids dynamically
- Authentication behavior depends on your upstream
- Response normalization is intentionally minimal
