import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import ShaderBackground from "@/components/ui/ShaderBackground";
import { Link } from "@/i18n/navigation";
import { auth } from "@/lib/auth";
import { getSessionAwareNav } from "@/lib/session-routing";
import { headers } from "next/headers";

export const dynamic = "force-dynamic";

interface LandingPlan {
  id: string;
  name: string;
  price_cents: number;
  price_display?: string;
  stripe_price_id?: string | null;
  priceCents?: number;
  priceDisplay?: string;
  stripePriceId?: string | null;
}

interface LandingCard {
  title: string;
  description: string;
  features: string[];
  cta: string;
  badge?: string;
}

const FALLBACK_PLANS: LandingPlan[] = [
  { id: "basic", name: "Basic", price_cents: 0 },
  { id: "pro", name: "Pro", price_cents: 6490 },
  { id: "scale", name: "Scale", price_cents: 9900 },
  { id: "enterprise", name: "Enterprise", price_cents: 14900 },
];

const CARD_COPY: Record<string, LandingCard> = {
  basic: {
    title: "Basic access for a clean launch",
    description: "Get your first clone live with the essentials: a polished public page, core knowledge, and simple actions.",
    features: ["1 active clone", "Knowledge upload", "Public landing", "Starter analytics"],
    cta: "Choose Basic",
  },
  pro: {
    title: "The most balanced setup for growth",
    description: "Unlock the everyday workflows teams use most, with more control, better automation, and stronger support.",
    features: ["Everything in Basic", "Multi-mode prompts", "Email triage", "Priority support"],
    cta: "Start Pro",
    badge: "Most popular",
  },
  scale: {
    title: "More capacity for serious operations",
    description: "Expand into a larger setup with higher usage limits, more collaborators, and room to scale safely.",
    features: ["Higher usage limits", "Multi-clone workflows", "Advanced analytics", "API access"],
    cta: "Choose Scale",
  },
  enterprise: {
    title: "Custom architecture for bigger teams",
    description: "For organizations that need governance, custom onboarding, and a plan tailored to their deployment.",
    features: ["Unlimited collaborators", "Whitelabel options", "SSO / governance", "Dedicated success"],
    cta: "Talk to sales",
  },
};

export default async function LandingPage() {
  const session = await auth();
  const nav = getSessionAwareNav(session);
  const plans = await loadLandingPlans();

  return (
    <main className="landing-stage">
      <ShaderBackground />
      <section className="landing-card">
        <nav className="landing-nav" aria-label="Main">
          <Link href="/" className="landing-brand" aria-label="MyOwnClone home">
            <AnimatedLogoMark size={26} />
            <span>MyOwnClone</span>
          </Link>

          <div className="landing-menu">
            <Link href="/">Product</Link>
            <Link href="/">
              Solutions
              <span className="landing-chevron" aria-hidden="true">v</span>
            </Link>
            <Link href="/">About</Link>
            <Link href={nav.signInHref}>{nav.signInLabel}</Link>
          </div>

          <div className="landing-actions">
            <Link href={nav.signInHref} className="landing-signin">
              {nav.signInLabel}
            </Link>
            <Link href={nav.primaryHref} className="landing-contact">
              {nav.primaryLabel}
            </Link>
          </div>
        </nav>

        <div className="landing-hero">
          <div className="landing-logo-animated">
            <AnimatedLogoMark size={72} cycle />
          </div>

          <span className="landing-kicker">Current brand. Current pricing. Softer presentation.</span>

          <h1>
            Create an AI clone
            <br />
            that works like you
          </h1>

          <p>
            Train a clone with your content. Answer questions, reply to emails,
            and book meetings 24/7 in your own tone, with the same plan prices you see in the dashboard.
          </p>

          <div className="landing-cta-row">
            <Link href={nav.primaryHref} className="landing-primary">
              {session?.user ? nav.primaryLabel : "Start free"}
            </Link>
            <Link href={nav.signInHref} className="landing-secondary">
              {session?.user ? "Open dashboard" : "Watch demo"}
            </Link>
          </div>
        </div>

        <section id="pricing" className="landing-pricing-section">
          <div className="landing-pricing-shell">
            <div className="landing-pricing-head">
              <p className="landing-pricing-kicker">Pricing</p>
              <h2>Plans aligned with the dashboard</h2>
              <p>
                These prices are pulled from the same plan catalog used in the dashboard, so the public landing stays in sync.
              </p>
            </div>

            <div className="landing-pricing-grid">
              {plans.map((plan) => {
                const copy = CARD_COPY[plan.id] ?? {
                  title: plan.name,
                  description: "A flexible plan for your clone setup.",
                  features: ["Live billing sync", "Dashboard parity", "Scalable usage", "Support options"],
                  cta: `Choose ${plan.name}`,
                };
                const featured = plan.id === "pro" || Boolean(plan.stripe_price_id);

                return (
                  <article
                    key={plan.id}
                    className={`landing-plan-card${featured ? " landing-plan-card-featured" : ""}`}
                  >
                    <div className="landing-plan-top">
                      <span className="landing-plan-glyph" aria-hidden="true" />
                      {copy.badge ? <span className="landing-plan-badge">{copy.badge}</span> : null}
                    </div>

                    <div className="landing-plan-price">
                      <span>{formatPlanPrice(plan)}</span>
                      <small>/mo</small>
                    </div>

                    <h3>{plan.name}</h3>
                    <p>{copy.description}</p>

                    <div className="landing-plan-divider" />

                    <div className="landing-plan-features">
                      <strong>{copy.title}</strong>
                      <ul>
                        {copy.features.map((feature) => (
                          <li key={feature}>{feature}</li>
                        ))}
                      </ul>
                    </div>

                    <Link href={nav.primaryHref} className={featured ? "landing-plan-cta-inverse" : "landing-plan-cta"}>
                      {copy.cta}
                    </Link>
                  </article>
                );
              })}
            </div>
          </div>
        </section>
      </section>

      <footer className="landing-footer">
        <div className="landing-footer-inner">
          <div className="landing-footer-brand">
            <AnimatedLogoMark size={20} />
            <span>MyOwnClone</span>
          </div>
          <div className="landing-footer-links">
            <Link href="/">Product</Link>
            <Link href="/">Pricing</Link>
            <a href="mailto:hello@myownclone.com">Contact</a>
            <Link href="/legal">Legal</Link>
          </div>
          <div className="landing-footer-copy">
            © 2026 MyOwnClone.com — All rights reserved
          </div>
        </div>
      </footer>
    </main>
  );
}

