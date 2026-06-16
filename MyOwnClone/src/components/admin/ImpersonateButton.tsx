"use client";

import { useState } from "react";
import { useTranslations } from "next-intl";
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
  const t = useTranslations("admin.impersonation");
  const tCommon = useTranslations("admin.common");

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
      setError(e instanceof Error ? e.message : tCommon("error"));
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
        {t("button")}
      </button>

      <Modal
        open={open}
        onClose={close}
        title={t("modalTitle", { name: tenantName })}
        size="md"
        footer={
          result ? (
            <button
              type="button"
              onClick={close}
              className="btn-secondary text-xs"
            >
              {tCommon("close")}
            </button>
          ) : (
            <>
              <button
                type="button"
                onClick={close}
                className="btn-secondary text-xs"
                disabled={submitting}
              >
                {tCommon("cancel")}
              </button>
              <button
                type="button"
                onClick={submit}
                className="btn-primary text-xs disabled:opacity-40"
                disabled={!reasonValid || submitting}
              >
                {submitting ? t("submitting") : t("submit")}
              </button>
            </>
          )
        }
      >
        {!result ? (
          <div className="space-y-3">
            <p className="text-xs text-[var(--text-muted)]">
              {t("modalHelp")}
            </p>
            <label className="block">
              <span className="stat-label">{t("reasonLabel")}</span>
              <textarea
                value={reason}
                onChange={(e) => setReason(e.target.value)}
                rows={3}
                placeholder={t("reasonPlaceholder")}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
              />
              <span className="mt-1 block text-[10px] text-[var(--text-muted)]">
                {t("charCount", {
                  current: reasonTrimmed.length,
                  max: REASON_MAX,
                  min: REASON_MIN,
                })}
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
              {t("resultHelp", {
                date: new Date(result.expires_at).toLocaleString("en-US"),
              })}
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
                {t("copy")}
              </button>
            </div>
            <p className="text-[10px] text-[var(--text-muted)]">
              {t("tokenHelp")}
            </p>
          </div>
        )}
      </Modal>
    </>
  );
}
