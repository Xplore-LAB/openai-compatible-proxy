# FAQ

## Why use this instead of calling the upstream directly?

Because many apps already speak the OpenAI API format. A compatibility layer reduces migration cost.

## Does this replace a full AI gateway?

No. This is a thin proxy focused on compatibility and simple forwarding.

## Can I use it with Open WebUI, Dify, or Cherry Studio?

Usually yes, as long as those tools allow a custom OpenAI-compatible base URL.

## Does it manage API keys?

Not by itself. It forwards requests to your configured upstream.

## Can I disable forced streaming?

Yes. Set `FORCE_CHAT_STREAM=false`.
