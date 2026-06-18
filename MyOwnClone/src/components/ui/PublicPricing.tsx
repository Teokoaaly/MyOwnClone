"use client";

import { useState } from "react";
import { Link } from "@/i18n/navigation";
import {
  formatPublicPlanPrice,
  getPublicBillingLabel,
  normalizePublicPlanId,
  PUBLIC_PRICING_COMPARISON,
  PUBLIC_PRICING_PLANS,
  type PublicPlanId,
} from "@/lib/public-pricing";

interface PublicPricingProps {
  mode: "landing" | "dashboard";
  currentPlanId?: string | null;
  onSelectPlan?: (planId: PublicPlanId) => void;
}

export default function PublicPricing({ mode, currentPlanId, onSelectPlan }: PublicPricingProps) {
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
            Pricing
          </button>
          <button
            className={`shared-pricing-tab ${view === "comparison" ? "is-active" : ""}`}
            type="button"
            role="tab"
            aria-selected={view === "comparison"}
            onClick={() => setView("comparison")}
          >
            Compare features
          </button>
        </div>

        <button
          className="shared-billing-toggle"
          type="button"
          aria-label="Toggle annual billing"
          onClick={() => setAnnual((value) => !value)}
        >
          <span>Monthly</span>
          <span className={`shared-billing-switch ${annual ? "is-on" : ""}`} aria-hidden="true" />
          <span>Annual</span>
        </button>

        <span className="shared-pricing-note">
          {annual ? "Annual equivalent" : "Dashboard prices"}
        </span>
      </div>

      {view === "cards" ? (
        <div className="shared-pricing-grid" id={`${mode}PricingCards`}>
          {PUBLIC_PRICING_PLANS.map((plan) => {
            const isCurrent = normalizedCurrentPlan === plan.id;

            return (
              <article
                key={plan.id}
                className={`shared-plan-card reveal ${plan.featured ? "is-featured" : ""}`}
              >
                <div className="shared-plan-top">
                  <span className="shared-plan-badge">{plan.badge}</span>
                  {mode === "dashboard" && isCurrent ? (
                    <span className="shared-plan-current">Current</span>
                  ) : null}
                </div>

                <h3 className="shared-plan-name">{plan.name}</h3>
                <p className="shared-plan-price">
                  <strong>{formatPublicPlanPrice(annual ? plan.annual : plan.monthly)}</strong>
                  {plan.monthly !== null ? <span>{annual ? "/year" : "/month"}</span> : null}
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
                <th>Feature</th>
                <th>Free</th>
                <th>Pro</th>
                <th>Enterprise</th>
              </tr>
            </thead>
            <tbody>
              {PUBLIC_PRICING_COMPARISON.map(([feature, free, pro, enterprise]) => (
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
