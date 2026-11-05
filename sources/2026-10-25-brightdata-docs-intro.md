---
url: https://brightdata.com/faq
captured: 2026-10-25
word_count: 545
status: raw
---

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.brightdata.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.brightdata.com/introduction#content-area)

# [​](https://docs.brightdata.com/introduction\#start-building-with-live-web-data)  Start building with live web data

Scrape any site, buy ready-made datasets. Thousands of pre-built scrapers, one API key.

Read [https://docs.brightdata.com/llms.txt](https://docs.brightdata.com/llms.txt) and get me set up with Bright Data

CopiedCopy prompt

**5,000 free credits per month**, no credit card required. See the [free tier](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier).

[![Quickstart](https://mintcdn.com/brightdata/2ePdI98bOlsJ7Z5O/images/home/tile-quickstart.svg?fit=max&auto=format&n=2ePdI98bOlsJ7Z5O&q=85&s=2451064a3e45eb39e3f6326fd9b608d0)\\
\\
Quickstart\\
\\
Scrape your first page and get structured JSON in three steps.](https://docs.brightdata.com/quickstart) [![Agent resources](https://mintcdn.com/brightdata/2ePdI98bOlsJ7Z5O/images/home/tile-agent.svg?fit=max&auto=format&n=2ePdI98bOlsJ7Z5O&q=85&s=9701bf3e9271cbd608de4cdb517301cc)\\
\\
You're an agent? Start here\\
\\
llms.txt, skills and MCP tools for AI readers.](https://docs.brightdata.com/quickstart-coding-agent) [![Product catalog](https://mintcdn.com/brightdata/2ePdI98bOlsJ7Z5O/images/home/tile-products.svg?fit=max&auto=format&n=2ePdI98bOlsJ7Z5O&q=85&s=c490bb3e08ee263220579be041b5b646)\\
\\
All products\\
\\
Data extraction, web search, AI training data and proxy networks.](https://docs.brightdata.com/products) [![API reference](https://mintcdn.com/brightdata/2ePdI98bOlsJ7Z5O/images/home/tile-api.svg?fit=max&auto=format&n=2ePdI98bOlsJ7Z5O&q=85&s=ffab48d43166442a9d844d129ffd7005)\\
\\
API reference\\
\\
Authentication, endpoints, SDKs and the CLI.](https://docs.brightdata.com/api-reference/authentication)

## [​](https://docs.brightdata.com/introduction\#browse-by-product)  Browse by product

### [​](https://docs.brightdata.com/introduction\#data-extraction)  Data extraction

Extract structured data, unblock pages and collect search results.

[Scraper APIStructured data from thousands of sites](https://docs.brightdata.com/products/scrapers/overview) [Scraper StudioBuild and host custom scrapers](https://docs.brightdata.com/products/scraper-studio/overview) [Dataset MarketplaceReady-made datasets, 250+ domains](https://docs.brightdata.com/left-over/marketplace-overview) [Web Unlocker APIUnblock any protected page](https://docs.brightdata.com/products/web-unlocker/introduction) [Browser APIRemote browsers for automation](https://docs.brightdata.com/products/scraping-browser/introduction) [SERP APISearch results as structured JSON](https://docs.brightdata.com/products/serp-api/introduction) [Managed servicesDone-for-you data collection](https://brightdata.com/pricing/managed-services)

### [​](https://docs.brightdata.com/introduction\#web-search)  Web search

Search records and the live web by API.

[Business SearchFind people and companies by criteria](https://docs.brightdata.com/products/business-search/introduction)

### [​](https://docs.brightdata.com/introduction\#ai-training-data)  AI training data

Media and archived pages for model training.

[Media Data APIVideo, audio and captions at scale](https://docs.brightdata.com/datasets/media-data-api) [Web ArchiveCached web page snapshots](https://docs.brightdata.com/products/archive/overview)

### [​](https://docs.brightdata.com/introduction\#proxy-networks)  Proxy networks

Five network types for routing traffic at scale.

[Residential proxies400M+ real-user IPs](https://docs.brightdata.com/products/residential/introduction) [Datacenter proxiesFast, low-cost IPs](https://docs.brightdata.com/products/data-center/introduction) [ISP proxiesStatic residential-grade IPs](https://docs.brightdata.com/products/isp/introduction) [Proxy ManagerOpen-source proxy routing](https://docs.brightdata.com/products/proxy-manager/introduction) [Browser ExtensionProxies in Chrome](https://docs.brightdata.com/left-over/browser-extension/introduction)

### [​](https://docs.brightdata.com/introduction\#ai-tools)  AI tools

Tools that connect agents to the live web.

[Bright Data MCPLive web access for agents](https://docs.brightdata.com/products/mcp-server/overview) [SDKsPython and JavaScript clients](https://docs.brightdata.com/api-reference/SDK) [Bright Data CLIThe platform from your terminal](https://docs.brightdata.com/products/cli/overview)

## [​](https://docs.brightdata.com/introduction\#set-up-your-ai-tools)  Set up your AI tools

Connect Bright Data to the tool you already use. Each command is the same one documented in its [MCP integration guide](https://docs.brightdata.com/products/mcp-server/integrations/overview).

Claude Code

Cursor

Codex CLI

Bright Data CLI

```
claude mcp add --transport sse brightdata "https://mcp.brightdata.com/sse?token=YOUR_API_KEY"
```

```
{
  "mcpServers": {
    "brightdata-mcp": {
      "command": "npx",
      "args": ["-y", "@brightdata/mcp"],
      "env": {
        "API_TOKEN": "<your API token>"
      }
    }
  }
}
```

```
codex mcp add brightdata --env API_TOKEN=YOUR_API_KEY -- npx -y @brightdata/mcp
```

```
npx -p @brightdata/cli brightdata --version
```

## [​](https://docs.brightdata.com/introduction\#send-your-first-request)  Send your first request

Each example scrapes a LinkedIn profile with the Scraper API and works as-is after you replace `YOUR_API_KEY` with a key from your [account settings](https://brightdata.com/cp/setting/users). See [authentication](https://docs.brightdata.com/api-reference/authentication) for how API keys work across all products.

cURL

Python

Node.js

```
curl -X POST \
  "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_l1viktl72bvl7bjuj0&format=json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '[{"url": "https://www.linkedin.com/in/satyanadella"}]'
```

```
import requests

response = requests.post(
    "https://api.brightdata.com/datasets/v3/scrape",
    params={"dataset_id": "gd_l1viktl72bvl7bjuj0", "format": "json"},
    headers={
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    },
    json=[{"url": "https://www.linkedin.com/in/satyanadella"}],
)

print(response.json())
```

```
const response = await fetch(
  "https://api.brightdata.com/datasets/v3/scrape?dataset_id=gd_l1viktl72bvl7bjuj0&format=json",
  {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json",
    },
    body: JSON.stringify([\
      { url: "https://www.linkedin.com/in/satyanadella" }\
    ]),
  }
);

const data = await response.json();
console.log(data);
```

The same request pattern works for every scraper: swap the dataset ID and input URL. See the [Instagram](https://docs.brightdata.com/products/scrapers/instagram/quickstart) and [SERP API](https://docs.brightdata.com/products/serp-api/quickstart) quickstarts for the next targets.

[Service status](https://brightdata.com/network-status) [Contact support](https://brightdata.zendesk.com/hc/en-us/requests/new) [Release notes](https://docs.brightdata.com/release-notes) [llms.txt for agents](https://docs.brightdata.com/llms.txt)

Was this page helpful?

YesNo
