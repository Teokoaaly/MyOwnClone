import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import LandingBehavior from "@/components/ui/LandingBehavior";
import PublicPricing from "@/components/ui/PublicPricing";
import { Link } from "@/i18n/navigation";

const services = [
  {
    label: "Overview",
    title: "See your whole clone operation at a glance.",
    description: "Monitor activity, conversations, and usage from a single clean dashboard.",
  },
  {
    label: "Knowledge",
    title: "Upload your content and teach the clone your way.",
    description: "Documents, creator memories and business context stay organized for richer answers.",
  },
  {
    label: "Automation",
    title: "Handle inbox, products and bookings in one flow.",
    description: "Automate support and sales workflows while keeping your unique voice.",
  },
];

const steps = [
  ["01", "Sign up", "Create your account and start with the same public pricing shown in the dashboard."],
  ["02", "Configure", "Set name, language, tone and the core behavior of your digital clone."],
  ["03", "Train", "Upload knowledge and memories so responses stay accurate and aligned with you."],
  ["04", "Deploy", "Publish the clone and keep it available around the clock for support, sales or education."],
] as const;

export default function LandingPage() {
  return (
    <main className="moc-local-landing">
      <LandingBehavior />

      <nav className="nav">
        <Link href="/" className="nav-logo" aria-label="MyOwnClone home">
          <AnimatedLogoMark size={26} forceMotion />
          <span>MyOwnClone</span>
        </Link>

        <div className="nav-links">
          <a href="#services">Services</a>
          <a href="#process">Process</a>
          <a href="#plans">Plans</a>
        </div>

        <div className="nav-actions">
          <Link className="nav-signin" href="/login">
            Sign in
          </Link>
          <Link className="nav-cta" href="/registro">
            Get started
          </Link>
        </div>
      </nav>

      <section className="hero" id="hero">
        <div className="hero-content">
          <div className="flex justify-center mb-6 reveal">
            <AnimatedLogoMark size={48} forceMotion />
          </div>
          <span className="hero-kicker reveal">AI-Powered Digital Clone</span>
          <h1 className="reveal">
            Create an AI clone
            <br />
            that <span className="accent">works for you.</span>
          </h1>
          <p className="hero-sub reveal">
            Train an AI assistant with your knowledge, personality and business data.
            Answer customers, guide leads and automate daily work without losing your voice.
          </p>
          <div className="hero-ctas reveal">
            <Link className="btn btn-primary" href="/registro">
              Get started free
            </Link>
            <Link className="btn btn-secondary" href="/login">
              Sign in
            </Link>
          </div>
        </div>
      </section>

      <section className="section" id="services">
        <div className="sec-head">
          <span className="sec-kicker reveal">What it does</span>
          <h2 className="sec-title reveal">Everything your clone can handle.</h2>
          <p className="sec-desc reveal">
            From knowledge management to automated bookings, everything your AI clone needs in one place.
          </p>
        </div>
        <div className="services-grid">
          {services.map((service) => (
            <article className="service-card reveal" key={service.label}>
              <span className="service-label">{service.label}</span>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section process-section" id="process">
        <div className="sec-head">
          <span className="sec-kicker reveal">How it works</span>
          <h2 className="sec-title reveal">Four steps to your clone.</h2>
          <p className="sec-desc reveal">
            Get your clone running in four simple steps, from sign-up to deployment.
          </p>
        </div>
        <div className="process-grid">
          {steps.map(([number, title, description]) => (
            <article className="process-step reveal" key={number}>
              <div className="step-num">{number}</div>
              <h3>{title}</h3>
              <p>{description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section" id="plans">
        <div className="sec-head">
          <span className="sec-kicker reveal">Pricing</span>
          <h2 className="sec-title reveal">Plans that scale with you</h2>
          <p className="sec-desc reveal">
            Start free. Go pro when you’re ready. Cancel anytime.
          </p>
        </div>
        <PublicPricing mode="landing" />
      </section>

      <section className="cta-final" id="cta">
        <h2 className="reveal">
          Ready to clone
          <br />
          yourself?
        </h2>
        <p className="reveal">
          Start on the landing page, continue in the dashboard. Same pricing, same experience.
        </p>
        <div className="hero-ctas reveal">
          <Link className="btn btn-primary" href="/registro">
            Start building your clone
          </Link>
          <Link className="btn btn-secondary" href="/login">
            Sign in
          </Link>
        </div>
      </section>

      <footer className="footer">
        <span className="footer-brand">
          <AnimatedLogoMark size={20} forceMotion />
          © 2026 MyOwnClone
        </span>
        <div className="footer-links">
          <Link href="/legal">Legal</Link>
          <a href="/docs">Docs</a>
          <a href="mailto:hello@myownclone.com">Contact</a>
        </div>
      </footer>
    </main>
  );
}
