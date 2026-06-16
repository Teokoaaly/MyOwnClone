import type { CSSProperties } from "react";
import ReflectiveOrb from "@/components/ui/ReflectiveOrb";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { Link } from "@/i18n/navigation";
import { auth } from "@/lib/auth";
import { getSessionAwareNav } from "@/lib/session-routing";

const orbitApps = [
  { emoji: "🧠", label: "AI",      style: "left: 22%; top: 14%;" },
  { emoji: "💬", label: "Chat",    style: "right: 22%; top: 14%;" },
  { emoji: "📚", label: "Library", style: "right: 10%; top: 38%;" },
  { emoji: "📅", label: "Booking", style: "right: 10%; bottom: 38%;" },
  { emoji: "🎓", label: "Teach",   style: "right: 22%; bottom: 16%;" },
  { emoji: "📧", label: "Inbox",   style: "left: 22%; bottom: 16%;" },
  { emoji: "🛒", label: "Sell",    style: "left: 10%; bottom: 38%;" },
  { emoji: "📊", label: "Stats",   style: "left: 10%; top: 38%;" },
];

const landingPlans = [
  {
    name: "Free Plan",
    price: "$0",
    suffix: "/mo",
    description: "Start with the basics and publish your first AI clone at no cost.",
    cta: "Choose Free Plan",
    accent: "light" as const,
    features: ["1 active clone", "Basic knowledge upload", "Community support", "Simple analytics"],
  },
  {
    name: "Pro Plan",
    price: "$64.90",
    suffix: "/mo",
    description: "Unlock advanced tools and premium support for a production-ready clone.",
    cta: "Start Pro",
    accent: "dark" as const,
    badge: "Popular",
    features: ["Everything in Free", "Multi-mode prompts", "Priority support", "Advanced analytics"],
  },
  {
    name: "Enterprise",
    price: "$100",
    suffix: "/mo",
    description: "For teams that need custom workflows, governance, and dedicated support.",
    cta: "Contact Sales",
    accent: "light" as const,
    features: ["Unlimited collaborators", "SSO and governance", "Custom onboarding", "Dedicated success manager"],
  },
];

export default async function LandingPage() {
  const session = await auth();
  const nav = getSessionAwareNav(session);

  return (
    <main className="landing-stage">
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

        <div className="landing-orbits" aria-hidden="true">
          <span className="orbit orbit-one" />
          <span className="orbit orbit-two" />
          <span className="orbit orbit-three" />
          <span className="orbit orbit-four" />
          <span className="orbit-accent orbit-accent-left" />
          <span className="orbit-accent orbit-accent-right" />
          {orbitApps.map((app) => (
            <span
              key={app.label}
              className="landing-app"
              style={styleFromString(app.style)}
              aria-label={app.label}
            >
              {app.emoji}
            </span>
          ))}
        </div>

        <div className="landing-hero">
          <div className="landing-logo-animated">
            <ReflectiveOrb size={72} />
          </div>

          <h1>
            Create an AI clone
            <br />
            that works like you
          </h1>

          <p>
            Train a clone with your content. Answer questions, reply to emails,
            and book meetings 24/7 in your own tone — in pedagogy, sales, or support mode.
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
      </section>

      {/* Pricing section hidden — restore when ready */}
      {/* <section id="pricing" className="landing-pricing-section">...</section> */}

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

function styleFromString(style: string) {
  return Object.fromEntries(
    style
      .split(";")
      .map((rule) => rule.trim())
      .filter(Boolean)
      .map((rule) => {
        const [property, value] = rule.split(":").map((part) => part.trim());
        return [property.replace(/-([a-z])/g, (_, char) => char.toUpperCase()), value];
      }),
  ) as CSSProperties;
}
