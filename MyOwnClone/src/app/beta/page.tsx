"use client";

import { useState, useEffect, Suspense } from "react";
import { signIn } from "next-auth/react";
import { useSearchParams } from "next/navigation";
import { useTranslations } from "next-intl";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { Link } from "@/i18n/navigation";

function BetaContent() {
  const t = useTranslations("landing");
  const searchParams = useSearchParams();
  const planFromUrl = searchParams.get("plan") ?? "";

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [plan, setPlan] = useState(planFromUrl);
  const [reason, setReason] = useState("");
  const [comment, setComment] = useState("");
  const [status, setStatus] = useState<"idle" | "sending" | "sent" | "error">("idle");

  useEffect(() => {
    if (planFromUrl) setPlan(planFromUrl);
  }, [planFromUrl]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!name || !email || !plan || !reason) return;
    setStatus("sending");
    try {
      const res = await fetch("/api/beta-access", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, reason: `${plan} — ${reason}`, comment }),
      });
      if (res.ok) {
        setStatus("sent");
      } else {
        setStatus("error");
      }
    } catch {
      setStatus("error");
    }
  }

  const inputStyle: React.CSSProperties = {
    width: "100%",
    padding: "10px 14px",
    borderRadius: "10px",
    border: "1px solid var(--border-soft, #e5e0dc)",
    background: "var(--surface-1, #fff)",
    fontSize: "0.9rem",
    outline: "none",
    boxSizing: "border-box",
  };

  if (status === "sent") {
    return (
      <div className="card reveal" style={{ maxWidth: 560, margin: "0 auto", textAlign: "center", padding: "2rem" }}>
        <p style={{ fontSize: "1.2rem", fontWeight: 600 }}>{t("betaSentTitle")}</p>
        <p style={{ color: "var(--text-muted)", marginTop: "0.5rem" }}>
          {t("betaSentDesc", { email: `<strong>${email}</strong>` })}
        </p>
      </div>
    );
  }

  return (
    <div className="reveal" style={{ maxWidth: 520, margin: "0 auto" }}>
      <div className="card" style={{ padding: "2rem" }}>
        <p style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "0.3rem" }}>
          {t("betaTitle")}
        </p>
        <p style={{ color: "var(--text-muted)", fontSize: "0.85rem", marginBottom: "1.5rem" }}>
          {t("betaDesc")}
        </p>

        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "0.9rem" }}>
          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              {t("betaNameLabel")}
            </label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder={t("betaNamePlaceholder")}
              style={inputStyle}
              required
            />
          </div>

          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              {t("betaEmailLabel")}
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder={t("betaEmailPlaceholder")}
              style={inputStyle}
              required
            />
          </div>

          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              {t("betaPlanLabel")}
            </label>
            <select
              value={plan}
              onChange={(e) => setPlan(e.target.value)}
              style={inputStyle}
              required
            >
              <option value="">{t("betaPlanPlaceholder")}</option>
              <option value="Free">{t("betaPlanFree")}</option>
              <option value="Pro">{t("betaPlanPro")}</option>
              <option value="Enterprise">{t("betaPlanEnterprise")}</option>
            </select>
          </div>

          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              {t("betaReasonLabel")}
            </label>
            <select
              value={reason}
              onChange={(e) => setReason(e.target.value)}
              style={inputStyle}
              required
            >
              <option value="">{t("betaReasonPlaceholder")}</option>
              <option value="Customer support automation">{t("betaReasonSupport")}</option>
              <option value="Sales & lead qualification">{t("betaReasonSales")}</option>
              <option value="Teaching & onboarding">{t("betaReasonTeaching")}</option>
              <option value="Personal AI assistant">{t("betaReasonPersonal")}</option>
              <option value="Curiosity / exploration">{t("betaReasonCuriosity")}</option>
              <option value="Other">{t("betaReasonOther")}</option>
            </select>
          </div>

          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              {t("betaCommentLabel")}{" "}
              <span style={{ color: "var(--text-muted)", fontWeight: 400 }}>{t("betaCommentOptional")}</span>
            </label>
            <textarea
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              placeholder={t("betaCommentPlaceholder")}
              rows={3}
              style={{ ...inputStyle, resize: "vertical" }}
            />
          </div>

          <button
            type="submit"
            disabled={status === "sending" || !name || !email || !plan || !reason}
            style={{
              padding: "12px 24px",
              borderRadius: "12px",
              background: status === "sending" ? "#999" : "linear-gradient(135deg, #1c1917, #292524)",
              color: "#fff",
              fontWeight: 600,
              fontSize: "0.95rem",
              border: "none",
              cursor: status === "sending" ? "wait" : "pointer",
              opacity: (!name || !email || !plan || !reason) ? 0.5 : 1,
            }}
          >
            {status === "sending" ? t("betaSending") : t("betaSubmit")}
          </button>

          {status === "error" && (
            <p style={{ color: "#dc2626", fontSize: "0.8rem", textAlign: "center" }}>
              {t("betaError")}
            </p>
          )}
        </form>

        <div style={{ marginTop: "1.5rem" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", marginBottom: "1rem" }}>
            <div style={{ flex: 1, height: "1px", background: "var(--border-soft, #e5e0dc)" }} />
            <span style={{ fontSize: "0.8rem", color: "var(--text-muted)", whiteSpace: "nowrap" }}>
              {t("betaOrContinue")}
            </span>
            <div style={{ flex: 1, height: "1px", background: "var(--border-soft, #e5e0dc)" }} />
          </div>

          <button
            type="button"
            onClick={() => signIn("google", { callbackUrl: "/resumen" })}
            style={{
              width: "100%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              gap: "0.5rem",
              padding: "10px 14px",
              borderRadius: "10px",
              border: "1px solid var(--border-soft, #e5e0dc)",
              background: "var(--surface-1, #fff)",
              cursor: "pointer",
              fontSize: "0.9rem",
              fontWeight: 500,
            }}
          >
            <svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z" />
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
            </svg>
            {t("betaGoogle")}
          </button>
        </div>
      </div>
    </div>
  );
}

export default function BetaPage() {
  const t = useTranslations("landing");

  return (
    <main
      className="flex min-h-screen flex-col items-center justify-center px-4 py-12"
      style={{ background: "var(--bg-page, #fafaf9)" }}
    >
      <Link href="/" className="inline-flex items-center gap-2 mb-8">
        <AnimatedLogoMark size={28} forceMotion />
        <span style={{ fontSize: "1.1rem", fontWeight: 700 }}>MyOwnClone</span>
      </Link>

      <Suspense fallback={<p style={{ color: "var(--text-muted)" }}>{t("betaLoading")}</p>}>
        <BetaContent />
      </Suspense>
    </main>
  );
}
