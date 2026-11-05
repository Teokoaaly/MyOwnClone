## stripe-pricing-2026-10-29 — Atoms created from Stripe pricing page capture (2026-10-29)

### Atoms created:
1. **2026-1029-stripe-stablecoin-pricing** — Stripe stablecoin payments at 1.5% of transaction amount USD, including fiat conversion, wallet, AML screening, fraud prevention, and gas sponsorship. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

2. **2026-1029-stripe-dispute-fees** — Stripe dispute charges: $15.00 per dispute received, $15.00 per dispute countered manually, 30% Smart Disputes fee on won disputes. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

3. **2026-1029-stripe-payment-links-custom-domain** — Payment Links custom domain option at $10.00 per month. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

4. **2026-1029-stripe-checkout-custom-domain** — Checkout custom domain at $10.00 per month plus 0.4% of transaction total capped at $2.00 per invoice. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

5. **2026-1029-stripe-terminal-pricing** — Terminal pricing: 2.7% + 5¢ domestic, 1.5% international, $0.10 per Tap to Pay authorization. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

6. **2026-1029-stripe-financial-connections-verification** — Financial Connections: $1.50 per successful instant verification, $0.10 per successful API call. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

7. **2026-1029-stripe-treasury-payouts** — Treasury payouts: $1.50 per local bank payout, $1.50 per debit card payout, 0.75% of amount (min 50¢). Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

8. **2026-1029-stripe-issuing-cards** — Issuing: $0.10 per virtual card, $3.50 per standard physical card. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

9. **2026-1029-stripe-tax-pricing** — Tax: 0.5% per transaction (registered) or $0.50 per API integration transaction (includes 10 free calculation API calls). Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

10. **2026-1029-stripe-radar-screening** — Radar: starting at $0.05 per screened transaction. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

11. **2026-1029-stripe-metronome-billing** — Metronome: $0.04 per 1K ingest events, 0.8% of billing volume. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

12. **2026-1029-stripe-invoicing-pricing** — Invoicing: 0.4% per paid invoice. Links to [[2026-1022-stripe-planes-trial-30-dias]] and [[2026-1022-stripe-webhook-confirmado]].

### Cross-atom tensions:
- **Trial card requirement vs. cardless onboarding**: Atoms 1, 5, 6, 8, 9, 11 all note that [[2026-1022-stripe-planes-trial-30-dias]] requires a card upfront for trial conversions, creating friction for new users. Several atoms (stablecoin, Financial Connections, Treasury, Issuing, Tax, Radar) offer cardless or lower-friction alternatives at per-transaction cost, creating a tension between the trial's card requirement and the per-transaction pricing model of complementary services.

- **Variable vs. fixed pricing models**: Atoms with per-transaction fees (stablecoin 1.5%, dispute $15/fixed, Payment Links $10/month, Checkout 0.4% + $10, Terminal percentage + $0.10, Financial Connections $1.50/$0.10, Treasury $1.50 + 0.75%, Issuing $0.10/$3.50, Tax 0.5% or $0.50, Radar $0.05, Metronome $0.04/1K + 0.8%, Invoicing 0.4%) versus percentage-based payment processing (2.9% + 30¢ standard) create different cost structures depending on business model — low average order value vs. high volume, subscription vs. one-time, fiat vs. crypto.

- **Sequencing friction**: Multiple atoms note that tax compliance (0.5% per transaction) cannot activate until after the trial's card-upfront requirement is satisfied, creating a sequencing barrier where pricing features are locked behind billing information provision.

### Follow-up needed:
- Monitor whether the $15 per dispute fee disproportionately affects low average order value businesses compared to high-ticket models.
- Test whether the 0.4% per-invoice Checkout fee or the $10/month custom domain offers better cost efficiency at different transaction volumes.
- Track user adoption of cardless onboarding paths (stablecoin, Financial Connections) versus the trial's card-upfront requirement.
- Evaluate whether Metronome's dual pricing ($0.04/1K events + 0.8% billing volume) better serves usage-based or subscription business models.

### Railway pricing atoms (2026-10-29 capture)
Atoms created from Railway pricing page capture (2026-10-29):

1. **2026-1029-railway-pricing-free-credit** — Free/Hobby plan includes $5 monthly credits applied to resource usage before charging, auto-recharged every 30 days, no credit card required for trial initial. Links to [[2026-1026-brightdata-free-tier-de-5000-creditos-sin-tarjeta]] and [[2026-1022-myclone-limites-plan-free]]. Concerns: $5 credit with 30-day expiration vs. myownclone's feature limits as the primary barrier.

2. **2026-1029-railway-pricing-pro-credit** — Pro plan includes $20 monthly credits that accumulate carry-over from the $5 trial initial, auto-recharged every 30 days. Links to [[2026-1028-proton-business-mail-recommended-y-distincion-por-plan]] and [[2026-1029-aws-ses-ala-carte-pricing]]. Concerns: $20 as platform-wide credit vs. Proton's "Recommended" per-user signaling at $12,99/user/mes — different granularity and pricing models create tension for team-based vs. resource-based decision making.

3. **2026-1029-railway-pricing-cpu-rate** — CPU at $0.00000772 per vCPU-second, metered billing per second, no idle time charges (sandboxes destroyed after idle timeout). Links to [[2026-1026-heroku-cedar-cpu-share-compute-y-columna-dedicated]] and [[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]. Concerns: Metered per-second pricing is 3-4× cheaper than Heroku dyno hourly rates but Railway sells compliance (SOC 2, HIPAA BAA) as expensive add-on ($1,000+), creating tension between "previsibilidad sobre cumplimiento" principle and regulated workloads.