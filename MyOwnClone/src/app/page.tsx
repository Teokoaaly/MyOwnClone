import Link from "next/link";
import type { CSSProperties } from "react";

const orbitApps = [
  {
    label: "S",
    className: "landing-app-slack",
    style: "left: 20%; top: 18%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><path d="M6 15a2 2 0 1 1-4 0 2 2 0 0 1 4 0z" fill="#E01E5A"/><path d="M8 15a2 2 0 1 1 4 0 2 2 0 0 1-4 0z" fill="#E01E5A"/><path d="M10 13V6a2 2 0 1 1 4 0v7a2 2 0 1 1-4 0z" fill="#36C5F0"/><path d="M10 8H6a2 2 0 1 1 0-4h4a2 2 0 1 1 0 4z" fill="#2EB67D"/></svg>`,
  },
  {
    label: "Z",
    className: "landing-app-zapier",
    style: "right: 20%; top: 18%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><path d="M12 2l3.2 6.8L22 12l-6.8 3.2L12 22l-3.2-6.8L2 12l6.8-3.2L12 2z" fill="#FF4A00"/><path d="M12 5l2.2 4.8L19 12l-4.8 2.2L12 19l-2.2-4.8L5 12l4.8-2.2L12 5z" fill="#fff"/></svg>`,
  },
  {
    label: "A",
    className: "landing-app-asterisk",
    style: "left: 10%; top: 36%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><rect x="2" y="2" width="9" height="9" rx="1.5" fill="#A855F7"/><rect x="13" y="2" width="9" height="9" rx="1.5" fill="#A855F7" opacity="0.6"/><rect x="2" y="13" width="9" height="9" rx="1.5" fill="#A855F7" opacity="0.6"/><rect x="13" y="13" width="9" height="9" rx="1.5" fill="#A855F7" opacity="0.3"/></svg>`,
  },
  {
    label: "aws",
    className: "landing-app-aws",
    style: "right: 10%; top: 36%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><path d="M12 3L5 9l2 2 5-5 5 5 2-2-7-6z" fill="#FF9900"/><path d="M5 15l7 6 7-6-2-2-5 5-5-5-2 2z" fill="#FF9900" opacity="0.7"/></svg>`,
  },
  {
    label: "M",
    className: "landing-app-meta",
    style: "left: 24%; top: 47%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" fill="#1877F2"/><path d="M16.5 10.5c0 3-2 5.5-4.5 6.5-2.5-1-4.5-3.5-4.5-6.5S9.5 5 12 5s4.5 2.5 4.5 5.5z" fill="white"/></svg>`,
  },
  {
    label: "F",
    className: "landing-app-framer",
    style: "right: 24%; top: 47%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><rect x="4" y="2" width="16" height="6" rx="1" fill="#0055FF"/><rect x="4" y="8" width="16" height="6" rx="1" fill="#0055FF" opacity="0.6"/><rect x="4" y="14" width="16" height="6" rx="1" fill="#0055FF" opacity="0.3"/></svg>`,
  },
  {
    label: "G",
    className: "landing-app-google",
    style: "left: 25%; bottom: 23%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><path d="M21.5 12.3c0-.5-.1-1-.2-1.5H12v3h5.5a5.2 5.2 0 0 1-2.3 3.4v2.8h3.7c2.2-2 3.6-5 3.6-7.7z" fill="#4285F4"/><path d="M12 22c3.2 0 5.8-1 7.7-2.8l-3.7-2.8c-1 .7-2.3 1.1-4 1.1-3 0-5.6-2-6.6-4.8H1.5v2.9C3.4 19.8 7.4 22 12 22z" fill="#34A853"/><path d="M5.4 14.7c-.2-.6-.3-1.2-.3-1.9s.1-1.3.3-1.9V8H1.5A12 12 0 0 0 0 12c0 2 .5 3.9 1.5 5.6l3.9-2.9z" fill="#FBBC05"/><path d="M12 5.5c1.8 0 3.3.6 4.5 1.7l3.4-3.4C17.8 2 15.2 1 12 1 7.4 1 3.4 3.2 1.5 6.4l3.9 2.9c1-2.8 3.6-3.8 6.6-3.8z" fill="#EA4335"/></svg>`,
  },
  {
    label: "C",
    className: "landing-app-clickup",
    style: "right: 6%; bottom: 36%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><path d="M12 2L2 8v2l10-6 10 6V8l-10-6zM2 14l10 6 10-6v2l-10 6-10-6v-2z" fill="#7B68EE"/><circle cx="12" cy="12" r="3" fill="white"/></svg>`,
  },
  {
    label: "A",
    className: "landing-app-airtable",
    style: "right: 18%; bottom: 22%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><path d="M12 3L3 8l3 2 6-3 6 3 3-2-9-5zM3 14l9 5 9-5-3-2-6 3-6-3-3 2z" fill="#FFBF00"/></svg>`,
  },
  {
    label: "M",
    className: "landing-app-mailchimp",
    style: "left: 6%; bottom: 36%;",
    svg: `<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" fill="#FFE01B"/><path d="M8 11c0-2 2-3.5 4-3.5s4 1.5 4 3.5" stroke="#333" stroke-width="1.5" fill="none"/><circle cx="9" cy="13" r="1" fill="#333"/><circle cx="15" cy="13" r="1" fill="#333"/></svg>`,
  },
];

