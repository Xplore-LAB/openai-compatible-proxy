# Deployment

## Local

```bash
cp .env.example .env
pip install -r requirements.txt
export $(grep -v '^#' .env | xargs)
uvicorn proxy:app --host 0.0.0.0 --port 9000
```

## Docker

```bash
docker build -t openai-compatible-proxy .
docker run --rm -p 9000:9000 --env-file .env openai-compatible-proxy
```

## Docker Compose

```bash
docker compose up -d --build
```

## systemd

```ini
[Unit]
Description=OpenAI-Compatible API Proxy
After=network.target

[Service]
WorkingDirectory=/opt/openai-compatible-proxy
EnvironmentFile=/opt/openai-compatible-proxy/.env
ExecStart=/usr/bin/python3 -m uvicorn proxy:app --host 0.0.0.0 --port 9000
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

## Reverse Proxy

You can place Nginx or Caddy in front of this service if you need:

- TLS termination
- auth layer
- domain binding
- rate limiting
