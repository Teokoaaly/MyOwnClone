import type { Metadata } from "next";
import { ArrowUpRight, CheckCircle, Sparkle, StackSimple } from "@phosphor-icons/react/dist/ssr";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import PublicPricing from "@/components/ui/PublicPricing";
import { Link } from "@/i18n/navigation";
import { LiquidOrb } from "./_components/LiquidOrb";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "MyOwnClone | AI-Powered Digital Clone",
  description: "Create an AI clone that works for you.",
};

const modules = [
  ["Overview", "See your whole clone operation at a glance.", "Track activity, recent conversations, usage and commercial signals from one dashboard."],
  ["Knowledge", "Upload your content and teach the clone your way.", "Documents, creator memories and business context stay organized for richer answers."],
  ["Automation", "Handle inbox, products and bookings in one flow.", "Turn common support and sales work into repeatable actions without losing your tone."],
] as const;

const steps = [
  ["01", "Sign up", "Create your account and start with the same public pricing shown in the dashboard."],
  ["02", "Configure", "Set name, language, tone and the core behavior of your digital clone."],
  ["03", "Train", "Upload knowledge and memories so responses stay accurate and aligned with you."],
  ["04", "Deploy", "Publish the clone and keep it available around the clock for support, sales or education."],
] as const;

const technologies = ["Next.js", "Flask", "PostgreSQL", "Redis", "Ollama"] as const;

export default function LiquidLandingPage() {
  return (
    <main className={styles.page} lang="en">
      <div className={styles.ambient} aria-hidden="true" />
      <header className={styles.header}>
        <nav aria-label="Main navigation" className={styles.nav}>
          <Link aria-label="MyOwnClone home" className={styles.brand} href="/">
            <AnimatedLogoMark forceMotion size={28} />
            <span>MyOwnClone</span>
          </Link>
          <div className={styles.navLinks}>
            <a href="#features">What it does</a>
            <a href="#process">How it works</a>
            <a href="#plans">Plans &amp; pricing</a>
            <a href="#simulator">Live demo</a>
          </div>
          <Link className={styles.navCta} href="/registro">Get started free <ArrowUpRight aria-hidden="true" size={16} weight="bold" /></Link>
        </nav>
      </header>

      <section className={styles.hero} id="hero">
        <div className={styles.heroCopy}>
          <p className={styles.kicker}><Sparkle aria-hidden="true" size={15} weight="fill" /> AI-Powered Digital Clone</p>
          <h1>Create an AI clone that works for you.</h1>
          <p>Train an AI assistant with your knowledge, personality and business data. Answer customers, guide leads and automate daily work without losing your voice.</p>
          <div className={styles.heroActions}>
            <Link className={styles.primaryCta} href="/registro">Get started free <span aria-hidden="true"><ArrowUpRight size={18} weight="bold" /></span></Link>
            <Link className={styles.secondaryCta} href="#simulator">Explore clone simulator</Link>
          </div>
          <div className={styles.valueProps}>
            <span><CheckCircle aria-hidden="true" size={15} weight="fill" /> Free to start</span>
            <span><CheckCircle aria-hidden="true" size={15} weight="fill" /> Setup in minutes</span>
            <span><CheckCircle aria-hidden="true" size={15} weight="fill" /> 24/7 availability</span>
          </div>
        </div>
        <div className={styles.orbFrame}>
          <LiquidOrb />
          <div className={styles.orbCaption}><StackSimple aria-hidden="true" size={18} weight="duotone" /><span>Knowledge, conversations and automation in one workspace.</span></div>
        </div>
      </section>

      <section className={styles.modules} id="features">
        <div className={styles.sectionHead}>
          <span>What it does</span>
          <h2>Everything your clone can handle.</h2>
          <p>Three connected surfaces for knowledge, communications and business workflows.</p>
        </div>
        <div className={styles.moduleGrid}>
          {modules.map(([label, title, description], index) => (
            <article className={styles.moduleCard} data-testid="capability-card" key={label}>
              <span className={styles.moduleIcon}>{String(index + 1).padStart(2, "0")}</span>
              <p className={styles.moduleLabel}>{label}</p>
              <h3>{title}</h3>
              <p>{description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className={styles.simulator} id="simulator">
        <div className={styles.simulatorHead}>
          <div><span>MYOWNCLONE SIMULATOR</span><h2>See the clone workspace in action.</h2></div>
          <Link className={styles.secondaryCta} href="/login">Open your workspace</Link>
        </div>
        <div className={styles.workspaceGrid}>
          <article><h3>Knowledge</h3><p>Documents, memories and context ready for accurate answers.</p><span>Source library</span></article>
          <article><h3>Conversations</h3><p>Recent interactions remain visible so your team keeps context.</p><span>Live activity</span></article>
          <article><h3>Automation</h3><p>Inbox triage, products and bookings become repeatable actions.</p><span>Workflow ready</span></article>
        </div>
      </section>

      <section className={styles.process} id="process">
        <div className={styles.sectionHead}>
          <span>How it works</span>
          <h2>Four steps to your clone.</h2>
        </div>
        <ol className={styles.processGrid}>
          {steps.map(([number, title, description]) => <li data-testid="process-step" key={number}><span>{number}</span><h3>{title}</h3><p>{description}</p></li>)}
        </ol>
      </section>

      <section className={styles.pricing} id="plans">
        <div className={styles.sectionHead}>
          <span>Pricing</span>
          <h2>The same pricing inside and outside.</h2>
          <p>Landing and dashboard read from the same public pricing model.</p>
        </div>
        <PublicPricing mode="landing" />
      </section>

      <section className={styles.technology} aria-label="Technology powering MyOwnClone">
        <p>Technology powering MyOwnClone</p>
        <div>{technologies.map((technology) => <span data-testid="technology-wordmark" key={technology}>{technology}</span>)}</div>
      </section>

      <section className={styles.finalCta}>
        <div><h2>Ready to clone yourself?</h2><p>Start publicly, continue in the dashboard and keep one consistent story from the first visit to billing.</p></div>
        <Link className={styles.primaryCta} href="/registro">Start building your clone <span aria-hidden="true"><ArrowUpRight size={18} weight="bold" /></span></Link>
      </section>

      <footer className={styles.footer}>
        <span><AnimatedLogoMark forceMotion size={20} /> © 2026 MyOwnClone</span>
        <div><Link href="/legal">Legal</Link><a href="/docs">Docs</a><a href="mailto:hello@myownclone.com">Contact</a></div>
      </footer>
    </main>
  );
}
