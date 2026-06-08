"use client";

import { useState } from "react";
import { Modal } from "@/components/ui/Modal";

interface ImpersonateButtonProps {
  tenantId: string;
  tenantName: string;
  onImpersonated?: (token: string, expiresAt: string) => void;
}

const REASON_MIN = 10;
const REASON_MAX = 1000;

export function ImpersonateButton({
  tenantId,
  tenantName,
  onImpersonated,
}: ImpersonateButtonProps) {
  const [open, setOpen] = useState(false);
  const [reason, setReason] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<{
    token: string;
    expires_at: string;
  } | null>(null);

  const reasonTrimmed = reason.trim();
  const reasonValid =
    reasonTrimmed.length >= REASON_MIN && reasonTrimmed.length <= REASON_MAX;

  function reset() {
    setReason("");
    setError(null);
    setResult(null);
    setSubmitting(false);
  }

  function close() {
    setOpen(false);
    reset();
  }

  async function submit() {
    if (!reasonValid) return;
    setSubmitting(true);
    setError(null);
    try {
      const res = await fetch("/api/admin/impersonate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tenant_id: tenantId, reason: reasonTrimmed }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.message ?? `Error ${res.status}`);
      }
      const data = await res.json();
      setResult({ token: data.token, expires_at: data.expires_at });
      onImpersonated?.(data.token, data.expires_at);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Error");
    } finally {
      setSubmitting(false);
    }
  }

  async function copyToken() {
    if (!result) return;
    try {
      await navigator.clipboard.writeText(result.token);
    } catch {
      // Clipboard API may be unavailable in some browsers; ignore.
    }
  }

  return (
    <>
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="btn-primary text-xs"
      >
        Impersonar
      </button>

      <Modal
        open={open}
        onClose={close}
        title={`Impersonar a ${tenantName}`}
        size="md"
        footer={
          result ? (
            <button
              type="button"
              onClick={close}
              className="btn-secondary text-xs"
            >
              Cerrar
            </button>
          ) : (
            <>
              <button
                type="button"
                onClick={close}
                className="btn-secondary text-xs"
                disabled={submitting}
              >
                Cancelar
              </button>
              <button
                type="button"
                onClick={submit}
                className="btn-primary text-xs disabled:opacity-40"
                disabled={!reasonValid || submitting}
              >
                {submitting ? "Generando…" : "Iniciar impersonación"}
              </button>
            </>
          )
        }
      >
        {!result ? (
          <div className="space-y-3">
            <p className="text-xs text-[var(--text-muted)]">
              La impersonación expira en 30 minutos. El token se muestra una
              sola vez y queda registrado en el audit log.
            </p>
            <label className="block">
              <span className="stat-label">Razón (obligatorio)</span>
              <textarea
                value={reason}
                onChange={(e) => setReason(e.target.value)}
                rows={3}
                placeholder="Describe el motivo del soporte…"
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
              />
              <span className="mt-1 block text-[10px] text-[var(--text-muted)]">
                {reasonTrimmed.length} / {REASON_MAX} caracteres (mínimo{" "}
                {REASON_MIN})
              </span>
            </label>
            {error && (
              <p className="text-xs text-red-600" role="alert">
                {error}
              </p>
            )}
          </div>
        ) : (
          <div className="space-y-3">
            <p className="text-xs text-[var(--text-muted)]">
              Copia este token. Caduca el{" "}
              <span className="font-mono text-[var(--text-primary)]">
                {new Date(result.expires_at).toLocaleString("es-ES")}
              </span>
              .
            </p>
            <div className="flex items-center gap-2">
              <code className="flex-1 break-all rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 font-mono text-[11px] text-[var(--text-primary)]">
                {result.token}
              </code>
              <button
                type="button"
                onClick={copyToken}
                className="btn-secondary text-xs shrink-0"
              >
                Copiar
              </button>
            </div>
            <p className="text-[10px] text-[var(--text-muted)]">
              Envíalo como header <code>X-Impersonate-Token</code> en tus
              siguientes requests.
            </p>
          </div>
        )}
      </Modal>
    </>
  );
}
