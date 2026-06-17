import { Link } from "@/i18n/navigation";
import { auth } from "@/lib/auth";
import { getSessionAwareNav } from "@/lib/session-routing";
import { getTranslations } from "next-intl/server";
import { HowItWorks } from "@/components/landing/HowItWorks";

const landingPlans = [
  { name: "Free Plan", price: "$0", suffix: "/mo", description: "Start with the basics and publish your first AI clone at no cost.", cta: "Choose Free Plan", accent: "light" as const, planId: "free", features: ["1 active clone", "Basic knowledge upload", "Community support", "Simple analytics"] },
  { name: "Pro Plan", price: "$64.90", suffix: "/mo", description: "Unlock advanced tools and premium support for a production-ready clone.", cta: "Start Pro", accent: "dark" as const, badge: "Popular", planId: "pro", features: ["Everything in Free", "Multi-mode prompts", "Priority support", "Advanced analytics"] },
  { name: "Enterprise", price: "$100", suffix: "/mo", description: "For teams that need custom workflows, governance, and dedicated support.", cta: "Contact Sales", accent: "light" as const, planId: "enterprise", features: ["Unlimited collaborators", "SSO and governance", "Custom onboarding", "Dedicated success manager"] },
];

export default async function LandingPage() {
  const t = await getTranslations("landing");
  const session = await auth();
  const nav = getSessionAwareNav(session);

  return (
    <main className="landing-stage-v2">
      {/* Nav */}
      <nav className="landing-nav-v2" aria-label="Main">
        <Link href="/" className="landing-brand-v2" aria-label="MyOwnClone home">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <rect x="2" y="2" width="9" height="9" rx="4" fill="#EA580C" />
            <rect x="13" y="2" width="9" height="9" rx="4" fill="#F97316" />
            <rect x="2" y="13" width="9" height="9" rx="4" fill="#F97316" />
            <rect x="13" y="13" width="9" height="9" rx="4" fill="#EA580C" />
          </svg>
          <span>MyOwnClone</span>
        </Link>

        <div className="landing-nav-links-v2">
          <a href="#how-it-works">How it works</a>
          <a href="#pricing">Pricing</a>
        </div>

        <div className="landing-nav-actions-v2">
          <Link href={nav.signInHref} className="btn-nav-signin">
            {nav.signInLabel}
          </Link>
          <Link href={nav.primaryHref} className="btn-nav-primary">
            {nav.primaryLabel}
          </Link>
        </div>
      </nav>

      {/* Hero */}
      <section className="landing-hero-v2">
        <h1>
          Create an AI clone
          <br />
          <span className="text-accent">that works like you</span>
        </h1>
        <p>
          Train a clone with your content. Answer questions, reply to emails,
          and book meetings 24/7 in your own tone, in pedagogy, sales, or support mode.
        </p>
        <div className="landing-hero-ctas">
          <Link href={nav.primaryHref} className="btn-hero-primary">
            {session?.user ? nav.primaryLabel : "Start free"}
          </Link>
          <Link href={nav.signInHref} className="btn-hero-secondary">
            {session?.user ? "Open dashboard" : "Watch demo"}
          </Link>
        </div>
      </section>

      {/* How It Works */}
      <div id="how-it-works">
        <HowItWorks />
      </div>

      {/* Pricing */}
      <section id="pricing" className="landing-pricing-v2">
        <div className="landing-pricing-shell-v2">
          <div className="landing-pricing-head-v2">
            <p className="landing-pricing-kicker-v2">{t("navPricing")}</p>
            <h2>Select a plan</h2>
            <p>
              Start free, upgrade when your clone grows, and keep the same polished workspace all the way up.
            </p>
          </div>

          <div className="landing-pricing-grid-v2">
            {landingPlans.map((plan) => (
              <article key={plan.name} className={plan.accent === "dark" ? "plan-card plan-card-featured" : "plan-card"}>
                <div className="plan-card-top">
                  {plan.badge && <span className="plan-badge">{plan.badge}</span>}
                </div>
                <div className="plan-price">
                  <span className="plan-amount">{plan.price}</span>
                  <span className="plan-suffix">{plan.suffix}</span>
                </div>
                <h3>{plan.name}</h3>
                <p>{plan.description}</p>
                <Link href={`${nav.primaryHref}?plan=${plan.planId}`} className={plan.accent === "dark" ? "plan-cta plan-cta-inverse" : "plan-cta"}>
                  {plan.cta}
                </Link>
                <div className="plan-divider" />
                <div className="plan-features">
                  <strong>Features</strong>
                  <ul>{plan.features.map((f) => <li key={f}>{f}</li>)}</ul>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="landing-footer-v2">
        <div className="landing-footer-inner-v2">
          <div className="landing-footer-brand-v2">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" aria-hidden="true">
              <rect x="2" y="2" width="9" height="9" rx="4" fill="#EA580C" />
              <rect x="13" y="2" width="9" height="9" rx="4" fill="#F97316" />
              <rect x="2" y="13" width="9" height="9" rx="4" fill="#F97316" />
              <rect x="13" y="13" width="9" height="9" rx="4" fill="#EA580C" />
            </svg>
            <span>MyOwnClone</span>
          </div>
          <div className="landing-footer-links-v2">
            <a href="#how-it-works">How it works</a>
            <a href="#pricing">Pricing</a>
            <a href="mailto:hello@myownclone.com">{t("contact")}</a>
            <Link href="/legal">Legal</Link>
          </div>
          <p className="landing-footer-copy-v2">&copy; 2026 MyOwnClone.com &mdash; All rights reserved</p>
        </div>
      </footer>
    </main>
  );
}
