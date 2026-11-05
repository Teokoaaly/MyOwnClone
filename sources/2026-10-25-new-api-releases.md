---
url: https://github.com/QuantumNous/new-api/releases
captured: 2026-10-25
word_count: 5076
status: raw
---

# Releases: QuantumNous/new-api

## Release list

## v1.0.0-rc.47

Important

增加了普通渠道和任务插件一起选择渠道的功能。同一个模型名，插件和普通渠道都有的时候，以前请求都发给插件，现在按优先级和权重选择渠道。

这个模型的定价如果还是按任务插件写的，普通渠道会报价格错误，不会扣额度。可以单独给普通渠道设置价格。

增加了 OpenAI 12 小时提示缓存单独计价的功能，按输入价格的 2.5 倍收费。

修复了视频任务超过 24 小时就被退款的问题。默认等到 72 小时才退款。

Added selecting a channel from both a regular channel and a task plugin. On image, video, and Responses endpoints, a model both can serve used to send every request to the plugin. The channel is now selected by priority and weight.

If that model's price is still written for the task plugin, a regular channel returns a price error and does not charge. Set a regular price for it in pricing.

Added a separate price for OpenAI's 12-hour prompt cache, at 2.5 times the input price. It was charged at the 30-minute rate.

Fixed the problem of video tasks being refunded after 24 hours. They now wait 72 hours. If you set TASK_TIMEOUT_MINUTES yourself, that time stays.

## 中文

- **渠道**：增加了图片、视频和 Responses 上，普通渠道和任务插件按优先级和权重一起选择渠道的功能。原生插件地址继续走对应的插件。普通渠道和插件各用各的价格。
- **计费**：增加了 OpenAI 12 小时提示缓存单独计价的功能，按输入价格的 2.5 倍收费。gpt-6-astra 的 12 小时写入是每百万 token 25 美元，超过 272K token 是 50 美元。修复了 Claude 缓存写入没拆成 5 分钟和 1 小时时不计费的问题，没拆开的按 5 分钟计费。
- **价格同步**：增加了按站点汇率调整上游价格的功能。可以保持来源价格，也可以乘以或除以汇率。价格相同的模型也能选出来一起改。
- **任务**：修复了视频任务超过 24 小时就被退款的问题，默认等到 72 小时。自己设过 TASK_TIMEOUT_MINUTES 的，还是用你设的数。修复了可灵按 metadata 里的时长生成、计费却按外面的时长算的问题。增加了任务插件原生接口接收文件上传的功能。任务插件可以读到客户端请求头，Authorization 和 Cookie 不会给插件。
- **流式**：修复了大段内容传得慢就被当成断开的问题。修复了 Responses 已经回复完、日志里却记成断开的问题，用量照常记。
- **其他**：修复了结构化输出和工具参数字段顺序被打乱的问题，按客户端原来的顺序发给上游。修复了 Chat 转 Gemini 时丢掉 imageConfig 的问题，图片尺寸和比例会带过去。修复了高级自定义保存后「透传请求体」丢失的问题。修复了编辑令牌或模型时，切到另一条还留着上一条内容的问题。修复了访问日志记下网址里的密钥的问题。增加了使用日志详情里复制模型名的功能。

## English

- **Channels**: Added selecting a channel by priority and weight between a regular channel and a task plugin, on image, video, and Responses endpoints. A plugin's own address still goes to that plugin. Regular channels and plugins keep separate prices.
- **Billing**: Added a separate price for OpenAI's 12-hour prompt cache, at 2.5 times the input price. gpt-6-astra bills 12-hour writes at $25 per million tokens, and $50 above 272K tokens. Fixed the problem of Claude cache writes going unbilled when they were not split into 5-minute and 1-hour amounts. The unsplit part is billed as 5-minute writes.
- **Price sync**: Added adjusting synced upstream prices by the site exchange rate. You can keep the source price, or multiply or divide by the rate. Models that already match can be selected and adjusted too.
- **Tasks**: Fixed the problem of video tasks being refunded after 24 hours. The default wait is now 72 hours. A TASK_TIMEOUT_MINUTES you already set is left as it is. Fixed the problem of Kling billing the outer duration while generating the duration in metadata. Added file uploads on a plugin's own routes. Task plugins can read the client's request headers. Authorization and Cookie are not given to the plugin.
- **Streaming**: Fixed the problem of a slow transfer of a large event being recorded as a disconnect. Fixed the problem of a finished Responses reply being logged as a disconnect. The usage is still recorded.
- **Also**: Fixed the problem of structured output and tool parameters having their field order rearranged. They are sent in the client's order. Fixed the problem of Chat requests losing imageConfig on the way to Gemini, so image size and aspect ratio are kept. Fixed the problem of Advanced Custom dropping Pass Through Body on save. Fixed the problem of an edit drawer keeping the previous token or model when you switch records. Fixed the problem of access logs storing keys from the URL. Added copying model names from a usage log's details.

---

## What's Changed

