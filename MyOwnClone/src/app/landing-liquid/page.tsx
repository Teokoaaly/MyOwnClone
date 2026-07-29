import type { Metadata } from "next";
import { ArrowUpRight, CheckCircle, Sparkle } from "@phosphor-icons/react/dist/ssr";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import PublicPricing from "@/components/ui/PublicPricing";
import { Link } from "@/i18n/navigation";
import { CloneSimulator } from "./_components/CloneSimulator";
import { LiquidOrb } from "./_components/LiquidOrb";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "MyOwnClone | Clon digital con IA",
  description: "Crea un clon de IA que trabaje para ti.",
};

const modules = [
  ["Resumen", "Panel en tiempo real", "Supervisa la actividad del clon, las interacciones recientes y las métricas clave de un vistazo."],
  ["Biblioteca y memoria", "Conocimiento estructurado", "Sube documentos, crea bases de conocimiento y guarda memorias para respuestas más ricas."],
  ["Buzón y ventas", "Buzón impulsado por IA", "Clasifica intención, sugiere respuestas y recomienda productos sin perder el tono de tu marca."],
] as const;

const steps = [
  ["01", "Regístrate", "Crea tu cuenta y elige un plan. Gratis para empezar."],
  ["02", "Configura", "Nombra tu clon y establece personalidad, tono e idioma."],
  ["03", "Entrena", "Sube documentos y añade memorias para que responda con tu contexto."],
  ["04", "Despliega", "Publica el chat y comparte un asistente que funciona 24/7."],
] as const;

export default function LiquidLandingPage() {
  return (
    <main className={styles.page} lang="es">
      <div className={styles.ambient} aria-hidden="true" />
      <header className={styles.header}>
        <nav aria-label="Navegación principal" className={styles.nav}>
          <Link aria-label="Inicio de MyOwnClone" className={styles.brand} href="/">
            <AnimatedLogoMark forceMotion size={28} />
            <span>MyOwnClone</span>
          </Link>
          <div className={styles.navLinks}>
            <a href="#services">Servicios</a><a href="#process">Proceso</a><a href="#plans">Planes</a><a href="#demo">Demo en vivo</a>
          </div>
          <div className={styles.navActions}>
            <span className={styles.language} aria-label="Idioma"><b>ES</b><span>EN</span></span>
            <Link className={styles.signIn} href="/login">Iniciar sesión</Link>
            <Link className={styles.navCta} href="/registro">Empezar <ArrowUpRight aria-hidden="true" size={16} weight="bold" /></Link>
          </div>
        </nav>
      </header>

      <section className={styles.hero} id="hero">
        <div className={styles.heroLogo} aria-hidden="true"><AnimatedLogoMark forceMotion size={92} /></div>
        <p className={styles.kicker}><Sparkle aria-hidden="true" size={15} weight="fill" /> Clon digital con inteligencia artificial</p>
        <h1>Crea un clon de IA que <span>trabaje para ti.</span></h1>
        <p className={styles.heroDescription}>Entrena un asistente de IA con tu conocimiento, personalidad y datos de negocio. Gestiona emails, recomienda productos y atiende clientes 24/7.</p>
        <div className={styles.heroActions}>
          <Link className={styles.primaryCta} href="/registro">Empieza gratis <span aria-hidden="true"><ArrowUpRight size={18} weight="bold" /></span></Link>
          <Link className={styles.secondaryCta} href="/login">Iniciar sesión</Link>
        </div>
        <div className={styles.valueProps}><span><CheckCircle aria-hidden="true" size={15} weight="fill" /> Gratis para empezar</span><span><CheckCircle aria-hidden="true" size={15} weight="fill" /> Configuración en minutos</span><span><CheckCircle aria-hidden="true" size={15} weight="fill" /> Disponible 24/7</span></div>
        <div className={styles.orbFrame}><LiquidOrb /></div>
      </section>

      <section className={styles.modules} id="services">
        <div className={styles.sectionHead}><span>Qué hace</span><h2>Todo lo que tu clon puede gestionar.</h2><p>Tres módulos trabajando juntos para gestionar conocimiento, comunicaciones y ventas en un solo espacio.</p></div>
        <div className={styles.moduleGrid}>{modules.map(([label, title, description], index) => <article className={styles.moduleCard} data-testid="capability-card" key={label}><span className={styles.moduleIcon}>{String(index + 1).padStart(2, "0")}</span><p className={styles.moduleLabel}>{label}</p><h3>{title}</h3><p>{description}</p></article>)}</div>
      </section>

      <section className={styles.demoSection} id="demo"><div className={styles.sectionHead}><span>Demo en vivo</span><h2>Prueba las capacidades de tu clon de IA.</h2><p>Explora cómo conecta preguntas, conocimiento y automatización.</p></div><CloneSimulator /></section>

      <section className={styles.process} id="process"><div className={styles.sectionHead}><span>Cómo funciona</span><h2>Cuatro pasos para tu clon.</h2><p>Desde el registro hasta un asistente en vivo, en minutos y no semanas.</p></div><ol className={styles.processGrid}>{steps.map(([number, title, description]) => <li data-testid="process-step" key={number}><span>{number}</span><h3>{title}</h3><p>{description}</p></li>)}</ol></section>

      <section className={styles.pricing} id="plans"><div className={styles.sectionHead}><span>Precios</span><h2>Elige tu plan.</h2><p>Empieza gratis y escala a medida que crece tu clon.</p></div><PublicPricing mode="landing" /></section>

      <section className={styles.technology} aria-label="Tecnología que ya impulsa MyOwnClone"><p>Tecnología que ya impulsa MyOwnClone</p><div>{["Next.js", "Flask", "PostgreSQL", "Redis", "Ollama"].map((technology) => <span data-testid="technology-wordmark" key={technology}>{technology}</span>)}</div></section>
      <section className={styles.finalCta}><div><h2>¿Listo para clonarte <span>a ti mismo?</span></h2><p>Construye un asistente que escala tu conocimiento y automatiza conversaciones sin perder tu voz.</p></div><Link className={styles.primaryCta} href="/registro">Empieza a construir tu clon <span aria-hidden="true"><ArrowUpRight size={18} weight="bold" /></span></Link></section>
      <footer className={styles.footer}><span><AnimatedLogoMark forceMotion size={20} /> © 2026 MyOwnClone</span><div><Link href="/legal">Legal</Link><a href="/docs">Documentación</a><a href="mailto:hello@myownclone.com">Contacto</a></div></footer>
    </main>
  );
}
