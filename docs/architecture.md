# Architecture

```text
Clients / SDKs / Apps
        |
        v
OpenAI-Compatible API Proxy
        |
        v
Upstream LLM endpoint
```

## Flow

1. Clients send requests to the proxy using OpenAI-style `/v1/*` routes.
2. The proxy keeps a stable interface for downstream tools.
3. Requests are forwarded to `REAL_BASE`.
4. Responses are passed back with minimal transformation.

## Why this matters

This keeps downstream integrations stable while letting you swap or control the upstream provider behind the same API surface.
