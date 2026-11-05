---
url: https://devcenter.heroku.com/articles/dyno-sizes
captured: 2026-10-25
word_count: 974
status: raw
---

# Technical Specifications by Dyno Size

## Table of Contents \[expand\]

- [Dynos in Cedar](https://devcenter.heroku.com/articles/dyno-sizes#dynos-in-cedar)
- [Dynos in Fir](https://devcenter.heroku.com/articles/dyno-sizes#dynos-in-fir)
- [Dyno Limits](https://devcenter.heroku.com/articles/dyno-sizes#dyno-limits)
- [Pricing and Billing](https://devcenter.heroku.com/articles/dyno-sizes#pricing-and-billing)
- [Additional Reading](https://devcenter.heroku.com/articles/dyno-sizes#additional-reading)

Last updated July 24, 2025

This article covers the technical specifications of each dyno size. To see the features for different dyno tiers, see [Dyno Tiers](https://devcenter.heroku.com/articles/dyno-tiers).

To change the dyno size on your app, see [Scaling Your Dyno Formation](https://devcenter.heroku.com/articles/scaling).

## [Dynos in Cedar](https://devcenter.heroku.com/articles/dyno-sizes\#dynos-in-cedar)

We limit access to Performance dynos to customers with an established payment history.
Private and Shield dynos are only available with [Cedar](https://devcenter.heroku.com/articles/generations#cedar)-generation [Private Spaces](https://devcenter.heroku.com/articles/private-spaces) and [Shield Spaces](https://devcenter.heroku.com/articles/shield-private-space).

The following dynos are available for [Cedar](https://devcenter.heroku.com/articles/generations#cedar)-generation apps, depending on the runtime.

### [Common Runtime](https://devcenter.heroku.com/articles/dyno-sizes\#common-runtime)

| Plan | Memory (RAM) | CPU Share | Compute | $/Month | Dyno Units Consumed | Dedicated | [Sleeps](https://devcenter.heroku.com/articles/eco-dyno-hours#dyno-sleeping) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Eco | 0.5 GB | 1x | 1x-4x | [$5 flat\*](https://devcenter.heroku.com/articles/eco-dyno-hours) | N/A | No | ✔ |
| Basic | 0.5 GB | 1x | 1x-4x | $7 | 0.28 | No |  |
| Standard-1X | 0.5 GB | 1x | 1x-4x | $25 | 1 | No |  |
| Standard-2X | 1 GB | 2x | 2x-8x | $50 | 2 | No |  |
| Performance-M | 2.5 GB | 100% | 12x | $250 | 8 | Yes |  |
| Performance-L | 14 GB | 100% | 50x | $500 | 16 | Yes |  |
| Performance-L-RAM | 30 GB | 100% | 24x | $500 | 16 | Yes |  |
| Performance-XL | 62 GB | 100% | 50x | $750 | 30 | Yes |  |
| Performance-2XL | 126 GB | 100% | 100x | $1500 | 60 | Yes |  |

\*Eco dynos require a [$5 flat fee monthly subscription](https://devcenter.heroku.com/articles/eco-dyno-hours) that covers a pool of 1000 hours shared by all Eco dynos in an account. Eco dynos are not available for Heroku Enterprise customers.

### [Cedar Private Spaces](https://devcenter.heroku.com/articles/dyno-sizes\#cedar-private-spaces)

All Private dynos have dedicated compute resources.

| Plan | Memory (RAM) | CPU Share | Compute | $/Month | Dyno Units<br>Consumed |
| --- | --- | --- | --- | --- | --- |
| Private-S | 1 GB | 100% | 12x | $125 | 5 |
| Private-M | 2.5 GB | 100% | 12x | $250 | 10 |
| Private-L | 14 GB | 100% | 50x | $500 | 20 |
| Private-L-RAM | 30 GB | 100% | 24x | $500 | 20 |
| Private-XL | 62 GB | 100% | 50x | $750 | 30 |
| Private-2XL | 126 GB | 100% | 100x | $1500 | 60 |

### [Cedar Shield Private Spaces](https://devcenter.heroku.com/articles/dyno-sizes\#cedar-shield-private-spaces)

All Shield dynos have dedicated compute resources.

| Plan | Memory (RAM) | CPU Share | Compute | $/Month | Dyno Units<br>Consumed |
| --- | --- | --- | --- | --- | --- |
| Shield-S | 1 GB | 100% | 12x | $150 | 6 |
| Shield-M | 2.5 GB | 100% | 12x | $300 | 12 |
| Shield-L | 14 GB | 100% | 50x | $600 | 24 |
| Shield-L-RAM | 30 GB | 100% | 24x | $600 | 24 |
| Shield-XL | 62 GB | 100% | 50x | $900 | 36 |
| Shield-2XL | 126 GB | 100% | 100x | $1800 | 72 |

## [Dynos in Fir](https://devcenter.heroku.com/articles/dyno-sizes\#dynos-in-fir)

All Fir dynos are dedicated compute resources and are only available with [Fir](https://devcenter.heroku.com/articles/generations#fir)-generation Private Spaces.

| Family | Plan | Memory (RAM) | vCPUs | $/Month | Dyno Units Consumed |
| --- | --- | --- | --- | --- | --- |
| Classic | dyno-1c-0.5gb | 0.5 GB | 1 | $25 | 1 |
| Classic | dyno-2c-1gb | 1 GB | 2 | $50 | 2 |
| General Purpose | dyno-1c-4gb | 4 GB | 1 | $80 | 3 |
| General Purpose | dyno-2c-8gb | 8 GB | 2 | $160 | 6 |
| General Purpose | dyno-4c-16gb | 16 GB | 4 | $320 | 13 |
| General Purpose | dyno-8c-32gb | 32 GB | 8 | $640 | 26 |
| General Purpose | dyno-16c-64gb | 64 GB | 16 | $1200 | 48 |
| Compute | dyno-2c-4gb | 4 GB | 2 | $150 | 6 |
| Compute | dyno-4c-8gb | 8 GB | 4 | $300 | 12 |
| Compute | dyno-8c-16gb | 16 GB | 8 | $600 | 24 |
| Compute | dyno-16c-32gb | 32 GB | 16 | $1000 | 40 |
| Compute | dyno-32c-64gb | 64 GB | 32 | $2400 | 96 |
| Memory | dyno-1c-8gb | 8 GB | 1 | $100 | 4 |
| Memory | dyno-2c-16gb | 16 GB | 2 | $250 | 10 |
| Memory | dyno-4c-32gb | 32 GB | 4 | $500 | 20 |
| Memory | dyno-8c-64gb | 64 GB | 8 | $750 | 30 |
| Memory | dyno-16c-128gb | 128 GB | 16 | $1500 | 60 |

## [Dyno Limits](https://devcenter.heroku.com/articles/dyno-sizes\#dyno-limits)

See [Dyno Scaling and Process Limits](https://devcenter.heroku.com/articles/dyno-scaling-and-process-limits) and [Dyno Memory Behavior](https://devcenter.heroku.com/articles/dyno-memory-behavior).

## [Pricing and Billing](https://devcenter.heroku.com/articles/dyno-sizes\#pricing-and-billing)

We limit access to Performance dynos to customers with an established payment history.

Heroku charges for dynos based on usage, except for the [Eco Dynos Plan](https://devcenter.heroku.com/articles/eco-dyno-hours). See [Dynos Usage & Costs](https://devcenter.heroku.com/articles/usage-and-billing#dyno-usage-and-costs) for more info, or [Dyno Units](https://devcenter.heroku.com/articles/heroku-enterprise#dyno-units) if you’re an Heroku Enterprise customer.

## [Additional Reading](https://devcenter.heroku.com/articles/dyno-sizes\#additional-reading)

- [Guidance for Choosing a Dyno](https://devcenter.heroku.com/articles/guidance-for-choosing-a-dyno)
- [Dyno Scaling and Process Limits](https://devcenter.heroku.com/articles/dyno-scaling-and-process-limits)
- [Scaling Your Dyno Formation](https://devcenter.heroku.com/articles/scaling)
- [Dyno Tiers](https://devcenter.heroku.com/articles/dyno-tiers)
- [Application Load Testing](https://devcenter.heroku.com/articles/application-load-testing)

### Feedback

[Log in to submit feedback.](https://devcenter.heroku.com/login?back_to=%2Farticles%2Fdyno-sizes&utm_campaign=login&utm_medium=feedback&utm_source=web)