export default function LandingPage() {
  return (
    <main className="landing-stage">
      <section className="landing-card">
        <nav className="landing-nav" aria-label="Main">
          <Link href="/" className="landing-brand" aria-label="MyOwnClone home">
            <span className="landing-brand-mark" aria-hidden="true">
              <span /><span /><span /><span />
            </span>
            <span>MyOwnClone</span>
          </Link>

          <div className="landing-menu">
            <Link href="/registro">Producto</Link>
            <Link href="/registro">
              Soluciones
              <span className="landing-chevron" aria-hidden="true">v</span>
            </Link>
            <Link href="/facturacion">Precios</Link>
            <Link href="/login">Acceder</Link>
          </div>

          <div className="landing-actions">
            <Link href="/login" className="landing-signin">
              Iniciar sesión
            </Link>
            <Link href="/registro" className="landing-contact">
              Crear cuenta
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
              key={`${app.label}-${app.className}`}
              className={`landing-app ${app.className}`}
              style={styleFromString(app.style)}
              dangerouslySetInnerHTML={{ __html: app.svg }}
            />
          ))}
        </div>

        <div className="landing-hero">
          <div className="landing-rating" aria-label="Ratings">
            <span className="landing-google">G</span>
            <span>4.6 Google</span>
            <span className="landing-star">★</span>
            <span>4.9 Trustpilot</span>
          </div>

          <h1>
            Crea un clon de IA
            <br />
            que atiende como tú
          </h1>

          <p>
            Entrena un clon con tu contenido. Atiende consultas, responde correos
            y reserva reuniones 24/7 en tu propio tono, en modo pedagogía, ventas y soporte.
          </p>

          <div className="landing-cta-row">
            <Link href="/registro" className="landing-primary">
              Empezar gratis
            </Link>
            <Link href="/login" className="landing-secondary">
              Ver demo
            </Link>
          </div>
        </div>
      </section>

      <footer className="landing-footer">
        <div className="landing-footer-inner">
          <div className="landing-footer-brand">
            <span className="landing-brand-mark" aria-hidden="true">
              <span /><span /><span /><span />
            </span>
            <span>MyOwnClone</span>
          </div>
          <div className="landing-footer-links">
            <Link href="/registro">Producto</Link>
            <Link href="/facturacion">Precios</Link>
            <Link href="/login">Contacto</Link>
            <Link href="/login">Aviso legal</Link>
          </div>
          <div className="landing-footer-copy">
            © 2026 MyOwnClone.com — Todos los derechos reservados
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
