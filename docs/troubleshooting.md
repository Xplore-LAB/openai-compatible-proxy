# Troubleshooting

## 502 / upstream timeout

- Check `REAL_BASE`
- Check upstream network reachability
- Increase `PROXY_TIMEOUT`

## Client cannot connect

- Confirm the service is listening on the expected host and port
- Check firewall and reverse proxy config

## `GET /v1/models` returns the wrong models

- Update `PROXY_MODELS`
- Restart the service after changing env vars

## Streaming behaves unexpectedly

- Set `FORCE_CHAT_STREAM=false` if your upstream or client expects non-streaming responses

## Auth issues

- Confirm your client is sending the correct `Authorization` header
- Confirm the upstream accepts the forwarded token format