async function loadLandingPlans(): Promise<LandingPlan[]> {
  const fallback = FALLBACK_PLANS;

  try {
    const requestHeaders = await headers();
    const host = requestHeaders.get("host");
    if (!host) return fallback;

    const protocol = requestHeaders.get("x-forwarded-proto") ?? "http";
    const res = await fetch(`${protocol}://${host}/api/clone/plans`, {
      cache: "no-store",
      headers: {
        cookie: requestHeaders.get("cookie") ?? "",
      },
    });

    if (!res.ok) return fallback;

    const data = await res.json();
    const plans = Array.isArray(data) ? data : data?.items;
    if (!Array.isArray(plans) || plans.length === 0) return fallback;

    const preferredOrder = new Map(["basic", "pro", "scale", "enterprise"].map((id, index) => [id, index]));

    return [...plans]
      .map(normalizePlan)
      .filter((plan): plan is LandingPlan => Boolean(plan))
      .sort((a, b) => {
        const aRank = preferredOrder.get(a.id) ?? 99;
        const bRank = preferredOrder.get(b.id) ?? 99;
        if (aRank !== bRank) return aRank - bRank;
        return Number(getPlanPriceCents(a)) - Number(getPlanPriceCents(b));
      });
  } catch {
    return fallback;
  }
}

function formatPlanPrice(plan: LandingPlan) {
  const cents = getPlanPriceCents(plan);
  const display = plan.price_display ?? plan.priceDisplay;
  if (display) return display;
  if (cents === 0) return "Free";

  return new Intl.NumberFormat("es-ES", {
    style: "currency",
    currency: "EUR",
    maximumFractionDigits: 2,
  }).format(cents / 100);
}

function normalizePlan(plan: unknown): LandingPlan | null {
  if (!plan || typeof plan !== "object") return null;

  const item = plan as Record<string, unknown>;
  const id = typeof item.id === "string" ? item.id : "";
  const name = typeof item.name === "string" ? item.name : id;
  if (!id || !name) return null;

  const priceCents = typeof item.price_cents === "number"
    ? item.price_cents
    : typeof item.priceCents === "number"
      ? item.priceCents
      : 0;

  return {
    id,
    name,
    price_cents: priceCents,
    price_display: typeof item.price_display === "string" ? item.price_display : undefined,
    stripe_price_id: typeof item.stripe_price_id === "string" ? item.stripe_price_id : undefined,
    priceCents: typeof item.priceCents === "number" ? item.priceCents : undefined,
    priceDisplay: typeof item.priceDisplay === "string" ? item.priceDisplay : undefined,
    stripePriceId: typeof item.stripePriceId === "string" ? item.stripePriceId : undefined,
  };
}

function getPlanPriceCents(plan: LandingPlan) {
  return plan.price_cents ?? plan.priceCents ?? 0;
}
