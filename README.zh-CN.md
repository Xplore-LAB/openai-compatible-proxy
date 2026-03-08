# OpenAI 兼容代理

<p align="center">
  <img src="assets/banner.svg" alt="OpenAI-Compatible API Proxy 横幅" width="100%" />
</p>

<p align="center">
  <img src="assets/icon.svg" alt="OpenAI-Compatible API Proxy 图标" width="120" />
</p>

<p align="center">
  <a href="README.md">English Docs</a> · <a href="docs/architecture.md">架构说明</a>
</p>

在几分钟内，把任意大模型 API 包装成 OpenAI 兼容接口。

这是一个轻量代理层，用来把上游模型接口统一暴露为 OpenAI 风格的 `/v1/*` API，方便现有 SDK、客户端和工作流系统快速接入。

## 它解决什么问题

很多 AI 工具已经默认支持 OpenAI API，但你的真实上游可能是别家的模型服务、自建网关，或者内部统一出口。

这个项目的价值在于：

- 不重写现有客户端
- 不改造现有 OpenAI 集成链路
- 用一层轻代理完成模型接入兼容
- 方便后续做切换、治理和控成本

## 功能

- 提供 `GET /v1/models`
- 转发 `GET/POST /v1/{path}` 到上游
- 透传大部分请求头，自动移除冲突头
- 可选强制 `chat/completions` 使用 `stream=true`
- 支持环境变量配置
- 自带 Docker、Compose、systemd 和使用示例

## 最适合什么场景

- 把私有模型或第三方模型包装成 OpenAI 风格 API
- 沿用现有 OpenAI SDK，不重写客户端代码
- 让 Open WebUI、Dify、Cherry Studio 等工具直接接入
- 作为内部 AI 网关的轻量兼容层

## 快速启动

### 本地运行

```bash
cp .env.example .env
pip install -r requirements.txt
export $(grep -v '^#' .env | xargs)
uvicorn proxy:app --host 0.0.0.0 --port 9000
```

### Docker

```bash
cp .env.example .env
docker build -t openai-compatible-proxy .
docker run --rm -p 9000:9000 --env-file .env openai-compatible-proxy
```

### Docker Compose

```bash
cp .env.example .env
docker compose up -d --build
```

## 核心配置

- `REAL_BASE`：上游 OpenAI-compatible 地址
- `PROXY_MODELS`：`/v1/models` 返回的模型列表
- `FORCE_CHAT_STREAM`：是否强制聊天接口流式返回
- `PROXY_TIMEOUT`：上游超时秒数
- `PROXY_TITLE`：根路径显示的服务标题

详情见 `.env.example`。

## 适合接什么

- OpenAI Python SDK
- OpenAI Node SDK
- Cherry Studio
- Open WebUI
- Dify
- 任何支持 `base_url` / `api_base` 的客户端

## 架构说明

<p align="center">
  <img src="assets/banner.svg" alt="架构横幅" width="100%" />
</p>

可在 `docs/architecture.md` 查看简化后的请求链路和定位说明。

## 项目结构

```text
.
├── assets/
│   └── icon.svg
├── proxy.py
├── requirements.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── docs/
│   ├── compatibility.md
│   ├── deployment.md
│   ├── faq.md
│   └── troubleshooting.md
└── examples/
    ├── python-openai-sdk/
    ├── cherry-studio/
    ├── open-webui/
    └── dify/
```

## 文档

- `README.md`
- `docs/compatibility.md`
- `docs/deployment.md`
- `docs/faq.md`
- `docs/troubleshooting.md`

## 适用场景

- 把非 OpenAI 上游包装成统一接口
- 给多个内部工具提供稳定的模型出口
- 在不改客户端的情况下切换模型供应商
- 做私有部署、统一网关或模型中转

## 谁适合用

- 已经依赖 OpenAI SDK 的开发者
- 想摆脱单一模型供应商绑定的团队
- 想先上兼容层、后面再演进到完整 AI 网关的项目
- 需要给工具、自动化和内部平台提供稳定 API 的团队

## 路线图

见 `ROADMAP.md`。

## 更新记录

见 `CHANGELOG.md`。

## 许可证

MIT
