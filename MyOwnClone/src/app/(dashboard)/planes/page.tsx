"use client";

export const dynamic = "force-dynamic";

import { useEffect, useState } from "react";
import { useSession } from "next-auth/react";
import { useRouter } from "@/i18n/navigation";
import PublicPricing from "@/components/ui/PublicPricing";
import { LoadingState } from "@/components/ui/LoadingState";

interface PlanInfo {
  id: string;
  name: string;
  price_cents: number;
  price_display?: string;
  stripe_price_id?: string | null;
}

interface BillingInfo {
  plan: string | null;
  portal_url?: string | null;
}

export default function PlanesPage() {
  const { status } = useSession();
  const router = useRouter();
  const [plans, setPlans] = useState<PlanInfo[]>([]);
  const [billing, setBilling] = useState<BillingInfo | null>(null);
  const [loading, setLoading] = useState(true);
  const [checkoutLoading, setCheckoutLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login");
  }, [status, router]);

  useEffect(() => {
    let cancelled = false;
    async function load() {
      try {
        const [billingRes, plansRes] = await Promise.all([
          fetch("/api/clone/billing", { cache: "no-store" }),
          fetch("/api/clone/plans", { cache: "no-store" }),
        ]);
        if (!cancelled && billingRes.ok) setBilling(await billingRes.json());
        if (!cancelled && plansRes.ok) {
          const data = await plansRes.json();
          setPlans(Array.isArray(data) ? data : []);
        }
      } catch (e) {
        if (!cancelled) setError(e instanceof Error ? e.message : "Unable to load plans");
      } finally {
        if (!cancelled) setLoading(false);
      }
    }
    load();
    return () => { cancelled = true; };
  }, []);

  const startCheckout = async () => {
    const plan = plans.find((p) => p.id === "pro" || p.name.toLowerCase() === "pro") ?? plans.find((p) => p.stripe_price_id) ?? plans[0];
    if (!plan) { setError("No billing plan configured yet."); return; }
    setCheckoutLoading(true);
    setError(null);
    try {
      const res = await fetch("/api/clone/stripe/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ plan_id: plan.id, success_url: "/planes", cancel_url: "/planes" }),
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok || !data.url) {
        setError(data.error === "stripe_not_configured" ? "Stripe is not configured." : data.error ?? "Unable to start checkout.");
        return;
      }
      window.location.assign(data.url);
    } finally { setCheckoutLoading(false); }
  };

  const handlePlanAction = (planId: string) => {
    if (planId === "enterprise") { window.location.href = "mailto:hello@myownclone.com"; return; }
    if (planId === "free") { router.push("/resumen"); return; }
    startCheckout();
  };

  if (status === "loading" || loading) return <LoadingState />;

  const currentPlan = plans.find((p) => p.id === billing?.plan || p.name.toLowerCase() === billing?.plan);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-xl font-semibold text-[var(--text-primary)]">Plans</h1>
        <p className="mt-1 text-sm text-[var(--text-secondary)]">
          {currentPlan ? `Current: ${currentPlan.name}` : "Choose a plan"} — upgrade or downgrade anytime
        </p>
      </div>

      {error && (
        <div className="rounded-md border border-amber-300 bg-amber-50 px-4 py-3 text-sm text-amber-950">{error}</div>
      )}

      <PublicPricing
        mode="dashboard"
        currentPlanId={currentPlan?.id ?? billing?.plan}
        onSelectPlan={handlePlanAction}
      />
    </div>
  );
}
