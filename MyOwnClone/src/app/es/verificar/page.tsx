import Link from "next/link";

interface Props {
  searchParams: Promise<{ email?: string }>;
}

export default async function VerificarPage({ searchParams }: Props) {
  const { email } = await searchParams;

  return (
    <main
      className="flex min-h-screen flex-col items-center justify-center px-4"
      style={{ background: "var(--bg-page)" }}
    >
      <div className="w-full max-w-md card text-center">
        <div
          className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full"
          style={{ background: "var(--surface-2)" }}
        >
          <svg
            aria-hidden="true"
            className="h-8 w-8"
            style={{ color: "var(--color-accent-warm)" }}
          ***REMOVED***ll="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
            />
          </svg>
        </div>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Revisa tu email
        </h1>
        <p className="mt-2 text-sm text-[var(--text-muted)]">
          Te hemos enviado un enlace mágico para acceder a tu cuenta.
        </p>
        {email && (
          <p className="mt-4 text-sm text-[var(--text-secondary)] bg-[var(--surface-2)] rounded-lg py-2 px-4">
            Enviado a: <strong className="text-[var(--text-primary)]">{email}</strong>
          </p>
        )}
        <p className="mt-4 text-xs text-[var(--text-muted)]">
          Si no ves el email, revisa la carpeta de spam o{" "}
          <Link
            href="/login"
            className="font-medium text-[var(--text-primary)] underline decoration-[var(--color-accent-warm)] underline-offset-4 hover:text-[var(--color-accent-warm)]"
          >
            vuelve a intentarlo
          </Link>
          .
        </p>
        <Link href="/login" className="btn-primary text-sm mt-6 inline-block">
          Volver al inicio
        </Link>
      </div>
    </main>
  );
}
