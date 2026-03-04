# OpenAI-Compatible API Proxy

一个轻量本地转发服务：将第三方大模型 API 转换为 OpenAI 兼容接口（`/v1/*`）。

## 功能

- 提供 `GET /v1/models`
- 转发 `GET/POST /v1/{path}` 到第三方上游
- 保留原始请求头（移除 `host` 和 `content-length`）
- 对 `chat/completions` 自动强制 `stream=true`（可按需修改）

## 快速启动

```bash
pip install -r requirements.txt
uvicorn proxy:app --host 0.0.0.0 --port 9000
```

## 配置上游

编辑 `proxy.py`：

```python
REAL_BASE = "https://ai.love-gwen.top/openai/v1"
```

## 示例

```bash
curl http://127.0.0.1:9000/v1/models
```

```bash
curl http://127.0.0.1:9000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"gpt-5.3-codex","messages":[{"role":"user","content":"hello"}]}'
```

## systemd（可选）

```ini
[Unit]
Description=OpenAI Proxy (local forwarder)
After=network.target

[Service]
WorkingDirectory=/opt/openai-proxy
ExecStart=/usr/bin/python3 -m uvicorn proxy:app --host 0.0.0.0 --port 9000
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```
