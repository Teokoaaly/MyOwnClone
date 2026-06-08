import Link from "next/link";

export default function LandingPage() {
  return (
    <div
      className="min-h-screen flex flex-col"
      style={{
        background: `
          radial-gradient(circle at 12% 8%, rgba(249, 115, 22, 0.20), transparent 36%),
          radial-gradient(circle at 88% 90%, rgba(236, 72, 153, 0.16), transparent 36%),
          var(--bg-page)
        `,
      }}
    >
      <header className="w-full flex justify-center pt-6 px-6">
        <nav className="w-full max-w-5xl flex items-center justify-between rounded-full border border-[var(--border-soft)] bg-[var(--bg-shell)]/80 backdrop-blur-md px-6 py-3 shadow-[0_2px_16px_rgba(15,23,42,0.04)]">
          <Link href="/" className="flex items-center gap-2">
            <div className="h-7 w-7 rounded-lg bg-black text-white flex items-center justify-center text-[10px] font-bold">
              M
            </div>
            <span className="text-sm font-semibold text-[var(--text-primary)]">
              MyOwnClone
            </span>
          </Link>

          <div className="hidden md:flex items-center gap-6 text-sm text-[var(--text-secondary)]">
            <Link href="/login" className="hover:text-[var(--text-primary)] transition-colors">
              Producto
            </Link>
            <Link href="/login" className="hover:text-[var(--text-primary)] transition-colors">
              Precios
            </Link>
            <Link
              href="/registro"
              className="hover:text-[var(--text-primary)] transition-colors"
            >
              Empezar
            </Link>
          </div>

          <div className="flex items-center gap-2">
            <Link
              href="/login"
              className="rounded-full border border-[var(--border-soft)] px-4 py-1.5 text-sm font-medium text-[var(--text-primary)] hover:bg-[var(--surface-2)] transition-colors"
            >
              Iniciar sesión
            </Link>
            <Link
              href="/registro"
              className="rounded-full bg-black text-white px-4 py-1.5 text-sm font-medium hover:opacity-90 transition-opacity"
            >
              Crear cuenta
            </Link>
          </div>
        </nav>
      </header>

      <main className="flex-1 flex flex-col items-center text-center px-6 pt-20 pb-12">
        <span className="mb-6 inline-flex items-center gap-2 rounded-full border border-[var(--border-soft)] bg-[var(--bg-shell)] px-3 py-1 text-[11px] font-medium text-[var(--text-secondary)]">
          <span className="h-1.5 w-1.5 rounded-full bg-[var(--color-accent-green)]" />
          Disponible en beta cerrada
        </span>

        <h1 className="text-4xl md:text-5xl font-semibold text-[var(--text-primary)] tracking-tight max-w-3xl leading-[1.05]">
          Crea un clon de IA
          <br />
          que atiende como tú
        </h1>

        <p className="mt-5 text-base text-[var(--text-secondary)] max-w-xl leading-relaxed">
          Entrenado con tu contenido. Atiende consultas, responde correos y
          reserva reuniones 24/7 en tu propio tono.
        </p>

        <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
          <Link
            href="/registro"
            className="btn-primary text-sm"
          >
            Empezar gratis
          </Link>
          <Link
            href="/login"
            className="btn-secondary text-sm"
          >
            Ver demo
          </Link>
        </div>
      </main>

      <footer className="text-center py-6 text-xs text-[var(--text-muted)]">
        MyOwnClone — Clones de IA para infoproductores
      </footer>
    </div>
  );
}
