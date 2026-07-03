/**
 * Testimonials — sección de testimonios de usuarios.
 *
 * NOTA ÉTICA: no mostramos testimonios inventados. Cuando haya usuarios reales
 * con consentimiento, se añadiran aquí via un CMS o admin panel.
 *
 * Por ahora, la sección muestra un placeholder honesto invitando a ser el primero.
 */
"use client";

export function Testimonials() {
  return (
    <section className="py-16 bg-white">
      <div className="max-w-4xl mx-auto px-6 text-center">
        <p className="text-xs uppercase tracking-wider text-[var(--color-accent-violet)] mb-3">
          Testimonios
        </p>
        <h2 className="text-2xl md:text-3xl font-bold text-[var(--text-primary)] mb-4">
          Sé el primero en compartir tu experiencia
        </h2>
        <p className="text-[var(--text-secondary)] max-w-xl mx-auto mb-6">
          Estamos en fase beta con usuarios pioneros. Si MyOwnClone te ha ayudado,
          nos encantaría conocer tu historia y publicarla aquí (con tu permiso).
        </p>

        <a
          href="mailto:testimonials@myownclone.com?subject=Quiero%20compartir%20mi%20testimonio"
          className="inline-block px-6 py-3 rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] text-[var(--text-primary)] font-medium hover:bg-[var(--surface-3)] transition-colors"
        >
          Compartir mi testimonio →
        </a>

        <p className="mt-8 text-xs text-[var(--text-muted)]">
          Publicamos solo testimonios reales con consentimiento explicito.
        </p>
      </div>
    </section>
  );
}