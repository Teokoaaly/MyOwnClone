"use client";

import { useState, useEffect } from "react";

interface BetaFormProps {
  selectedPlan?: string;
}

export default function BetaForm({ selectedPlan }: BetaFormProps) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [reason, setReason] = useState("");
  const [comment, setComment] = useState("");
  const [status, setStatus] = useState<"idle" | "sending" | "sent" | "error">("idle");

  useEffect(() => {
    if (selectedPlan) {
      setReason(selectedPlan);
    }
  }, [selectedPlan]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!name || !email || !reason) return;
    setStatus("sending");
    try {
      const res = await fetch("/api/beta-access", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, reason, comment }),
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
        <button
          onClick={() => setStatus("idle")}
          style={{
            marginTop: "1rem",
            padding: "8px 20px",
            borderRadius: "8px",
            border: "1px solid var(--border-soft)",
            background: "transparent",
            cursor: "pointer",
            fontSize: "0.85rem",
          }}
        >
          Send another
        </button>
      </div>
    );
  }

  return (
    <div className="reveal" style={{ maxWidth: 560, margin: "0 auto" }}>
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
              Selected plan
            </label>
            <select
              value={reason}
              onChange={(e) => setReason(e.target.value)}
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
            disabled={status === "sending" || !name || !email || !reason}
            style={{
              padding: "12px 24px",
              borderRadius: "12px",
              background: status === "sending" ? "#999" : "linear-gradient(135deg, #1c1917, #292524)",
              color: "#fff",
              fontWeight: 600,
              fontSize: "0.95rem",
              border: "none",
              cursor: status === "sending" ? "wait" : "pointer",
              opacity: (!name || !email || !reason) ? 0.5 : 1,
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
      </div>
    </div>
  );
}
