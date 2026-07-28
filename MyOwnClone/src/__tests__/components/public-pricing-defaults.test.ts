import { describe, expect, it } from "vitest";
import {
  PUBLIC_PRICING_COMPARISON,
  PUBLIC_PRICING_PLANS,
} from "@/lib/public-pricing";
import {
  liquidPricingComparison,
  liquidPricingPlans,
} from "@/app/landing-liquid/content";

describe("PublicPricing canonical defaults", () => {
  it("keeps the public Free, Pro and Enterprise catalog unchanged", () => {
    expect(PUBLIC_PRICING_PLANS.map(({ id, name, monthly, annual, href }) => ({
      id,
      name,
      monthly,
      annual,
      href,
    }))).toEqual([
      { id: "free", name: "Free", monthly: 0, annual: 0, href: "/registro" },
      { id: "pro", name: "Pro", monthly: 64.9, annual: 778.8, href: "/planes" },
      { id: "enterprise", name: "Enterprise", monthly: null, annual: null, href: "mailto:hello@myownclone.com" },
    ]);
  });

  it("localizes a copy of the catalog without mutating its canonical data", () => {
    expect(liquidPricingPlans.map((plan) => plan.name)).toEqual(["Free", "Pro", "Enterprise"]);
    expect(liquidPricingPlans.map((plan) => plan.monthly)).toEqual([0, 64.9, null]);
    expect(liquidPricingComparison).toHaveLength(PUBLIC_PRICING_COMPARISON.length);
    expect(PUBLIC_PRICING_PLANS[1]?.description).toBe("For creators and growing businesses.");
  });
});
