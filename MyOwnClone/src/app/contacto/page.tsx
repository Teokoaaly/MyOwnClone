import type { Metadata } from "next";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { Link } from "@/i18n/navigation";

export const metadata: Metadata = {
  title: "Contacto | MyOwnClone",
  description: "Contacta con el equipo de MyOwnClone.",
};

export default function ContactPage() {
  return (
    <main className="min-h-screen bg-[var(--bg-page)] px-4 py-6 md:px-8 md:py-8">
      <section className="mx-auto flex min-h-[calc(100vh-4rem)] w-full max-w-5xl flex-col rounded-2xl border border-[var(--border-soft)] bg-white p-6 shadow-[0_18px_60px_rgba(15,23,42,0.06)] md:p-10">
        <nav className="flex items-center justify-between border-b border-[var(--border-soft)] pb-5">
          <Link href="/" className="inline-flex items-center gap-2 font-semibold">
            <AnimatedLogoMark size={22} />
            <span>MyOwnClone</span>
          </Link>
          <Link href="/" className="btn-secondary text-xs">
            Volver
          </Link>
        </nav>

        <div className="flex flex-1 items-center justify-center text-center">
          <div className="mx-auto max-w-2xl py-16">
            <p className="section-label mb-2">Contacto</p>
            <h1 className="text-3xl font-semibold text-[var(--text-primary)] md:text-4xl">
              Estamos a tu disposición
            </h1>
            <p className="mt-4 text-sm leading-6 text-[var(--text-secondary)] md:text-base">
              Para información general, soporte o consultas comerciales, contacta
              con nosotros por correo electrónico.
            </p>
            <a
              className="mt-8 inline-flex rounded-xl bg-blue-600 px-5 py-3 font-semibold text-white transition-colors hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
              href="mailto:info@myownclone.com"
            >
              info@myownclone.com
            </a>
          </div>
        </div>
      </section>
    </main>
  );
}
