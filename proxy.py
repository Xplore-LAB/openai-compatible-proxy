import json
import os
from typing import List

import httpx
from fastapi import FastAPI, Request, Response

DEFAULT_MODELS = ["gpt-5", "gpt-5.3-codex"]


def get_env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_models() -> List[str]:
    raw = os.getenv("PROXY_MODELS", ",".join(DEFAULT_MODELS)).strip()
    if not raw:
        return DEFAULT_MODELS
    return [item.strip() for item in raw.split(",") if item.strip()]


REAL_BASE = os.getenv("REAL_BASE", "https://ai.love-gwen.top/openai/v1").rstrip("/")
PROXY_TIMEOUT = float(os.getenv("PROXY_TIMEOUT", "120"))
FORCE_CHAT_STREAM = get_env_bool("FORCE_CHAT_STREAM", True)
PROXY_TITLE = os.getenv("PROXY_TITLE", "OpenAI-Compatible API Proxy")

app = FastAPI(title=PROXY_TITLE)


@app.get("/")
async def index():
    return {
        "name": PROXY_TITLE,
        "upstream": REAL_BASE,
        "models_endpoint": "/v1/models",
        "health_endpoint": "/healthz",
    }


@app.get("/healthz")
async def healthz():
    return {"ok": True, "upstream": REAL_BASE}


@app.get("/v1/models")
async def models():
    return {
        "object": "list",
        "data": [
            {"id": model_id, "object": "model", "owned_by": "proxy"}
            for model_id in get_models()
        ],
    }


@app.api_route("/v1/{path:path}", methods=["GET", "POST"])
async def proxy(request: Request, path: str):
    url = f"{REAL_BASE}/{path}"

    body = await request.body()
    headers = dict(request.headers)

    headers.pop("host", None)
    headers.pop("content-length", None)

    if FORCE_CHAT_STREAM and path == "chat/completions":
        try:
            data = json.loads(body)
            data["stream"] = True
            body = json.dumps(data).encode()
        except Exception:
            pass

    async with httpx.AsyncClient(timeout=PROXY_TIMEOUT) as client:
        resp = await client.request(
            request.method,
            url,
            content=body,
            headers=headers,
            params=request.query_params,
        )

    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=dict(resp.headers),
        media_type=resp.headers.get("content-type"),
    )
