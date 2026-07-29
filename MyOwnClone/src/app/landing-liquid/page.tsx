import type { Metadata } from "next";
import { ArrowUpRight, CheckCircle, Sparkle, StackSimple } from "@phosphor-icons/react/dist/ssr";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import PublicPricing from "@/components/ui/PublicPricing";
import { Link } from "@/i18n/navigation";
import { LiquidOrb } from "./_components/LiquidOrb";
import { liquidPricingComparison, liquidPricingCopy, liquidPricingPlans } from "./content";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "MyOwnClone | Clon digital que trabaja contigo",
  description: "Convierte tu conocimiento en un clon digital para responder, enseñar y automatizar sin perder tu voz.",
};

const capabilities = [
  ["Visión completa", "Controla actividad, conversaciones, uso y señales comerciales desde un solo espacio."],
  ["Conocimiento que responde", "Organiza documentos y contexto para que cada respuesta mantenga tu criterio."],
  ["Automatización con voz propia", "Coordina bandeja, productos y reservas con flujos repetibles y humanos."],
] as const;

const processSteps = [
  ["01", "Crea tu espacio", "Abre tu cuenta y elige el punto de partida que mejor encaja contigo."],
  ["02", "Define tu clon", "Configura nombre, idioma, tono y las reglas que sostienen cada respuesta."],
  ["03", "Enséñale contexto", "Carga conocimiento y memoria para que responda con precisión."],
  ["04", "Ponlo a trabajar", "Publica tu clon para acompañar soporte, ventas o formación todo el día."],
] as const;

const technologies = ["Next.js", "Flask", "PostgreSQL", "Redis", "Ollama"] as const;

export default function LiquidLandingPage() {
  return (
    <main className={styles.page} lang="es">
      <div className={styles.ambient} aria-hidden="true" />
      <nav aria-label="Navegación principal" className={styles.nav}>
        <Link aria-label="Inicio de MyOwnClone" className={styles.brand} href="/">
          <span aria-hidden="true"><AnimatedLogoMark forceMotion size={26} /></span>
          <span>MyOwnClone</span>
        </Link>
        <div className={styles.navLinks}>
          <a href="#capacidades">Capacidades</a>
          <a href="#proceso">Proceso</a>
          <a href="#precios">Precios</a>
        </div>
        <div className={styles.navActions}>
          <Link className={styles.signIn} href="/login">Entrar</Link>
          <Link className={styles.navCta} href="/registro">Crear clon <ArrowUpRight aria-hidden="true" size={16} weight="bold" /></Link>
        </div>
      </nav>

      <section className={styles.hero} id="inicio">
        <div className={styles.heroCopy}>
          <p className={styles.eyebrow}><Sparkle aria-hidden="true" size={16} weight="fill" /> Clones digitales que conservan tu criterio</p>
          <h1>Trabaja con más inteligencia, avanza más rápido.</h1>
          <p className={styles.heroLead}>Convierte conocimiento, conversaciones y procesos en un clon digital que acompaña a tu equipo cada día.</p>
          <div className={styles.heroActions}>
            <Link className={styles.primaryCta} href="/registro">Empezar ahora <span aria-hidden="true"><ArrowUpRight size={18} weight="bold" /></span></Link>
            <Link className={styles.secondaryCta} href="/login">Ver mi espacio</Link>
          </div>
        </div>
        <div className={styles.orbFrame}>
          <LiquidOrb />
          <div className={styles.orbCaption}><StackSimple aria-hidden="true" size={18} weight="duotone" /><span>RAG, embeddings locales y automatización en una sola capa.</span></div>
        </div>
      </section>

      <section aria-label="Tecnología de MyOwnClone" className={styles.techStrip}>
        <p>Tecnología que ya impulsa MyOwnClone</p>
        <div>{technologies.map((technology) => <span data-testid="technology-wordmark" key={technology}>{technology}</span>)}</div>
      </section>

      <section className={styles.section} id="capacidades">
        <div className={styles.sectionHeading}>
          <p className={styles.eyebrow}>Capacidades</p>
          <h2>Un clon que entiende el trabajo que ya haces.</h2>
        </div>
        <div className={styles.capabilityGrid}>
          {capabilities.map(([title, description], index) => (
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
          <p className={styles.eyebrow}>Proceso</p>
          <h2>De tu experiencia a una conversación útil en cuatro pasos.</h2>
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
          <p className={styles.eyebrow}>Planes</p>
          <h2>Precios claros para empezar.</h2>
          <p>Los mismos planes y rutas que ya están disponibles en MyOwnClone.</p>
        </div>
        <div className={styles.pricingWrap}>
          <PublicPricing
            comparison={liquidPricingComparison}
            copy={liquidPricingCopy}
            mode="landing"
            plans={liquidPricingPlans}
          />
        </div>
      </section>

      <section className={styles.finalCta}>
        <div><CheckCircle aria-hidden="true" size={28} weight="fill" /><h2>Tu conocimiento ya hace el trabajo difícil.</h2><p>Haz que tu clon lo convierta en respuestas y acciones consistentes.</p></div>
        <Link className={styles.primaryCta} href="/registro">Crear mi clon <span aria-hidden="true"><ArrowUpRight size={18} weight="bold" /></span></Link>
      </section>

      <footer className={styles.footer}>
        <span className={styles.footerBrand}><span aria-hidden="true"><AnimatedLogoMark size={20} /></span> MyOwnClone</span>
        <div><Link href="/legal">Legal</Link><a href="/docs">Documentación</a><a href="mailto:hello@myownclone.com">Contacto</a></div>
      </footer>
    </main>
  );
}
