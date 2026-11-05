---
url: https://veridrop.org/faq
captured: 2026-10-26
word_count: 1266
status: raw
---

×

## 中转站交流

扫码加入中转站同行交流群

![中转站同行交流群二维码](https://veridrop.org/static/veridrop-community.jpg)

# 常见问题

Veridrop 是 AI API 中转站检测工具,通过 Claude thinking signature 加密级验证 + 协议字段
\+ 用量指纹,识别中转站是否真实透传 Claude / OpenAI / Gemini 模型。本页汇总 **50 个**
关于中转站、真伪检测、工具使用、数据安全的常见问题。


最后更新:2026-10-16

## 中转站基础

「AI API 中转站」是第三方搭建的 API 转发服务,把你的请求代理给 OpenAI / Anthropic / Google 官方,再把响应返回给你。中转站千差万别 — 有的 1:1 透传,有的会改写字段、替换模型、注入 system prompt。这一组问题先讲清楚什么是中转站、为什么需要、风险在哪。

什么是 AI API 中转站?
[#](https://veridrop.org/faq#basics-what-is-relay)

中转站(relay,又叫「镜像」「代理」)是第三方搭建的 API 转发服务,把你的请求转给 OpenAI / Anthropic / Google 官方,再把响应原样返回给你。常见出现原因:国内无法直连官方域名、便宜的批发价、统一一个接口调多家模型。

为什么需要中转站?直接用官方不行吗?
[#](https://veridrop.org/faq#basics-why-use-relay)

三个常见原因:① 国内访问 anthropic.com / openai.com 需要科学上网;② 部分中转站把多家厂商的批发额度打包零售,价格比官方低 30-70%;③ 一些中转站把 Claude / GPT / Gemini 全统一成 OpenAI 兼容接口,代码只用维护一套。

中转站和官方 API 有什么区别?
[#](https://veridrop.org/faq#basics-relay-vs-official)

官方 API 字段、签名、错误格式都是确定的;中转站之间差异巨大 — 有的 1:1 透传,有的会改写 usage 字段、剥离 thinking 块、用别的模型替换、甚至注入额外 system prompt。Veridrop 检测的就是这种「中间到底动了什么」。

中转站合法吗?用了会不会出问题?
[#](https://veridrop.org/faq#basics-relay-legal)

法律上灰色地带,看具体合作模式。真正的实务风险有三:① **跑路风险** — 中转站随时可能停服、涨价、卷款消失,大额充值要慎重;② **模型响应跟官方不一致** — 中转站可能在中间动手脚(替换模型、剥离能力、虚报 token),影响你下游业务的稳定性;③ **prompt 内容被记录** — 涉及商业机密 / 用户数据的对话最好避开来路不明的中转站。建议小额测试,选信誉好的运营方,大额场景考虑直连官方。

用中转站的 API key 有什么风险?
[#](https://veridrop.org/faq#basics-relay-steal-key)

Veridrop 实测过很多家中转站,常见的坑有 5 种(都见过真实案例):① **偷偷换成别的模型** — 你买的是 GPT,实际给你跑的可能是 Claude 或其他更便宜的模型。表面上看不出来,但写出来的内容风格、思路、解题习惯都不对,用来做正经事很容易翻车。② **高级功能用不了** — 比如让模型严格按指定格式回话、让它读 PDF、调用工具这些进阶能力,在被「偷换」的中转站上经常失灵 — 因为后台换上来的便宜模型根本不会这一套。③ **计费数字不可信** — 同样一句话问几次,每次扣的钱都不一样;有的中转站干脆不告诉你这次用了多少 token,你根本对不上账。充值的钱很可能比官方贵不少,却没有任何凭证可查。④ **菜单上的模型实际没货** — 它对外宣称支持几十个模型,你真去用其中一些,直接报「没有这个模型」。Veridrop 在你提交检测前会先帮你试一下,免得你白等半分钟拿到一份全 0 分的报告。⑤ **规则说变就变** — 同一把 key,今天用得好好的,第二天可能突然提示「需要升级套餐」「分组失效」甚至直接封号。中转站后台规则可以无通知调整,大额充值之前最好先小额试用,并跑一次 Veridrop 看看实际表现。

「token 中转站」和「API 中转站」是一回事吗?
[#](https://veridrop.org/faq#basics-token-relay)

是一回事。中转站按 token 计费转售 Claude、GPT、Gemini 等模型的 API,所以也被叫作 token 中转站、token 站或 API 中转站。选的时候看两件事:给的是不是真模型,token 数有没有多算。这两项都可以在 Veridrop 用自己的 key 实测, [红黑榜](https://veridrop.org/leaderboard) 里也能查到别人测过的结果。

## 真伪识别

中转站「假货」是行业最大的痛点 — 你以为在用 Claude,实际可能跑的是 Kiro / Amazon Q;你以为在用 GPT-4o,实际后端是 Claude Haiku。这一组问题讲清楚作假手段和检测方法。

怎么知道我用的是真 Claude / GPT / Gemini 而不是替身?
[#](https://veridrop.org/faq#authenticity-verify-authentic)

三个方向:① 协议字段(id 前缀、object、finish\_reason 是否符合官方规范);② 能力指纹(thinking signature 加密签名、PDF 多模态、function calling shape);③ 用量字段(usage 里有没有混入异源痕迹如 claude\_cache\_creation\_\*)。Veridrop 把这三类合成 7-10 项检测。

中转站常见的「作假」手段有哪些?
[#](https://veridrop.org/faq#authenticity-common-fake-tactics)

5 种常见:① 用 Kiro / Amazon Q / Bedrock 跑 Claude 替身;② 用 Claude 后端跑 GPT 请求(usage 字段会暴露 claude\_\* 残留);③ 把 GPT-4o 偷换成 GPT-4o-mini 省成本;④ 剥离 thinking 块、PDF 多模态等高级能力;⑤ 注入额外 system prompt 改写身份回答。

直接问「你是谁」能验证模型真假吗?
[#](https://veridrop.org/faq#authenticity-ask-who-are-you)

不能。现代模型都被训练得知道怎么回答身份问题,而且中转站可以注入 system prompt 让模型说「我是 Claude」。Veridrop 把「身份一致性」检测的权重设为 5%,只作为最弱的辅助信号 — 真正可信的是 thinking signature 这种加密级指标。

Kiro / Amazon Q 假冒 Claude 怎么识破?
[#](https://veridrop.org/faq#authenticity-kiro-amazon-q)

Kiro 和 Amazon Q 是 Amazon 的 Claude 替身网关,响应没有 Claude thinking signature (它们走的是 AWS Bedrock 的简化接口,不返回服务端签名)。Veridrop 在 thinking\_signature 检测上会直接判 0 分,fail 整体检测。

中转站把 GPT 请求转给 Claude 后端,怎么发现?
[#](https://veridrop.org/faq#authenticity-gpt-becomes-claude)

看响应的 usage 字段。原生 OpenAI 只有 prompt\_tokens / completion\_tokens / total\_tokens 三个键。如果出现 claude\_cache\_creation\_5\_m\_tokens、usage\_source: anthropic 等字段,基本可以判定中转站在做协议转换。Veridrop 把这种指纹标记为严重问题。

有没有专门检测 Claude 的网站?和检测 OpenAI 有什么不同?
[#](https://veridrop.org/faq#authenticity-claude-detection-site)

Veridrop 的 [Claude 检测](https://veridrop.org/claude) 就是。Claude 有 thinking signature 这种服务端加密签名,可以直接验真,所以它是 Claude 检测里最硬的证据(权重 25%)。OpenAI 协议没有对应的签名, [OpenAI 检测](https://veridrop.org/openai) 主要看协议字段和 usage 指纹,比如响应里出现 `claude_*` 字段,就说明后端不是 GPT。两边都是发真实请求,每份报告有公开链接可以复核。

## 掺水与降智

「掺水」是中转站用户问得最多的问题之一:钱花了,模型却变笨了、token 用得特别快。这一组讲掺水有哪几种、怎么验。

中转站「掺水」是什么意思?有哪几种?
[#](https://veridrop.org/faq#watering-what-is-watering)

掺水指中转站实际给的比宣称的少,常见 3 种:① **换模型**,把 Opus、GPT 旗舰换成便宜型号或别家模型;② **多算 token**,usage 里的输入输出数比真实值高;③ **砍能力**,截断长上下文,去掉 thinking、工具调用或多模态。掺水的站照样能正常回复,所以发一句话测试看不出来,要用针对性的检测。

怎么检测中转站有没有掺水(纯度测试)?
[#](https://veridrop.org/faq#watering-detect-watering)

分三步:① 验模型:Claude 看 thinking signature 服务端签名,GPT 看 usage 里有没有 `claude_*` 这类异源字段;② 验 token:发受控请求,看输入 token 的涨幅是否合理、流式和非流式用量是否一致;③ 验能力:在长文本里埋 3 处信息看能否找回,再测工具调用和结构化输出。在 [Claude](https://veridrop.org/claude) / [OpenAI](https://veridrop.org/openai) / [Gemini](https://veridrop.org/gemini) 检测页跑一次 standard 模式可以覆盖前两步,长上下文要单独勾选。

Claude Code 变笨了,是中转站换了模型吗?
[#](https://veridrop.org/faq#watering-claude-code-dumber)

有可能,先分清两种情况。如果中转站换了模型或走了替身渠道(如 Kiro、Amazon Q),响应里拿不到 Claude 的 thinking signature,Veridrop 这一项会直接判 0 分。如果签名正常,变笨更可能是上下文被截断,或者中转站注入了额外的 system prompt,这时看 integrity 和长上下文两项。用你在 Claude Code 里配的同一个 base\_url 和 key 去 [Claude 检测页](https://veridrop.org/claude) 跑一次就能区分。

## Claude API 中转站

Claude 是 Veridrop 检测最深入的协议 — 因为 Claude 有 thinking signature 这种加密级可验证指标,业内目前只有 Veridrop 利用了这个信号。

thinking signature 是什么?为什么是真伪验证的金标准?
[#](https://veridrop.org/faq#claude-thinking-signature)

thinking signature 是 Claude 启用扩展思考时,响应里 signature 字段返回的服务端加密产物,长度 500-2000 字符。这个签名由 Anthropic 服务端生成,带加密验证 — 中转站理论上无法伪造。Veridrop 把它作为 25% 权重的核心检测项。

Claude code 中转站怎么挑?
[#](https://veridrop.org/faq#claude-claude-code-relay)

关键看 4 点:① 跑一次 Veridrop 看 thinking signature 是否拿到 100 分;② 看 usage 里有没有 claude\_\* 之外的异源字段;③ 看 stream / non-stream 一致性(中转站常常在两条路径上做不同处理);④ 看消息 id 是否符合 msg\_ / toolu\_ / srvtoolu\_ 前缀规范。

Veridrop 的 Claude 检测覆盖哪些维度?
[#](https://veridrop.org/faq#claude-claude-detector-coverage)

11 项常规检测,另有 1 项用户主动付费启用的长上下文检测。常规检测按权重:thinking signature (25%) > behavioral signature (15%) > structured output (12%) > consistency / knowledge / token usage (各 10%) > pdf (8%) > identity / protocol / integrity / message\_id (各 5%)。standard 模式跑 9 项常规检测 ~45 秒,full 模式跑完整 11 项常规检测 ~75 秒;长上下文结果独立显示,不由普通总分代替。

Claude 中转站 stream 模式没返回 thinking 怎么回事?
[#](https://veridrop.org/faq#claude-claude-stream-no-thinking)

这是 Claude Opus 4.7 已知的 API drift — adaptive thinking + streaming + summarized 的组合下,SSE 流里不出现 thinking 块(non-stream 正常)。Veridrop 的 thinking\_signature detector 已经针对这个切到非流式,确保检测可靠。

检测时为什么要消耗 token?成本多少?
[#](https://veridrop.org/faq#claude-claude-cost)

检测发真请求,每次 standard 模式约 12 个 API 调用,token 总消耗 ~3000-5000 (取决于 thinking 是否触发)。按 Haiku 价格 ~$0.012,Sonnet ~$0.05,Opus ~$0.20。Veridrop 自己不收费 — 你付的是上游 API 的真实 token 钱。

检测出 0 分是不是这家中转站完全没用?
[#](https://veridrop.org/faq#claude-claude-zero-score)

看具体情况。常见 0 分原因:① API key 失效或额度耗尽(检测无效 banner 会提示);② 中转站不支持你选的模型(preflight 会提前 422 拒绝);③ 真的是非常垃圾的中转站。看每项 detector 的 details 而不是只看总分。

## OpenAI 中转站

OpenAI 协议没有像 thinking signature 这样的加密级指标,Veridrop 在 OpenAI 上主要做「协议合规 + 适配层指纹识别」 — 抓中转站用 Anthropic / Google 后端伪装 GPT 的痕迹。

OpenAI 中转站把 GPT 偷换成 Claude 有什么直接证据?
[#](https://veridrop.org/faq#openai-openai-fake-evidence)

响应的 usage 字段是最直接的证据。真原生 OpenAI 只有 prompt\_tokens / completion\_tokens / total\_tokens。如果发现 claude\_cache\_creation\_5\_m\_tokens、usage\_source: anthropic、或 input\_tokens / output\_tokens(Anthropic 命名),基本可以判定中转站在协议转换。Veridrop 标为严重问题,直接拒绝该项 detector。

我的 GPT-4o 检测出 75 分,verdict 是 marginal,怎么解读?
[#](https://veridrop.org/faq#openai-openai-75-marginal)

75 分本身在「通过」区间,但如果有任何严重问题 (尤其 protocol detector 报多个严重问题),Veridrop 会把 verdict 砍到 marginal — 圆圈变黄、提示「存在风险」。这通常意味着接口能用但中转站在做协议转换,实际跑的可能不是真的 GPT 模型。

response\_format=json\_schema strict 不生效是什么意思?
[#](https://veridrop.org/faq#openai-openai-strict-json)

OpenAI strict 模式应该返回纯 JSON,不能包 Markdown 代码块。如果返回 \`\`\`json {...} \`\`\` 格式,有两种可能:① 中转站没透传 response\_format 参数;② 透传了但底层模型(很可能不是 GPT)不理解 strict 模式。Veridrop 通过 markdown\_json\_seen 标志区分这两种情况。

我用的中转站 model 字段返回 gpt-4o,但响应明显不像 GPT,怎么办?
[#](https://veridrop.org/faq#openai-openai-model-mismatch)

model 字段只是字符串,中转站可以填任何值。真伪要看其他指标:① Veridrop 协议规范性 detector 会扫 usage 字段指纹;② 行为差异(GPT 偏简洁,Claude 偏礼貌啰嗦);③ 多次调用的 token 数 CV(模型一致性 detector)。

OpenAI 中转站测出来 0 个模型可用怎么办?
[#](https://veridrop.org/faq#openai-openai-no-models)

Veridrop 的预探测会列出该 key 在中转站上有多少模型属于本协议。如果当前页是 OpenAI 但 0 个 GPT 模型,会显示一个黄色卡片提示「该 key 在此中转站没有 GPT 模型,但有 X 个 Claude 模型 / Y 个 Gemini 模型 → 一键跳转测那边」。

Codex 中转站怎么验证给的是真 GPT?
[#](https://veridrop.org/faq#openai-codex-relay-verify)

用你在 Codex 里配置的同一个 base\_url 和 key,到 [OpenAI 检测页](https://veridrop.org/openai) 选对应的 GPT 模型跑一次。重点看三项:① protocol 有没有严重问题,usage 里出现 `claude_*` 或 Anthropic 命名的字段,说明后端不是 GPT;② function calling 是否正常,Codex 依赖工具调用;③ token 数是否可信。检测走的是对话接口,通过说明这家的模型和用量是真的;Codex 客户端自己的配置问题不在检测范围内。

## Gemini API 中转站

Veridrop 的 Gemini 检测只走 OpenAI 兼容路径(POST /chat/completions),因为 99% 的第三方 Gemini 中转站都用这条。Gemini 3 系列默认开 thinking,对 max\_tokens 设置和 token 用量统计有特殊要求。

为什么 Gemini API 中转站经常 model\_not\_found?
[#](https://veridrop.org/faq#gemini-gemini-model-not-found)

三种可能:① 中转站只代理部分 Gemini 模型(很多中转站只有 3.x preview 系列,没有 2.5);② 模型名拼写差异(gemini-2.5-flash vs models/gemini-2.5-flash);③ 模型已下架。Veridrop 提交前会做 preflight,500ms 内识别死模型并给出可用列表替代。

Gemini 3.x preview 检测时 max\_completion\_tokens 应该填多少?
[#](https://veridrop.org/faq#gemini-gemini-thinking-default)

至少 64,推荐 128+。Gemini 3 默认开 thinking,会消耗 30-60 reasoning\_tokens 才输出文本。如果 max 太小(< 32),thinking 占满后没空间出文本,响应就是空字符串 + finish\_reason=length。Veridrop 的 detector 已经把 max 调到 64-384。

Veridrop 为什么不支持 Gemini 原生 /v1beta/models/X:generateContent 路径?
[#](https://veridrop.org/faq#gemini-gemini-no-native)

99% 的第三方 Gemini 中转站只暴露 OpenAI 兼容协议,Google 官方也提供 OpenAI 兼容端点 /v1beta/openai。维护两套独立的检测逻辑成本高且容易引入翻译层导致结果失真,所以 Veridrop 集中在 OpenAI 兼容路径上做透。

Gemini 中转站怎么挑?
[#](https://veridrop.org/faq#gemini-gemini-pick)

三档:① 必须支持 gemini-2.5-flash 或 gemini-3-flash-preview(2026 stable);② Veridrop 上跑出 protocol 检测 ≥ 80;③ usage 字段没有 gemini\_\* 之外的异源残留(意味着没在转协议)。Veridrop 自动按推荐顺序排序中转站的模型列表。

Google 官方 Gemini API 也能用 Veridrop 测吗?
[#](https://veridrop.org/faq#gemini-gemini-google-official)

可以。base\_url 填 https://generativelanguage.googleapis.com/v1beta/openai,api\_key 用 Google AI Studio 申请的 AIza... key。Google 官方端点应该全 7 项 100 分,可作为基线对比第三方中转站。

## Veridrop 工具使用

工具本身的使用、报告解读、自托管等问题。

Veridrop 怎么用?最简流程?
[#](https://veridrop.org/faq#veridrop-how-to-use)

三步:① 打开 veridrop.org/claude(或 /openai、/gemini);② 填中转站 base\_url + api\_key,选模型(下拉自动列出该 key 在该中转站可用的模型);③ 点「开始检测」,30-60 秒拿到报告。报告 URL 永久可分享(/r/{job\_id}),也能下载 JPG。

standard / quick / full 三档模式有什么区别?
[#](https://veridrop.org/faq#veridrop-modes-difference)

quick (~15s, 3-5 项) 适合快速摸排;standard (~40s, 7-8 项) 是默认推荐;full (~70s, 全 10 项) 是完整检测,推荐拿来跟官方基线 1:1 对比。所有模式都会跑 thinking signature 这种核心项。

报告分数怎么解读?
[#](https://veridrop.org/faq#veridrop-how-to-read-score)

总分加权:≥85 优秀(绿)/ 70-84 通过(浅绿)/ 50-69 marginal(黄)/ <50 未达标(红)。但任意 detector 报严重问题,verdict 会被砍到 marginal(圆圈变黄)— 即使分数够 70 也不绿。点每项 detector 看 details 里的 sub\_checks 找扣分原因。

检测报告链接 /r/xxx 谁能看到?
[#](https://veridrop.org/faq#veridrop-report-link-public)

任何人拿到链接都能看(匿名、不加密)。报告里不含你的 API key 明文,只有脱敏形式(sk-y7xU••••••0h)。如果你测的是私有中转站不想公开,不要分享 URL。后续会加 opt-in 的「私有报告」开关。

可以本地自托管 Veridrop 吗?
[#](https://veridrop.org/faq#veridrop-self-host)

可以,Veridrop 完全开源。clone 仓库 → pip install -e .\[web\] → uvicorn web.server:app 即可。CLI 也可以单独用:relay-detector detect --base-url ... --api-key ... --mode full。详见 README。

Veridrop 怎么赚钱?会变成 SaaS 收费吗?
[#](https://veridrop.org/faq#veridrop-how-veridrop-earns)

三个收入流:① 联盟合作— 用户通过站内「前往中转站」按钮注册时,我们可能从中转站获得佣金,但不影响用户实际支付价格;② 基础收录与站长后台套餐;③ 已上线的模型级 S 赞助位（当前 4 个模型组均为 S1–S10）和 Top1–Top10精选位(均明确标识为付费展示)。公开检测工具本身永久免费、无需注册。详见 /about/affiliate 联盟透明度页。

联盟合作会影响中转站评分吗?Veridrop 是公正的吗?
[#](https://veridrop.org/faq#veridrop-affiliate-bias)

联盟收入与评分严格隔离 — 我们不会因为商家给佣金就把「未达标」改成「通过」。检测算法对所有中转站一视同仁,代码完全开源(AGPL-3.0),评分公式公开,可逐行审计。即使是付费 Featured 客户,被检出严重问题 仍标严重问题。如发现实际行为与承诺不符,欢迎在 GitHub Issues 公开举报。详见 /about/affiliate。

## 隐私与安全

把 API key 交给一个检测工具是有风险的事,所以 Veridrop 在数据处理上的承诺需要可验证 — 我们的代码完全开源,你可以审计、可以自托管。

Veridrop 会记录我的 API key 吗?
[#](https://veridrop.org/faq#privacy-key-stored)

不会把 API key 明文写入报告或日志。生产异步检测会把经过认证加密的密文临时存入任务队列,worker 执行时只在内存解密,任务成功或失败后清空;站长主动开启持续探测时,专用 key 会以密文保存到撤销为止。报告里只保留脱敏形式 (sk-y7xU••••••0h)。

跟 cctest.ai 在数据安全上有什么区别?
[#](https://veridrop.org/faq#privacy-vs-cctest-privacy)

cctest.ai 也声称不上传 key,但代码闭源无法验证。Veridrop 完全开源,你可以 clone 代码自己跑(git clone ... && uvicorn web.server:app),或者审计服务端代码(GitHub 上完全公开)。

检测过程会调用上游产生费用吗?
[#](https://veridrop.org/faq#privacy-upstream-cost)

会,但很少。standard 模式约 12 个真实请求,token 总消耗 3000-5000。按 Haiku 大约 $0.012,Sonnet $0.05,Opus $0.20。这个钱付给上游(中转站或官方),Veridrop 自身不收费。

报告里有什么个人信息?可以删除吗?
[#](https://veridrop.org/faq#privacy-personal-info)

报告只包含:① 脱敏后的 base\_url;② 脱敏后的 api\_key;③ 检测结果。没有个人姓名、邮箱、IP。如果需要删除特定报告,GitHub issue 联系即可。

## 工具对比

中转站检测领域不止 Veridrop 一家,这一组讲清楚 Veridrop 跟同类工具的差异、以及怎么挑中转站。

Veridrop 跟 cctest.ai 有什么区别?
[#](https://veridrop.org/faq#compare-vs-cctest)

CCTest 以 Claude 检测为主,现在也可以选 ChatGPT,提供「模型是否被替换」和「Token 用量是否异常」两项检测。Veridrop 覆盖 Claude / OpenAI / Gemini 三个协议,Claude 上用加密级的 thinking signature 验真,OpenAI 上能识别「GPT 实为 Claude」的协议转换指纹,每份报告公开可复核,并且完全开源。

Veridrop 跟 hvoy.ai 有什么区别?
[#](https://veridrop.org/faq#compare-vs-hvoy)

hvoy 也支持三协议,但检测维度浅(主要是协议合规)。Veridrop 在 Claude 上有加密级 thinking signature 验证(独家)、OpenAI 上有协议转换指纹识别(usage\_source 等严重问题)、Gemini 上适配 thinking-by-default 模型,深度更够。

中转站排行榜和评测站这么多,和 Veridrop 是什么关系?
[#](https://veridrop.org/faq#compare-vs-leaderboards)

可以分三类:① 排名和推荐类(如 aiapipk.com、禾维 AI 的排名),适合找候选;② 目录和监测类(如 LMSpeed、TokenAPI Scan、AI中转站监视者、OkkMax),看价格、延迟和排行;③ 检测类(Veridrop、CCTest、Ofox、真测等),验证模型真假。可以配合用:先用榜单找候选,再用检测工具验证。Veridrop 的每份报告都有公开链接可以复核。详见 [检测工具横评](https://veridrop.org/compare/relay-detectors)。

怎么挑中转站?有什么硬性指标?
[#](https://veridrop.org/faq#compare-how-to-pick-relay)

Veridrop 推荐 5 条硬指标:① thinking signature ≥ 100;② protocol 严重问题数量 = 0;③ stream / non-stream usage 一致;④ 模型 id 字段匹配请求模型(model\_consistency pass);⑤ 多次请求 completion\_tokens CV < 0.10(稳定性)。

AI 中转站哪个好用又便宜?怎么自己判断?
[#](https://veridrop.org/faq#compare-which-relay-good-cheap)

没有固定答案,价格和质量一直在变,而且便宜的站更容易掺水。建议这样筛:先在 [红黑榜](https://veridrop.org/leaderboard) 找检测次数多、中位分高、没有严重问题的站;再比它们的倍率;最后用自己的 key 跑一次检测确认。只看价格,或者只看一次高分,都不可靠。

中转站的价格和倍率怎么比才公平?
[#](https://veridrop.org/faq#compare-price-multiplier)

倍率只有在 token 数真实时才有意义。同样标 0.5 倍,如果输入 token 被多算了三成,实际花的并不少。比价之前先确认三件事:① token 数是否可信(Veridrop 的 token usage / token billing 检测);② 给的是不是标称的模型;③ 缓存读写怎么计费。三条都过了,再比倍率。

怎么查某一家中转站靠不靠谱?
[#](https://veridrop.org/faq#compare-check-one-relay)

在 [历史查询](https://veridrop.org/search) 输入它的域名,能看到 Veridrop 有没有测过、测过多少次、最近的分数和结论。点进详情页看三样:检测次数(一两次说明不了问题)、中位分、有没有严重问题记录。没有记录的站,用自己的 key 跑一次检测,结果会进入历史。

## 没找到答案?

欢迎在
[GitHub](https://github.com/canarybyte/veridrop)
提 issue,或者直接 [跑一次检测](https://veridrop.org/claude) 看实际结果 — Veridrop
的报告 details 里包含具体的扣分原因,通常自带答案。