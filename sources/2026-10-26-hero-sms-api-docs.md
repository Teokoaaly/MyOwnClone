---
url: https://hero-sms.com/en/api
captured: 2026-10-26
word_count: 424
status: raw
---

v1.0

OpenAPI 3.2.0

# API protocol for working with HEROSMS

Download OpenAPI Document
json
Download OpenAPI Document
yaml

Do you use software for registrations? HeroSMS is compatible with former SMS-Activate partners

1. Choose any software that includes SMS-Activate among its SMS reception services.
2. Select SMS-Activate as the service for receiving SMS.
3. Replace the host from [https://api.sms-activate.ae](https://api.sms-activate.ae/) to [https://hero-sms.com](https://hero-sms.com/) in your software settings.
4. Enter the API key from your HeroSMS account (request it on our website).

If you face any difficulties, contact our tech support, please. We will deal with everything.

Server

Server:https://hero-sms.com/api/v1

HeroSMS API server

## Authentication

Select Auth Type

No authentication selected

Client Libraries

Shell

Ruby

Node.js

PHP

Python

MoreSelect from all clients

Shell Curl

## Activations

​Copy link

List of active activations, purchase, and current offers

Activations Operations

- get/activations/history
- get/activations
- post/activations
- delete/activations/{activationId}
- post/activations/{activationId}/finish
- post/activations/{activationId}/replace
- post/activations/{activationId}/reactivate
- get/activations/{activationId}/reactivate/options
- post/activations/{activationId}/prolong
- get/activations/{activationId}/prolong/options
- get/activations/{activationId}/prolong/history
- get/activations/stats
- get/activations/offers/{verificationType}

Show sidebar

GET

Server: https://hero-sms.com/api/v1

/activations/history

Copy URL

Send Send get request to https://hero-sms.com/api/v1/activations/history

GET

Copy URLSend Send get request to https://hero-sms.com/api/v1/activations/history

Close Client

Activation history

AllAuthCookiesHeadersQuery

All

## AuthenticationRequired

Selected Auth Type: apiKeyAuth

|     |
| --- |
| Format: ApiKey {your\_token} |
| Name : <br>Authorization<br>Clear Value |
| Value : <br>Clear ValueShow Password |

## Variables

| Enabled | Key | Value |
| --- | --- | --- |

## Cookies

| Enabled | Key | Value |
| --- | --- | --- |
|  |  |  |

## Headers

| Enabled | Key | Value |
| --- | --- | --- |
|  | accept | application/json |
|  |  |  |

## Query Parameters

Clear All Query Parameters

| Enabled | Key | Value |
| --- | --- | --- |
|  | from<br>Required | 2025-10-10T00:00:00Z |
|  | to<br>Required | 2025-10-20T00:00:00Z |
|  | services\[\] |  |
|  | countries\[\] |  |
|  | statuses\[\] | Select a value |
|  | size |  |
|  | page |  |
|  | sort\[id\] |  |
|  | search |  |
|  |  |  |

## Request Body

No Body

| None |
| --- |

## Code Snippet (Collapsed)

Shell Curl

Response

AllCookiesHeadersBody

All

[Powered By Scalar.com](https://www.scalar.com/)

.,,uod8B8bou,,. ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:. \|\|\|\|\|\|\|\|\|\|\|\|\|\|!?TFPRBBBBBBBBBBBBBBB8m=, \|\|\|\| '""^^!!\|\|\|\|\|\|\|\|\|\|TFPRBBBVT!:...! \|\|\|\| '""^^!!\|\|\|\|\|?!:.......! \|\|\|\| \|\|\|\|.........! \|\|\|\| \|\|\|\|.........! \|\|\|\| \|\|\|\|.........! \|\|\|\| \|\|\|\|.........! \|\|\|\| \|\|\|\|.........! \|\|\|\| \|\|\|\|.........! \|\|\|\|, \|\|\|\|.........\` \|\|\|\|\|!!-.\_ \|\|\|\|.......;. ':!\|\|\|\|\|\|\|\|\|!!-.\_ \|\|\|\|.....bBBBBWdou,. bBBBBB86foi!\|\|\|\|\|\|\|!!-..:\|\|\|!..bBBBBBBBBBBBBBBY! ::!?TFPRBBBBBB86foi!\|\|\|\|\|\|\|\|!!bBBBBBBBBBBBBBBY..! :::::::::!?TFPRBBBBBB86ftiaabBBBBBBBBBBBBBBY....! :::;\`"^!:;::::::!?TFPRBBBBBBBBBBBBBBBBBBBY......! ;::::::...''^::::::::::!?TFPRBBBBBBBBBBY........! .ob86foi;::::::::::::::::::::::::!?TFPRBY..........\` .b888888888886foi;:::::::::::::::::::::::..........\` .b888888888888888888886foi;::::::::::::::::...........b888888888888888888888888888886foi;:::::::::......\`!Tf998888888888888888888888888888888886foi;:::....\` '"^!\|Tf9988888888888888888888888888888888!::..\` '"^!\|Tf998888888888888888888888889!! '\` '"^!\|Tf9988888888888888888!!\` iBBbo. '"^!\|Tf998888888889!\` WBBBBbo. '"^!\|Tf9989!\` YBBBP^' '"^!\` \`

Send Request

ctrlControl

↵Enter