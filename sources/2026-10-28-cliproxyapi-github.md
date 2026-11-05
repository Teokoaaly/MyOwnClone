---
url: https://github.com/router-for-me/CLIProxyAPI
captured: 2026-10-28
word_count: 5355
status: raw
---

[Skip to content](https://github.com/router-for-me/CLIProxyAPI#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/router-for-me/CLIProxyAPI) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/router-for-me/CLIProxyAPI) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/router-for-me/CLIProxyAPI) to refresh your session.Dismiss alert

{{ message }}

main

[**5** Branches](https://github.com/router-for-me/CLIProxyAPI/branches) [**1159** Tags](https://github.com/router-for-me/CLIProxyAPI/tags)

[Go to Branches page](https://github.com/router-for-me/CLIProxyAPI/branches)[Go to Tags page](https://github.com/router-for-me/CLIProxyAPI/tags)

Go to file

Code

Open more actions menu

## Latest commit

[![luispater](https://avatars.githubusercontent.com/u/4966831?v=4&size=40)](https://github.com/luispater)[luispater](https://github.com/router-for-me/CLIProxyAPI/commits?author=luispater)

[fix(responses): reject late websocket interrupts after terminal events](https://github.com/router-for-me/CLIProxyAPI/commit/9717e325ba6ab2c7483ea93ccb5f2047eb2e7dd5)

Open commit detailssuccess

12 hours agoOct 28, 2026

[9717e32](https://github.com/router-for-me/CLIProxyAPI/commit/9717e325ba6ab2c7483ea93ccb5f2047eb2e7dd5) · 12 hours agoOct 28, 2026

## History

[4,589 Commits](https://github.com/router-for-me/CLIProxyAPI/commits/main/)

Open commit details

[View commit history for this file.](https://github.com/router-for-me/CLIProxyAPI/commits/main/) 4,589 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [.github](https://github.com/router-for-me/CLIProxyAPI/tree/main/.github ".github") | [.github](https://github.com/router-for-me/CLIProxyAPI/tree/main/.github ".github") | [ci(workflow): bump Go version to 1.26.10 in release pipeline](https://github.com/router-for-me/CLIProxyAPI/commit/ceb045a129d43f805e93a5e4aef3a59b108f34f7 "ci(workflow): bump Go version to 1.26.10 in release pipeline  - Update GO_VERSION environment variable to `1.26.10` in the release workflow configuration.") | last weekOct 22, 2026 |
| [assets](https://github.com/router-for-me/CLIProxyAPI/tree/main/assets "assets") | [assets](https://github.com/router-for-me/CLIProxyAPI/tree/main/assets "assets") | [docs(readme): remove APIMart sponsor sections and assets](https://github.com/router-for-me/CLIProxyAPI/commit/1f917e77c4562623aa49e9804d999524151a2f96 "docs(readme): remove APIMart sponsor sections and assets  - Remove APIMart sponsor entries from README.md, README_CN.md, and README_JA.md. - Delete associated sponsor image assets for APIMart.") | 2 days agoOct 26, 2026 |
| [auths](https://github.com/router-for-me/CLIProxyAPI/tree/main/auths "auths") | [auths](https://github.com/router-for-me/CLIProxyAPI/tree/main/auths "auths") | [rebuild branch](https://github.com/router-for-me/CLIProxyAPI/commit/f5dc380b636c4fb9dd50a37cb54b52fb6693d3df "rebuild branch") | last yearSep 25, 2025 |
| [cmd](https://github.com/router-for-me/CLIProxyAPI/tree/main/cmd "cmd") | [cmd](https://github.com/router-for-me/CLIProxyAPI/tree/main/cmd "cmd") | [feat(devin): aggregate swe-2 lightning UIDs into swe-2-lightning model](https://github.com/router-for-me/CLIProxyAPI/commit/3dae075de2724d0d24140a170774b855ca5b4253 "feat(devin): aggregate swe-2 lightning UIDs into swe-2-lightning model  - Aggregate -{level}-lightning compound suffixes into a single swe-2-lightning catalog entry and preserve the Lightning display name suffix across registry and fetch_devin_models. - Resolve -lightning base models into stem-{effort}-lightning UIDs while passing through complete upstream lightning UIDs and regenerating the embedded Devin catalog.  Closes: #6975") | 3 days agoOct 25, 2026 |
| [docs](https://github.com/router-for-me/CLIProxyAPI/tree/main/docs "docs") | [docs](https://github.com/router-for-me/CLIProxyAPI/tree/main/docs "docs") | [docs(discovery): describe LAN resolution limits and trust boundaries](https://github.com/router-for-me/CLIProxyAPI/commit/999526c76def7063e9baa09c1ea2750e8cf5a5b6 "docs(discovery): describe LAN resolution limits and trust boundaries") | 2 days agoOct 26, 2026 |
| [examples](https://github.com/router-for-me/CLIProxyAPI/tree/main/examples "examples") | [examples](https://github.com/router-for-me/CLIProxyAPI/tree/main/examples "examples") | [chore(deps): bump Go version to 1.26.10 and update dependencies](https://github.com/router-for-me/CLIProxyAPI/commit/633a294f4c3ab043ff3849aedc06d40c2c57994f "chore(deps): bump Go version to 1.26.10 and update dependencies  - Update Go version to 1.26.10 across modules. - Update indirect and direct dependencies including go-git, golang.org/x packages, and plugin go.mod files.") | last weekOct 22, 2026 |
| [internal](https://github.com/router-for-me/CLIProxyAPI/tree/main/internal "internal") | [internal](https://github.com/router-for-me/CLIProxyAPI/tree/main/internal "internal") | [fix(responses): reject late websocket interrupts after terminal events](https://github.com/router-for-me/CLIProxyAPI/commit/9717e325ba6ab2c7483ea93ccb5f2047eb2e7dd5 "fix(responses): reject late websocket interrupts after terminal events  - Track the running response identity in the Codex websocket session and reject interrupts that do not target it, so an interrupt after response.completed is never forwarded upstream while turn teardown is pending. - Gate the handler's local interrupt path by explicit turn ownership and close it before terminal payloads are written downstream, preventing fabricated response.incomplete events and silently dropped claimed frames. - Add deterministic regression tests covering late and unknown interrupts across completion, failure, queued rejection, upstream loss, and HTTP fallback turns.  Closes: #7065") | 12 hours agoOct 28, 2026 |
| [sdk](https://github.com/router-for-me/CLIProxyAPI/tree/main/sdk "sdk") | [sdk](https://github.com/router-for-me/CLIProxyAPI/tree/main/sdk "sdk") | [fix(responses): reject late websocket interrupts after terminal events](https://github.com/router-for-me/CLIProxyAPI/commit/9717e325ba6ab2c7483ea93ccb5f2047eb2e7dd5 "fix(responses): reject late websocket interrupts after terminal events  - Track the running response identity in the Codex websocket session and reject interrupts that do not target it, so an interrupt after response.completed is never forwarded upstream while turn teardown is pending. - Gate the handler's local interrupt path by explicit turn ownership and close it before terminal payloads are written downstream, preventing fabricated response.incomplete events and silently dropped claimed frames. - Add deterministic regression tests covering late and unknown interrupts across completion, failure, queued rejection, upstream loss, and HTTP fallback turns.  Closes: #7065") | 12 hours agoOct 28, 2026 |
| [test](https://github.com/router-for-me/CLIProxyAPI/tree/main/test "test") | [test](https://github.com/router-for-me/CLIProxyAPI/tree/main/test "test") | [fix(schema): preserve Gemini $ref sibling constraints](https://github.com/router-for-me/CLIProxyAPI/commit/29150a2262b4e9d102986c7775d794c7122670a7 "fix(schema): preserve Gemini $ref sibling constraints  - Preserve root and nested reference conjunctions without changing sibling evaluation scope. - Prevent JSON Schema cleanup from weakening retained conjunctions. - Add regression coverage for reference constraints and Gemini translation paths.  Closes: #6897") | 5 days agoOct 23, 2026 |
| [.dockerignore](https://github.com/router-for-me/CLIProxyAPI/blob/main/.dockerignore ".dockerignore") | [.dockerignore](https://github.com/router-for-me/CLIProxyAPI/blob/main/.dockerignore ".dockerignore") | [chore(docker): simplify `.dockerignore` patterns by removing wildcard…](https://github.com/router-for-me/CLIProxyAPI/commit/b94178bfd9df0accf2c373c287e9b32bdbbf2030 "chore(docker): simplify `.dockerignore` patterns by removing wildcard entries") | 4 months agoJun 13, 2026 |
| [.env.cluster.example](https://github.com/router-for-me/CLIProxyAPI/blob/main/.env.cluster.example ".env.cluster.example") | [.env.cluster.example](https://github.com/router-for-me/CLIProxyAPI/blob/main/.env.cluster.example ".env.cluster.example") | [feat(docker): add cluster-specific docker-compose configuration for C…](https://github.com/router-for-me/CLIProxyAPI/commit/7efc1629baa9cda4a9c957d095e7c4796cfc14ec "feat(docker): add cluster-specific docker-compose configuration for CLIProxyAPI") | 5 months agoMay 19, 2026 |
| [.env.example](https://github.com/router-for-me/CLIProxyAPI/blob/main/.env.example ".env.example") | [.env.example](https://github.com/router-for-me/CLIProxyAPI/blob/main/.env.example ".env.example") | [Add Object Storage](https://github.com/router-for-me/CLIProxyAPI/commit/9ef76dcc61f70c6373ede2638767dc263fff7425 "Add Object Storage") | last yearOct 15, 2025 |
| [.gitignore](https://github.com/router-for-me/CLIProxyAPI/blob/main/.gitignore ".gitignore") | [.gitignore](https://github.com/router-for-me/CLIProxyAPI/blob/main/.gitignore ".gitignore") | [docs: prune obsolete management notes](https://github.com/router-for-me/CLIProxyAPI/commit/b1a33b80dc4c77baa1cc7fd977155998ba7860a5 "docs: prune obsolete management notes") | last monthSep 27, 2026 |
| [AGENTS.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/AGENTS.md "AGENTS.md") | [AGENTS.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/AGENTS.md "AGENTS.md") | [feat(payload): introduce payload finalizer for protobuf and multipart…](https://github.com/router-for-me/CLIProxyAPI/commit/868e137f6c1dd10bc78a4e6fcdee99889f8af77d "feat(payload): introduce payload finalizer for protobuf and multipart requests  - Add `PayloadFinalizer` to apply configuration rules at the final serialization barrier - Support decoding, modifying, and re-encoding Devin protobuf business fields - Add multipart form-data payload normalization to JSON for media payload rules  Closes: #5067") | last monthOct 3, 2026 |
| [CLAUDE.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/CLAUDE.md "CLAUDE.md") | [CLAUDE.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/CLAUDE.md "CLAUDE.md") | [feat(api): add support for local management password validation and s…](https://github.com/router-for-me/CLIProxyAPI/commit/605adaa3c22b51de8d6c1930237780b80c0c28ad "feat(api): add support for local management password validation and spoofed IP rejection  - Introduced `newTestServerWithOptions` to customize server initialization in tests. - Added `TestManagementLocalPasswordRejectsSpoofedForwardedFor` to validate security against spoofed `X-Forwarded-For` headers. - Enabled default WebSocket authentication (`ws-auth`) in `config.example.yaml`. - Disabled trusted proxy headers in Gin engine with appropriate logging to enhance security.") | 5 months agoMay 17, 2026 |
| [Dockerfile](https://github.com/router-for-me/CLIProxyAPI/blob/main/Dockerfile "Dockerfile") | [Dockerfile](https://github.com/router-for-me/CLIProxyAPI/blob/main/Dockerfile "Dockerfile") | [chore(build): include `ca-certificates` in Docker image for improved …](https://github.com/router-for-me/CLIProxyAPI/commit/d55f215c63864dd612c01a00ca56a2a4107d0abb "chore(build): include `ca-certificates` in Docker image for improved HTTPS support") | 4 months agoJun 8, 2026 |
| [LICENSE](https://github.com/router-for-me/CLIProxyAPI/blob/main/LICENSE "LICENSE") | [LICENSE](https://github.com/router-for-me/CLIProxyAPI/blob/main/LICENSE "LICENSE") | [Update LICENSE to reflect extended copyright ownership](https://github.com/router-for-me/CLIProxyAPI/commit/9c6832cc22a1234edde72fe279bb1b3ae042b03e "Update LICENSE to reflect extended copyright ownership") | last yearOct 11, 2025 |
| [README.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/README.md "README.md") | [README.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/README.md "README.md") | [Merge pull request](https://github.com/router-for-me/CLIProxyAPI/commit/f6d29ec7330d58a765e1e282336d46fae639bace "Merge pull request #6989 from kdcokenny/docs/kimi-k31-availability  docs(readme): update Kimi and OpenAI model availability") [#6989](https://github.com/router-for-me/CLIProxyAPI/pull/6989) [from kdcokenny/docs/kimi-k31-availability](https://github.com/router-for-me/CLIProxyAPI/commit/f6d29ec7330d58a765e1e282336d46fae639bace "Merge pull request #6989 from kdcokenny/docs/kimi-k31-availability  docs(readme): update Kimi and OpenAI model availability") | yesterdayOct 27, 2026 |
| [README\_CN.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/README_CN.md "README_CN.md") | [README\_CN.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/README_CN.md "README_CN.md") | [Merge pull request](https://github.com/router-for-me/CLIProxyAPI/commit/f6d29ec7330d58a765e1e282336d46fae639bace "Merge pull request #6989 from kdcokenny/docs/kimi-k31-availability  docs(readme): update Kimi and OpenAI model availability") [#6989](https://github.com/router-for-me/CLIProxyAPI/pull/6989) [from kdcokenny/docs/kimi-k31-availability](https://github.com/router-for-me/CLIProxyAPI/commit/f6d29ec7330d58a765e1e282336d46fae639bace "Merge pull request #6989 from kdcokenny/docs/kimi-k31-availability  docs(readme): update Kimi and OpenAI model availability") | yesterdayOct 27, 2026 |
| [README\_JA.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/README_JA.md "README_JA.md") | [README\_JA.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/README_JA.md "README_JA.md") | [Merge pull request](https://github.com/router-for-me/CLIProxyAPI/commit/f6d29ec7330d58a765e1e282336d46fae639bace "Merge pull request #6989 from kdcokenny/docs/kimi-k31-availability  docs(readme): update Kimi and OpenAI model availability") [#6989](https://github.com/router-for-me/CLIProxyAPI/pull/6989) [from kdcokenny/docs/kimi-k31-availability](https://github.com/router-for-me/CLIProxyAPI/commit/f6d29ec7330d58a765e1e282336d46fae639bace "Merge pull request #6989 from kdcokenny/docs/kimi-k31-availability  docs(readme): update Kimi and OpenAI model availability") | yesterdayOct 27, 2026 |
| [config.example.yaml](https://github.com/router-for-me/CLIProxyAPI/blob/main/config.example.yaml "config.example.yaml") | [config.example.yaml](https://github.com/router-for-me/CLIProxyAPI/blob/main/config.example.yaml "config.example.yaml") | [refactor(api): reuse response compression encoders and add tests](https://github.com/router-for-me/CLIProxyAPI/commit/a3e76891b1a149d9cb4dd718dd54db06f976d987 "refactor(api): reuse response compression encoders and add tests") | 20 hours agoOct 28, 2026 |
| [docker-build.ps1](https://github.com/router-for-me/CLIProxyAPI/blob/main/docker-build.ps1 "docker-build.ps1") | [docker-build.ps1](https://github.com/router-for-me/CLIProxyAPI/blob/main/docker-build.ps1 "docker-build.ps1") | [rebuild branch](https://github.com/router-for-me/CLIProxyAPI/commit/f5dc380b636c4fb9dd50a37cb54b52fb6693d3df "rebuild branch") | last yearSep 25, 2025 |
| [docker-build.sh](https://github.com/router-for-me/CLIProxyAPI/blob/main/docker-build.sh "docker-build.sh") | [docker-build.sh](https://github.com/router-for-me/CLIProxyAPI/blob/main/docker-build.sh "docker-build.sh") | [chore: remove usage tracking and logging functionality](https://github.com/router-for-me/CLIProxyAPI/commit/18bb9c315fced2c428f57b4a0e66b06183c46c06 "chore: remove usage tracking and logging functionality  - Deleted the `LoggerPlugin` along with associated usage tracking and in-memory statistics logic. - Removed all related tests (`logger_plugin_test.go`, `usage_tab_test.go`) and external-facing handler (`usage.go`) for usage statistics export/import. - Cleaned up TUI integration by deleting `usage_tab.go`.") | 6 months agoMay 1, 2026 |
| [docker-compose.cluster.yml](https://github.com/router-for-me/CLIProxyAPI/blob/main/docker-compose.cluster.yml "docker-compose.cluster.yml") | [docker-compose.cluster.yml](https://github.com/router-for-me/CLIProxyAPI/blob/main/docker-compose.cluster.yml "docker-compose.cluster.yml") | [feat(docker): add plugin volume mapping to docker-compose files](https://github.com/router-for-me/CLIProxyAPI/commit/01f387f44754af09783ac52a2051cb2c66a7bf44 "feat(docker): add plugin volume mapping to docker-compose files") | 3 months agoJul 21, 2026 |
| [docker-compose.yml](https://github.com/router-for-me/CLIProxyAPI/blob/main/docker-compose.yml "docker-compose.yml") | [docker-compose.yml](https://github.com/router-for-me/CLIProxyAPI/blob/main/docker-compose.yml "docker-compose.yml") | [feat(docker): add plugin volume mapping to docker-compose files](https://github.com/router-for-me/CLIProxyAPI/commit/01f387f44754af09783ac52a2051cb2c66a7bf44 "feat(docker): add plugin volume mapping to docker-compose files") | 3 months agoJul 21, 2026 |
| [go.mod](https://github.com/router-for-me/CLIProxyAPI/blob/main/go.mod "go.mod") | [go.mod](https://github.com/router-for-me/CLIProxyAPI/blob/main/go.mod "go.mod") | [fix(discovery): resolve split mDNS responses with scoped bounded caches](https://github.com/router-for-me/CLIProxyAPI/commit/11e5f67bdb36c42af94ab5338440975f2b4f3746 "fix(discovery): resolve split mDNS responses with scoped bounded caches  Validate draft TXT values and RFC 3986 paths without legacy schema mixing; preserve first-key-wins and legacy base-path compatibility. Validate RFC 6335 names, filter unusable addresses, and display scoped IPv6 and WebSocket URLs.  Replace the single-packet browser with per-interface RR caching, source validation, TTL and cache-flush handling, PTR maintenance and known-answer suppression. Add deterministic split-order, capacity, expiry, scope and schema regression tests.") | 2 days agoOct 26, 2026 |
| [go.sum](https://github.com/router-for-me/CLIProxyAPI/blob/main/go.sum "go.sum") | [go.sum](https://github.com/router-for-me/CLIProxyAPI/blob/main/go.sum "go.sum") | [chore(deps): bump Go version to 1.26.10 and update dependencies](https://github.com/router-for-me/CLIProxyAPI/commit/633a294f4c3ab043ff3849aedc06d40c2c57994f "chore(deps): bump Go version to 1.26.10 and update dependencies  - Update Go version to 1.26.10 across modules. - Update indirect and direct dependencies including go-git, golang.org/x packages, and plugin go.mod files.") | last weekOct 22, 2026 |
| View all files |

## Repository files navigation

# CLI Proxy API

[Permalink: CLI Proxy API](https://github.com/router-for-me/CLIProxyAPI#cli-proxy-api)

English \| [中文](https://github.com/router-for-me/CLIProxyAPI/blob/main/README_CN.md) \| [日本語](https://github.com/router-for-me/CLIProxyAPI/blob/main/README_JA.md)

If you want to use CLIProxyAPI on your desktop, we recommend our [EasyCLIProxyAPI](https://github.com/router-for-me/EasyCLIProxyAPI) desktop client. It provides a graphical configuration UI, automatic updates, system tray integration, and one-click start/stop for the CLIProxyAPI service.

CLIProxyAPI is a proxy server that provides OpenAI/Gemini/Claude/Codex/Grok compatible API interfaces for CLI.

You can access the following providers locally and with multiple CLI accounts through any OpenAI (including Responses), Gemini (including Interactions), or Claude-compatible client or SDK.

| Provider | Description |
| :-: | :-: |
| [![Kimi](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/logo/kimi.svg)](https://www.kimi.com/code/?aff=cliproxyapi) | Kimi series models (Kimi K3.1 Pro, K3.1 Pro Highspeed, K3, K2.8 Preview, etc.). [Kimi K3](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart) is Moonshot AI’s previous-generation flagship and the world’s first open 3T-class model. With 2.8 trillion parameters, native vision, and a 1-million-token context window, K3 is built for long-horizon coding, knowledge work, and reasoning. CLIProxyAPI supports Kimi through OAuth or compatible API interfaces. Try a **Kimi Code plan** ( [中文站](https://www.kimi.com/code?aff=cliproxyapi) \| [Global](https://www.kimi.ai/code?aff=cliproxyapi)), or get an **API key** from the Kimi Open Platform ( [中文站](https://platform.kimi.com/?track_id=track-f15622e7182046baa22ca35e006e13a7&aff=cliproxyapi) \| [Global](https://platform.kimi.ai/?track_id=track-8a28e4b291d84f62af2fccc3e7a21cb3&aff=cliproxyapi)). Thanks to Kimi for supporting CLIProxyAPI and the open-source community! |
| [![OpenAI](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/logo/openai.svg)](https://developers.openai.com/api/docs/models) | OpenAI GPT-6 models (GPT-6 Astra, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Luna), including access through Codex OAuth. Astra is the flagship for complex reasoning and coding, Sol balances capability and cost, Terra focuses on visual reasoning and computer use, and Luna handles focused, high-volume work. |
| [![Anthropic](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/logo/claude.svg)](https://www.anthropic.com/claude/fable) | Anthropic Claude models (Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5). Fable 5.1 is built for ambitious, long-running coding and knowledge work; Opus 5.5 brings strong agentic coding at a lower cost. |
| [![Antigravity](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/logo/antigravity.svg)](https://antigravity.google/) | Google Gemini models include Gemini 4 Argon and Gemini 3.8 Flash. CLIProxyAPI supports Gemini API, AI Studio, Vertex AI, Gemini CLI, and Antigravity accounts; model availability varies by channel. Gemini 3.8 Flash is Google's latest Flash model for long-horizon software engineering and agentic workflows. Antigravity's [official model availability](https://antigravity.google/docs/models/) lists Claude Sonnet 5.5 (thinking) and Claude Opus 5.5 (thinking) for Google AI Pro (non-trial), Google AI Ultra, and Enterprise. |
| [![xAI](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/logo/xai.svg)](https://docs.x.ai/developers/grok-4-7) | xAI Grok models (Grok 4.7, Grok 4.7 Build Fast, etc.). Grok 4.7 is SpaceXAI's latest model for coding, agentic tasks, and knowledge work. |
| [![Meta](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/logo/meta.svg)](https://dev.meta.ai/docs/overview) | Meta Muse models (Muse Wonder Full, Muse Wonder, Muse Spark 1.3, etc.). CLIProxyAPI supports Muse Code accounts through Meta login and Meta Model API keys, with Muse Spark 1.3 for coding and agentic workflows. Meta has announced Muse Wonder for Meta Model API and Muse Code, and Muse Wonder Full for Muse Code subscribers. |
| [Devin](https://devin.ai/cli) | Devin models (SWE-2, GPT-6 Astra, Claude Fable 5.1, etc.). Connect a Devin account with `--devin-login` to route the models available to that account. |

## Sponsor

[Permalink: Sponsor](https://github.com/router-for-me/CLIProxyAPI#sponsor)

[![https://www.packyapi.com/register?aff=cliproxyapi](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/packycode-en.png)](https://www.packyapi.com/register?aff=cliproxyapi)

Thanks to PackyCode for sponsoring this project!

PackyCode is a reliable and efficient API relay service provider, offering relay services for Claude Code, Codex, Gemini, and more.

PackyCode provides special discounts for our software users: register using [this link](https://www.packyapi.com/register?aff=cliproxyapi) and enter the "cliproxyapi" promo code during recharge to get 10% off.

* * *

|     |     |
| --- | --- |
| [![AICodeMirror](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/aicodemirror.png)](https://www.aicodemirror.ai/register?invitecode=TJNAIF) | Thanks to AICodeMirror for sponsoring this project! AICodeMirror provides official high-stability relay services for Claude Code / Codex / Gemini, with enterprise-grade concurrency, fast invoicing, and 24/7 dedicated technical support. Claude Code / Codex / Gemini official channels at 38% / 2% / 9% of original price, with extra discounts on top-ups! AICodeMirror offers special benefits for CLIProxyAPI users: register via [this link](https://www.aicodemirror.ai/register?invitecode=TJNAIF) to enjoy 20% off your first top-up, and enterprise customers can get up to 25% off! |
| [![APIKEY.FUN](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/apikey.png)](https://apikey.fan/register?aff=CLIProxyAPI) | Thanks to APIKEY.FUN for sponsoring this project! APIKEY.FUN is a professional enterprise-grade AI relay platform dedicated to providing stable, efficient, and low-cost AI model API access for enterprises and individual developers. The platform supports popular mainstream models such as Claude, OpenAI, and Gemini, with prices as low as 7% of the official price. Register through this project's [exclusive link](https://apikey.fan/register?aff=CLIProxyAPI) to enjoy a special **permanent 5% top-up discount**. |
| [![FennoAI](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/fennoai.png)](https://api.fenno.ai/s/Cvf0) | FennoAI is a stable and efficient API relay service provider, currently focused on Codex relay services. It is compatible with OpenAI and Anthropic protocols and can flexibly integrate with mainstream coding tools such as Codex, Claude Code, and OpenCode. It can reliably support enterprise-grade demand of hundreds of billions of tokens per day, with B2B settlement and invoicing available for both domestic and overseas entities. FennoAI offers an exclusive benefit for CLIProxyAPI users: purchase a subscription through the [exclusive link](https://api.fenno.ai/s/Cvf0) and receive $50 worth of Coding Plan credits for just $1.99. Referral rewards are also available: earn up to 20% commission when invited friends make a purchase. The more friends you invite, the greater the rewards. |
| [![Qiniu Cloud AI](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/qiniucloud.png)](https://s.qiniu.com/7zUJri) | Thanks to [Qiniu Cloud AI](https://s.qiniu.com/7zUJri) for sponsoring this project! Qiniu Cloud AI is an enterprise-grade large-model MaaS platform under Qiniu Cloud (02567.HK). It provides one-stop access to 150+ mainstream global models, is compatible with protocols from major global model providers, and covers full-modal processing capabilities for text, image, audio, video, and files. It serves more than 1.69 million enterprise and developer users. Exclusive benefits: enterprise users can claim 12 million free tokens, and invite friends to earn up to tens of billions of tokens. |
| [![Cubence](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/cubence.png)](https://cubence.com/signup?code=CLIPROXYAPI&source=cpa) | Thanks to Cubence for sponsoring this project! Cubence is a reliable and efficient API relay service provider, offering relay services for Claude Code, Codex, Gemini, and more. Cubence provides special discounts for our software users: register using [this link](https://cubence.com/signup?code=CLIPROXYAPI&source=cpa) and enter the "CLIPROXYAPI" promo code during recharge to get 10% off. |
| [![Bestproxy](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/bestproxy.png)](https://bestproxy.com/?keyword=ayh7otlb) | Bestproxy provides high-purity residential IPs with dedicated one-IP-per-account support. 🟡Residential Proxy - $0.5/GB；🟡Static Residential Proxy - Starting at $3/IP；🟡Unlimited Residential Proxy - Starting at $67/Day. ✅ [Get Free Trial.](https://bestproxy.com/?keyword=ayh7otlb) |
| [![Swiftproxy](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/swiftproxy.png)](https://www.swiftproxy.net/?code=PR67S9A95) | Swiftproxy provides 90M+ clean residential IPs across 220+ locations, supporting HTTP(S)/SOCKS5, IP rotation, Sticky Sessions, and precise location targeting. It helps AI API tools and automation workflows access online services reliably from different locations, making it ideal for API requests, web access, data collection, and location-based testing. Residential proxies from $0.7/GB. Free testing is available, with 10% off using code PROXY90. [Try Swiftproxy Now](https://www.swiftproxy.net/?code=PR67S9A95) |
| [![RapidProxy](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/rapidproxy.png)](https://www.rapidproxy.io/?code=KHM9B6E6M) | [RapidProxy](https://www.rapidproxy.io/?code=KHM9B6E6M) is a high-performance proxy provider built for automation and multi-account operations, offering clean residential proxies and native static ISP IPs. With 90M+ residential IPs worldwide, smart rotation, stable sessions, and high-concurrency support, RapidProxy is ideal for web scraping, browser automation, social media account management, e-commerce operations, bulk account registration, and more. Residential proxies start at just $0.55/GB, with traffic that never expires. Use code RAPID10 for 10% off, and [start your free trial today.](https://www.rapidproxy.io/?code=KHM9B6E6M) |
| [![PatewayAI](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/patewayai.png)](https://pateway.ai/?ch=jjvdb) | PatewayAI is an API relay service provider for experienced AI developers, with full support for the Claude and Codex model families. All models come from high-quality official channels, with no dilution or counterfeiting, and transparent, verifiable billing details. Economy mode starts at just 5% of the official price. Register through [this link](https://pateway.ai/?ch=jjvdb) to receive trial credits and participate in occasional promotions for free credits. The platform also supports enterprise-grade concurrency, a dedicated management dashboard, formal contracts and invoices, and two-way referral rewards of up to $150. |
| [![OpenLux](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/openlux.png)](https://www.openlux.ai/register?channel=c_6axb1q5n) | Thank you to OpenLux for sponsoring this project!<br>OpenLux is an all-in-one AI platform for businesses, bringing together leading AI models from major providers worldwide. With fast, reliable service and responsive technical support, OpenLux offers base pricing for Claude, OpenAI, and Gemini models as low as 8.82%, 4%, and 8% of official rates, respectively.<br>Exclusive offer for CLI Proxy API users: Sign up through our referral link and enjoy up to 7.5% off credit top-ups!<br>Get started with OpenLux → [https://www.openlux.ai/register?channel=c\_6axb1q5n](https://www.openlux.ai/register?channel=c_6axb1q5n) |
| [![Modelflare](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/modelflare.png)](https://modelflare.dev/sign-up?utm_source=github&utm_campaign=cliproxyapi) | Thanks to Modelflare for sponsoring this project! Modelflare: Full strength, stable, nothing watered down. Global SOTA models at a lower cost. Operated by US-based Havenbyte LLC, Modelflare supports GPT, Claude, Gemini, Grok, and other leading models through common compatible protocols, plus 40+ image and video models. Cache compensation is a highlight: selected OpenAI groups (price-first, stable, and premium) guarantee daily cache hit rates of 65%, 75%, or 85%, and if eligible requests fall short, Modelflare refunds the difference, visible on the usage dashboard after settlement. Special offers: a single top-up of US$20 unlocks the GPT discount group at a 0.015x price multiplier, and a single top-up of US$50 unlocks the Claude discount group at a 0.03x multiplier. Register via [this exclusive link](https://modelflare.dev/sign-up?utm_source=github&utm_campaign=cliproxyapi) to get started. |
| [![kedaya.ai](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/kedaya.jpg)](https://kedaya.ai/register?aff=824X8RAHCYXM) | kedaya.ai is a stable and efficient AI model API relay service provider, covering leading models including Claude, GPT, Gemini, Grok, Antigravity, and DeepSeek. It supports native OpenAI (including Responses), Anthropic, and Gemini protocols, enabling seamless integration with clients such as CLIProxyAPI, Claude Code, Codex, Gemini CLI, and Grok CLI. OpenAI and Grok model prices can be as low as 0.1% of official rates! [Exclusive registration link](https://kedaya.ai/register?aff=824X8RAHCYXM). |
| [![Xcode](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/xcode.gif)](https://xcode.best/register?aff=OuDv)[![Xcode](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/xcode.gif)](https://xcode.best/register?aff=OuDv)[Open Xcode in new window](https://xcode.best/register?aff=OuDv) | This AI model transfer service provider offers immediate refunds; any user can obtain a free invoice; it can be done for both corporate and individual clients; all major models are available. The customer service is always online and ready to respond to your requests; just let us know what you need and we'll take care of it！！！<br>Xcode VIP access： [https://xcode.best](https://xcode.best/register?aff=OuDv) |
| [![Chenju](https://github.com/router-for-me/CLIProxyAPI/raw/main/assets/chenju.png)](https://x.com/chenju_ai) | Thanks to [陈局 (Chenju)](https://x.com/chenju_ai) for sponsoring this project! Probably the only slot here that won't ask you to sign up — no signup link, no promo code. Just raising a glass to the maintainers, because good open source deserves to be paid for. Come shoot the breeze on X: [@chenju\_ai](https://x.com/chenju_ai) |

## Overview

[Permalink: Overview](https://github.com/router-for-me/CLIProxyAPI#overview)

- OpenAI/Gemini/Claude/Grok compatible API endpoints for CLI models
- OpenAI Codex support (GPT models) via OAuth login
- Claude Code support via OAuth login
- Grok Build support via OAuth login
- Streaming, non-streaming, and WebSocket responses where supported
- Function calling/tools support
- Multimodal input support (text and images)
- Multiple accounts with round-robin load balancing (Gemini, OpenAI, Claude, Grok)
- Simple CLI authentication flows (Gemini, OpenAI, Claude, Grok)
- Generative Language API Key support
- AI Studio Build multi-account load balancing
- Claude Code multi-account load balancing
- OpenAI Codex multi-account load balancing
- Grok Build multi-account load balancing
- OpenAI-compatible upstream providers via config (e.g., OpenRouter)
- Reusable Go SDK for embedding the proxy (see `docs/sdk-usage.md`)

## Getting Started

[Permalink: Getting Started](https://github.com/router-for-me/CLIProxyAPI#getting-started)

CLIProxyAPI Guides: [https://help.router-for.me/](https://help.router-for.me/)

## Management API

[Permalink: Management API](https://github.com/router-for-me/CLIProxyAPI#management-api)

see [MANAGEMENT\_API.md](https://help.router-for.me/management/api)

## Usage Statistics

[Permalink: Usage Statistics](https://github.com/router-for-me/CLIProxyAPI#usage-statistics)

Since v6.10.0, CLIProxyAPI and [CPAMC](https://github.com/router-for-me/Cli-Proxy-API-Management-Center) no longer ship built-in usage statistics. If you need usage statistics, use:

### [CPA Usage Keeper](https://github.com/Willxup/cpa-usage-keeper)

[Permalink: CPA Usage Keeper](https://github.com/router-for-me/CLIProxyAPI#cpa-usage-keeper)

Standalone persistence and visualization service for CLIProxyAPI, with periodic data sync, SQLite storage, aggregate APIs, and a built-in dashboard for usage and statistics.

### [CPA-Manager-Plus](https://github.com/seakee/CPA-Manager-Plus)

[Permalink: CPA-Manager-Plus](https://github.com/router-for-me/CLIProxyAPI#cpa-manager-plus)

A self-hosted CLIProxyAPI management console and observability dashboard, available as a lightweight drop-in panel or a full Manager Server with persistent analytics. Manage OAuth credentials, AI providers, client API keys, model aliases, plugins, and CPA settings in one interface. SQLite-backed request history enables live monitoring, failure diagnosis, and token, latency, and estimated-cost breakdowns by model, provider, account, key, and channel. Supports editable model prices and one-click price sync, alongside Codex and xAI quota checks, reset information, account-health inspection, and controlled recovery actions. Deploy via Docker or cross-platform native packages, with data stored locally.

### [Oh-My-CPA](https://github.com/WizisCool/oh-my-cpa)

[Permalink: Oh-My-CPA](https://github.com/router-for-me/CLIProxyAPI#oh-my-cpa)

Modern Ant Design-based management console for CLIProxyAPI v8+, combining CPAMC-style administration with SQLite-backed request records and usage analytics. Covers OAuth accounts, API providers, client keys, quotas, pricing and CPA operations in one interface. Tracks request-level latency, TTFT, tokens and cost, with multi-dimensional filtering, live dashboards and token heatmaps. OpenRouter price sync, custom rates and per-request price snapshots keep historical costs stable; a built-in Agent and MCP tools support assisted investigation and management.

## SDK Docs

[Permalink: SDK Docs](https://github.com/router-for-me/CLIProxyAPI#sdk-docs)

- Usage: [docs/sdk-usage.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/docs/sdk-usage.md)
- Advanced (executors & translators): [docs/sdk-advanced.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/docs/sdk-advanced.md)
- Access: [docs/sdk-access.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/docs/sdk-access.md)
- Watcher: [docs/sdk-watcher.md](https://github.com/router-for-me/CLIProxyAPI/blob/main/docs/sdk-watcher.md)
- Custom Provider Example: `examples/custom-provider`

## Contributing

[Permalink: Contributing](https://github.com/router-for-me/CLIProxyAPI#contributing)

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Who is with us?

[Permalink: Who is with us?](https://github.com/router-for-me/CLIProxyAPI#who-is-with-us)

Those projects are based on CLIProxyAPI:

### [vibeproxy](https://github.com/automazeio/vibeproxy)

[Permalink: vibeproxy](https://github.com/router-for-me/CLIProxyAPI#vibeproxy)

Native macOS menu bar app to use your Claude Code & ChatGPT subscriptions with AI coding tools - no API keys needed

### [Subtitle Translator](https://github.com/VjayC/SRT-Subtitle-Translator-Validator)

[Permalink: Subtitle Translator](https://github.com/router-for-me/CLIProxyAPI#subtitle-translator)

A cross-platform desktop and web app to translate and validate SRT subtitles using your existing LLM subscriptions (Gemini, ChatGPT, Claude, etc.) via CLIProxyAPI - no API keys needed.

### [CCS (Claude Code Switch)](https://github.com/kaitranntt/ccs)

[Permalink: CCS (Claude Code Switch)](https://github.com/router-for-me/CLIProxyAPI#ccs-claude-code-switch)

CLI wrapper for instant switching between multiple Claude accounts and alternative models (Gemini, Codex, Antigravity) via CLIProxyAPI OAuth - no API keys needed

### [Quotio](https://github.com/nguyenphutrong/quotio)

[Permalink: Quotio](https://github.com/router-for-me/CLIProxyAPI#quotio)

Native macOS menu bar app that unifies Claude, Gemini, OpenAI, and Antigravity subscriptions with real-time quota tracking and smart auto-failover for AI coding tools like Claude Code, OpenCode, and Droid - no API keys needed.

### [ProxyPilot](https://github.com/Finesssee/ProxyPilot)

[Permalink: ProxyPilot](https://github.com/router-for-me/CLIProxyAPI#proxypilot)

Windows-native CLIProxyAPI fork with TUI, system tray, and multi-provider OAuth for AI coding tools - no API keys needed.

### [CPA-XXX Panel](https://github.com/ferretgeek/CPA-X)

[Permalink: CPA-XXX Panel](https://github.com/router-for-me/CLIProxyAPI#cpa-xxx-panel)

A lightweight web admin panel for CLIProxyAPI with health checks, resource monitoring, real-time logs, auto-update, request statistics and pricing display. Supports one-click installation and systemd service.

### [CLIProxyAPI Tray](https://github.com/kitephp/CLIProxyAPI_Tray)

[Permalink: CLIProxyAPI Tray](https://github.com/router-for-me/CLIProxyAPI#cliproxyapi-tray)

A Windows tray application implemented using PowerShell scripts, without relying on any third-party libraries. The main features include: automatic creation of shortcuts, silent running, password management, channel switching (Main / Plus), and automatic downloading and updating.

### [霖君](https://github.com/wangdabaoqq/LinJun)

[Permalink: 霖君](https://github.com/router-for-me/CLIProxyAPI#%E9%9C%96%E5%90%9B)

霖君 is a cross-platform desktop application for managing AI programming assistants, supporting macOS, Windows, and Linux systems. Unified management of Claude Code, Gemini, OpenAI Codex, and other AI coding tools, with local proxy for multi-account quota tracking and one-click configuration.

### [CLIProxyAPI Dashboard](https://github.com/itsmylife44/cliproxyapi-dashboard)

[Permalink: CLIProxyAPI Dashboard](https://github.com/router-for-me/CLIProxyAPI#cliproxyapi-dashboard)

A modern web-based management dashboard for CLIProxyAPI built with Next.js, React, and PostgreSQL. Features real-time log streaming, structured configuration editing, API key management, OAuth provider integration for Claude/Gemini/Codex, usage analytics, container management, and config sync with OpenCode via companion plugin - no manual YAML editing needed.

### [All API Hub](https://github.com/qixing-jk/all-api-hub)

[Permalink: All API Hub](https://github.com/router-for-me/CLIProxyAPI#all-api-hub)

Browser extension for one-stop management of New API-compatible relay site accounts, featuring balance and usage dashboards, auto check-in, one-click key export to common apps, in-page API availability testing, and channel/model sync and redirection. It integrates with CLIProxyAPI through the Management API for one-click provider import and config sync.

### [Shadow AI](https://github.com/HEUDavid/shadow-ai)

[Permalink: Shadow AI](https://github.com/router-for-me/CLIProxyAPI#shadow-ai)

Shadow AI is an AI assistant tool designed specifically for restricted environments. It provides a stealthy operation
mode without windows or traces, and enables cross-device AI Q&A interaction and control via the local area network (
LAN). Essentially, it is an automated collaboration layer of "screen/audio capture + AI inference + low-friction delivery",
helping users to immersively use AI assistants across applications on controlled devices or in restricted environments.

### [ProxyPal](https://github.com/buddingnewinsights/proxypal)

[Permalink: ProxyPal](https://github.com/router-for-me/CLIProxyAPI#proxypal)

Cross-platform desktop app (macOS, Windows, Linux) wrapping CLIProxyAPI with a native GUI. Connects Claude, ChatGPT, Gemini, GitHub Copilot, and custom OpenAI-compatible endpoints with usage analytics, request monitoring, and auto-configuration for popular coding tools - no API keys needed.

### [CLIProxyAPI Quota Inspector](https://github.com/AllenReder/CLIProxyAPI-Quota-Inspector)

[Permalink: CLIProxyAPI Quota Inspector](https://github.com/router-for-me/CLIProxyAPI#cliproxyapi-quota-inspector)

Ready-to-use cross-platform quota inspector for CLIProxyAPI, supporting per-account codex 5h/7d quota windows, plan-based sorting, status coloring, and multi-account summary analytics.

### [CLIProxy Pool Watch](https://github.com/murasame612/CLIProxyPoolWidget)

[Permalink: CLIProxy Pool Watch](https://github.com/router-for-me/CLIProxyAPI#cliproxy-pool-watch)

Native macOS SwiftUI app for monitoring ChatGPT/Codex account quotas in CLIProxyAPI pools. Displays account availability, Plus-base capacity, 5-hour and weekly quota bars, plan weights, and restore forecasts through the Management API.

### [Panopticon](https://github.com/eltmon/panopticon-cli)

[Permalink: Panopticon](https://github.com/router-for-me/CLIProxyAPI#panopticon)

Multi-agent orchestration for AI coding assistants. Runs CLIProxyAPI as a local sidecar so its agents can drive GPT models through a ChatGPT subscription, pointing Claude Code at an Anthropic-compatible endpoint with no OpenAI API key required.

### [Tunnel Agent](https://github.com/Villoh/tunnel-agent)

[Permalink: Tunnel Agent](https://github.com/router-for-me/CLIProxyAPI#tunnel-agent)

Windows desktop UI that manages CLIProxyAPI and Perplexity WebUI Scraper from a single interface, inspired by Quotio and VibeProxy. Connect OAuth providers (Claude, Gemini, Codex, Kimi, Antigravity), custom API keys, and Perplexity session accounts, then point any coding agent at the local endpoint.

### [Quotio Desktop](https://github.com/xiaocoss/quotio-desktop)

[Permalink: Quotio Desktop](https://github.com/router-for-me/CLIProxyAPI#quotio-desktop)

Cross-platform (Tauri) port of Quotio for Windows, macOS and Linux. Manages a pool of AI accounts (Codex, Claude Code, GitHub Copilot, Gemini, Antigravity, Kiro, Cursor, Trae, GLM) through CLIProxyAPI, with per-account 5-hour/weekly quota bars, Codex rate-limit reset credits with one-click reset, smart scheduling, usage statistics, and multi-instance Codex — no API keys needed.

### [Universal Chat Provider](https://github.com/maxdewald/vscode-universal-chat-provider)

[Permalink: Universal Chat Provider](https://github.com/router-for-me/CLIProxyAPI#universal-chat-provider)

VS Code extension that brings your Claude, ChatGPT/Codex, Antigravity, Grok, and Kimi subscriptions into GitHub Copilot Chat as native language models — and can power your Git commit messages, chat titles, and summaries too. Runs CLIProxyAPI in a fully managed background lifecycle (download, verify, supervise) shared across all windows, so it's zero-setup. No API keys needed, just OAuth.

### [CPA-Tray-Powershell](https://github.com/ztzpro/CPA-Tray-Powershell.git)

[Permalink: CPA-Tray-Powershell](https://github.com/router-for-me/CLIProxyAPI#cpa-tray-powershell)

A PowerShell-based Windows system tray launcher for CLIProxyAPI. It supports running in the background without a console window, opening the management page, keeping the backend running after the management window closes, and reopening the page from the tray. It also supports checking for CLIProxyAPI updates on startup, SHA-256 verification with rollback, one-click CLIProxyAPI restart and update, PID-validated process management, and safe service shutdown.

### [Grok Search MCP](https://github.com/MapleMapleCat/Grok_Search_Mcp)

[Permalink: Grok Search MCP](https://github.com/router-for-me/CLIProxyAPI#grok-search-mcp)

An HTTP-only Model Context Protocol server that uses a CLIProxyAPI deployment to provide Grok-powered real-time web search, X/Twitter search, and model discovery to MCP clients. It adds MCP transport, client API-key management, quotas, usage tracking, and a web administration panel.

### [AIUsage](https://github.com/sylearn/AIUsage)

[Permalink: AIUsage](https://github.com/router-for-me/CLIProxyAPI#aiusage)

Native macOS SwiftUI dashboard for AI subscriptions and coding proxies. It manages official CLIProxyAPI releases end to end (download, verify, supervise, update, and roll back), unifies OAuth accounts and live models, and connects one gateway to Codex, Claude Code/Science, OpenCode, or OpenAI/Anthropic/Gemini clients, with optional LAN access.

### [Claude Dialects](https://github.com/stefandevo/claude-dialects)

[Permalink: Claude Dialects](https://github.com/router-for-me/CLIProxyAPI#claude-dialects)

Run multiple native-feeling Claude Code commands, each powered by a different model (Codex, GLM, Kimi, Gemini, Grok, MiniMax, DeepSeek, Cursor, Copilot, Claude). Every dialect launches the real Claude Code interface with its own isolated config, history, ports, and an embedded CLIProxyAPI instance linked through the Go SDK — no separate proxy install. macOS only. Learn more at [claude-dialects.cc](https://claude-dialects.cc/).

### [WebBrain](https://github.com/webbrain-one/webbrain)

[Permalink: WebBrain](https://github.com/router-for-me/CLIProxyAPI#webbrain)

Browser agent that can connect to CLIProxyAPI's local OpenAI-compatible endpoint as a model provider. See WebBrain's independent [setup, security, and account-risk guide](https://webbrain.one/docs/easy-cli-proxy/) for using CLIProxyAPI through EasyCLIProxyAPI.

### [Infinitus](https://github.com/deathemperor/infinitus)

[Permalink: Infinitus](https://github.com/router-for-me/CLIProxyAPI#infinitus)

Native macOS menu bar app that runs a fleet of Claude accounts through CLIProxyAPI's Management API (claude-swap and 9Router too): 5h / 7d / per-model quota gauges, switch / hold / star from the popup, a run-rate forecast of when each window runs out, and an iPhone companion that mirrors it all - no API keys needed.

### [PiCloud](https://github.com/cookerpapa/pi-cloud)

[Permalink: PiCloud](https://github.com/router-for-me/CLIProxyAPI#picloud)

Self-hosted coding-agent platform built on the Pi SDK, with a web UI, concurrent subagents, and CubeSandbox KVM workspaces. Uses CLIProxyAPI as its provider gateway, keeping provider credentials outside the guest workspaces.

### [cc-status-line](https://github.com/kinka/cc-status-line)

[Permalink: cc-status-line](https://github.com/router-for-me/CLIProxyAPI#cc-status-line)

Claude Code status line for CLIProxyAPI: per-account Codex / Grok / Antigravity / Claude quotas (5h / 7d / weekly) and reset countdown for the current instance. Picks the CPA instance from `ANTHROPIC_BASE_URL` and reads quotas through the Management API.

### [CLIProxy Quota Tray](https://github.com/ZYHUO/CLIProxy-Quota-Tray)

[Permalink: CLIProxy Quota Tray](https://github.com/router-for-me/CLIProxyAPI#cliproxy-quota-tray)

Cross-platform Electron tray dashboard for CLIProxyAPI. Shows the real OAuth quota windows per account across ChatGPT/Codex, Claude, Gemini/Antigravity, Grok, Kimi and Cursor, estimates usage-queue cost, and tracks OpenAI/Claude service status. Dark terminal-style UI; runs on Windows and Linux.

### [panel4cliproxyapi](https://github.com/yaanlaan/panel4cliproxyapi)

[Permalink: panel4cliproxyapi](https://github.com/router-for-me/CLIProxyAPI#panel4cliproxyapi)

A modern, responsive web dashboard and management console for CLIProxyAPI built with React and Tailwind CSS. Features multi-provider OAuth login with LAN redirect assistance, visual zero-YAML configuration, real-time traffic analytics charts, client API key management, core version checking & hot-reloading, and a live SSE streaming playground.

### [sub2api](https://github.com/PlaygrndLabs/sub2api)

[Permalink: sub2api](https://github.com/router-for-me/CLIProxyAPI#sub2api)

A Cloudflare-based LLM gateway and proxy server: CLIProxyAPI deployed to Cloudflare Workers + Containers in one click. Logins and config persist in R2, the dashboard sits behind a password, and API calls are refused until a client API key exists.

### [Hermes CLIProxyAPI Provider](https://github.com/duu261/hermes-cliproxyapi-provider)

[Permalink: Hermes CLIProxyAPI Provider](https://github.com/router-for-me/CLIProxyAPI#hermes-cliproxyapi-provider)

Model-provider plugin for [Hermes Agent](https://github.com/NousResearch/hermes-agent) that registers one Hermes provider per CLIProxyAPI provider, each on the wire its executor accepts (Anthropic Messages, Responses or Chat Completions), with context windows and reasoning levels read from CLIProxyAPI. Optional read-only Management API pass for exact provider grouping. Listed in the [Hermes plugin catalog](https://hermes-agent.nousresearch.com/docs/plugins/cliproxyapi-provider): `hermes plugins install cliproxyapi-provider`.

### [Ebb](https://github.com/lucasnsaraujo/ebb)

[Permalink: Ebb](https://github.com/router-for-me/CLIProxyAPI#ebb)

Native macOS menu bar app for CLIProxyAPI pools. It shows how much of the pool's Claude, Codex and other providers' 5-hour and weekly limits is left and when it comes back, and sets each login's routing weight through the Management API so the accounts drain evenly.

Note

If you developed a project based on CLIProxyAPI, please open a PR to add it to this list.

## More choices

[Permalink: More choices](https://github.com/router-for-me/CLIProxyAPI#more-choices)

Those projects are ports of CLIProxyAPI or inspired by it:

### [9Router](https://github.com/decolua/9router)

[Permalink: 9Router](https://github.com/router-for-me/CLIProxyAPI#9router)

A Next.js implementation inspired by CLIProxyAPI, easy to install and use, built from scratch with format translation (OpenAI/Claude/Gemini/Ollama), combo system with auto-fallback, multi-account management with exponential backoff, a Next.js web dashboard, and support for CLI tools (Cursor, Claude Code, Cline, RooCode) - no API keys needed.

### [OmniRoute](https://github.com/diegosouzapw/OmniRoute)

[Permalink: OmniRoute](https://github.com/router-for-me/CLIProxyAPI#omniroute)

Never stop coding. Smart routing to FREE & low-cost AI models with automatic fallback.

OmniRoute is an AI gateway for multi-provider LLMs: an OpenAI-compatible endpoint with smart routing, load balancing, retries, and fallbacks. Add policies, rate limits, caching, and observability for reliable, cost-aware inference.

### [Codex Switch](https://github.com/9ycrooked/CodexSwitch)

[Permalink: Codex Switch](https://github.com/router-for-me/CLIProxyAPI#codex-switch)

This is a tool built with Tauri 2 + Vue 3 for managing multiple OpenAI Codex desktop accounts. Switch between saved ChatGPT/Codex certification profiles, check 5-hour and weekly quota usage in real time, verify token health, view active account details, and import or save auth.json files without manual copying.

### [cliproxy-rs](https://github.com/vayungodara/cliproxy-rs)

[Permalink: cliproxy-rs](https://github.com/router-for-me/CLIProxyAPI#cliproxy-rs)

A Rust port of CLIProxyAPI that reads the same `config.yaml` and auth files and serves the same routes and v8 Management API, so you can switch between the two in either direction. Ships as a single binary with the management dashboard built in (per-account 5-hour and weekly quota view, account sign-in, client setup guides), and adds an opt-in `soonest-reset` routing strategy that spends the account whose weekly window resets first.

Note

If you have developed a port of CLIProxyAPI or a project inspired by it, please open a PR to add it to this list.

## License

[Permalink: License](https://github.com/router-for-me/CLIProxyAPI#license)

This project is licensed under the MIT License - see the [LICENSE](https://github.com/router-for-me/CLIProxyAPI/blob/main/LICENSE) file for details.

## About

Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build, Muse Code, Devin as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini Series, GPT Series, Grok Series, Claude model through API

### Topics

[antigravity](https://github.com/topics/antigravity) [claude-code](https://github.com/topics/claude-code) [cluade](https://github.com/topics/cluade) [codex](https://github.com/topics/codex) [devin](https://github.com/topics/devin) [gemini](https://github.com/topics/gemini) [muse](https://github.com/topics/muse) [openai](https://github.com/topics/openai)

### Resources

[Readme](https://github.com/router-for-me/CLIProxyAPI#readme-ov-file)

[MIT license](https://github.com/router-for-me/CLIProxyAPI#MIT-1-ov-file)

[Activity](https://github.com/router-for-me/CLIProxyAPI/activity)

[Custom properties](https://github.com/router-for-me/CLIProxyAPI/custom-properties)

### Stars

**56.8k** stars

### Watchers

**113** watching

### Forks

[**8.7k** forks](https://github.com/router-for-me/CLIProxyAPI/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Frouter-for-me%2FCLIProxyAPI&report=router-for-me+%28user%29)

## Releases

## Sponsor this project

## Packages

## Used by

## Contributors

## Languages

You can’t perform that action at this time.
