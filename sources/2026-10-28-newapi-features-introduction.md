---
url: https://docs.newapi.pro/en/docs/guide/wiki/basic-concepts/features-introduction
captured: 2026-10-28
word_count: 520
status: raw
---

[User Guide](https://docs.newapi.pro/en/docs) [Installation](https://docs.newapi.pro/en/docs/installation) [API Reference](https://docs.newapi.pro/en/docs/api) [AI Applications](https://docs.newapi.pro/en/docs/apps) [Skills](https://docs.newapi.pro/en/docs/skills) [Help & Support](https://docs.newapi.pro/en/docs/support) [Business Cooperation](https://docs.newapi.pro/en/docs/business)

# Features Description

Copy MarkdownOpen

01. 🎨 Brand new UI interface (some interfaces are yet to be updated)
02. 🌍 Multi-language support (to be improved)
03. 🎨 Added [Midjourney-Proxy(Plus)](https://github.com/novicezk/midjourney-proxy) API support (Before use, please confirm third-party project and upstream service authorization, content security, and terms of service requirements)
04. 💰 Supports internal balance, cost allocation, or enterprise customer account management in legally authorized deployments, configurable in system settings:
    - [x] Epay
05. 🔍 Supports querying usage or balance information of legally authorized channels:
    - In conjunction with the project [new-api-key-tool](https://github.com/Calcium-Ion/new-api-key-tool), usage can be queried by key.
06. 📑 Pagination supports selecting the number of items displayed per page
07. 🔄 Supports SQLite database storage, out-of-the-box, lightweight and convenient
08. 💵 Supports internal cost accounting or enterprise customer billing, configurable in System Settings - Operations Settings
09. ⚖️ Supports channel **Weighted Random**
10. 📈 Data Dashboard (Console)
11. 🔒 Can set models that a token can call
12. 🤖 Supports Telegram authorized login:
    1. System Settings - Configure Login & Registration - Allow Login via Telegram
    2. Enter command /setdomain to [@Botfather](https://t.me/botfather)
    3. Select your bot, then enter http(s)://your\_website\_address/login
    4. The Telegram Bot name is the bot username string without the @.
13. 🎵 Added [Suno API](https://github.com/Suno-API/Suno-API) API support (Before use, please confirm third-party project and upstream service authorization, content security, and terms of service requirements)
14. 🔄 Supports Rerank models, currently compatible with Cohere and Jina, and can be integrated with Dify
15. ⚡ **[OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime/integration)** \- Supports OpenAI's Realtime API, supports Azure channels
16. Supports using the route /chat2link to enter the chat interface
17. 🧠 Supports setting reasoning effort via model name suffix:
    1. OpenAI o-series models
       - Add suffix `-high` to set as high reasoning effort (e.g., `o3-mini-high`)
       - Add suffix `-medium` to set as medium reasoning effort (e.g., `o3-mini-medium`)
       - Add suffix `-low` to set as low reasoning effort (e.g., `o3-mini-low`)
    2. Claude thinking models
       - Add suffix `-thinking` to enable thinking mode (e.g., `claude-3-7-sonnet-20250219-thinking`)
18. 🔄 Thinking to Content: Supports setting the `thinking_to_content` option in `Channel - Edit - Channel Extra Settings`. Default is `false`. When enabled, it will convert the thinking content `reasoning_content` into a `<think>` tag and append it to the returned content.
19. 🔄 Model Rate Limiting: Supports setting model rate limiting in `System Settings - Rate Limit Settings`, including total request limit and successful request limit.
20. 💰 Cache Billing Support: When enabled, billing can be performed according to the set ratio upon cache hit:

    1. Set the `Prompt Cache Ratio` option in `System Settings - Operations Settings`.
    2. Set the `Prompt Cache Ratio` in the channel, range 0-1. For example, setting it to 0.5 means billing at 50% upon cache hit.
    3. Supported channels:

    - [x] OpenAI
    - [x] Azure
    - [x] DeepSeek
    - [ ] Claude

How is this guide?

GoodBad

Last updated on 9/11/2026

[Project Introduction\\
\\
Learn about New API, an AI API gateway and usage management system for legally authorized scenarios.](https://docs.newapi.pro/en/docs/guide/wiki/basic-concepts/project-introduction) [Technical Architecture\\
\\
Next Page](https://docs.newapi.pro/en/docs/guide/wiki/basic-concepts/technical-architecture)

### On this page

No Headings
