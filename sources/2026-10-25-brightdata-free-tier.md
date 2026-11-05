---
url: https://docs.brightdata.com/general/account/billing-and-pricing/free-tier
captured: 2026-10-25
word_count: 1412
status: raw
---

> ## Documentation Index
>
> Fetch the complete documentation index at: [/llms.txt](https://docs.brightdata.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier#content-area)

Every new Bright Data account gets **5,000 free credits per month** (~$7.50 value), usable across the Web Unlocker API, SERP API, Web Scraper API, Scraper Studio and Browser API. No credit card, no promo code, no commitment.**The Browser API is also included in the monthly free credits.** The Browser API consumes 5 credits per MB of traffic, so a full 5,000-credit allowance gives you nearly 1 GB of free Browser API traffic every month.

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#what-is-the-bright-data-free-tier)  What is the Bright Data free tier?

The free tier is a recurring monthly credit allowance that applies automatically to every new account. Credits renew on the first of each month and draw from a single shared pool, so you can spend them on any combination of the eligible products. The Web Unlocker API, SERP API and Web Scraper API cost one credit per request or record. Scraper Studio draws from the same pool and costs one credit per page load. The Browser API draws from the same pool at 5 credits per MB of traffic.Bright Data operates on a **pre-paid wallet model**: you are only ever charged for funds you have explicitly deposited. A free tier account has a hard stop when credits are exhausted, never a surprise bill.

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#what-can-i-use-the-free-credits-on)  What can I use the free credits on?

| Product | What it does |
| --- | --- |
| **Web Unlocker API** | Retrieve any web page, bypassing anti-bot protections automatically. |
| **SERP API** | Extract structured search results from Google, Bing and more. |
| **Web Scraper API** | Get structured data from popular websites using pre-built, maintained scrapers. |
| **Scraper Studio** | Build and run custom scrapers in a cloud IDE or with an AI agent. One credit per page load, not per record. |
| **[Browser API](https://docs.brightdata.com/products/scraping-browser/introduction)** | Run Puppeteer, Playwright or Selenium scripts on Bright Data’s cloud browsers with unblocking built in. Included at 5 credits per MB of traffic. |

Proxy products (Datacenter, ISP and Residential proxies) are **not** included in the monthly free credits. New accounts receive a separate one-time **$2 trial credit** (valid 7 days) to test the proxy products, plus an additional **$5 bonus** upon adding a payment method (valid 30 days).

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#how-are-free-credits-consumed)  How are free credits consumed?

Free credits are drawn from a **single shared pool of 5,000 credits per account**. The Web Unlocker API, SERP API and Web Scraper API consume one credit per request or record. Scraper Studio draws from the same pool and consumes one credit per page load, so its consumption depends on how many pages each scraper loads. The Browser API consumes 5 credits per MB of traffic, so its consumption depends on how much data each browser session transfers. Usage is metered and deducted from the same pool, regardless of which product made the call.The Control Panel shows in real time whether you are drawing from free credits or your deposited balance.

Bright Data MCP server requests also draw from this pool. The MCP free tier of 5,000 requests per month is the same shared allowance, because the MCP server runs on the Web Unlocker API.

Unused free credits do not roll over to the next month. Credits reset to 5,000 on the first of each month.

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#what-happens-when-free-credits-run-out)  What happens when free credits run out?

There are two outcomes, depending on whether you have deposited funds:

- **With funds in your account:** usage transitions automatically to your pre-paid balance at your plan’s PAYG rates. There is no interruption in service.
- **Without funds:** requests return an error and you are prompted to add funds to continue.

In both cases, your 5,000 free credits renew on the first of the following month.

Accounts operating on the free tier (unfunded) are restricted to a default rate limit of 1,000 requests per minute across the SERP API, Web Unlocker API and Proxy products. You can view this limit in the Control Panel, under the zone’s Overview tab > Access details. This rate limit is automatically removed once you add funds to your account.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#how-do-i-keep-service-running-after-free-credits)  How do I keep service running after free credits?

Enable **auto-recharge** in your billing settings to ensure uninterrupted service. Auto-recharge triggers when your available balance drops below 85 percent of your configured amount and tops it back up automatically. You can set any denomination. Configure it in [Billing Settings](https://brightdata.com/cp/billing/settings).

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#who-is-eligible-for-the-free-tier)  Who is eligible for the free tier?

The free tier is available to **all new accounts** and is applied automatically at signup.The following account types are **not** eligible:

- Accounts on custom PAYG pricing plans
- Accounts on pre-commit (subscription) plans

If you upgrade to a pre-commit plan, recurring monthly free credits will no longer be issued. Any remaining unused free credits at the time of upgrade remain available to use.

Adding a credit card is a verification step only. You will not be charged unless your free credits are exhausted and you have funds deposited in your account.

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#how-do-i-monitor-my-free-credit-usage)  How do I monitor my free credit usage?

Track your free credit balance and consumption directly in the Control Panel:

1. Go to [Billing Overview](https://brightdata.com/cp/billing/overview).
2. The **Free Tier Credits** section displays your remaining credits and next renewal date.
3. To set up balance threshold alerts, go to [Billing Settings](https://brightdata.com/cp/billing/settings).

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#how-do-i-get-support-on-a-free-tier-account)  How do I get support on a free tier account?

Free tier accounts can open a ticket with Bright Data Support or get help from **Sophie**, Bright Data’s AI assistant. Both are available in the Control Panel.

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#faq)  FAQ

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#how-many-requests-do-5000-free-credits-cover)  How many requests do 5,000 free credits cover?

One credit equals one request for the Web Unlocker API and SERP API, and one delivered record for the Web Scraper API, so your 5,000 monthly free credits cover up to 5,000 requests or records in any combination across these three products. Scraper Studio also draws from the pool and consumes one credit per page load, so its credit consumption depends on how many pages each scraper loads rather than a per-record rate. The Browser API consumes 5 credits per MB, so a full 5,000-credit allowance covers 1,000 MB, nearly 1 GB, of Browser API traffic.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#do-free-credits-roll-over)  Do free credits roll over?

No. Credits reset to 5,000 on the first of each month. Unused credits are forfeited.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#will-i-be-charged-automatically-when-credits-run-out)  Will I be charged automatically when credits run out?

No. If you have no deposited funds, a hard stop is applied and no charges will occur. If you have pre-deposited funds, usage continues against your balance at standard PAYG rates. Enable [auto-recharge](https://brightdata.com/cp/billing/settings) to replenish your balance automatically.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#can-i-use-the-free-tier-for-the-browser-api)  Can I use the free tier for the Browser API?

Yes. The Browser API draws from the same shared pool of 5,000 monthly free credits at 5 credits per MB of traffic. Spend the whole allowance on the Browser API and it gives you nearly 1 GB of free traffic every month.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#can-i-use-the-free-tier-for-proxies)  Can I use the free tier for proxies?

No. Datacenter, ISP and Residential proxies are not covered by the monthly free credits. A separate one-time $2 trial credit is available for the proxy products upon signup, with an additional $5 bonus when you add a payment method.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#can-i-use-the-free-tier-for-scraper-studio)  Can I use the free tier for Scraper Studio?

Yes. Scraper Studio is covered by the monthly free credits and draws from the same shared pool of 5,000 credits. In the free tier, Scraper Studio consumes one credit per page load, so credit consumption depends on how many pages your scrapers load rather than a per-record rate.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#what-happens-to-unused-credits-if-i-upgrade-to-a-pre-commit-plan)  What happens to unused credits if I upgrade to a pre-commit plan?

Recurring monthly free credits stop upon upgrading. Any remaining unused credits at the time of upgrade can still be consumed.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#can-i-combine-free-credits-with-a-promo-code)  Can I combine free credits with a promo code?

Yes. Free credits are consumed first. Promo code discounts apply to any PAYG usage that follows.

### [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#how-do-i-start-using-payg-after-the-free-tier)  How do I start using PAYG after the free tier?

Add funds to your account from the [Billing page](https://brightdata.com/cp/billing). There is no minimum commitment. You stay on PAYG and only pay for what you use.

## [​](https://docs.brightdata.com/general/account/billing-and-pricing/free-tier\#related-pages)  Related pages

- [Accepted payment methods](https://docs.brightdata.com/general/account/billing-and-pricing/payment-methods)
- [Billing](https://docs.brightdata.com/general/account/billing-and-pricing/billing)
- [Bright Data promo codes](https://docs.brightdata.com/general/account/billing-and-pricing/promo-codes)

Was this page helpful?

YesNo