- fix(relay): 正确结束已完成的 Responses 流 by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7956](https://github.com/QuantumNous/new-api/pull/7956)
- feat(billing): bill OpenAI 12-hour prompt cache writes at their own price by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7965](https://github.com/QuantumNous/new-api/pull/7965)
- fix(channels): preserve advanced custom body passthrough settings by [@seefs001](https://github.com/seefs001) in [#7971](https://github.com/QuantumNous/new-api/pull/7971)
- fix(logging): 隐藏访问日志中的查询凭据 by [@ceezyyy](https://github.com/ceezyyy) in [#7972](https://github.com/QuantumNous/new-api/pull/7972)
- fix: prevent stale values when switching edit drawer records by [@seefs001](https://github.com/seefs001) in [#7989](https://github.com/QuantumNous/new-api/pull/7989)
- chore(deps): bump react-resizable-panels from 4.12.2 to 4.14.6 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7982](https://github.com/QuantumNous/new-api/pull/7982)
- chore(deps): bump input-otp from 1.4.2 to 1.5.0 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7980](https://github.com/QuantumNous/new-api/pull/7980)
- chore(deps): bump i18next from 26.3.6 to 26.5.3 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7979](https://github.com/QuantumNous/new-api/pull/7979)
- chore(deps): bump react-i18next from 17.0.10 to 17.1.0 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7981](https://github.com/QuantumNous/new-api/pull/7981)
- chore(deps): bump axios from 1.18.1 to 1.20.0 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7835](https://github.com/QuantumNous/new-api/pull/7835)

## New Contributors

- [@ceezyyy](https://github.com/ceezyyy) made their first contribution in [#7972](https://github.com/QuantumNous/new-api/pull/7972)
**Full Changelog**: [v1.0.0-rc.46...v1.0.0-rc.47](https://github.com/QuantumNous/new-api/compare/v1.0.0-rc.46...v1.0.0-rc.47)

### Contributors

- [ ![@dependabot](https://avatars.githubusercontent.com/u/27347476?s=64&v=4) ](https://github.com/dependabot)
- [ ![@ceezyyy](https://avatars.githubusercontent.com/u/38361866?s=64&v=4) ](https://github.com/ceezyyy)
- [ ![@seefs001](https://avatars.githubusercontent.com/u/40468931?s=64&v=4) ](https://github.com/seefs001)
- [ ![@Calcium-Ion](https://avatars.githubusercontent.com/u/61247483?s=64&v=4) ](https://github.com/Calcium-Ion)
 dependabot, ceezyyy, and 2 other contributors

Assets 9

## v1.0.0-rc.46

Important

修复 CVE-2026-111943，请尽快升级。这一版用 Go 1.26.10。Go 校验证书时，会拒绝一小批已经不再可信的中间证书。用源码编译的，Go 也要换成 1.26.10。

Fixes CVE-2026-111943. Please upgrade soon. This release runs on Go 1.26.10. When Go checks a certificate, it rejects a small set of intermediate certificates that are no longer trusted. Builds from source need Go 1.26.10 too.

## 中文

- **安全**：修复 CVE-2026-111943。运行时改为 Go 1.26.10，校验证书时会拒绝一小批已经不再可信的中间证书。
- **邮件**：新增用 Resend 发邮件的功能，可以代替 SMTP。发件地址和发件人名称单独填。
- **数据看板**：新增缓存用量的显示，和总 token 放在一起。
- **向量**：新增阿里云百炼多模态向量模型 qwen3-vl-embedding 的支持，同系列的视觉向量模型也走这个接口。
- **任务**：修复任务换渠道重试时还按上一次价格计费的问题。更贵的渠道会先补预扣，余额不够就不会发出去。修复任务提交和轮询没用上「请求头覆盖」的问题。修复轮询跳到别的地址时密钥跟着过去的问题。
- **渠道**：修复可灵不接受单个密钥的问题。插件 1.1.1，不带竖线的密钥可以直接用。修复 DeepSeek 美元余额是 0、人民币有钱时，余额显示成 0 的问题。
- **修复**：修复通知限流每到整点就重新计数的问题，超过 60 分钟也按你设的时长算。修复 Claude 流式请求在准备和重试期间断开的问题。修复连续的助手消息合并后丢掉工具调用、Claude 报错的问题。修复 Redis 清掉脚本后限流失效的问题。发给 Gemini 的向量请求里带了图片或视频时，会直接拒绝，不再计费。

## English

- **Security**: Fixed CVE-2026-111943 by moving to Go 1.26.10. Certificate checks reject a small set of intermediate certificates that are no longer trusted.
- **Email**: Added Resend for sending mail, in place of SMTP. The sender address and sender name are set on their own.
- **Dashboard**: Added cache usage next to the total token count.
- **Embeddings**: Added Alibaba Bailian multimodal embeddings, starting with qwen3-vl-embedding. The other vision embedding models on Bailian use the same endpoint.
- **Tasks**: Fixed a retry on another channel still using the previous price. A more expensive channel reserves the difference first, and is not called when the balance cannot cover it. Fixed task submission and polling ignoring Request Header Override. Fixed polling redirects carrying the key to another address.
- **Channels**: Fixed Kling rejecting a single key. Plugin 1.1.1 accepts a key with no vertical bar. Fixed DeepSeek balance showing 0 when the USD wallet is 0 and the CNY wallet has money.
- **Fixes**: Fixed notification rate limits resetting at each hour, so a window longer than 60 minutes lasts for the time you set. Fixed Claude streams dropping during preparation and retries. Fixed merged assistant messages dropping tool calls, which made Claude reject the request. Fixed rate limiting after Redis flushed its scripts. An embedding sent to Gemini with an image or video is rejected and not billed.

---

## What's Changed

- fix(notify): keep notification limit window from resetting every hour by [@RedwindA](https://github.com/RedwindA) in [#7877](https://github.com/QuantumNous/new-api/pull/7877)
- fix(audit): add composite index for audit log ordering by [@stl25](https://github.com/stl25) in [#7874](https://github.com/QuantumNous/new-api/pull/7874)
- fix(relay): Claude 流式请求在准备和重试期间持续保活 by [@mameikagou](https://github.com/mameikagou) in [#7857](https://github.com/QuantumNous/new-api/pull/7857)
- feat(email): 添加 resend 邮件服务商接口 by [@imysen](https://github.com/imysen) in [#7880](https://github.com/QuantumNous/new-api/pull/7880)
- feat(dashboard): show cache usage alongside total tokens by [@seefs001](https://github.com/seefs001) in [#7773](https://github.com/QuantumNous/new-api/pull/7773)
- fix(task): 修复任务提交与轮询的请求头覆盖 by [@qinhanlei](https://github.com/qinhanlei) in [#7918](https://github.com/QuantumNous/new-api/pull/7918)
- feat: 支持阿里多模态向量化模型qwen3-vl-embedding by [@feitianbubu](https://github.com/feitianbubu) in [#5179](https://github.com/QuantumNous/new-api/pull/5179)
- fix(relaykit): keep tool calls when merging adjacent assistant messages for Claude by [@rjchien728](https://github.com/rjchien728) in [#7921](https://github.com/QuantumNous/new-api/pull/7921)
- fix(kling): 支持单 API Key by [@ZIYUT](https://github.com/ZIYUT) in [#7897](https://github.com/QuantumNous/new-api/pull/7897)
- fix(limiter): recover redis script after flush([#6412](https://github.com/QuantumNous/new-api/issues/6412)) by [@BradleyZhang](https://github.com/BradleyZhang) in [#6486](https://github.com/QuantumNous/new-api/pull/6486)
- fix: fall back to CNY when the DeepSeek USD wallet is zero by [@brushax](https://github.com/brushax) in [#7917](https://github.com/QuantumNous/new-api/pull/7917)
- chore(deps): bump github.com/klauspost/compress from 1.18.3 to 1.18.7 by [@dependabot](https://github.com/dependabot)[bot] in [#7931](https://github.com/QuantumNous/new-api/pull/7931)
- chore(deps-dev): bump vitest from 4.1.10 to 5.0.4 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7838](https://github.com/QuantumNous/new-api/pull/7838)
- fix: upgrade Go to 1.26.10 for CVE-2026-111943 by [@seefs001](https://github.com/seefs001) in [#7942](https://github.com/QuantumNous/new-api/pull/7942)

## New Contributors

- [@stl25](https://github.com/stl25) made their first contribution in [#7874](https://github.com/QuantumNous/new-api/pull/7874)
- [@mameikagou](https://github.com/mameikagou) made their first contribution in [#7857](https://github.com/QuantumNous/new-api/pull/7857)
- [@imysen](https://github.com/imysen) made their first contribution in [#7880](https://github.com/QuantumNous/new-api/pull/7880)
- [@qinhanlei](https://github.com/qinhanlei) made their first contribution in [#7918](https://github.com/QuantumNous/new-api/pull/7918)
- [@ZIYUT](https://github.com/ZIYUT) made their first contribution in [#7897](https://github.com/QuantumNous/new-api/pull/7897)
- [@BradleyZhang](https://github.com/BradleyZhang) made their first contribution in [#6486](https://github.com/QuantumNous/new-api/pull/6486)
- [@brushax](https://github.com/brushax) made their first contribution in [#7917](https://github.com/QuantumNous/new-api/pull/7917)
**Full Changelog**: [v1.0.0-rc.45...v1.0.0-rc.46](https://github.com/QuantumNous/new-api/compare/v1.0.0-rc.45...v1.0.0-rc.46)

### Contributors

- [ ![@qinhanlei](https://avatars.githubusercontent.com/u/1567080?s=64&v=4) ](https://github.com/qinhanlei)
- [ ![@feitianbubu](https://avatars.githubusercontent.com/u/6916415?s=64&v=4) ](https://github.com/feitianbubu)
- [ ![@rjchien728](https://avatars.githubusercontent.com/u/20276663?s=64&v=4) ](https://github.com/rjchien728)
- [ ![@dependabot](https://avatars.githubusercontent.com/u/27347476?s=64&v=4) ](https://github.com/dependabot)
- [ ![@seefs001](https://avatars.githubusercontent.com/u/40468931?s=64&v=4) ](https://github.com/seefs001)
- [ ![@brushax](https://avatars.githubusercontent.com/u/56171752?s=64&v=4) ](https://github.com/brushax)
- [ ![@imysen](https://avatars.githubusercontent.com/u/102943051?s=64&v=4) ](https://github.com/imysen)
- [ ![@ZIYUT](https://avatars.githubusercontent.com/u/111171845?s=64&v=4) ](https://github.com/ZIYUT)
- [ ![@mameikagou](https://avatars.githubusercontent.com/u/116348059?s=64&v=4) ](https://github.com/mameikagou)
- [ ![@RedwindA](https://avatars.githubusercontent.com/u/128586631?s=64&v=4) ](https://github.com/RedwindA)
- [ ![@BradleyZhang](https://avatars.githubusercontent.com/u/200043940?s=64&v=4) ](https://github.com/BradleyZhang)
- [ ![@stl25](https://avatars.githubusercontent.com/u/317681732?s=64&v=4) ](https://github.com/stl25)
 qinhanlei, feitianbubu, and 10 other contributors

Assets 9

## v1.0.0-rc.45

Important

v1 正式版即将发布，现在是最后几个 RC 版本。新增 DeepSeek V4.1 Flash、Search 和 Fetch，通知分开开关，以及拖动排列渠道优先级的功能。

敏感词过滤默认关着。以前填过敏感词、但没保存过这个开关的，升级后到「请求检查」里打开。

v1 is coming soon. These are the last few release candidates. Added DeepSeek V4.1 Flash, Search and Fetch, separate notification switches, and dragging to set channel priority.

Sensitive word filtering is off by default. If you filled in a word list and never saved the switch, turn it on under Request checks after upgrading.

## 中文

- **DeepSeek**：新增 DeepSeek V4.1 Flash（deepseek-flash）和 deepseek-v4-pro 的支持，后面可以加 -none、-low、-max，`@thinking` 和 `@effort` 也能用。新增 Search 和 Fetch，地址是 /v1/tools/search 和 /v1/tools/fetch。Claude Code 和 Codex 让 DeepSeek 去搜索、打开网页时，按次数计费，每 1000 次 0.75 美元。
- **通知**：新增按种类开关通知的功能，余额不足提醒默认开着。验证码、重置密码、绑定邮箱，看 SMTP 有没有配好。余额低于你设的数时提醒一次，充回去之后，下次再低才会再提醒。
- **渠道**：新增拖动调整渠道优先级的功能，在渠道列表打开「拖拽模式」。新增 New API 渠道查询上游余额的功能，也可以绑定海螺、Vidu 和 Veo。新增令牌「允许查询用户额度」，新建的默认开着，以前建的还是关的。
- **限流和计费**：修复分组限流算到一起的问题，某个分组自己设了限流，就按这个分组的次数算。修复 Vidu 收费和实际生成对不上的问题，按它实际生成的模型、时长和分辨率计费。修复 Claude 流式把上游报的 0 丢掉的问题，报了 0 就按 0 算。提示词全在缓存里时，按读缓存的价格计费。
- **报错**：修复请求内容读失败时看不出原因的问题。上游报错里，你填的地址、IP 和密钥会被藏起来，文档链接和邮箱还看得到。
- **其他**：新增 Sub2API 查询余额的功能。新增 AWS 的 Mantle（Messages API），已经在用的还是 InvokeModel。新增 Vertex 用 API Key 时填写项目 ID 的功能。任务插件这一版更快。
- **修复**：修复 Vertex 的 us、eu 访问地址错误的问题。修复容器里过载保护看错 CPU 和内存的问题，看的是容器自己的，连续大约 15 秒都过高才会拒绝请求。

## English

- **DeepSeek**: Added deepseek-flash and deepseek-v4-pro. You can add -none, -low, or -max, and `@thinking` and `@effort` work too. Added Search and Fetch at /v1/tools/search and /v1/tools/fetch. When Claude Code or Codex has DeepSeek search or open a page, that is charged per request, $0.75 per 1,000.
- **Notifications**: Added a switch for each kind of notification. The low balance reminder starts on. Verification codes, password resets, and email binding go out when SMTP is set up. You get one reminder when the balance goes below the number you set, and another the next time it does, after a top-up.
- **Channels**: Added dragging to change channel priority. Turn on Drag mode in the channel list. Added upstream balance checks for New API channels, which can also bind Hailuo, Vidu, and Veo. Added Allow querying user quota on tokens. New tokens start with it on. Older tokens stay off.
- **Rate limits and billing**: Fixed group rate limits being counted together. A group with its own limit is counted on its own. Fixed Vidu charges that did not match the video it generated. The charge uses the model, duration, and resolution it actually made. Fixed Claude streams dropping a 0 from the upstream. A reported 0 stays 0. When the whole prompt is cached, the charge is the cache-read price.
- **Errors**: Fixed request failures that hid the real reason the body could not be read. If it is too large, the response is 413. In an upstream error, the address, IP, and key you entered are hidden. Documentation links and email addresses stay visible.
- **Also**: Added balance checks for Sub2API channels. Added Mantle (Messages API) for AWS channels. Ones already in use stay on InvokeModel. Added a project ID field for Vertex API Key mode. Task plugins are faster in this release.
- **Fixes**: Fixed wrong Vertex addresses for the us and eu regions. Fixed overload protection in containers reading the wrong CPU and memory. It uses the container's own, and turns requests away only after they stay too high for about 15 seconds.

---

## What's Changed

- feat(ui): show newly added pricing groups at the top by [@seefs001](https://github.com/seefs001) in [#7782](https://github.com/QuantumNous/new-api/pull/7782)
- feat(channel): support Sub2API balance queries by [@AdoreJc](https://github.com/AdoreJc) in [#7749](https://github.com/QuantumNous/new-api/pull/7749)
- fix: disable sensitive word filtering by default and clear list by [@seefs001](https://github.com/seefs001) in [#7814](https://github.com/QuantumNous/new-api/pull/7814)
- fix(vertex): pass project_id in API Key mode to avoid 404 on official endpoints by [@xiaoyuyu6420](https://github.com/xiaoyuyu6420) in [#6330](https://github.com/QuantumNous/new-api/pull/6330)
- fix(web): sort pricing models by input, output and per-request price by [@feitianbubu](https://github.com/feitianbubu) in [#7813](https://github.com/QuantumNous/new-api/pull/7813)
- fix(claude): preserve explicit zero usage and cache-only billing by [@paopaoandlingyia](https://github.com/paopaoandlingyia) in [#7816](https://github.com/QuantumNous/new-api/pull/7816)
- fix(relay): mask only the custom upstream address in error messages by [@RedwindA](https://github.com/RedwindA) in [#7822](https://github.com/QuantumNous/new-api/pull/7822)
- fix(playground): support the reasoning field in chat responses by [@seefs001](https://github.com/seefs001) in [#7831](https://github.com/QuantumNous/new-api/pull/7831)
- fix(dashboard): draw flow chart labels in the theme text color by [@RedwindA](https://github.com/RedwindA) in [#7821](https://github.com/QuantumNous/new-api/pull/7821)
- fix(relaykit): emit summary on reasoning items announced without one by [@rjchien728](https://github.com/rjchien728) in [#7833](https://github.com/QuantumNous/new-api/pull/7833)
- fix(middleware): 过载哨兵改用容器口径并加入连续性与新鲜度判定 by [@ax2](https://github.com/ax2) in [#7317](https://github.com/QuantumNous/new-api/pull/7317)
- fix(relayconvert): 保留 Chat/Claude → Responses 转换中 input_image 的 detail 字段 by [@sicnuyudidi](https://github.com/sicnuyudidi) in [#7855](https://github.com/QuantumNous/new-api/pull/7855)
- fix(web): 补全日志页模型厂商规则（Cloudflare clef、NVIDIA 家族） by [@xuu1998](https://github.com/xuu1998) in [#7840](https://github.com/QuantumNous/new-api/pull/7840)
- fix(web): apply theme before first paint to avoid light flash and Dark Reader misdetection by [@RedwindA](https://github.com/RedwindA) in [#7571](https://github.com/QuantumNous/new-api/pull/7571)
- fix: align model card summary with status bar hours by [@feitianbubu](https://github.com/feitianbubu) in [#7847](https://github.com/QuantumNous/new-api/pull/7847)
- feat(notify): turn each kind of notification on or off by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7868](https://github.com/QuantumNous/new-api/pull/7868)
- feat(deepseek): support V4.1 Flash, the Search and Fetch APIs, and @ reasoning modifiers by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7867](https://github.com/QuantumNous/new-api/pull/7867)

## New Contributors

- [@AdoreJc](https://github.com/AdoreJc) made their first contribution in [#7749](https://github.com/QuantumNous/new-api/pull/7749)
- [@xiaoyuyu6420](https://github.com/xiaoyuyu6420) made their first contribution in [#6330](https://github.com/QuantumNous/new-api/pull/6330)
- [@paopaoandlingyia](https://github.com/paopaoandlingyia) made their first contribution in [#7816](https://github.com/QuantumNous/new-api/pull/7816)
- [@rjchien728](https://github.com/rjchien728) made their first contribution in [#7833](https://github.com/QuantumNous/new-api/pull/7833)
- [@sicnuyudidi](https://github.com/sicnuyudidi) made their first contribution in [#7855](https://github.com/QuantumNous/new-api/pull/7855)
- [@xuu1998](https://github.com/xuu1998) made their first contribution in [#7840](https://github.com/QuantumNous/new-api/pull/7840)
**Full Changelog**: [v1.0.0-rc.44...v1.0.0-rc.45](https://github.com/QuantumNous/new-api/compare/v1.0.0-rc.44...v1.0.0-rc.45)

### Contributors

- [ ![@ax2](https://avatars.githubusercontent.com/u/2170318?s=64&v=4) ](https://github.com/ax2)
- [ ![@feitianbubu](https://avatars.githubusercontent.com/u/6916415?s=64&v=4) ](https://github.com/feitianbubu)
- [ ![@rjchien728](https://avatars.githubusercontent.com/u/20276663?s=64&v=4) ](https://github.com/rjchien728)
- [ ![@sicnuyudidi](https://avatars.githubusercontent.com/u/23434080?s=64&v=4) ](https://github.com/sicnuyudidi)
- [ ![@seefs001](https://avatars.githubusercontent.com/u/40468931?s=64&v=4) ](https://github.com/seefs001)
- [ ![@xuu1998](https://avatars.githubusercontent.com/u/40609659?s=64&v=4) ](https://github.com/xuu1998)
- [ ![@AdoreJc](https://avatars.githubusercontent.com/u/45906467?s=64&v=4) ](https://github.com/AdoreJc)
- [ ![@Calcium-Ion](https://avatars.githubusercontent.com/u/61247483?s=64&v=4) ](https://github.com/Calcium-Ion)
- [ ![@xiaoyuyu6420](https://avatars.githubusercontent.com/u/93528429?s=64&v=4) ](https://github.com/xiaoyuyu6420)
- [ ![@paopaoandlingyia](https://avatars.githubusercontent.com/u/104690059?s=64&v=4) ](https://github.com/paopaoandlingyia)
- [ ![@RedwindA](https://avatars.githubusercontent.com/u/128586631?s=64&v=4) ](https://github.com/RedwindA)
 ax2, feitianbubu, and 9 other contributors

Assets 9

## v1.0.0-rc.44

Important

**v1 Coming Soon & Log Export / v1 即将发布与日志导出**

v1 正式版即将发布，现在是最后几个 RC 版本。

使用日志支持导出 CSV。可以在日志维护里设置是否允许用户导出，以及日志最长时间范围，默认 365 天。普通用户的日志查询、导出和数据看板都按这个范围限制。

游乐场的数据按账号分开保存，升级后之前的聊天记录会清空一次。

Claude 请求按模型支持的档位发送思考强度。发给 Gemini 的工具和结构化输出保留完整的 JSON Schema。

v1 is coming soon. These are the last few release candidates.

Usage logs can be exported as CSV. In Log Maintenance you can choose whether users may export and set the longest log time range, 365 days by default. Regular users' log searches, exports, and dashboard charts all follow that range.

Playground data is stored per account. Earlier Playground history is cleared once after the upgrade.

Claude requests get the thinking effort each model accepts. Tools and structured output sent to Gemini keep their full JSON Schema.

## New Features

- The usage log page has an Export button next to Search. It downloads the current view, with the page's filters and a chosen time range, as a CSV file in the viewer's language. Users export their own logs, and administrators in the all-users view export every user's logs. Each user runs one export at a time, across tabs and, with Redis, across nodes ([#7774](https://github.com/QuantumNous/new-api/issues/7774)).
- Log Maintenance adds Allow users to export logs (on by default) and Longest log time range (days) (365 by default). Regular users' log searches had no limit before. Their searches, exports, and dashboard usage and traffic charts now share this range. The page is split into Log recording, Log search and export, history log cleanup, and server log management.
- Date and time pickers, including the date range filter on log pages, work down to the second.

## Fixes and Improvements

- Known Claude models get the nearest thinking effort they accept, and none when they accept none. This fixes 400s on Opus 4.5 with `max` or `xhigh`, on Sonnet 4.5 and Haiku 4.5, and when a model suffix or modifier turns thinking off. Native Claude requests without a suffix or modifier pass through as sent.
- Claude Haiku 5.5 uses adaptive thinking with medium effort by default. Converted requests drop `temperature`, `top_p`, and `top_k` for it. Gemini 2.5 Pro gets a 32768 thinking budget for `xhigh` and `max`.
- Tools and structured output sent to Gemini keep `const`, `oneOf`, `$ref`, `$defs`, type arrays, and non-string enums. A schema that Gemini's typed Schema can hold is sent as before, and any other schema goes in `parametersJsonSchema` or `responseJsonSchema`. Models set to Gemini API v1 get a cleaned schema and a conversion warning ([#7455](https://github.com/QuantumNous/new-api/issues/7455), [#7704](https://github.com/QuantumNous/new-api/issues/7704)).
- Responses images sent to Chat Completions upstreams use the object form of `image_url`, so vLLM and strict gateways accept Codex screenshots and tool images ([#7578](https://github.com/QuantumNous/new-api/issues/7578)).
- Chat streams converted to Claude Messages keep answer text that arrives in the same chunk as the last reasoning token ([#7664](https://github.com/QuantumNous/new-api/issues/7664)). Claude Messages converted to Chat Completions keep assistant text next to tool calls ([#6871](https://github.com/QuantumNous/new-api/issues/6871)).
- Claude requests forward `thinking.block_binding` and every `anthropic-beta` header value. This fixes "The block is bound to a different conversation" in multi-turn conversations whose system prompt or tools change ([#7732](https://github.com/QuantumNous/new-api/issues/7732)).
- Responses WebSocket sessions send a close frame when the server ends them, so Codex sees a normal close ([#7642](https://github.com/QuantumNous/new-api/issues/7642)).
- Without Redis, model rate-limit 429s carry the same error message and log line as with Redis ([#7721](https://github.com/QuantumNous/new-api/issues/7721)).
- The console reloads once when a page's code fails to load, and the error page shows a status code only when there is one ([#7634](https://github.com/QuantumNous/new-api/issues/7634)).
- The wallet, security, and OAuth callback pages and the user binding dialog load much less JavaScript. Linux DO bindings show the Linux DO logo.
- Date pickers and relative times follow the interface language ([#7654](https://github.com/QuantumNous/new-api/issues/7654)).
- The model square shows the latest 24 hourly status samples within 7 days, with no gaps. Expression model cards show the cache read price ([#7757](https://github.com/QuantumNous/new-api/issues/7757)).
- Usage log previews keep the recorded billing tiers ([#7763](https://github.com/QuantumNous/new-api/issues/7763)), and task settlement logs show tiered billing ([#7446](https://github.com/QuantumNous/new-api/issues/7446)).
- Pricing conversion accepts model metadata that declares endpoints as an array ([#7724](https://github.com/QuantumNous/new-api/issues/7724)). Root can manage pricing while the model square is disabled ([#7761](https://github.com/QuantumNous/new-api/issues/7761)).
- Performance metrics count streams that finished before the client disconnected ([#7638](https://github.com/QuantumNous/new-api/issues/7638)).
- The Sign in button on password login stays clickable and shows the legal consent warning ([#7771](https://github.com/QuantumNous/new-api/issues/7771)).
- The Auto font uses the browser's sans-serif again. Meta Muse Spark models show the Meta icon ([#7734](https://github.com/QuantumNous/new-api/issues/7734)), and billing source icons line up on mobile ([#7760](https://github.com/QuantumNous/new-api/issues/7760)).
- Dependency updates, including Electron 41.

---

## What's Changed

- fix(gemini): OpenAI 工具参数转换丢弃非字符串 enum，修复布尔枚举致上游 400 by [@zhaoruizhe81](https://github.com/zhaoruizhe81) in [#7729](https://github.com/QuantumNous/new-api/pull/7729)
- fix(web): map Meta Muse Spark models to Meta icon by [@i-richardwang](https://github.com/i-richardwang) in [#7734](https://github.com/QuantumNous/new-api/pull/7734)
- fix(web): show cache read price on expression model cards by [@i-richardwang](https://github.com/i-richardwang) in [#7757](https://github.com/QuantumNous/new-api/pull/7757)
- fix(metrics): count completed streams after context cancellation by [@jimmyleocn](https://github.com/jimmyleocn) in [#7638](https://github.com/QuantumNous/new-api/pull/7638)
- fix(logs): vertically align billing source icons on mobile by [@seefs001](https://github.com/seefs001) in [#7760](https://github.com/QuantumNous/new-api/pull/7760)
- fix: mark task settlement logs with is_task for tiered billing display by [@feitianbubu](https://github.com/feitianbubu) in [#7446](https://github.com/QuantumNous/new-api/pull/7446)
- fix(pricing): allow root access when the square is disabled by [@seefs001](https://github.com/seefs001) in [#7761](https://github.com/QuantumNous/new-api/pull/7761)
- fix(relaykit): preserve assistant text with tool calls by [@enwaiax](https://github.com/enwaiax) in [#6871](https://github.com/QuantumNous/new-api/pull/6871)
- fix(web): preserve recorded billing tiers in usage log previews by [@seefs001](https://github.com/seefs001) in [#7763](https://github.com/QuantumNous/new-api/pull/7763)
- chore(web): bump @lobehub/icons to 5.22.0 by [@i-richardwang](https://github.com/i-richardwang) in [#7764](https://github.com/QuantumNous/new-api/pull/7764)
- fix(pricing): accept declared endpoint arrays in pricing conversion by [@JohnUncle](https://github.com/JohnUncle) in [#7724](https://github.com/QuantumNous/new-api/pull/7724)
- fix(ci): stabilize checks and configure Bun dependency updates by [@seefs001](https://github.com/seefs001) in [#7765](https://github.com/QuantumNous/new-api/pull/7765)
- fix(auth): show legal consent warning on password login by [@seefs001](https://github.com/seefs001) in [#7771](https://github.com/QuantumNous/new-api/pull/7771)
- fix(claude): forward thinking.block_binding and every anthropic-beta value by [@RedwindA](https://github.com/RedwindA) in [#7732](https://github.com/QuantumNous/new-api/pull/7732)
- chore(deps-dev): bump @xmldom/xmldom from 0.8.13 to 0.8.15 in /electron by [@dependabot](https://github.com/dependabot)[bot] in [#7187](https://github.com/QuantumNous/new-api/pull/7187)
- build(deps): bump yace from 1.1.0 to 1.1.1 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7770](https://github.com/QuantumNous/new-api/pull/7770)
- build(deps): bump stream-markdown-parser from 1.1.3 to 1.2.18 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7769](https://github.com/QuantumNous/new-api/pull/7769)
- build(deps-dev): bump @tanstack/router-plugin from 1.168.23 to 1.168.42 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7768](https://github.com/QuantumNous/new-api/pull/7768)
- build(deps-dev): bump oxfmt from 0.57.0 to 0.72.0 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7766](https://github.com/QuantumNous/new-api/pull/7766)
- chore(deps-dev): bump electron from 39.8.10 to 41.10.6 in /electron by [@dependabot](https://github.com/dependabot)[bot] in [#7625](https://github.com/QuantumNous/new-api/pull/7625)
- chore(deps-dev): bump fast-uri from 3.1.5 to 3.1.7 in /electron by [@dependabot](https://github.com/dependabot)[bot] in [#7169](https://github.com/QuantumNous/new-api/pull/7169)
- chore(deps): bump github.com/gorilla/websocket from 1.5.0 to 1.5.3 by [@dependabot](https://github.com/dependabot)[bot] in [#7001](https://github.com/QuantumNous/new-api/pull/7001)
- chore(deps): bump ai from 7.0.31 to 7.0.136 in /web by [@dependabot](https://github.com/dependabot)[bot] in [#7767](https://github.com/QuantumNous/new-api/pull/7767)
- chore(deps-dev): bump brace-expansion from 1.1.16 to 1.1.21 in /electron by [@dependabot](https://github.com/dependabot)[bot] in [#7623](https://github.com/QuantumNous/new-api/pull/7623)
- chore(deps-dev): bump js-yaml from 4.3.1 to 4.3.2 in /electron by [@dependabot](https://github.com/dependabot)[bot] in [#7327](https://github.com/QuantumNous/new-api/pull/7327)
- chore(deps-dev): bump undici from 6.28.0 to 6.29.0 in /electron by [@dependabot](https://github.com/dependabot)[bot] in [#7624](https://github.com/QuantumNous/new-api/pull/7624)
- feat(logs): export usage logs from the common log page by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7774](https://github.com/QuantumNous/new-api/pull/7774)

## New Contributors

- [@zhaoruizhe81](https://github.com/zhaoruizhe81) made their first contribution in [#7729](https://github.com/QuantumNous/new-api/pull/7729)
- [@i-richardwang](https://github.com/i-richardwang) made their first contribution in [#7734](https://github.com/QuantumNous/new-api/pull/7734)
- [@JohnUncle](https://github.com/JohnUncle) made their first contribution in [#7724](https://github.com/QuantumNous/new-api/pull/7724)
**Full Changelog**: [v1.0.0-rc.43...v1.0.0-rc.44](https://github.com/QuantumNous/new-api/compare/v1.0.0-rc.43...v1.0.0-rc.44)

### Contributors

- [ ![@feitianbubu](https://avatars.githubusercontent.com/u/6916415?s=64&v=4) ](https://github.com/feitianbubu)
- [ ![@JohnUncle](https://avatars.githubusercontent.com/u/13462227?s=64&v=4) ](https://github.com/JohnUncle)
- [ ![@dependabot](https://avatars.githubusercontent.com/u/27347476?s=64&v=4) ](https://github.com/dependabot)
- [ ![@enwaiax](https://avatars.githubusercontent.com/u/32839114?s=64&v=4) ](https://github.com/enwaiax)
- [ ![@seefs001](https://avatars.githubusercontent.com/u/40468931?s=64&v=4) ](https://github.com/seefs001)
- [ ![@jimmyleocn](https://avatars.githubusercontent.com/u/42566991?s=64&v=4) ](https://github.com/jimmyleocn)
- [ ![@Calcium-Ion](https://avatars.githubusercontent.com/u/61247483?s=64&v=4) ](https://github.com/Calcium-Ion)
- [ ![@RedwindA](https://avatars.githubusercontent.com/u/128586631?s=64&v=4) ](https://github.com/RedwindA)
- [ ![@i-richardwang](https://avatars.githubusercontent.com/u/157827282?s=64&v=4) ](https://github.com/i-richardwang)
- [ ![@zhaoruizhe81](https://avatars.githubusercontent.com/u/229347043?s=64&v=4) ](https://github.com/zhaoruizhe81)
 feitianbubu, JohnUncle, and 8 other contributors

Assets 9

## v1.0.0-rc.43

Important

完善了 i18n，控制台、API 错误、邮件、通知和服务器日志都支持多语言。使用 DEFAULT_LANGUAGE 环境变量设置默认语言，不设置时为英文。

渠道新增“忽略上游证书校验”开关，可以连接使用自签证书的上游。

任务插件新增 utils.fetch，可以读取上游数据。

豆包 Seedance 1.5 Pro、2.x 和万相 3.0 支持传 -1 自动选择时长，按上游回报的时长计费。

Improved i18n. Console messages, API errors, emails, notifications, and server logs are now multilingual. Set the default language with the DEFAULT_LANGUAGE environment variable. It defaults to English.

Channels have a new Skip Upstream TLS Verification switch for upstreams that use self-signed certificates.

Task plugins can read upstream data with the new utils.fetch.

Doubao Seedance 1.5 Pro and 2.x, and Wan 3.0, accept -1 to pick the video duration automatically and bill the duration the upstream reports.

## New Features

- Improved i18n. The web console shows API messages and log entries in all seven interface languages. The backend translates errors for AI clients, emails, and notifications into English, Simplified Chinese, or Traditional Chinese, using the account language first and then the request's Accept-Language header. Log entries written before this release keep their original text.
- `DEFAULT_LANGUAGE` (`en`, `zh-CN`, or `zh-TW`) sets the default language of backend messages and server logs. It defaults to `en`.
- Skip Upstream TLS Verification is under the HTTP settings of each channel. It covers the channel's relay requests, Responses and Realtime WebSocket, task submission and polling, plugin fetches, balance, usage, and model-list queries, and media proxied through the channel. Codex OAuth refresh and Vertex or plugin service-account tokens still verify certificates.
- Task plugins can call `utils.fetch` in the submit, query, and content-download hooks. It reaches the channel Base URL and the additional request domains the plugin declares, and the upload dialog lists those domains. The [Task Plugin API v1](https://github.com/QuantumNous/new-api/blob/v1.0.0-rc.43/docs/plugin-api/v1.md) document lists the hooks and limits.
- Plugins can call `utils.json.clone` and export `parseSubmitEventDelta` with no capability declaration. Plugins that declare `json-clone@1` or `submit-sse-delta@1` keep loading.
- Doubao 1.3.0 and Alibaba Bailian 1.4.2 accept a duration of `-1` for Seedance 1.5 Pro and 2.x and for Wan 3.0. The request reserves the model's longest duration (12 seconds for Seedance 1.5 Pro, 15 for 2.0, 30 for 2.5 and Wan 3.0) and bills the duration the upstream reports. A JSON duration on `/v1/videos` now reaches Ark, and Wan 3.0 smart duration works on `/v1/video/generations`. ([#7700](https://github.com/QuantumNous/new-api/issues/7700))

## Fixes and Improvements

- Responses input converted for Claude and Gemini drops assistant text that comes after the last user message or tool result, and records a `trailing_assistant_omitted` warning. Codex sends such input when it retries a stream that failed after a reply finished. Claude 4.6 and later, Gemini 3.6 Flash, and Gemini 3.5 Flash-Lite and later rejected it with a 400. Chat Completions and Claude Messages requests keep their prefill.
- xAI Grok Imagine 1.1.0 bills video edits and extensions at the output resolution. The output keeps the input video's resolution up to 720p. The plugin reads the output file header and bills 480p when the shorter side is 480 pixels or less. It bills 720p otherwise, and when the header cannot be read.
- Hailuo 1.2.1 downloads MiniMax v1 videos through the file retrieve link. Those downloads returned 410 before. ([#7709](https://github.com/QuantumNous/new-api/issues/7709))
- Multipart task submissions send the Content-Type of the rebuilt body, so the boundary matches the body the upstream receives. ([#7655](https://github.com/QuantumNous/new-api/pull/7655))

---

## What's Changed

- fix(task-plugin): set multipart content type for upstream requests by [@LauZzL](https://github.com/LauZzL) in [#7655](https://github.com/QuantumNous/new-api/pull/7655)
- feat(i18n): translate web console messages in the frontend and AI-client errors in the backend by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7712](https://github.com/QuantumNous/new-api/pull/7712)
**Full Changelog**: [v1.0.0-rc.42...v1.0.0-rc.43](https://github.com/QuantumNous/new-api/compare/v1.0.0-rc.42...v1.0.0-rc.43)

### Contributors

- [ ![@Calcium-Ion](https://avatars.githubusercontent.com/u/61247483?s=64&v=4) ](https://github.com/Calcium-Ion)
- [ ![@LauZzL](https://avatars.githubusercontent.com/u/89786902?s=64&v=4) ](https://github.com/LauZzL)
 Calcium-Ion and LauZzL

Assets 9

## v1.0.0-rc.42

Important

**Search Billing & Task Plugins / 搜索计费与任务插件**

重做了搜索函数计费。渠道可以按上游自己的方式进行网络搜索，并按上游回报的搜索次数计费。

任务插件性能大幅提升。支持插件决定是否保留 JSON 字段顺序，声明 `json-order@1` 即可；其他插件行为不变。

高级自定义渠道可以把 Claude Messages 和 Gemini 转到 OpenAI Responses。

新增 xAI Grok Imagine 视频任务插件。

Search-function billing has been reworked. Channels can encode Web search for their upstream and settle from the search counts the vendor reports.

Task Plugins are substantially faster. A plugin that must keep the client’s JSON field order can declare `json-order@1`. Other plugins are unchanged.

Advanced Custom channels can convert Claude Messages and Gemini to OpenAI Responses. An xAI Grok Imagine video Task Plugin is added.

## New Features

- Reworked search-function billing, including per-Channel Web search encoding and vendor-reported search counts.
- Advanced Custom channels can convert Claude Messages and Gemini generateContent to OpenAI Responses.
- Moonshot Channels forward `/v1/responses` unchanged. Kimi currently serves `kimi-k3` on that path.
- Added the xAI Grok Imagine video Task Plugin: `grok-imagine-video`, `grok-imagine-video-1.5`, and `grok-imagine-video-1.5-lite`.
- Advanced parameter overrides support Regex conditions ([#7698](https://github.com/QuantumNous/new-api/issues/7698)).
- Users can be filtered by User Group.
- Task Plugins that declare `json-order@1` keep the client’s JSON field order through to the upstream.

## Fixes and Improvements

- Task Plugin requests are substantially faster, including passthrough submissions.
- Token counting is much faster, including long text without punctuation.
- Gemini stream usage is no longer multiplied by the number of frames ([#7687](https://github.com/QuantumNous/new-api/issues/7687)).
- Responses tool-output images are sent to Gemini as images, not as text. Claude Opus 5.5 defaults to medium effort when the client sets none.
- Responses custom tools such as `exec` and `apply_patch` are kept on Claude and Gemini upstreams ([#7636](https://github.com/QuantumNous/new-api/issues/7636)).
- Turning off the Thinking Suffix Adapter now also leaves effort suffixes such as `-high` unchanged.
- Completed image generations still bill when the Responses request later fails or is cancelled.
- Frontend build files no longer count against the page rate limit, so a cold load does not return 429 for the next session on the same IP.
- `gpt-6-sol` and `gpt-6-luna` use `max_completion_tokens` ([#7559](https://github.com/QuantumNous/new-api/issues/7559)).
- System Settings are hidden from non-root admins ([#7513](https://github.com/QuantumNous/new-api/issues/7513)).
- Fixed a blank Channels page on OriginOS 6. Fixed rounded clipping of Group names on API Keys ([#7645](https://github.com/QuantumNous/new-api/issues/7645)).

---

## What's Changed

- fix: isolate TLS configs across HTTP transports by [@seefs001](https://github.com/seefs001) in [#7627](https://github.com/QuantumNous/new-api/pull/7627)
- fix: use max_completion_tokens for gpt-6-sol and gpt-6-luna by [@feitianbubu](https://github.com/feitianbubu) in [#7559](https://github.com/QuantumNous/new-api/pull/7559)
- fix(web): Add class to wrap the long strings at auto-disable status tooltip content in channel manage page by [@makisekuris](https://github.com/makisekuris) in [#7604](https://github.com/QuantumNous/new-api/pull/7604)
- fix(web): hide system settings from non-root admins by [@jimmyleocn](https://github.com/jimmyleocn) in [#7513](https://github.com/QuantumNous/new-api/pull/7513)
- fix(i18n): keep cached zhTW interface code stable across page loads by [@yenchieh](https://github.com/yenchieh) in [#7139](https://github.com/QuantumNous/new-api/pull/7139)
- fix(web): correct translations, chart ordering, and font loading by [@seefs001](https://github.com/seefs001) in [#7628](https://github.com/QuantumNous/new-api/pull/7628)
- fix(relayconvert): keep Responses custom tools on Claude and Gemini upstreams by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7636](https://github.com/QuantumNous/new-api/pull/7636)
- fix(keys): prevent rounded clipping of group names by [@jimmyleocn](https://github.com/jimmyleocn) in [#7645](https://github.com/QuantumNous/new-api/pull/7645)
- fix(relaykit): Gemini stream token details, Responses tool-output media on Gemini, Opus 5.5 default effort by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7687](https://github.com/QuantumNous/new-api/pull/7687)
- feat(relay): web search encoding per channel and vendor-reported search billing by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7690](https://github.com/QuantumNous/new-api/pull/7690)
- feat: support regex conditions in advanced parameter overrides by [@seefs001](https://github.com/seefs001) in [#7698](https://github.com/QuantumNous/new-api/pull/7698)

## New Contributors

- [@makisekuris](https://github.com/makisekuris) made their first contribution in [#7604](https://github.com/QuantumNous/new-api/pull/7604)
- [@yenchieh](https://github.com/yenchieh) made their first contribution in [#7139](https://github.com/QuantumNous/new-api/pull/7139)
**Full Changelog**: [v1.0.0-rc.41...v1.0.0-rc.42](https://github.com/QuantumNous/new-api/compare/v1.0.0-rc.41...v1.0.0-rc.42)

### Contributors

- [ ![@yenchieh](https://avatars.githubusercontent.com/u/4801824?s=64&v=4) ](https://github.com/yenchieh)
- [ ![@feitianbubu](https://avatars.githubusercontent.com/u/6916415?s=64&v=4) ](https://github.com/feitianbubu)
- [ ![@makisekuris](https://avatars.githubusercontent.com/u/39204951?s=64&v=4) ](https://github.com/makisekuris)
- [ ![@seefs001](https://avatars.githubusercontent.com/u/40468931?s=64&v=4) ](https://github.com/seefs001)
- [ ![@jimmyleocn](https://avatars.githubusercontent.com/u/42566991?s=64&v=4) ](https://github.com/jimmyleocn)
- [ ![@Calcium-Ion](https://avatars.githubusercontent.com/u/61247483?s=64&v=4) ](https://github.com/Calcium-Ion)
 yenchieh, feitianbubu, and 4 other contributors

Assets 9

## v1.0.0-rc.41

Important

**Access Tokens & Task Plugins / 访问令牌与任务插件**

安全与访问里的单个面板访问令牌，改为最多 20 个具名访问令牌。创建时只显示一次，默认 30 天过期；作用域按本人已有权限勾选。升级后旧版令牌还能再用 30 天，之后会被拒绝，且不能重新生成，请在到期前换成新令牌。

管理员管理用户时，删除、改状态或角色、设置密码或权限、创建管理员、重置通行密钥、关闭两步验证、清除绑定，都需要一次性校验。额度调整，以及修改显示名、分组、备注，不需要。

任务插件改由 moejs 运行，性能大幅提升，插件接口不变。

豆包 Seedream 图片改走任务插件的 OpenAI Images（`/v1/images/generations`、`/v1/images/edits`）。新增 Seedream 5.0 Flash；各模型按自己的档位计价。任务插件收窄用量项之后，已保存的价格仍可编辑。

Security & Access replaces the single dashboard Access Token with up to 20 named Access tokens. A token is shown once at creation, expires in 30 days by default, and its Scopes stay within what the owner can already do. The Legacy token keeps working for 30 days after the upgrade, then it is rejected and cannot be regenerated. Replace it before then.

Admin user management now requires a single-use verification for delete, status or role changes, password or Permissions, creating an admin, resetting a Passkey, disabling 2FA, and clearing a binding. Quota adjustments, and edits to display name, Group, or remark, do not.

Task Plugins now run on moejs, with a large performance improvement.

Doubao Seedream images now go through the Task Plugin OpenAI Images paths (`/v1/images/generations`, `/v1/images/edits`). Seedream 5.0 Flash is added, and each model is priced on its own tiers. Prices saved before a Task Plugin narrows its usage facts stay editable.

## New Features

- Replaced the single dashboard Access Token with up to 20 named Access tokens on Security & Access. Tokens are shown once, use Scopes, and expire after 30 days by default.
- Access tokens can be renamed without verification. Changing Permissions requires a single-use proof bound to that token.
- Moved Task Plugins to moejs, with a large performance improvement. The plugin API is unchanged.
- Added Seedream 5.0 Flash, and price each Seedream model on its own tiers. Seedream images are served through the Task Plugin OpenAI Images protocol.
- Highlight differing values when comparing source price expressions ([#7543](https://github.com/QuantumNous/new-api/issues/7543)).
- Added a Refresh button on the Channels table.

## Fixes and Improvements

- Keep Pricing Configuration editable after a usage profile drops facts. Remaining prices stay in place.
- Keep Responses custom tools when converting to Chat Completions, so tools such as `exec` and `apply_patch` are no longer dropped.
- Preserve Claude auto-mode safeguards and per-message `output_config` ([#7598](https://github.com/QuantumNous/new-api/issues/7598), [#7561](https://github.com/QuantumNous/new-api/issues/7561)).
- Preserve the Responses WebSocket setting when saving a Channel ([#7468](https://github.com/QuantumNous/new-api/issues/7468)).
- Revalidate Marketplace downloads so a republished plugin source does not fail the integrity check from a stale cache.
- Reject non-standard roles when creating a user.
- Release binaries now embed the real version instead of `v0.0.0` ([#7536](https://github.com/QuantumNous/new-api/issues/7536)).

## What's Changed

- test(billing): fix websocket rejection refund test after pre-consume dropped output estimation by [@feitianbubu](https://github.com/feitianbubu) in [#7491](https://github.com/QuantumNous/new-api/pull/7491)
- fix(plugins/alibaba): keep upstream metadata in openai_image render by [@feitianbubu](https://github.com/feitianbubu) in [#7507](https://github.com/QuantumNous/new-api/pull/7507)
- fix(relayconvert): Responses→Chat 工具输出图片改为提升到后续 user 消息 by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7510](https://github.com/QuantumNous/new-api/pull/7510)
- fix(relayconvert): Claude tool_result 图片提升到 user 消息；Chat→Responses 流补齐 reasoning part 事件并按段切分 item by [@Calcium-Ion](https://github.com/Calcium-Ion) in [#7512](https://github.com/QuantumNous/new-api/pull/7512)
- fix(logs): keep model badge text readable and compact by [@Yorick-Ryu](https://github.com/Yorick-Ryu) in [#7504](https://github.com/QuantumNous/new-api/pull/7504)
- fix: move force operation into confirm slot so plugin-in-use dialog has one cancel button by [@feitianbubu](https://github.com/feitianbubu) in [#7528](https://github.com/QuantumNous/new-api/pull/7528)
- fix(web): keep text selection when opening a model pricing row for editing by [@RedwindA](https://github.com/RedwindA) in [#7403](https://github.com/QuantumNous/new-api/pull/7403)
- fix(ci): align ldflags -X package path with module path so release binaries embed the real version by [@mslchy](https://github.com/mslchy) in [#7536](https://github.com/QuantumNous/new-api/pull/7536)
- fix: match current price column width to source columns so expressions wrap alike by [@feitianbubu](https://github.com/feitianbubu) in [#7542](https://github.com/QuantumNous/new-api/pull/7542)
- feat: highlight differing values in source price expressions by [@feitianbubu](https://github.com/feitianbubu) in [#7543](https://github.com/QuantumNous/new-api/pull/7543)
- style(playground): add break-all to playground input by [@LauZzL](https://github.com/LauZzL) in [#6600](https://github.com/QuantumNous/new-api/pull/6600)
- fix(channel): preserve Responses WebSocket setting on save by [@zenor0](https://github.com/zenor0) in [#7468](https://github.com/QuantumNous/new-api/pull/7468)
- fix(claude): preserve per-message output_config in Claude mess

..._This content has been truncated to stay below 50000 characters_...
