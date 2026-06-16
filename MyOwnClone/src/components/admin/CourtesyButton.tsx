"use client";

import { useState } from "react";
import { useTranslations } from "next-intl";
import { Modal } from "@/components/ui/Modal";

interface CourtesyButtonProps {
  onCreated?: (email: string) => void;
}

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;

export function CourtesyButton({ onCreated }: CourtesyButtonProps) {
  const t = useTranslations("admin.courtesy");
  void t;
  const tCommon = useTranslations("admin.common");
  const tValidation = useTranslations("validation");
  void tValidation;

  const [open, setOpen] = useState(false);
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [plan, setPlan] = useState("pro");
  const [durationDays, setDurationDays] = useState(30);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<{ tenant_id: string; trial_ends_at: string } | null>(null);

  const emailValid = EMAIL_RE.test(email.trim());
  const nameValid = name.trim().length >= 1;
  const formValid = emailValid && nameValid && !submitting;

  function reset() {
    setEmail("");
    setName("");
    setPlan("pro");
    setDurationDays(30);
    setError(null);
    setResult(null);
    setSubmitting(false);
  }

  function close() {
    setOpen(false);
    reset();
  }

  async function submit() {
    if (!formValid) return;
    setSubmitting(true);
    setError(null);
    try {
      const res = await fetch("/api/admin/courtesy", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email: email.trim(),
          name: name.trim(),
          plan,
          duration_days: durationDays,
        }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.message ?? `Error ${res.status}`);
      }
      const data = await res.json();
      setResult({ tenant_id: data.tenant_id, trial_ends_at: data.trial_ends_at });
      onCreated?.(email.trim());
    } catch (e) {
      setError(e instanceof Error ? e.message : tCommon("error"));
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <>
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="btn-primary text-xs"
      >
        {t("trigger")}
      </button>

      <Modal
        open={open}
        onClose={close}
        title={t("modalTitle")}
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
                disabled={!formValid}
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
              <span className="stat-label">{t("emailLabel")}</span>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder={t("emailPlaceholder")}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
              />
            </label>
            <label className="block">
              <span className="stat-label">{t("nameLabel")}</span>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder={t("namePlaceholder")}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
              />
            </label>
            <div className="grid grid-cols-2 gap-3">
              <label className="block">
                <span className="stat-label">{t("planLabel")}</span>
                <select
                  value={plan}
                  onChange={(e) => setPlan(e.target.value)}
                  className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
                >
                  <option value="free">{t("planOptions.free")}</option>
                  <option value="pro">{t("planOptions.pro")}</option>
                  <option value="enterprise">{t("planOptions.enterprise")}</option>
                </select>
              </label>
              <label className="block">
                <span className="stat-label">{t("durationLabel")}</span>
                <input
                  type="number"
                  min={1}
                  max={365}
                  value={durationDays}
                  onChange={(e) => setDurationDays(parseInt(e.target.value, 10) || 1)}
                  className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-white px-3 py-2 text-sm text-[var(--text-primary)] outline-none focus:border-[var(--color-accent-warm)]"
                />
              </label>
            </div>
            {error && (
              <p className="text-xs text-red-600" role="alert">
                {error}
              </p>
            )}
          </div>
        ) : (
          <div className="space-y-2 text-sm">
            <p className="text-[var(--text-primary)]">
              {t("successMessage")}
            </p>
            <p className="font-mono text-[11px] text-[var(--text-muted)]">
              {t("successId", { id: result.tenant_id })}
            </p>
            <p className="font-mono text-[11px] text-[var(--text-muted)]">
              {t("successTrial", {
                date: new Date(result.trial_ends_at).toLocaleString("en-US"),
              })}
            </p>
          </div>
        )}
      </Modal>
    </>
  );
}
