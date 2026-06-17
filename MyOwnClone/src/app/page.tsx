import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import LandingPricing from "@/components/ui/LandingPricing";
import ShaderBackground from "@/components/ui/ShaderBackground";
import { Link } from "@/i18n/navigation";
import { auth } from "@/lib/auth";
import { getSessionAwareNav } from "@/lib/session-routing";

const services = [
  ["Overview", "Real-time dashboard with clone activity, recent interactions and key metrics at a glance.", "◉"],
  ["Library & Memory", "Upload documents, build structured knowledge and store creator memories for richer responses.", "✦"],
  ["Inbox", "AI triage for incoming emails: classify intent, suggest replies and apply templates automatically.", "✉"],
  ["Booking", "Configure meeting types, availability and let the clone manage your calendar and reservations.", "📅"],
  ["Products", "Product catalog and commercial context so the clone recommends the right offer in sales mode.", "◆"],
  ["Usage", "Analytics on consumption, top questions, knowledge gaps and cost tracking per period.", "▦"],
];

const steps = [
  ["1", "Sign up", "Create your account and pick a plan. Free to start."],
  ["2", "Configure", "Name your clone, set personality, tone and language."],
  ["3", "Train", "Upload documents and add creator memories."],
  ["4", "Deploy", "Publish and share the public chat link. It runs 24/7."],
];

export default async function LandingPage() {
  const session = await auth();
  const nav = getSessionAwareNav(session);

  return (
    <main className="moc-local-landing">
      <style
        dangerouslySetInnerHTML={{
          __html: `
            .moc-local-landing{
              background:
                radial-gradient(circle at 18% 12%,rgba(255,255,255,.9),transparent 36%),
                radial-gradient(circle at 82% 18%,rgba(251,146,60,.16),transparent 30%),
                radial-gradient(circle at 18% 82%,rgba(255,237,213,.26),transparent 30%),
                radial-gradient(circle at 88% 88%,rgba(255,210,120,.16),transparent 34%),
                #f3ece4 !important;
            }
            .moc-local-landing canvas{
              opacity:.42!important;
              mix-blend-mode:normal!important;
              filter:saturate(1.45) brightness(1.22) contrast(.82);
            }
            .moc-local-landing .site-backdrop:before{
              background:radial-gradient(circle,rgba(255,255,255,.42),rgba(251,146,60,.1) 42%,transparent 72%)!important;
            }
            .moc-local-landing .site-backdrop:after{
              background:radial-gradient(circle,rgba(255,237,213,.32),rgba(234,88,12,.1) 40%,transparent 74%)!important;
            }
          `,
        }}
      />
      <div className="site-backdrop" aria-hidden="true" />
      <ShaderBackground />

      <nav className="nav">
        <Link href="/" className="nav-logo" aria-label="MyOwnClone home">
          <AnimatedLogoMark size={26} />
          <span>MyOwnClone</span>
        </Link>
        <div className="nav-links">
          <a href="#services">Services</a>
          <a href="#process">Process</a>
          <a href="#plans">Plans</a>
          <Link className="nav-cta" href={nav.primaryHref}>
            {session?.user ? nav.primaryLabel : "Get started"}
          </Link>
        </div>
      </nav>

      <section className="hero" id="hero">
        <div className="hero-content">
          <span className="hero-kicker reveal">AI-Powered Digital Clone</span>
          <h1 className="reveal">
            Create an AI clone
            <br />
            that <span className="accent">works for you.</span>
          </h1>
          <p className="hero-sub reveal">
            Train an AI assistant with your knowledge, personality and business data.
            Handle emails, recommend products and answer customers 24/7.
          </p>
          <div className="hero-ctas reveal">
            <Link className="btn btn-primary" href={nav.primaryHref}>
              {session?.user ? nav.primaryLabel : "Get started free"}
            </Link>
            <a className="btn btn-secondary" href="#plans">See plans</a>
          </div>
        </div>
      </section>

      <section className="section mesh-bg" id="services">
        <div className="sec-head">
          <span className="sec-kicker reveal">What it does</span>
          <h2 className="sec-title reveal">Everything your clone can handle.</h2>
          <p className="sec-desc reveal">
            Six modules working together so your AI clone manages knowledge, communications, sales and analytics in one workspace.
          </p>
        </div>
        <div className="services-grid">
          {services.map(([title, description, icon]) => (
            <article className="service-card reveal" key={title}>
              <div className="service-icon">{icon}</div>
              <h3>{title}</h3>
              <p>{description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section" id="process">
        <div className="sec-head">
          <span className="sec-kicker reveal">How it works</span>
          <h2 className="sec-title reveal">Four steps to your clone.</h2>
          <p className="sec-desc reveal">From sign-up to a live assistant, the whole process takes minutes, not weeks.</p>
        </div>
        <div className="process-grid">
          {steps.map(([number, title, description]) => (
            <div className="process-step reveal" key={number}>
              <div className="step-num">{number}</div>
              <h3>{title}</h3>
              <p>{description}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="section mesh-bg" id="plans">
        <div className="sec-head">
          <span className="sec-kicker reveal">Pricing</span>
          <h2 className="sec-title reveal">Pick your plan.</h2>
          <p className="sec-desc reveal">Start free, scale as your clone grows. All plans include the core AI assistant.</p>
        </div>
        <LandingPricing />
      </section>

      <section className="cta-final" id="cta">
        <h2 className="reveal">
          Ready to clone
          <br />
          yourself?
        </h2>
        <p className="reveal">Join creators and businesses already using AI clones to scale their knowledge and automate conversations.</p>
        <Link className="btn btn-glow" href={nav.primaryHref}>
          Start building your clone →
        </Link>
      </section>

      <footer className="footer">
        <span className="footer-brand">
          <AnimatedLogoMark size={20} />
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
