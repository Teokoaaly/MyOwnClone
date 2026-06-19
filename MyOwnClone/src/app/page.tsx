"use client";

import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import LandingBehavior from "@/components/ui/LandingBehavior";
import PublicPricing from "@/components/ui/PublicPricing";
import TubesBackground from "@/components/ui/neon-flow";
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
    <TubesBackground className="moc-local-landing" enableClickInteraction>
      <LandingBehavior />

      <nav className="nav" style={{ borderBottom: "none", background: "rgba(10,10,10,0.85)", backdropFilter: "blur(12px)" }}>
        <Link href="/" className="nav-logo" aria-label="MyOwnClone home" style={{ color: "#fff" }}>
          <AnimatedLogoMark size={26} forceMotion />
          <span>MyOwnClone</span>
        </Link>

        <div className="nav-links">
          <a href="#services" style={{ color: "rgba(255,255,255,0.7)" }}>{t("navServices")}</a>
          <a href="#process" style={{ color: "rgba(255,255,255,0.7)" }}>{t("navProcess")}</a>
          <a href="#plans" style={{ color: "rgba(255,255,255,0.7)" }}>{t("navPlans")}</a>
        </div>

        <div className="nav-actions">
          <Link className="nav-signin" href="/login" style={{ color: "rgba(255,255,255,0.7)" }}>
            {t("navSignIn")}
          </Link>
          <Link className="nav-cta" href="/beta" style={{ background: "#ea580c", color: "#fff" }}>
            {t("navCta")}
          </Link>
        </div>
      </nav>

      <section className="hero" id="hero" style={{ borderBottom: "none", color: "#fff" }}>
        <div className="hero-content">
          <div className="flex justify-center mb-6 reveal">
            <AnimatedLogoMark size={120} forceMotion />
          </div>
          <span className="hero-kicker reveal" style={{ color: "#ea580c" }}>{t("heroKicker")}</span>
          <h1 className="reveal" style={{ color: "#fff" }}>
            {t("heroTitleLine1")}
            <br />
            <span className="accent" style={{ color: "#f97316" }}>{t("heroTitleLine2")}</span>
          </h1>
          <p className="hero-sub reveal" style={{ color: "rgba(255,255,255,0.65)" }}>{t("heroSub")}</p>
          <div className="hero-ctas reveal">
            <Link className="btn btn-primary" href="/beta">
              {t("heroCta")}
            </Link>
            <Link className="btn btn-secondary" href="/login" style={{ borderColor: "rgba(255,255,255,0.3)", color: "#fff", background: "rgba(255,255,255,0.08)" }}>
              {t("heroSignIn")}
            </Link>
          </div>
        </div>
      </section>

      <section className="section" id="services" style={{ borderBottom: "none", color: "#fff" }}>
        <div className="sec-head">
          <span className="sec-kicker reveal" style={{ color: "#ea580c" }}>{t("servicesKicker")}</span>
          <h2 className="sec-title reveal" style={{ color: "#fff" }}>{t("servicesTitle")}</h2>
          <p className="sec-desc reveal" style={{ color: "rgba(255,255,255,0.55)" }}>{t("servicesDesc")}</p>
        </div>
        <div className="services-grid">
          {serviceKeys.map((svc) => (
            <article className="service-card reveal" key={svc.label} style={{ background: "rgba(255,255,255,0.05)", borderColor: "rgba(255,255,255,0.08)", backdropFilter: "blur(12px)" }}>
              <span className="service-label" style={{ color: "#f97316" }}>{t(svc.label)}</span>
              <h3 style={{ color: "#fff" }}>{t(svc.title)}</h3>
              <p style={{ color: "rgba(255,255,255,0.55)" }}>{t(svc.desc)}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section process-section" id="process" style={{ borderBottom: "none", color: "#fff" }}>
        <div className="sec-head">
          <span className="sec-kicker reveal" style={{ color: "#ea580c" }}>{t("processKicker")}</span>
          <h2 className="sec-title reveal" style={{ color: "#fff" }}>{t("processTitle")}</h2>
          <p className="sec-desc reveal" style={{ color: "rgba(255,255,255,0.55)" }}>{t("processDesc")}</p>
        </div>
        <div className="process-grid">
          {steps.map(([number, titleKey, descKey]) => (
            <article className="process-step reveal" key={number} style={{ background: "rgba(255,255,255,0.05)", borderColor: "rgba(255,255,255,0.08)", backdropFilter: "blur(12px)" }}>
              <div className="step-num">{number}</div>
              <h3 style={{ color: "#fff" }}>{t(titleKey)}</h3>
              <p style={{ color: "rgba(255,255,255,0.55)" }}>{t(descKey)}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section" id="plans" style={{ borderBottom: "none", color: "#fff" }}>
        <div className="sec-head">
          <span className="sec-kicker reveal" style={{ color: "#ea580c" }}>{t("plansKicker")}</span>
          <h2 className="sec-title reveal" style={{ color: "#fff" }}>{t("plansTitle")}</h2>
          <p className="sec-desc reveal" style={{ color: "rgba(255,255,255,0.55)" }}>{t("plansDesc")}</p>
        </div>
        <PublicPricing mode="landing" />
      </section>

      <section className="cta-final" id="cta" style={{ borderBottom: "none", color: "#fff" }}>
        <h2 className="reveal" style={{ color: "#fff" }}>
          {t("ctaTitleLine1")}
          <br />
          {t("ctaTitleLine2")}
        </h2>
        <p className="reveal" style={{ color: "rgba(255,255,255,0.65)" }}>{t("ctaDesc")}</p>
        <div className="hero-ctas reveal">
          <Link className="btn btn-primary" href="/beta">
            {t("ctaCta")}
          </Link>
          <Link className="btn btn-secondary" href="/login" style={{ borderColor: "rgba(255,255,255,0.3)", color: "#fff", background: "rgba(255,255,255,0.08)" }}>
            {t("ctaSignIn")}
          </Link>
        </div>
      </section>

      <footer className="footer" style={{ color: "rgba(255,255,255,0.4)" }}>
        <span className="footer-brand">
          <AnimatedLogoMark size={20} forceMotion />
          &copy; 2026 MyOwnClone
        </span>
        <div className="footer-links">
          <Link href="/legal" style={{ color: "rgba(255,255,255,0.4)" }}>{t("footerLegal")}</Link>
          <a href="/docs" style={{ color: "rgba(255,255,255,0.4)" }}>{t("footerDocs")}</a>
          <a href="mailto:hello@myownclone.com" style={{ color: "rgba(255,255,255,0.4)" }}>{t("footerContact")}</a>
        </div>
      </footer>
    </TubesBackground>
  );
}
