---
id: 2026-1029-aws-ses-tiered-rates-marginal
type: atom
certainty: solid
sources: [sources/2026-10-29-aws-ses-pricing.md]
links: ["[[2026-1029-aws-ses-three-pricing-plans]]", "[[2026-1029-aws-ses-fixed-region-fees]]"]
---

## Claim
Tiered rates in Amazon SES are applied marginally — each rate applies only to the emails within that tier, not to the entire volume cumulatively.

## Why It Matters
This means customers with 15M emails pay the $0.14/1K rate only for the 5M emails in the 10–100M tier, while the first 10M remain at $0.16/1K. Misinterpreting this as cumulative would overstate costs by ~13% at the 10M boundary.

## [FRICTION]
> No friction detected. This atom explains the marginal tiering mechanism. The three-pricing-plans atom provides complementary context on plan structure. No contradiction with any prior atom.