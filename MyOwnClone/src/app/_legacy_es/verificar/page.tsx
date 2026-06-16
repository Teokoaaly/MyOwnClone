"use client";

import { useEffect, useState, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { Link, useRouter } from "@/i18n/navigation";

type Status = "verifying" | "success" | "invalid" | "missing";

function VerifyContent() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const token = searchParams.get("token") ?? "";
  const email = searchParams.get("email") ?? "";
  const [status, setStatus] = useState<Status>(token ? "verifying" : "missing");
  const [message, setMessage] = useState(
    token ? "Verificando tu correo…" : "Falta el token de verificación.",
  );

  useEffect(() => {
    if (!token) {
      setStatus("missing");
      setMessage("Falta el token de verificación.");
      return;
    }
    let cancelled = false;
    (async () => {
      try {
        const res = await fetch("/api/auth/verify-email", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ token, email }),
        });
        if (cancelled) return;
        if (res.ok) {
          setStatus("success");
          setMessage("Tu correo ha sido verificado. Redirigiendo…");
          setTimeout(() => router.push("/login"), 1500);
        } else {
          const data = await res.json().catch(() => ({}));
          setStatus("invalid");
          setMessage(data.error ?? "El enlace no es válido o ha caducado.");
        }
      } catch {
        if (cancelled) return;
        setStatus("invalid");
        setMessage("Error de conexión. Inténtalo de nuevo.");
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [token, email, router]);

  return (
    <div className="w-full max-w-md card text-center">
      <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
        {status === "success"
          ? "Correo verificado"
          : status === "invalid" || status === "missing"
            ? "Enlace no válido"
            : "Verificando…"}
      </h1>
      <p className="mt-2 text-sm text-[var(--text-muted)]">{message}</p>
      {email && (
        <p className="mt-4 text-sm text-[var(--text-secondary)] bg-[var(--surface-2)] rounded-lg py-2 px-4">
          Cuenta: <strong className="text-[var(--text-primary)]">{email}</strong>
        </p>
      )}
      <div className="mt-6 flex flex-col items-center gap-2">
        <Link href="/login" className="btn-primary text-sm inline-block">
          Ir a iniciar sesión
        </Link>
        {status === "invalid" || status === "missing" ? (
          <Link
            href="/registro"
            className="text-xs text-[var(--text-muted)] underline underline-offset-4 hover:text-[var(--text-primary)]"
          >
            Volver a registrarse
          </Link>
        ) : null}
      </div>
    </div>
  );
}

export default function VerificarPage() {
  return (
    <main
      className="flex min-h-screen flex-col items-center justify-center px-4"
      style={{ background: "var(--bg-page)" }}
    >
      <Suspense
        fallback={
          <div className="text-sm text-[var(--text-muted)]">Cargando…</div>
        }
      >
        <VerifyContent />
      </Suspense>
    </main>
  );
}
