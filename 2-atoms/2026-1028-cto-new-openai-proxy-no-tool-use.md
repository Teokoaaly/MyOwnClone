--- 
id: 2026-1028-cto-new-openai-proxy-no-tool-use
type: atom
certainty: tentative
sources: [sources/2026-10-28-cto-new-openai-proxy.md]
links: ["[[2026-1028-cto-new-openai-proxy-go-reverse-proxy]]", "[[2026-1028-cto-new-openai-proxy-turnstile-friction]]"]
---

## Claim

The proxy does not support OpenAI function calling or Anthropic `tool_use` because cto.new's `/engine-agent/chat` endpoint is itself a full coding agent with its own sandbox and system prompt; injecting the `tools` field at the proxy layer cannot hijack the upstream agent logic, which will emit its own agent reasoning instead of structured `tool_calls`.

## Why It Matters

This is a hard constraint: plain chat, code explanation/generation, documentation, and translation work fine. But Build/Agent modes in opencode/cline, Claude Code/Continue auto-coding tasks, and any pipeline depending on function calling must use providers that natively support it (official OpenAI/Anthropic relays). Users requiring tool use must route those calls through a different provider.

## Why It Matters (Alternative)

For read-only Plan mode (opencode/cline/continue.dev), the proxy is a good fit because it only serves chat completions without requiring structured tool responses.