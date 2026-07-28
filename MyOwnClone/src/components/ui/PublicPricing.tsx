"use client";

import { useState } from "react";
import { Link } from "@/i18n/navigation";
import {
  formatPublicPlanPrice,
  getPublicBillingLabel,
  normalizePublicPlanId,
  PUBLIC_PRICING_COMPARISON,
  PUBLIC_PRICING_PLANS,
  type PublicPlan,
  type PublicPlanId,
} from "@/lib/public-pricing";

export interface PublicPricingCopy {
  readonly annual: string;
  readonly annualEquivalent: string;
  readonly compareFeatures: string;
  readonly current: string;
  readonly dashboardPrices: string;
  readonly feature: string;
  readonly monthly: string;
  readonly pricing: string;
  readonly toggleAnnual: string;
  readonly year: string;
  readonly month: string;
}

const defaultCopy: PublicPricingCopy = {
  annual: "Annual",
  annualEquivalent: "Annual equivalent",
  compareFeatures: "Compare features",
  current: "Current",
  dashboardPrices: "Dashboard prices",
  feature: "Feature",
  monthly: "Monthly",
  pricing: "Pricing",
  toggleAnnual: "Toggle annual billing",
  year: "/year",
  month: "/month",
};

interface PublicPricingProps {
  mode: "landing" | "dashboard";
  currentPlanId?: string | null;
  onSelectPlan?: (planId: PublicPlanId) => void;
  plans?: readonly PublicPlan[];
  comparison?: readonly (readonly string[])[];
  copy?: PublicPricingCopy;
}

export default function PublicPricing({
  mode,
  currentPlanId,
  onSelectPlan,
  plans = PUBLIC_PRICING_PLANS,
  comparison = PUBLIC_PRICING_COMPARISON,
  copy = defaultCopy,
}: PublicPricingProps) {
  const [annual, setAnnual] = useState(false);
  const [view, setView] = useState<"cards" | "comparison">("cards");
  const normalizedCurrentPlan = normalizePublicPlanId(currentPlanId);

  return (
    <div className={`shared-pricing shared-pricing-${mode}`}>
      <div className="shared-pricing-controls reveal" aria-label="Pricing controls">
        <div className="shared-pricing-tabs" role="tablist" aria-label="Pricing view">
          <button
            className={`shared-pricing-tab ${view === "cards" ? "is-active" : ""}`}
            type="button"
            role="tab"
            aria-selected={view === "cards"}
            onClick={() => setView("cards")}
          >
            {copy.pricing}
          </button>
          <button
            className={`shared-pricing-tab ${view === "comparison" ? "is-active" : ""}`}
            type="button"
            role="tab"
            aria-selected={view === "comparison"}
            onClick={() => setView("comparison")}
          >
            {copy.compareFeatures}
          </button>
        </div>

        <button
          className="shared-billing-toggle"
          type="button"
          aria-label={copy.toggleAnnual}
          onClick={() => setAnnual((value) => !value)}
        >
          <span>{copy.monthly}</span>
          <span className={`shared-billing-switch ${annual ? "is-on" : ""}`} aria-hidden="true" />
          <span>{copy.annual}</span>
        </button>

        <span className="shared-pricing-note">
          {annual ? copy.annualEquivalent : copy.dashboardPrices}
        </span>
      </div>

      {view === "cards" ? (
        <div className="shared-pricing-grid" id={`${mode}PricingCards`}>
          {plans.map((plan) => {
            const isCurrent = normalizedCurrentPlan === plan.id;

            return (
              <article
                key={plan.id}
                className={`shared-plan-card reveal ${plan.featured ? "is-featured" : ""}`}
              >
                <div className="shared-plan-top">
                  <span className="shared-plan-badge">{plan.badge}</span>
                  {mode === "dashboard" && isCurrent ? (
                    <span className="shared-plan-current">{copy.current}</span>
                  ) : null}
                </div>

                <h3 className="shared-plan-name">{plan.name}</h3>
                <p className="shared-plan-price">
                  <strong>{formatPublicPlanPrice(annual ? plan.annual : plan.monthly)}</strong>
                  {plan.monthly !== null ? <span>{annual ? copy.year : copy.month}</span> : null}
                </p>
                <p className="shared-plan-billing">{getPublicBillingLabel(plan, annual)}</p>
                <p className="shared-plan-desc">{plan.description}</p>

                <ul className="shared-plan-features">
                  {plan.features.map((feature) => (
                    <li
                      key={feature.label}
                      className={feature.included ? "is-included" : "is-excluded"}
                    >
                      <span className="shared-plan-feature-mark" aria-hidden="true" />
                      <span>{feature.label}</span>
                    </li>
                  ))}
                </ul>

                {onSelectPlan ? (
                  <button
                    type="button"
                    onClick={() => onSelectPlan(plan.id)}
                    className={`shared-plan-action ${plan.featured ? "is-featured" : ""}`}
                  >
                    {plan.cta}
                  </button>
                ) : (
                  <Link
                    href={plan.href}
                    className={`shared-plan-action ${plan.featured ? "is-featured" : ""}`}
                  >
                    {plan.cta}
                  </Link>
                )}
              </article>
            );
          })}
        </div>
      ) : (
        <div className="shared-pricing-comparison reveal" id={`${mode}PricingComparison`}>
          <table>
            <thead>
              <tr>
                <th>{copy.feature}</th>
                <th>Free</th>
                <th>Pro</th>
                <th>Enterprise</th>
              </tr>
            </thead>
            <tbody>
              {comparison.map(([feature, free, pro, enterprise]) => (
                <tr key={feature}>
                  <td>{feature}</td>
                  {[free, pro, enterprise].map((value, index) => (
                    <td key={`${feature}-${index}`}>{value}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
