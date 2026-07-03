/**
 * UseCasesShowcase — sección de demos interactivas en el landing.
 *
 * Muestra 3 demos con icono + descripción + CTA que abre el chat embebido.
 * Similar a myclone.is (insurance-quoter, hvac-dispatch, restaurant)
 * pero con nuestros 3 clones demo: insurance, restaurant, teacher.
 */
"use client";

import { useState } from "react";

interface Demo {
  slug: string;
  title: string;
  description: string;
  icon: string;
  mode: "support" | "sales" | "teach";
}

const DEMOS: Demo[] = [
  {
    slug: "demo-insurance",
    title: "Cotizador de Seguros",
    description: "Pregúntale por tu vehículo y presupuesto. Calcula primas al instante.",
    icon: "🛡️",
    mode: "sales",
  },
  {
    slug: "demo-restaurant",
    title: "Host de Restaurante",
    description: "Reserva mesa, ve el menú o consulta horarios en lenguaje natural.",
    icon: "🍽️",
    mode: "support",
  },
  {
    slug: "demo-teacher",
    title: "Profesor de IA",
    description: "Aprende cualquier tema con explicaciones paso a paso y ejemplos.",
    icon: "🎓",
    mode: "teach",
  },
];

export function UseCasesShowcase() {
  const [openSlug, setOpenSlug] = useState<string | null>(null);

  return (
    <section className="py-20 bg-[var(--bg-page)]">
      <div className="max-w-6xl mx-auto px-6">
        <header className="text-center mb-12">
          <p className="text-xs uppercase tracking-wider text-[var(--color-accent-warm)] mb-2">
            Pruébalo en acción
          </p>
          <h2 className="text-3xl md:text-4xl font-bold text-[var(--text-primary)]">
            Tres clones demo, listos para usar
          </h2>
          <p className="mt-3 text-[var(--text-secondary)] max-w-2xl mx-auto">
            Cada demo es un clon real con conocimiento precargado. Haz clic para chatear.
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {DEMOS.map((demo) => (
            <DemoCard
              key={demo.slug}
              demo={demo}
              isOpen={openSlug === demo.slug}
              onToggle={() =>
                setOpenSlug(openSlug === demo.slug ? null : demo.slug)
              }
            />
          ))}
        </div>
      </div>
    </section>
  );
}

function DemoCard({
  demo,
  isOpen,
  onToggle,
}: {
  demo: Demo;
  isOpen: boolean;
  onToggle: () => void;
}) {
  return (
    <article className="bg-white rounded-2xl border border-[var(--border-soft)] overflow-hidden hover:shadow-md transition-shadow">
      <div className="p-6">
        <div className="text-5xl mb-3" aria-hidden="true">
          {demo.icon}
        </div>
        <h3 className="text-lg font-semibold text-[var(--text-primary)] mb-2">
          {demo.title}
        </h3>
        <p className="text-sm text-[var(--text-secondary)] mb-4">
          {demo.description}
        </p>
        <button
          onClick={onToggle}
          className="w-full px-4 py-2 rounded-lg bg-[var(--color-accent-warm)] text-white text-sm font-medium hover:opacity-90 transition-opacity"
        >
          {isOpen ? "Cerrar chat" : "Probar chat →"}
        </button>
      </div>

      {isOpen && (
        <div className="border-t border-[var(--border-soft)] p-4 bg-[var(--surface-2)]">
          <iframe
            src={`/embed/${demo.slug}?mode=${demo.mode}`}
            title={demo.title}
            className="w-full h-[480px] border-0 rounded-lg bg-white"
            loading="lazy"
          />
        </div>
      )}
    </article>
  );
}