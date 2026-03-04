from fastapi import FastAPI, Request, Response
import httpx
import json

app = FastAPI()

REAL_BASE = "https://ai.love-gwen.top/openai/v1"

@app.get("/v1/models")
async def models():
    return {
        "object": "list",
        "data": [
            {"id": "gpt-5", "object": "model", "owned_by": "custom"},
            {"id": "gpt-5.3-codex", "object": "model", "owned_by": "custom"},
        ],
    }

@app.api_route("/v1/{path:path}", methods=["GET", "POST"])
async def proxy(request: Request, path: str):
    url = f"{REAL_BASE}/{path}"

    body = await request.body()
    headers = dict(request.headers)

    headers.pop("host", None)
    headers.pop("content-length", None)  # ⭐ 关键修复

    if path == "chat/completions":
        try:
            data = json.loads(body)
            data["stream"] = True
            body = json.dumps(data).encode()
        except:
            pass

    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.request(
            request.method,
            url,
            content=body,
            headers=headers,
        )

    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=dict(resp.headers),
    )
