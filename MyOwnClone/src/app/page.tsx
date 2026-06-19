"use client";

import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import LandingBehavior from "@/components/ui/LandingBehavior";
import TubesBackground from "@/components/ui/neon-flow";
import PublicPricing from "@/components/ui/PublicPricing";
import { Link } from "@/i18n/navigation";
import { useTranslations } from "next-intl";

const steps = [
  ["01", "stepSignUp", "stepSignUpDesc"],
  ["02", "stepConfigure", "stepConfigureDesc"],
  ["03", "stepTrain", "stepTrainDesc"],
  ["04", "stepDeploy", "stepDeployDesc"],
] as const;

const serviceKeys = [
  { label: "overviewLabel", title: "overviewTitle", desc: "overviewDesc" },
  { label: "knowledgeLabel", title: "knowledgeTitle", desc: "knowledgeDesc" },
  { label: "automationLabel", title: "automationTitle", desc: "automationDesc" },
] as const;

export default function LandingPage() {
  const t = useTranslations("landing");

  return (
    <TubesBackground className="moc-local-landing">
      <main className="moc-local-landing" style={{ background: "transparent" }}>
      <LandingBehavior />

      <nav className="nav" style={{ borderBottom: "none" }}>
        <Link href="/" className="nav-logo" aria-label="MyOwnClone home">
          <AnimatedLogoMark size={26} forceMotion />
          <span>MyOwnClone</span>
        </Link>

        <div className="nav-links">
          <a href="#services">{t("navServices")}</a>
          <a href="#process">{t("navProcess")}</a>
          <a href="#plans">{t("navPlans")}</a>
        </div>

        <div className="nav-actions">
          <Link className="nav-signin" href="/login">
            {t("navSignIn")}
          </Link>
          <Link className="nav-cta" href="/beta">
            {t("navCta")}
          </Link>
        </div>
      </nav>

      <section className="hero" id="hero" style={{ borderBottom: "none" }}>
        <div className="hero-content">
          <div className="flex justify-center mb-6 reveal">
            <AnimatedLogoMark size={120} forceMotion />
          </div>
          <span className="hero-kicker reveal">{t("heroKicker")}</span>
          <h1 className="reveal">
            {t("heroTitleLine1")}
            <br />
            <span className="accent">{t("heroTitleLine2")}</span>
          </h1>
          <p className="hero-sub reveal">{t("heroSub")}</p>
          <div className="hero-ctas reveal">
            <Link className="btn btn-primary" href="/beta">
              {t("heroCta")}
            </Link>
            <Link className="btn btn-secondary" href="/login">
              {t("heroSignIn")}
            </Link>
          </div>
        </div>
      </section>

      <section className="section" id="services" style={{ borderBottom: "none" }}>
        <div className="sec-head">
          <span className="sec-kicker reveal">{t("servicesKicker")}</span>
          <h2 className="sec-title reveal">{t("servicesTitle")}</h2>
          <p className="sec-desc reveal">{t("servicesDesc")}</p>
        </div>
        <div className="services-grid">
          {serviceKeys.map((svc) => (
            <article className="service-card reveal" key={svc.label}>
              <span className="service-label">{t(svc.label)}</span>
              <h3>{t(svc.title)}</h3>
              <p>{t(svc.desc)}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section process-section" id="process" style={{ borderBottom: "none" }}>
        <div className="sec-head">
          <span className="sec-kicker reveal">{t("processKicker")}</span>
          <h2 className="sec-title reveal">{t("processTitle")}</h2>
          <p className="sec-desc reveal">{t("processDesc")}</p>
        </div>
        <div className="process-grid">
          {steps.map(([number, titleKey, descKey]) => (
            <article className="process-step reveal" key={number}>
              <div className="step-num">{number}</div>
              <h3>{t(titleKey)}</h3>
              <p>{t(descKey)}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section" id="plans" style={{ borderBottom: "none" }}>
        <div className="sec-head">
          <span className="sec-kicker reveal">{t("plansKicker")}</span>
          <h2 className="sec-title reveal">{t("plansTitle")}</h2>
          <p className="sec-desc reveal">{t("plansDesc")}</p>
        </div>
        <PublicPricing mode="landing" />
      </section>

      <section className="cta-final" id="cta" style={{ borderBottom: "none" }}>
        <h2 className="reveal">
          {t("ctaTitleLine1")}
          <br />
          {t("ctaTitleLine2")}
        </h2>
        <p className="reveal">{t("ctaDesc")}</p>
        <div className="hero-ctas reveal">
          <Link className="btn btn-primary" href="/beta">
            {t("ctaCta")}
          </Link>
          <Link className="btn btn-secondary" href="/login">
            {t("ctaSignIn")}
          </Link>
        </div>
      </section>

      <footer className="footer">
        <span className="footer-brand">
          <AnimatedLogoMark size={20} forceMotion />
          &copy; 2026 MyOwnClone
        </span>
        <div className="footer-links">
          <Link href="/legal">{t("footerLegal")}</Link>
          <a href="/docs">{t("footerDocs")}</a>
          <a href="mailto:hello@myownclone.com">{t("footerContact")}</a>
        </div>
      </footer>
    </main>
    </TubesBackground>
  );
}
