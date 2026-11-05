---
url: https://docs.newapi.pro/en/docs/guide/wiki/basic-concepts/project-introduction
captured: 2026-10-28
word_count: 1771
status: raw
---

[User Guide](https://docs.newapi.pro/en/docs) [Installation](https://docs.newapi.pro/en/docs/installation) [API Reference](https://docs.newapi.pro/en/docs/api) [AI Applications](https://docs.newapi.pro/en/docs/apps) [Skills](https://docs.newapi.pro/en/docs/skills) [Help & Support](https://docs.newapi.pro/en/docs/support) [Business Cooperation](https://docs.newapi.pro/en/docs/business)

# Channels

Copy MarkdownOpen

Upstream channels must be legally owned or authorized accounts, API Keys, model services, or enterprise contracts of the deployer. Features such as load balancing, automatic failover, weighted random, and multi-key management are used for high availability and enterprise multi-account management. When using them, you should comply with upstream service terms, platform rules, and regulatory requirements.

Here you can manage NewAPI's upstream channels.

![渠道](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Fchannel.06znx2nvskiji.png&w=3840&q=75)

## [Channel Creation/Editing Page](https://docs.newapi.pro/en/docs/guide/console/channel-management\#channel-creationediting-page)

![渠道管理1](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Fcreate-channel-1.1tu1dw--7xfsh.png&w=3840&q=75)

![渠道管理2](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Fcreate-channel-2.1w3jktixhidb7.png&w=3840&q=75)

![渠道管理3](https://docs.newapi.pro/_next/image?url=%2F_next%2Fstatic%2Fimmutable%2Fmedia%2Fcreate-channel-3.01i936edlyje9.png&w=3840&q=75)

# [Parameter Override Settings Documentation](https://docs.newapi.pro/en/docs/guide/console/channel-management\#parameter-override-settings-documentation)

## [Overview](https://docs.newapi.pro/en/docs/guide/console/channel-management\#overview)

The parameter override system supports two modes: simple override mode (backward compatible) and advanced operation mode. Through flexible conditional logic and operation types, complex dynamic parameter adjustments can be achieved. The parameter override feature can only be used for compatibility with legal upstream interface formats, enterprise network compatibility, and request normalization.

## [Usage](https://docs.newapi.pro/en/docs/guide/console/channel-management\#usage)

### [Simple Override Mode](https://docs.newapi.pro/en/docs/guide/console/channel-management\#simple-override-mode)

For backward compatibility, directly specify the fields and values to be overridden. The system will merge these fields into the original request.

```
{
  "temperature": 0.8,
  "max_tokens": 2000,
  "model": "gpt-4"
}
```

### [Advanced Operation Mode](https://docs.newapi.pro/en/docs/guide/console/channel-management\#advanced-operation-mode)

Define complex parameter operations using the `operations` array, supporting advanced features such as conditional logic, array operations, string concatenation, and string normalization.

#### [Basic Structure](https://docs.newapi.pro/en/docs/guide/console/channel-management\#basic-structure)

```
{
  "operations": [\
    {\
      "path": "temperature",\
      "mode": "set",\
      "value": 0.8,\
      "conditions": [...],\
      "logic": "AND"\
    }\
  ]
}
```

**Field Description (fill as needed):**

- `mode`: Required
- `path`: Applicable to `set` / `delete` / `append` / `prepend` / `trim_prefix` / `trim_suffix` / `ensure_prefix` / `ensure_suffix` / `trim_space` / `to_lower` / `to_upper` / `replace` / `regex_replace`
- `value`: Commonly used with `set` / `append` / `prepend` / `trim_prefix` / `trim_suffix` / `ensure_prefix` / `ensure_suffix`
- `from` / `to`: Applicable to `move` / `copy` / `replace` / `regex_replace`
- `keep_origin`: Used for `set` (skips if value already exists) and for `append` / `prepend` during object merging.

## [Operation Modes (mode)](https://docs.newapi.pro/en/docs/guide/console/channel-management\#operation-modes-mode)

### [1\. set - Set Value](https://docs.newapi.pro/en/docs/guide/console/channel-management\#1-set---set-value)

Sets the value at the specified path.

```
{
  "path": "temperature",
  "mode": "set",
  "value": 0.8,
  "keep_origin": false
}
```

**Parameter Description:**

- `keep_origin`: If `true`, setting is skipped if the target path already has a value.

### [2\. delete - Delete Field](https://docs.newapi.pro/en/docs/guide/console/channel-management\#2-delete---delete-field)

Deletes the field at the specified path.

```
{
  "path": "messages.0",
  "mode": "delete"
}
```

### [3\. move - Move Field](https://docs.newapi.pro/en/docs/guide/console/channel-management\#3-move---move-field)

Moves the value of one field to another location.

```
{
  "mode": "move",
  "from": "messages.0.content",
  "to": "system"
}
```

### [4\. append - Append Content](https://docs.newapi.pro/en/docs/guide/console/channel-management\#4-append---append-content)

Appends new content after existing content.

```
{
  "path": "messages.0.content",
  "mode": "append",
  "value": "\n\nPlease answer in Chinese."
}
```

**Supported Data Types:**

- **String**: Appends to the end of the original string.
- **Array**: Adds elements to the end of the array (supports adding single elements or arrays).
- **Object**: Merges object properties.

### [5\. prepend - Prepend Content](https://docs.newapi.pro/en/docs/guide/console/channel-management\#5-prepend---prepend-content)

Adds new content before existing content.

```
{
  "path": "messages.0.content",
  "mode": "prepend",
  "value": "Important Note: Please read the following carefully.\n\n"
}
```

**Supported Data Types:**

- **String**: Prepends to the beginning of the original string.
- **Array**: Adds elements to the beginning of the array (supports adding single elements or arrays).
- **Object**: Merges object properties.

### [6\. copy - Copy Field](https://docs.newapi.pro/en/docs/guide/console/channel-management\#6-copy---copy-field)

Copies the value from the `from` path to the `to` path (does not delete the source field).

```
{
  "mode": "copy",
  "from": "model",
  "to": "original_model"
}
```

**Parameter Requirements:**

- `from` / `to`: Required.
- An error will occur if the source path does not exist.

### [7\. trim\_prefix - Trim Prefix](https://docs.newapi.pro/en/docs/guide/console/channel-management\#7-trim_prefix---trim-prefix)

Removes the specified prefix from a string field (remains unchanged if no match).

```
{
  "path": "model",
  "mode": "trim_prefix",
  "value": "openai/"
}
```

**Parameter Requirements:**

- `value`: Required.

### [8\. trim\_suffix - Trim Suffix](https://docs.newapi.pro/en/docs/guide/console/channel-management\#8-trim_suffix---trim-suffix)

Removes the specified suffix from a string field (remains unchanged if no match).

```
{
  "path": "model",
  "mode": "trim_suffix",
  "value": "-latest"
}
```

**Parameter Requirements:**

- `value`: Required.

### [9\. ensure\_prefix - Ensure Prefix](https://docs.newapi.pro/en/docs/guide/console/channel-management\#9-ensure_prefix---ensure-prefix)

Ensures a string field starts with the specified prefix (remains unchanged if already present).

```
{
  "path": "model",
  "mode": "ensure_prefix",
  "value": "openai/"
}
```

**Parameter Requirements:**

- `value`: Required and cannot be an empty string.

### [10\. ensure\_suffix - Ensure Suffix](https://docs.newapi.pro/en/docs/guide/console/channel-management\#10-ensure_suffix---ensure-suffix)

Ensures a string field ends with the specified suffix (remains unchanged if already present).

```
{
  "path": "model",
  "mode": "ensure_suffix",
  "value": "-latest"
}
```

**Parameter Requirements:**

- `value`: Required and cannot be an empty string.

### [11\. trim\_space - Trim Whitespace](https://docs.newapi.pro/en/docs/guide/console/channel-management\#11-trim_space---trim-whitespace)

Performs `TrimSpace` on a string field (spaces, newlines, tabs, etc., will be removed).

```
{
  "path": "model",
  "mode": "trim_space"
}
```

### [12\. to\_lower - Convert to Lowercase](https://docs.newapi.pro/en/docs/guide/console/channel-management\#12-to_lower---convert-to-lowercase)

Converts a string field to lowercase.

```
{
  "path": "model",
  "mode": "to_lower"
}
```

### [13\. to\_upper - Convert to Uppercase](https://docs.newapi.pro/en/docs/guide/console/channel-management\#13-to_upper---convert-to-uppercase)

Converts a string field to uppercase.

```
{
  "path": "model",
  "mode": "to_upper"
}
```

### [14\. replace - String Replace](https://docs.newapi.pro/en/docs/guide/console/channel-management\#14-replace---string-replace)

Performs substring replacement on a string field.

```
{
  "path": "model",
  "mode": "replace",
  "from": "openai/",
  "to": ""
}
```

**Parameter Requirements:**

- `from`: Required and cannot be an empty string.
- `to`: Optional; omitting it is equivalent to an empty string.

### [15\. regex\_replace - Regex Replace](https://docs.newapi.pro/en/docs/guide/console/channel-management\#15-regex_replace---regex-replace)

Performs regex matching and replacement on a string field.

```
{
  "path": "model",
  "mode": "regex_replace",
  "from": "^gpt-",
  "to": "openai/gpt-"
}
```

**Parameter Requirements:**

- `from`: Required (regular expression, Go regexp syntax).
- `to`: Optional; omitting it is equivalent to an empty string.

## [Conditional Logic](https://docs.newapi.pro/en/docs/guide/console/channel-management\#conditional-logic)

Set conditions for operation execution using the `conditions` array. The corresponding operation will only be executed if the conditions are met.

### [Condition Structure](https://docs.newapi.pro/en/docs/guide/console/channel-management\#condition-structure)

```
{
  "conditions": [\
    {\
      "path": "model",\
      "mode": "contains",\
      "value": "gpt-4",\
      "invert": false,\
      "pass_missing_key": false\
    }\
  ],
  "logic": "AND"
}
```

### [Condition Matching Modes](https://docs.newapi.pro/en/docs/guide/console/channel-management\#condition-matching-modes)

- `full`: Exact match (default)
- `prefix`: Prefix match
- `suffix`: Suffix match
- `contains`: Contains match
- `gt`: Greater than (numeric types only)
- `gte`: Greater than or equal to (numeric types only)
- `lt`: Less than (numeric types only)
- `lte`: Less than or equal to (numeric types only)

Note:

- Numeric comparisons are only for numeric types.
- String operations (prefix, suffix, contains) convert values to strings for comparison.

### [Condition Parameter Description](https://docs.newapi.pro/en/docs/guide/console/channel-management\#condition-parameter-description)

- `invert`: Inverts the condition. `true` means the result is negated.
- `pass_missing_key`: Behavior when the specified path does not exist.
  - `true`: Condition passes if the path is missing.
  - `false`: Condition fails if the path is missing (default).

### [Logical Relationship (logic)](https://docs.newapi.pro/en/docs/guide/console/channel-management\#logical-relationship-logic)

- `AND`: All conditions must be met.
- `OR`: Any condition can be met (default).

## [Path Syntax](https://docs.newapi.pro/en/docs/guide/console/channel-management\#path-syntax)

Use JSON path syntax to access nested fields:

- `temperature` \- Root-level field
- `messages.0.content` \- Content field of the first element in the array
- `messages.-1.content` \- Content field of the last element in the array
- `metadata.user.name` \- Nested object field

Additionally, `path` supports the following built-in variables (which do not need to be explicitly present in the request body) and can be directly used for conditional logic:

| Variable | Meaning | Typical Use Case |
| --- | --- | --- |
| `model` / `upstream_model` | Target model after redirection | Conditional matching based on the actual upstream model called |
| `original_model` | Target model before redirection | Conditional matching based on the original model requested by the user |

## [Practical Examples](https://docs.newapi.pro/en/docs/guide/console/channel-management\#practical-examples)

### [1\. Dynamically Adjust Model Parameters](https://docs.newapi.pro/en/docs/guide/console/channel-management\#1-dynamically-adjust-model-parameters)

Dynamically adjust temperature parameters based on message content:

```
{
  "operations": [\
    {\
      "path": "temperature",\
      "mode": "set",\
      "value": 0.3,\
      "conditions": [\
        {\
          "path": "messages.0.content",\
          "mode": "contains",\
          "value": "代码"\
        }\
      ]\
    },\
    {\
      "path": "temperature",\
      "mode": "set",\
      "value": 0.9,\
      "conditions": [\
        {\
          "path": "messages.0.content",\
          "mode": "contains",\
          "value": "创意"\
        }\
      ]\
    }\
  ]
}
```

### [2\. Add System Prompt](https://docs.newapi.pro/en/docs/guide/console/channel-management\#2-add-system-prompt)

Add a system message at the beginning of the message array:

```
{
  "operations": [\
    {\
      "path": "messages",\
      "mode": "prepend",\
      "value": [\
        {\
          "role": "system",\
          "content": "You are a professional AI assistant, please always be polite and professional."\
        }\
      ]\
    }\
  ]
}
```

### [3\. Adjust Parameters Based on Model Type](https://docs.newapi.pro/en/docs/guide/console/channel-management\#3-adjust-parameters-based-on-model-type)

Set different max\_tokens for different models:

```
{
  "operations": [\
    {\
      "path": "max_tokens",\
      "mode": "set",\
      "value": 4000,\
      "conditions": [\
        {\
          "path": "model",\
          "mode": "prefix",\
          "value": "gpt-4"\
        }\
      ]\
    },\
    {\
      "path": "max_tokens",\
      "mode": "set",\
      "value": 2000,\
      "conditions": [\
        {\
          "path": "model",\
          "mode": "prefix",\
          "value": "gpt-3.5"\
        }\
      ]\
    }\
  ]
}
```

### [4\. Multiple Condition Combination (AND Logic)](https://docs.newapi.pro/en/docs/guide/console/channel-management\#4-multiple-condition-combination-and-logic)

Execute operations only when multiple conditions are met simultaneously:

```
{
  "operations": [\
    {\
      "path": "stream",\
      "mode": "set",\
      "value": false,\
      "conditions": [\
        {\
          "path": "model",\
          "mode": "contains",\
          "value": "claude"\
        },\
        {\
          "path": "messages.0.content",\
          "mode": "contains",\
          "value": "长文"\
        }\
      ],\
      "logic": "AND"\
    }\
  ]
}
```

### [5\. Numeric Comparison Conditions](https://docs.newapi.pro/en/docs/guide/console/channel-management\#5-numeric-comparison-conditions)

Perform conditional logic based on numeric values:

```
{
  "operations": [\
    {\
      "path": "temperature",\
      "mode": "set",\
      "value": 0.1,\
      "conditions": [\
        {\
          "path": "max_tokens",\
          "mode": "gt",\
          "value": 1000\
        }\
      ]\
    }\
  ]
}
```

### [6\. Invert Condition](https://docs.newapi.pro/en/docs/guide/console/channel-management\#6-invert-condition)

Use `invert` to implement inverse logic:

```
{
  "operations": [\
    {\
      "path": "stream",\
      "mode": "set",\
      "value": true,\
      "conditions": [\
        {\
          "path": "model",\
          "mode": "contains",\
          "value": "gpt-3.5",\
          "invert": true\
        }\
      ]\
    }\
  ]
}
```

### [7\. Handle Missing Fields](https://docs.newapi.pro/en/docs/guide/console/channel-management\#7-handle-missing-fields)

Use `pass_missing_key` to handle potentially missing fields:

```
{
  "operations": [\
    {\
      "path": "temperature",\
      "mode": "set",\
      "value": 0.7,\
      "conditions": [\
        {\
          "path": "custom_field",\
          "mode": "full",\
          "value": "special",\
          "pass_missing_key": true\
        }\
      ]\
    }\
  ]
}
```

### [8\. String Concatenation Example](https://docs.newapi.pro/en/docs/guide/console/channel-management\#8-string-concatenation-example)

Append instructions after the user's message:

```
{
  "operations": [\
    {\
      "path": "messages.-1.content",\
      "mode": "append",\
      "value": "\n\nPlease explain your thought process in detail."\
    }\
  ]
}
```

## [Important Notes](https://docs.newapi.pro/en/docs/guide/console/channel-management\#important-notes)

**Execution Order**: Operations are executed sequentially according to their order in the `operations` array; earlier operations may affect subsequent ones.

How is this guide?

GoodBad

Last updated on 9/11/2026

### On this page

[Channel Creation/Editing Page](https://docs.newapi.pro/en/docs/guide/console/channel-management#channel-creationediting-page) [Parameter Override Settings Documentation](https://docs.newapi.pro/en/docs/guide/console/channel-management#parameter-override-settings-documentation) [Overview](https://docs.newapi.pro/en/docs/guide/console/channel-management#overview) [Usage](https://docs.newapi.pro/en/docs/guide/console/channel-management#usage) [Simple Override Mode](https://docs.newapi.pro/en/docs/guide/console/channel-management#simple-override-mode) [Advanced Operation Mode](https://docs.newapi.pro/en/docs/guide/console/channel-management#advanced-operation-mode) [Basic Structure](https://docs.newapi.pro/en/docs/guide/console/channel-management#basic-structure) [Operation Modes (mode)](https://docs.newapi.pro/en/docs/guide/console/channel-management#operation-modes-mode) [1\. set - Set Value](https://docs.newapi.pro/en/docs/guide/console/channel-management#1-set---set-value) [2\. delete - Delete Field](https://docs.newapi.pro/en/docs/guide/console/channel-management#2-delete---delete-field) [3\. move - Move Field](https://docs.newapi.pro/en/docs/guide/console/channel-management#3-move---move-field) [4\. append - Append Content](https://docs.newapi.pro/en/docs/guide/console/channel-management#4-append---append-content) [5\. prepend - Prepend Content](https://docs.newapi.pro/en/docs/guide/console/channel-management#5-prepend---prepend-content) [6\. copy - Copy Field](https://docs.newapi.pro/en/docs/guide/console/channel-management#6-copy---copy-field) [7\. trim\_prefix - Trim Prefix](https://docs.newapi.pro/en/docs/guide/console/channel-management#7-trim_prefix---trim-prefix) [8\. trim\_suffix - Trim Suffix](https://docs.newapi.pro/en/docs/guide/console/channel-management#8-trim_suffix---trim-suffix) [9\. ensure\_prefix - Ensure Prefix](https://docs.newapi.pro/en/docs/guide/console/channel-management#9-ensure_prefix---ensure-prefix) [10\. ensure\_suffix - Ensure Suffix](https://docs.newapi.pro/en/docs/guide/console/channel-management#10-ensure_suffix---ensure-suffix) [11\. trim\_space - Trim Whitespace](https://docs.newapi.pro/en/docs/guide/console/channel-management#11-trim_space---trim-whitespace) [12\. to\_lower - Convert to Lowercase](https://docs.newapi.pro/en/docs/guide/console/channel-management#12-to_lower---convert-to-lowercase) [13\. to\_upper - Convert to Uppercase](https://docs.newapi.pro/en/docs/guide/console/channel-management#13-to_upper---convert-to-uppercase) [14\. replace - String Replace](https://docs.newapi.pro/en/docs/guide/console/channel-management#14-replace---string-replace) [15\. regex\_replace - Regex Replace](https://docs.newapi.pro/en/docs/guide/console/channel-management#15-regex_replace---regex-replace) [Conditional Logic](https://docs.newapi.pro/en/docs/guide/console/channel-management#conditional-logic) [Condition Structure](https://docs.newapi.pro/en/docs/guide/console/channel-management#condition-structure) [Condition Matching Modes](https://docs.newapi.pro/en/docs/guide/console/channel-management#condition-matching-modes) [Condition Parameter Description](https://docs.newapi.pro/en/docs/guide/console/channel-management#condition-parameter-description) [Logical Relationship (logic)](https://docs.newapi.pro/en/docs/guide/console/channel-management#logical-relationship-logic) [Path Syntax](https://docs.newapi.pro/en/docs/guide/console/channel-management#path-syntax) [Practical Examples](https://docs.newapi.pro/en/docs/guide/console/channel-management#practical-examples) [1\. Dynamically Adjust Model Parameters](https://docs.newapi.pro/en/docs/guide/console/channel-management#1-dynamically-adjust-model-parameters) [2\. Add System Prompt](https://docs.newapi.pro/en/docs/guide/console/channel-management#2-add-system-prompt) [3\. Adjust Parameters Based on Model Type](https://docs.newapi.pro/en/docs/guide/console/channel-management#3-adjust-parameters-based-on-model-type) [4\. Multiple Condition Combination (AND Logic)](https://docs.newapi.pro/en/docs/guide/console/channel-management#4-multiple-condition-combination-and-logic) [5\. Numeric Comparison Conditions](https://docs.newapi.pro/en/docs/guide/console/channel-management#5-numeric-comparison-conditions) [6\. Invert Condition](https://docs.newapi.pro/en/docs/guide/console/channel-management#6-invert-condition) [7\. Handle Missing Fields](https://docs.newapi.pro/en/docs/guide/console/channel-management#7-handle-missing-fields) [8\. String Concatenation Example](https://docs.newapi.pro/en/docs/guide/console/channel-management#8-string-concatenation-example) [Important Notes](https://docs.newapi.pro/en/docs/guide/console/channel-management#important-notes)
