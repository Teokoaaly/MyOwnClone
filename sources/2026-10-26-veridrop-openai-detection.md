---
url: https://veridrop.org/openai
captured: 2026-10-26
word_count: 287
status: raw
---

×

## 中转站交流

扫码加入中转站同行交流群

![中转站同行交流群二维码](https://veridrop.org/static/veridrop-community.jpg)

# OpenAI / GPT 中转站检测

**Veridrop** 通过 8 项 Chat Completions 协议检测 + **usage 字段后端指纹识别**,
**1 分钟** 识别中转站是真透传 GPT,还是把请求偷偷转给 Claude / Gemini 后端再伪装成 OpenAI 响应。免费、API key 不留存、代码开源。


新模型支持

## GPT‑6 Astra 检测已上线

Veridrop 已支持 GPT‑6 Astra 检测，覆盖接口响应、工具调用、结构化输出、流式一致性与 Token 用量检查，并提供可选的标准与极限长上下文检测，帮助你检查中转站的接口兼容性与长文本召回表现。

**23** 今日 Astra 报告

[立即检测 Astra](https://veridrop.org/openai#detect-form) [查看 OpenAI 排名 →](https://veridrop.org/leaderboard/openai)

**行为/协议级验证:**
 本检测无法可靠区分高配模型真品与低配模型伪装。我们检测的是中转站接口是否符合 OpenAI
 Chat Completions 协议规范、能力是否完整、usage 字段是否符合官方响应形状。

中转站接口地址

OpenAI-compatible 根 URL,可填 `https://api.example.com` 或 `https://api.example.com/v1`。

API 密钥

仅用于本次检测,不写入报告、不持久化。

目标模型

- gpt-5.6-sol
- gpt-6-astra
- gpt-5.6-terra
- gpt-5.6-luna
- gpt-5.5
- gpt-5.4
- gpt-5.3-codex
- gpt-5.4-nano
- gpt-5.4-mini

检测深度快速 (~15 秒,3 项)标准 (~40 秒,6 项)完整 (~70 秒,全 6 项)

**深度检测:长上下文真实性**
额外发 32k → 100k → 200k tokens 探针验证中转站是否真实兑现宣传的
context window(识别截断 / 路由到小窗口模型)。失败立即停。
**费用随模型和中转站定价而变,由你的 API key 支付。GPT-6 Astra 官方标准输入价估算约 $3.32。**

**极限检测:模型完整 context**
按模型上限等比探测(如 1M 模型测 32k → 500k → 950k)。
能 catch「宣传 1M 实际只给 200k」这类高端中转站欺诈,
标准档完全测不到。
**费用随模型和中转站定价而变。GPT-6 Astra 最大输入 922k,探测 32k → 461k → 875.9k,官方标准输入价估算约 $27.06,不含输出和中转站加价。**

GPT-6 Astra 的函数调用通过 Responses API 检查；中转站需同时支持 Chat Completions 和 Responses。常规检测默认不启用长上下文。

 开始检测


### Chat Completions

验证 `chatcmpl-`、`chat.completion`、choices、finish\_reason、usage 等官方响应结构。

### 能力完整性

执行 tool call 与 JSON schema 探测,识别把 OpenAI 协议包装成简化文本接口的中转层。

### 字段差异

记录 stream/non-stream 一致性与 usage 字段结构,识别常见包装层和协议适配异常。

## 常见问题(精选)

我花钱买的是 GPT,怎么知道中转站没偷偷换成更便宜的模型?

看响应里有没有「穿帮」的字段。OpenAI 官方回包里只会出现三个 token 计数字段;
但如果中转站偷偷把你的请求转给了 Claude 后端、再包装成 OpenAI 格式发回来,
Anthropic 那边的字段经常会跟着漏出来。Veridrop 一旦在响应里抓到这种本不该出现的字段,
就会把它标记成「严重问题」,整体评级降到黄色。

简单说:正版 GPT 会按 OpenAI 自家说明书回话,
冒牌的偷懒包装层经常露出对面厂家的痕迹。

我得了 75 分,为什么圆圈还是黄色而不是绿色?

分数只是其中一个维度。Veridrop 还会看「有没有严重问题」 — 哪怕分数到了通过线,
只要存在 1 条严重问题(比如上面说的字段穿帮),整体结论就会降到黄色「小心使用」。

遇到这种情况通常意味着:接口能用、能返回结果,但跑的可能不是你以为的那个模型。
如果你只是聊天、写写日常文本可能没大问题;但如果用来跑代码、做严肃任务,建议换一家。

测完显示「0 个 GPT 模型可用」,是中转站挂了吗?

大概率不是中转站坏了,而是 **这把 key 没开通 GPT 模型权限**。
很多综合中转站把模型按厂家分组卖,有的客户买的是 Claude 卡、有的是 Gemini 卡,
没买就调不出对应模型。

Veridrop 检测前会先快速看一眼你这把 key 能用哪些模型 — 如果当前是 OpenAI 页但 0 个 GPT,
系统会自动提示你「这把 key 实际能用 X 个 Claude 模型,要去那边测吗?」直接点过去就行。

为什么 OpenAI 的检测不像 Claude 那样能「拍胸脯保证真伪」?

因为 OpenAI 没在响应里放「数学证明」级别的防伪码。Claude 有一种叫
**thinking signature** 的加密签名,中转站没法伪造,所以 Veridrop 在
Claude 那边能给出非常确定的结论。

OpenAI 这边只能从「行为像不像 GPT、字段格式对不对、能力完不完整」这些间接线索判断,
所以我们的口径是「 **行为/协议级**」检测 — 能告诉你「看起来正常」或者
「看起来可疑」,但做不到 100% 数学证明。想要确定结论,推荐用 Claude 模型检测同一家中转站。

更多 OpenAI 中转站问题 → [/faq#openai](https://veridrop.org/faq#openai)
· 全部 [常见问题](https://veridrop.org/faq)