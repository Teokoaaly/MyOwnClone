"use client";

import { useState, useEffect, Suspense } from "react";
import { signIn } from "next-auth/react";
import { useSearchParams } from "next/navigation";
import AnimatedLogoMark from "@/components/ui/AnimatedLogoMark";
import { Link } from "@/i18n/navigation";

function BetaContent() {
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
        <p style={{ fontSize: "1.2rem", fontWeight: 600 }}>Request sent</p>
        <p style={{ color: "var(--text-muted)", marginTop: "0.5rem" }}>
          We will review your request and get back to you at <strong>{email}</strong> within a few hours.
        </p>
      </div>
    );
  }

  return (
    <div className="reveal" style={{ maxWidth: 520, margin: "0 auto" }}>
      <div className="card" style={{ padding: "2rem" }}>
        <p style={{ fontSize: "1rem", fontWeight: 600, marginBottom: "0.3rem" }}>
          Beta mode
        </p>
        <p style={{ color: "var(--text-muted)", fontSize: "0.85rem", marginBottom: "1.5rem" }}>
          During beta, all features are free. Accounts are activated under personal supervision.
        </p>

        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "0.9rem" }}>
          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              Name
            </label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Your full name"
              style={inputStyle}
              required
            />
          </div>

          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              Email
            </label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="you@email.com"
              style={inputStyle}
              required
            />
          </div>

          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              Plan
            </label>
            <select
              value={plan}
              onChange={(e) => setPlan(e.target.value)}
              style={inputStyle}
              required
            >
              <option value="">Select a plan...</option>
              <option value="Free">Free — Starter</option>
              <option value="Pro">Pro — Most popular</option>
              <option value="Enterprise">Enterprise — Scale</option>
            </select>
          </div>

          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              Reason for beta access
            </label>
            <select
              value={reason}
              onChange={(e) => setReason(e.target.value)}
              style={inputStyle}
              required
            >
              <option value="">Select a reason...</option>
              <option value="Customer support automation">Customer support automation</option>
              <option value="Sales & lead qualification">Sales & lead qualification</option>
              <option value="Teaching & onboarding">Teaching & onboarding</option>
              <option value="Personal AI assistant">Personal AI assistant</option>
              <option value="Curiosity / exploration">Curiosity / exploration</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <div>
            <label style={{ display: "block", fontSize: "0.8rem", fontWeight: 500, marginBottom: "0.3rem" }}>
              Leave us a comment <span style={{ color: "var(--text-muted)", fontWeight: 400 }}>(optional)</span>
            </label>
            <textarea
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              placeholder="Tell us about your use case, team size, or what you want to build..."
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
            {status === "sending" ? "Sending..." : "Request access"}
          </button>

          {status === "error" && (
            <p style={{ color: "#dc2626", fontSize: "0.8rem", textAlign: "center" }}>
              Something went wrong. Please try again or email us directly at info.myownclone@gmail.com
            </p>
          )}
        </form>

        <div style={{ marginTop: "1.5rem" }}>
          <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", marginBottom: "1rem" }}>
            <div style={{ flex: 1, height: "1px", background: "var(--border-soft, #e5e0dc)" }} />
            <span style={{ fontSize: "0.8rem", color: "var(--text-muted)", whiteSpace: "nowrap" }}>
              or continue with
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
            Continue with Google
          </button>
        </div>
      </div>
    </div>
  );
}

export default function BetaPage() {
  return (
    <main
      className="flex min-h-screen flex-col items-center justify-center px-4 py-12"
      style={{ background: "var(--bg-page, #fafaf9)" }}
    >
      <Link href="/" className="inline-flex items-center gap-2 mb-8">
        <AnimatedLogoMark size={28} forceMotion />
        <span style={{ fontSize: "1.1rem", fontWeight: 700 }}>MyOwnClone</span>
      </Link>

      <Suspense fallback={<p style={{ color: "var(--text-muted)" }}>Loading...</p>}>
        <BetaContent />
      </Suspense>
    </main>
  );
}
