import type { Metadata } from "next";
import { ArrowUpRight, CheckCircle, Sparkle, StackSimple } from "@phosphor-icons/react/dist/ssr";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import PublicPricing from "@/components/ui/PublicPricing";
import { Link } from "@/i18n/navigation";
import { LiquidOrb } from "./_components/LiquidOrb";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "MyOwnClone | Clon digital que trabaja contigo",
  description: "Convierte tu conocimiento en un clon digital para responder, enseñar y automatizar sin perder tu voz.",
};

const capabilities = [
  ["Overview", "See your whole clone operation at a glance.", "Track activity, recent conversations, usage and commercial signals from one dashboard."],
  ["Knowledge", "Upload your content and teach the clone your way.", "Documents, creator memories and business context stay organized for richer answers."],
  ["Automation", "Handle inbox, products and bookings in one flow.", "Turn common support and sales work into repeatable actions without losing your tone."],
] as const;

const processSteps = [
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
      <nav aria-label="Navegación principal" className={styles.nav}>
        <Link aria-label="Inicio de MyOwnClone" className={styles.brand} href="/">
          <span aria-hidden="true"><AnimatedLogoMark forceMotion size={26} /></span>
          <span>MyOwnClone</span>
        </Link>
        <div className={styles.navLinks}>
          <a href="#capacidades">Services</a>
          <a href="#proceso">Process</a>
          <a href="#precios">Plans</a>
        </div>
        <div className={styles.navActions}>
          <Link className={styles.signIn} href="/login">Sign in</Link>
          <Link className={styles.navCta} href="/registro">Get started <ArrowUpRight aria-hidden="true" size={16} weight="bold" /></Link>
        </div>
      </nav>

      <section className={styles.hero} id="inicio">
        <div className={styles.heroCopy}>
          <p className={styles.eyebrow}><Sparkle aria-hidden="true" size={16} weight="fill" /> AI-Powered Digital Clone</p>
          <h1>Create an AI clone that works for you.</h1>
          <p className={styles.heroLead}>Train an AI assistant with your knowledge, personality and business data. Answer customers, guide leads and automate daily work without losing your voice.</p>
          <div className={styles.heroActions}>
            <Link className={styles.primaryCta} href="/registro">Get started free <span aria-hidden="true"><ArrowUpRight size={18} weight="bold" /></span></Link>
            <Link className={styles.secondaryCta} href="/login">Sign in</Link>
          </div>
        </div>
        <div className={styles.orbFrame}>
          <LiquidOrb />
          <div className={styles.orbCaption}><StackSimple aria-hidden="true" size={18} weight="duotone" /><span>Knowledge, conversations and automation in one workspace.</span></div>
        </div>
      </section>

      <section aria-label="Tecnología de MyOwnClone" className={styles.techStrip}>
        <p>Technology powering MyOwnClone</p>
        <div>{technologies.map((technology) => <span data-testid="technology-wordmark" key={technology}>{technology}</span>)}</div>
      </section>

      <section className={styles.section} id="capacidades">
        <div className={styles.sectionHeading}>
          <p className={styles.eyebrow}>What it does</p>
          <h2>Everything your clone can handle.</h2>
        </div>
        <div className={styles.capabilityGrid}>
          {capabilities.map(([, title, description], index) => (
            <article className={styles.capability} data-testid="capability-card" key={title}>
              <span>{String(index + 1).padStart(2, "0")}</span>
              <h3>{title}</h3>
              <p>{description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className={`${styles.section} ${styles.process}`} id="proceso">
        <div className={styles.sectionHeading}>
          <p className={styles.eyebrow}>How it works</p>
          <h2>Four steps to your clone.</h2>
        </div>
        <ol className={styles.processGrid}>
          {processSteps.map(([number, title, description]) => (
            <li data-testid="process-step" key={number}>
              <span>{number}</span><h3>{title}</h3><p>{description}</p>
            </li>
          ))}
        </ol>
      </section>

      <section className={`${styles.section} ${styles.pricingSection}`} id="precios">
        <div className={styles.sectionHeading}>
          <p className={styles.eyebrow}>Pricing</p>
          <h2>The same pricing inside and outside.</h2>
          <p>Landing and dashboard use the same public pricing model, tabs, toggle and comparison view.</p>
        </div>
        <div className={styles.pricingWrap}><PublicPricing mode="landing" /></div>
      </section>

      <section className={styles.finalCta}>
        <div><CheckCircle aria-hidden="true" size={28} weight="fill" /><h2>Ready to clone yourself?</h2><p>Start publicly, continue in the dashboard and keep one consistent story from the first visit to billing.</p></div>
        <Link className={styles.primaryCta} href="/registro">Start building your clone <span aria-hidden="true"><ArrowUpRight size={18} weight="bold" /></span></Link>
      </section>

      <footer className={styles.footer}>
        <span className={styles.footerBrand}><span aria-hidden="true"><AnimatedLogoMark size={20} /></span> MyOwnClone</span>
        <div><Link href="/legal">Legal</Link><a href="/docs">Documentación</a><a href="mailto:hello@myownclone.com">Contacto</a></div>
      </footer>
    </main>
  );
}
