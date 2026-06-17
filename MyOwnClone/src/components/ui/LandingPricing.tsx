"use client";

import { useState } from "react";
import { Link } from "@/i18n/navigation";

const plans = [
  {
    id: "free",
    badge: "Starter",
    name: "Free",
    monthly: 0,
    annual: 0,
    billing: "No card required",
    description: "Perfect to explore and prototype.",
    features: ["1 AI clone", "Basic knowledge base", "Public chat", "Community support"],
    excluded: ["Inbox AI triage", "API access"],
    cta: "Get started",
    href: "/registro",
  },
  {
    id: "pro",
    badge: "Most popular",
    name: "Pro",
    monthly: 64.9,
    annual: 778.8,
    billing: "Monthly billing",
    description: "For creators and growing businesses.",
    features: ["5 AI clones", "Unlimited knowledge", "Inbox AI triage", "Product catalog", "Full analytics", "Priority support"],
    excluded: [],
    cta: "Choose Pro",
    href: "/planes",
    featured: true,
  },
  {
    id: "enterprise",
    badge: "Scale",
    name: "Enterprise",
    monthly: null,
    annual: null,
    billing: "Tailored contract",
    description: "For teams with advanced needs.",
    features: ["Unlimited clones", "API access", "Team management", "Custom integrations", "Dedicated support"],
    excluded: [],
    cta: "Contact sales",
    href: "/registro",
  },
];

const comparison = [
  ["AI clones", "1", "5", "Unlimited"],
  ["Knowledge base", "Basic", "Unlimited", "Unlimited"],
  ["Public chat", "✓", "✓", "✓"],
  ["Inbox AI triage", "x", "✓", "✓"],
  ["Product catalog", "x", "✓", "✓"],
  ["Analytics", "x", "Full", "Advanced"],
  ["API access", "x", "x", "✓"],
  ["Support", "Community", "Priority", "Dedicated"],
];

function money(value: number | null, annual: boolean) {
  if (value === null) return "Custom";
  if (value === 0) return "$0";

  return `$${value.toLocaleString("en-US", {
    minimumFractionDigits: value % 1 ? 2 : 0,
    maximumFractionDigits: 2,
  })}`;
}

export default function LandingPricing() {
  const [annual, setAnnual] = useState(false);
  const [view, setView] = useState<"cards" | "comparison">("cards");

  return (
    <>
      <div className="pricing-controls reveal" aria-label="Pricing controls">
        <div className="pricing-tabs" role="tablist" aria-label="Pricing view">
          <button
            className={`pricing-tab ${view === "cards" ? "is-active" : ""}`}
            type="button"
            role="tab"
            aria-selected={view === "cards"}
            onClick={() => setView("cards")}
          >
            Pricing
          </button>
          <button
            className={`pricing-tab ${view === "comparison" ? "is-active" : ""}`}
            type="button"
            role="tab"
            aria-selected={view === "comparison"}
            onClick={() => setView("comparison")}
          >
            Compare features
          </button>
        </div>
        <button className="billing-toggle" type="button" aria-label="Toggle annual billing" onClick={() => setAnnual((value) => !value)}>
          <span>Monthly</span>
          <span className={`switch ${annual ? "is-on" : ""}`} aria-hidden="true" />
          <span>Annual</span>
        </button>
        <span className="billing-note">{annual ? "Annual view" : "Dashboard prices"}</span>
      </div>

      {view === "cards" ? (
        <div className="plans-grid" id="pricingCards">
          {plans.map((plan) => (
            <article className={`plan-card reveal ${plan.featured ? "feat" : ""}`} key={plan.id}>
              <span className="plan-badge">{plan.badge}</span>
              <h3 className="plan-name">{plan.name}</h3>
              <p className="plan-price">
                <strong>{money(annual ? plan.annual : plan.monthly, annual)}</strong>
                {plan.monthly !== null ? <span> {annual ? "/year" : "/month"}</span> : null}
              </p>
              <p className="plan-billing">
                {plan.monthly === null ? plan.billing : annual ? "Annual equivalent from dashboard price" : plan.billing}
              </p>
              <p className="plan-desc">{plan.description}</p>
              <ul className="plan-features">
                {plan.features.map((feature) => (
                  <li key={feature}>{feature}</li>
                ))}
                {plan.excluded.map((feature) => (
                  <li className="not-included" key={feature}>{feature}</li>
                ))}
              </ul>
              <Link className={`btn ${plan.featured ? "btn-primary" : "btn-secondary"} plan-action`} href={plan.href}>
                {plan.cta}
              </Link>
            </article>
          ))}
        </div>
      ) : (
        <div className="pricing-comparison is-active" id="pricingComparison" aria-label="Plan comparison">
          <table>
            <thead>
              <tr><th>Features</th><th>Free</th><th>Pro</th><th>Enterprise</th></tr>
            </thead>
            <tbody>
              {comparison.map(([feature, free, pro, enterprise]) => (
                <tr key={feature}>
                  <td>{feature}</td>
                  {[free, pro, enterprise].map((value, index) => (
                    <td key={`${feature}-${index}`} className={value === "✓" ? "feature-yes" : value === "x" ? "feature-no" : ""}>
                      {value}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </>
  );
}
