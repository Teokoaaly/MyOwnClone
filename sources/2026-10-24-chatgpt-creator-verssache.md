---
url: https://github.com/verssache/chatgpt-creator
captured: 2026-10-24
word_count: 1049
status: raw
---

[Skip to content](https://github.com/verssache/chatgpt-creator#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/verssache/chatgpt-creator) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/verssache/chatgpt-creator) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/verssache/chatgpt-creator) to refresh your session.Dismiss alert

{{ message }}

main

[**1** Branch](https://github.com/verssache/chatgpt-creator/branches) [**0** Tags](https://github.com/verssache/chatgpt-creator/tags)

[Go to Branches page](https://github.com/verssache/chatgpt-creator/branches)[Go to Tags page](https://github.com/verssache/chatgpt-creator/tags)

Go to file

Code

Open more actions menu

## Latest commit

[![verssache](https://avatars.githubusercontent.com/u/27637948?v=4&size=40)](https://github.com/verssache)[verssache](https://github.com/verssache/chatgpt-creator/commits?author=verssache)

[feat: add sentinel token generation for account creation](https://github.com/verssache/chatgpt-creator/commit/28a4607d98e985fa74d948d5f4dc8155eb314708)

6 months agoApr 6, 2026

[28a4607](https://github.com/verssache/chatgpt-creator/commit/28a4607d98e985fa74d948d5f4dc8155eb314708) · 6 months agoApr 6, 2026

## History

[4 Commits](https://github.com/verssache/chatgpt-creator/commits/main/)

Open commit details

[View commit history for this file.](https://github.com/verssache/chatgpt-creator/commits/main/) 4 Commits

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| [cmd/register](https://github.com/verssache/chatgpt-creator/tree/main/cmd/register "This path skips through empty directories") | [cmd/register](https://github.com/verssache/chatgpt-creator/tree/main/cmd/register "This path skips through empty directories") | [Initial commit: ChatGPT Account Registration Bot](https://github.com/verssache/chatgpt-creator/commit/cd2890fb2106cf25e9f950bfc93e44070b5bb475 "Initial commit: ChatGPT Account Registration Bot") | 7 months agoMar 10, 2026 |
| [internal](https://github.com/verssache/chatgpt-creator/tree/main/internal "internal") | [internal](https://github.com/verssache/chatgpt-creator/tree/main/internal "internal") | [feat: add sentinel token generation for account creation](https://github.com/verssache/chatgpt-creator/commit/28a4607d98e985fa74d948d5f4dc8155eb314708 "feat: add sentinel token generation for account creation") | 6 months agoApr 6, 2026 |
| [.gitignore](https://github.com/verssache/chatgpt-creator/blob/main/.gitignore ".gitignore") | [.gitignore](https://github.com/verssache/chatgpt-creator/blob/main/.gitignore ".gitignore") | [feat: Persist domain blacklist to blacklist.json](https://github.com/verssache/chatgpt-creator/commit/d9c6645ce323a83315ec310d634b102526f5c7d8 "feat: Persist domain blacklist to blacklist.json") | 7 months agoMar 10, 2026 |
| [LICENSE](https://github.com/verssache/chatgpt-creator/blob/main/LICENSE "LICENSE") | [LICENSE](https://github.com/verssache/chatgpt-creator/blob/main/LICENSE "LICENSE") | [Initial commit: ChatGPT Account Registration Bot](https://github.com/verssache/chatgpt-creator/commit/cd2890fb2106cf25e9f950bfc93e44070b5bb475 "Initial commit: ChatGPT Account Registration Bot") | 7 months agoMar 10, 2026 |
| [README.md](https://github.com/verssache/chatgpt-creator/blob/main/README.md "README.md") | [README.md](https://github.com/verssache/chatgpt-creator/blob/main/README.md "README.md") | [Initial commit: ChatGPT Account Registration Bot](https://github.com/verssache/chatgpt-creator/commit/cd2890fb2106cf25e9f950bfc93e44070b5bb475 "Initial commit: ChatGPT Account Registration Bot") | 7 months agoMar 10, 2026 |
| [config.json](https://github.com/verssache/chatgpt-creator/blob/main/config.json "config.json") | [config.json](https://github.com/verssache/chatgpt-creator/blob/main/config.json "config.json") | [Initial commit: ChatGPT Account Registration Bot](https://github.com/verssache/chatgpt-creator/commit/cd2890fb2106cf25e9f950bfc93e44070b5bb475 "Initial commit: ChatGPT Account Registration Bot") | 7 months agoMar 10, 2026 |
| [go.mod](https://github.com/verssache/chatgpt-creator/blob/main/go.mod "go.mod") | [go.mod](https://github.com/verssache/chatgpt-creator/blob/main/go.mod "go.mod") | [Initial commit: ChatGPT Account Registration Bot](https://github.com/verssache/chatgpt-creator/commit/cd2890fb2106cf25e9f950bfc93e44070b5bb475 "Initial commit: ChatGPT Account Registration Bot") | 7 months agoMar 10, 2026 |
| [go.sum](https://github.com/verssache/chatgpt-creator/blob/main/go.sum "go.sum") | [go.sum](https://github.com/verssache/chatgpt-creator/blob/main/go.sum "go.sum") | [Initial commit: ChatGPT Account Registration Bot](https://github.com/verssache/chatgpt-creator/commit/cd2890fb2106cf25e9f950bfc93e44070b5bb475 "Initial commit: ChatGPT Account Registration Bot") | 7 months agoMar 10, 2026 |
| View all files |

## Repository files navigation

# ChatGPT Account Registration Bot

[Permalink: ChatGPT Account Registration Bot](https://github.com/verssache/chatgpt-creator#chatgpt-account-registration-bot)

Automated bulk ChatGPT account registration bot built with Go. Features concurrent workers, TLS fingerprint spoofing, automatic email generation, OTP verification, and retry-until-success logic.

## Features

[Permalink: Features](https://github.com/verssache/chatgpt-creator#features)

- **Concurrent Registration** — Configurable worker pool for parallel account creation
- **TLS Fingerprinting** — Randomized Chrome TLS profiles to avoid detection
- **Auto Email Generation** — Generates temporary emails via [generator.email](https://generator.email/) or custom domains
- **OTP Verification** — Automatic email OTP retrieval and validation
- **Retry Loop** — Automatically retries failed registrations until target count is reached
- **Proxy Support** — Optional HTTP/SOCKS proxy for all requests
- **Configurable** — JSON config file with interactive prompt overrides

## Requirements

[Permalink: Requirements](https://github.com/verssache/chatgpt-creator#requirements)

- Go 1.21+

## Installation

[Permalink: Installation](https://github.com/verssache/chatgpt-creator#installation)

```
git clone https://github.com/verssache/chatgpt-creator.git
cd chatgpt-creator
go mod download
```

## Usage

[Permalink: Usage](https://github.com/verssache/chatgpt-creator#usage)

```
go run cmd/register/main.go
```

### Interactive Prompts

[Permalink: Interactive Prompts](https://github.com/verssache/chatgpt-creator#interactive-prompts)

```
Proxy (enter to skip):
Total accounts to register: 5
Max concurrent workers (default: 3): 2
Default password (current: (random), press Enter to use, or enter new):
Default domain (current: (random from generator.email), press Enter to use, or enter new):
```

### Example Output

[Permalink: Example Output](https://github.com/verssache/chatgpt-creator#example-output)

```
[22:43:08] [W1] [1/5] Starting registration flow...
[22:43:09] [W1] [1/5] Visit Homepage (Try 1) | 200
[22:43:09] [W1] [1/5] Get CSRF | 200
[22:43:10] [W1] [1/5] Signin | 200
[22:43:12] [W1] [1/5] Authorize | 200
[22:43:15] [W1] [1/5] Register | 200
[22:43:17] [W1] [1/5] Send OTP | 200
[22:43:19] [W1] [1/5] Validate OTP [483291] | 200
[22:43:24] [W1] [1/5] Create Account | 200
[22:43:33] [W1] [1/5] Callback | 200
[22:43:33] [W1] SUCCESS: johndoe8x2kq@smartmail.de

--- Batch Registration Summary ---
Target:    5
Success:   5
Attempts:  6
Failures:  1
Elapsed:   1m 45s
----------------------------------
```

## Configuration

[Permalink: Configuration](https://github.com/verssache/chatgpt-creator#configuration)

Create a `config.json` in the project root (optional):

```
{
  "proxy": "",
  "output_file": "results.txt",
  "default_password": "",
  "default_domain": ""
}
```

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `proxy` | string | `""` | HTTP/SOCKS proxy URL. Leave empty for direct connection |
| `output_file` | string | `results.txt` | File path for saving registered accounts |
| `default_password` | string | `""` | Password for all accounts. Must be 12+ chars. Empty = random |
| `default_domain` | string | `""` | Email domain to use. Empty = random from generator.email |

Environment variable `PROXY` overrides the config file proxy value.

## Output Format

[Permalink: Output Format](https://github.com/verssache/chatgpt-creator#output-format)

Registered accounts are saved to the output file in the format:

```
email|password
```

## Project Structure

[Permalink: Project Structure](https://github.com/verssache/chatgpt-creator#project-structure)

```
.
├── cmd/
│   └── register/
│       └── main.go          # Entry point, interactive prompts
├── internal/
│   ├── config/
│   │   └── config.go        # Configuration loading & validation
│   ├── register/
│   │   ├── batch.go         # Batch orchestration, worker pool, retry logic
│   │   ├── client.go        # HTTP client with TLS fingerprinting
│   │   └── flow.go          # Registration flow (CSRF → signup → OTP → callback)
│   ├── email/
│   │   └── generator.go     # Temporary email generation
│   ├── chrome/
│   │   └── profiles.go      # Chrome TLS profile randomization
│   └── util/
│       ├── helpers.go       # Utility functions
│       ├── names.go         # Random name generation (gofakeit)
│       ├── password.go      # Random password generation
│       └── trace.go         # Datadog trace headers
├── config.json               # Configuration file
├── go.mod
└── go.sum
```

## Disclaimer

[Permalink: Disclaimer](https://github.com/verssache/chatgpt-creator#disclaimer)

This tool is provided for educational and research purposes only. Use of this tool to create accounts in violation of OpenAI's Terms of Service is solely at your own risk. The author assumes no responsibility for any misuse or consequences arising from the use of this software.

## License

[Permalink: License](https://github.com/verssache/chatgpt-creator#license)

This project is licensed under the MIT License. See the [LICENSE](https://github.com/verssache/chatgpt-creator/blob/main/LICENSE) file for details.

## About

A high-performance Go bot for automated bulk ChatGPT account creation, featuring TLS fingerprint spoofing and auto email OTP verification.

### Resources

[Readme](https://github.com/verssache/chatgpt-creator#readme-ov-file)

[MIT license](https://github.com/verssache/chatgpt-creator#MIT-1-ov-file)

[Activity](https://github.com/verssache/chatgpt-creator/activity)

### Stars

**338** stars

### Watchers

**1** watching

### Forks

[**90** forks](https://github.com/verssache/chatgpt-creator/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fverssache%2Fchatgpt-creator&report=verssache+%28user%29)

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.