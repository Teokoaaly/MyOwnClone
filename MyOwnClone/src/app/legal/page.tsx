import type { ReactNode } from "react";
import { Link } from "@/i18n/navigation";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { useTranslations } from "next-intl";

export default function LegalPage() {
  const t = useTranslations("legal");
  return (
    <main className="min-h-screen bg-[var(--bg-page)] px-4 py-6 md:px-8 md:py-8">
      <section className="mx-auto flex min-h-[calc(100vh-4rem)] w-full max-w-5xl flex-col rounded-2xl border border-[var(--border-soft)] bg-white p-6 shadow-[0_18px_60px_rgba(15,23,42,0.06)] md:p-10">
        <nav className="flex items-center justify-between border-b border-[var(--border-soft)] pb-5">
          <Link href="/" className="inline-flex items-center gap-2 font-semibold">
            <AnimatedLogoMark size={22} />
            <span>MyOwnClone</span>
          </Link>
          <Link href="/" className="btn-secondary text-xs">
            Back
          </Link>
        </nav>

        <div className="mt-10 max-w-3xl space-y-8">
          <header>
            <p className="section-label mb-2">{t("legal.legal")}</p>
            <h1 className="text-3xl font-semibold text-[var(--text-primary)]">
              Terms, privacy, and acceptable use
            </h1>
            <p className="mt-3 text-sm leading-6 text-[var(--text-secondary)]">
              This page is a production placeholder for the legal documents that
              should be reviewed with counsel before a public launch.
            </p>
          </header>

          <LegalBlock title={t("legal.terms_of_service")}>
            MyOwnClone provides tools to create and operate AI assistants trained
            on user-provided content. Users are responsible for the material they
            upload, the outputs they publish, and their compliance with applicable
            laws.
          </LegalBlock>

          <LegalBlock title="Privacy">
            Workspace content, account data, and operational logs are processed to
            provide the service, secure the platform, and improve reliability.
            Production deployments should connect this notice to the final data
            retention, subprocessors, and user rights policy.
          </LegalBlock>

          <LegalBlock title="Acceptable use">
            Do not use the service to impersonate people without authorization,
            process sensitive data without a lawful basis, or generate harmful,
            deceptive, or illegal content.
          </LegalBlock>
        </div>
      </section>
    </main>
  );
}

function LegalBlock({
  title,
  children,
}: {
  title: string;
  children: ReactNode;
}) {
  return (
    <section className="border-t border-[var(--border-soft)] pt-6">
      <h2 className="text-base font-semibold text-[var(--text-primary)]">
        {title}
      </h2>
      <p className="mt-2 text-sm leading-6 text-[var(--text-secondary)]">
        {children}
      </p>
    </section>
  );
}
