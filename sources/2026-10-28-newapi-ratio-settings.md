---
url: https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings
captured: 2026-10-28
word_count: 1422
status: raw
---

[User Guide](https://docs.newapi.pro/en/docs) [Installation](https://docs.newapi.pro/en/docs/installation) [API Reference](https://docs.newapi.pro/en/docs/api) [AI Applications](https://docs.newapi.pro/en/docs/apps) [Skills](https://docs.newapi.pro/en/docs/skills) [Help & Support](https://docs.newapi.pro/en/docs/support) [Business Cooperation](https://docs.newapi.pro/en/docs/business)

# Ratio Settings

Copy MarkdownOpen

Ratio settings are a core configuration of NewAPI's internal cost accounting system. By setting different ratios, you can flexibly control internal cost allocation, budget control, or enterprise customer billing standards for various models and user groups.

## [Ratio System Overview](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#ratio-system-overview)

NewAPI uses a three-tier ratio system to calculate user quota consumption:

1. **Model Ratio** \- Defines the base billing multiplier for different AI models
2. **Completion Ratio** \- Applies additional billing adjustments to output tokens
3. **Group Ratio** \- Sets differentiated billing multipliers for different user groups

### [Relationship between Quota and Ratios](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#relationship-between-quota-and-ratios)

In the New API system, ratios are key parameters for calculating quota consumption. Quota is the internal billing unit of the system, and all API calls are ultimately converted into quota points for deduction.

Quota Unit Conversion:

- 1 USD = 500,000 quota points
- Quota points are the basic unit for internal system billing
- User balances and consumption records are based on quota points

### [Quota Calculation Formulas](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#quota-calculation-formulas)

#### [Pay-as-you-go Models (Based on Token Consumption)](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#pay-as-you-go-models-based-on-token-consumption)

```
配额消耗 = (输入token数 + 输出token数 × 补全倍率) × 模型倍率 × 分组倍率
```

#### [Per-call Billing Models (Fixed Price)](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#per-call-billing-models-fixed-price)

```
配额消耗 = 模型固定价格 × 分组倍率 × 配额单位(500,000)
```

#### [Audio Models (Special handling, automatically processed internally by New API)](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#audio-models-special-handling-automatically-processed-internally-by-new-api)

```
配额消耗 = (文本输入token + 文本输出token × 补全倍率 + 音频输入token × 音频倍率 + 音频输出token × 音频倍率 × 音频补全倍率) × 模型倍率 × 分组倍率
```

#### [Pre-consumption and Post-consumption Mechanism](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#pre-consumption-and-post-consumption-mechanism)

New API adopts a dual billing mechanism of pre-consumption and post-consumption:

1. **Pre-consumption Phase**: Before an API call, calculate and pre-deduct quota consumption based on estimated token count.
2. **Post-consumption Phase**: After an API call is completed, recalculate quota consumption based on actual token count.
3. **Difference Adjustment**: If the actual consumption differs from the pre-consumption, the system will automatically adjust the user's quota balance.

```
预消费配额 = 预估token数 × 模型倍率 × 分组倍率
实际配额 = 实际token数 × 模型倍率 × 分组倍率
配额调整 = 实际配额 - 预消费配额
```

## [Model Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#model-ratio-settings)

Model ratios define the base billing multipliers for different AI models, and the system pre-sets default ratios for various models.

### [Examples of Common Model Ratios](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#examples-of-common-model-ratios)

| Model Name | Model Ratio | Completion Ratio | Official Price (Input) | Official Price (Output) |
| --- | --- | --- | --- | --- |
| gpt-4o | 1.25 | 4 | $2.5/1M Tokens | $10/1M Tokens |
| gpt-3.5-turbo | 0.25 | 1.33 | $0.5/1M Tokens | $1.5/1M Tokens |
| gpt-4o-mini | 0.075 | 4 | $0.15/1M Tokens | $0.6/1M Tokens |
| o1 | 7.5 | 4 | $15/1M Tokens | $60/1M Tokens |

Ratio Meaning Explanation:

- **Model Ratio**: A multiplier relative to the base billing unit, reflecting cost differences between models
- **Completion Ratio**: The billing multiplier for output tokens relative to input tokens, reflecting output cost differences
- Higher ratio means more quota consumed; lower ratio means less quota consumed

### [Setup Methods](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#setup-methods)

1. **JSON Format Setting**: Directly edit the model ratio JSON configuration
2. **Visual Editor**: Set ratios via a graphical interface

![倍率1](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Frate-setting-1.02dtz5rp-dq4j.png&w=3840&q=75)

## [Completion Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#completion-ratio-settings)

The completion ratio is used for additional billing of output tokens, primarily to balance the input and output cost differences of various models.

### [Default Completion Ratios](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#default-completion-ratios)

| Model Type | Official Price (Input) | Official Price (Output) | Completion Ratio | Description |
| --- | --- | --- | --- | --- |
| gpt-4o | 2.5$/1M Tokens | 10$/1M Tokens | 4 | Output is 4x input |
| gpt-3.5-turbo | 0.5$/1M Tokens | 1$/1M Tokens | 2 | Output is 2x input |
| gpt-image-1 | 5$/1M Tokens | 40$/1M Tokens | 8 | Output is 8x input |
| gpt-4o-mini | 0.15$/1M Tokens | 0.6$/1M Tokens | 4 | Output is 4x input |
| Other Models | 1 | 1 | 1 | Output is 1x input |

### [Setup Instructions](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#setup-instructions)

- The completion ratio primarily affects the billing of output tokens
- Setting it to 1 means output token billing is the same as input token billing
- Greater than 1 means higher billing for output tokens, less than 1 means lower billing for output tokens

## [Group Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#group-ratio-settings)

Group ratios allow setting differentiated billing multipliers for different user groups, enabling internal cost allocation, budget control, or enterprise customer billing configuration.

### [Group Ratio Configuration](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#group-ratio-configuration)

```
{
  "internal-test": 0.5,
  "standard": 1.0,
  "enterprise-client": 0.8,
  "trial": 2.0
}
```

### [Group Ratio Priority](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#group-ratio-priority)

1. **User-specific Ratio**: Individual ratio set for a particular user
2. **Group Ratio**: The ratio of the group the user belongs to
3. **Default Ratio**: System default ratio (usually 1.0)

![倍率2](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Frate-setting-2.3-sp2f4p1nlgt.png&w=3840&q=75)

## [Visual Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#visual-ratio-settings)

The visual editor provides an intuitive ratio management interface, supporting:

- Batch editing of model ratios
- Real-time preview of ratio configurations
- Conflict detection and alerts
- One-click synchronization of upstream ratios

![倍率3](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Frate-setting-3.0lj6oox2fk2ck.png&w=3840&q=75)

## [Models Without Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#models-without-ratio-settings)

For models without ratio settings, the system will:

1. **Self-use Mode**: Use the default ratio of 37.5
2. **Billing Mode**: Prompt with "Ratio or price not configured" error
3. **Automatic Detection**: Display unconfigured models in the management interface

![倍率4](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Frate-setting-4.0_z9xdzr0dn9j.png&w=3840&q=75)

## [Upstream Ratio Synchronization](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#upstream-ratio-synchronization)

The system supports automatic synchronization of ratio settings from upstream channels:

- Only synchronize legally authorized upstream public or authorized available price/model metadata
- Batch update local ratio configurations
- Stay synchronized with upstream prices
- Supports manual adjustment and override

![倍率5](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Frate-setting-5.0d1k0kkeqk-38.png&w=3840&q=75)

## [Frequently Asked Questions](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#frequently-asked-questions)

### [Q: How do I set ratios for new models?](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#q-how-do-i-set-ratios-for-new-models)

A: You can add new models via the visual editor or directly in the JSON configuration. It is recommended to set a conservative ratio first and adjust it based on actual usage.

### [Q: How do group ratios take effect?](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#q-how-do-group-ratios-take-effect)

A: Group ratios are multiplied by model ratios, ultimately affecting the calculation of user quota consumption. A user's actual ratio = Model Ratio × Group Ratio.

### [Q: What is the purpose of the completion ratio?](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#q-what-is-the-purpose-of-the-completion-ratio)

A: The completion ratio is mainly used to balance the cost differences between input and output tokens. The output cost of some models is significantly higher than the input cost, requiring adjustment via the completion ratio.

### [Q: How do I batch set ratios for similar models?](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#q-how-do-i-batch-set-ratios-for-similar-models)

A: You can perform batch operations through the visual editor, or directly add ratio settings for similar models in bulk within the JSON configuration.

## [Quota Calculation Examples](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#quota-calculation-examples)

### [Example 1: GPT-4 Standard User Conversation](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#example-1-gpt-4-standard-user-conversation)

Scenario Parameters:

- Input Tokens: 1,000
- Output Tokens: 500
- Model Ratio: 15
- Completion Ratio: 2
- Group Ratio: 1.0 (Standard User)

Calculation Process:

```
配额消耗 = (1,000 + 500 × 2) × 15 × 1.0
         = (1,000 + 1,000) × 15
         = 2,000 × 15
         = 30,000 配额点数
```

Equivalent USD Cost: 30,000 ÷ 500,000 = $0.06

### [Example 2: GPT-3.5 Internal Test Group Conversation](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#example-2-gpt-35-internal-test-group-conversation)

Scenario Parameters:

- Input Tokens: 2,000
- Output Tokens: 1,000
- Model Ratio: 0.25
- Completion Ratio: 1.33
- Group Ratio: 0.5 (Internal Test Group)

Calculation Process:

```
配额消耗 = (2,000 + 1,000 × 1.33) × 0.25 × 0.5
         = (2,000 + 1,330) × 0.125
         = 3,330 × 0.125
         = 416.25 配额点数
```

Equivalent USD Cost: 416.25 ÷ 500,000 = $0.00083

### [Example 3: Per-call Billing Model (e.g., Midjourney)](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings\#example-3-per-call-billing-model-eg-midjourney)

Scenario Parameters:

- Model Fixed Price: $0.02
- Group Ratio: 1.0 (Standard User)
- Quota Unit: 500,000

Calculation Process:

```
配额消耗 = 0.02 × 1.0 × 500,000
         = 10,000 配额点数
```

Equivalent USD Cost: 10,000 ÷ 500,000 = $0.02

For more billing rules, please refer to [Frequently Asked Questions](https://docs.newapi.pro/en/docs/support/faq)

How is this guide?

GoodBad

Last updated on 9/11/2026

### On this page

[Ratio System Overview](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#ratio-system-overview) [Relationship between Quota and Ratios](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#relationship-between-quota-and-ratios) [Quota Calculation Formulas](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#quota-calculation-formulas) [Pay-as-you-go Models (Based on Token Consumption)](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#pay-as-you-go-models-based-on-token-consumption) [Per-call Billing Models (Fixed Price)](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#per-call-billing-models-fixed-price) [Audio Models (Special handling, automatically processed internally by New API)](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#audio-models-special-handling-automatically-processed-internally-by-new-api) [Pre-consumption and Post-consumption Mechanism](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#pre-consumption-and-post-consumption-mechanism) [Model Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#model-ratio-settings) [Examples of Common Model Ratios](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#examples-of-common-model-ratios) [Setup Methods](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#setup-methods) [Completion Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#completion-ratio-settings) [Default Completion Ratios](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#default-completion-ratios) [Setup Instructions](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#setup-instructions) [Group Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#group-ratio-settings) [Group Ratio Configuration](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#group-ratio-configuration) [Group Ratio Priority](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#group-ratio-priority) [Visual Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#visual-ratio-settings) [Models Without Ratio Settings](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#models-without-ratio-settings) [Upstream Ratio Synchronization](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#upstream-ratio-synchronization) [Frequently Asked Questions](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#frequently-asked-questions) [Q: How do I set ratios for new models?](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#q-how-do-i-set-ratios-for-new-models) [Q: How do group ratios take effect?](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#q-how-do-group-ratios-take-effect) [Q: What is the purpose of the completion ratio?](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#q-what-is-the-purpose-of-the-completion-ratio) [Q: How do I batch set ratios for similar models?](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#q-how-do-i-batch-set-ratios-for-similar-models) [Quota Calculation Examples](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#quota-calculation-examples) [Example 1: GPT-4 Standard User Conversation](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#example-1-gpt-4-standard-user-conversation) [Example 2: GPT-3.5 Internal Test Group Conversation](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#example-2-gpt-35-internal-test-group-conversation) [Example 3: Per-call Billing Model (e.g., Midjourney)](https://docs.newapi.pro/en/docs/guide/console/settings/rate-settings#example-3-per-call-billing-model-eg-midjourney)
