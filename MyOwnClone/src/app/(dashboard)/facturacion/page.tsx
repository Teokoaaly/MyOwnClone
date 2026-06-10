"use client"

export const dynamic = "force-dynamic"


import { useState, useEffect } from "react"
import { useSession } from "next-auth/react"
import { LoadingState } from "@/components/ui/LoadingState"
import { ErrorState } from "@/components/ui/ErrorState"
import { StatusBadge, statusToKind } from "@/components/ui/StatusBadge"
import { useRouter } from "@/i18n/navigation"

interface Plan {
  id: string
  name: string
  price_cents: number
  price_display: string
  words_training_limit: number
  responses_month_limit: number
  modes_active: number
  email_triage: boolean
  booking: boolean
  api_access: boolean
  multi_clone: boolean
  whitelabel: boolean
}

interface BillingInfo {
  has_stripe: boolean
  plan: string | null
  subscription_status: string | null
  portal_url: string | null
}

export default function FacturacionPage() {
  const { status } = useSession()
  const router = useRouter()
  const [plans, setPlans] = useState<Plan[]>([])
  const [billing, setBilling] = useState<BillingInfo | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [checkingOut, setCheckingOut] = useState<string | null>(null)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  useEffect(() => {
    async function load() {
      setLoading(true)
      setError(null)
      try {
        const [plansRes, billingRes] = await Promise.all([
          fetch("/api/clone/plans"),
          fetch("/api/clone/billing"),
        ])
        if (plansRes.ok) setPlans(await plansRes.json())
        if (billingRes.ok) setBilling(await billingRes.json())
        if (!plansRes.ok || !billingRes.ok) {
          throw new Error("Could not load billing information")
        }
      } catch (e) {
        setError(e instanceof Error ? e.message : "Error")
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [])

  const checkout = async (planId: string) => {
    setCheckingOut(planId)
    try {
      const res = await fetch("/api/clone/stripe/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ plan_id: planId }),
      })
      if (res.ok) {
        const data = await res.json()
        if (data.url) window.location.href = data.url
      }
    } catch {
      // Error handled by UI state
    } finally {
      setCheckingOut(null)
    }
  }

  if (status === "loading" || loading) {
    return <LoadingState label="Loading plans..." rows={4} />
  }

  if (error) {
    return <ErrorState message={error} />
  }

  const currentPlan = billing?.plan || "basic"

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Billing
        </h1>
        <div className="mt-1 flex items-center gap-2 text-sm text-[var(--text-muted)]">
          <span>
            Current plan:{" "}
            <span className="font-semibold text-[var(--color-accent-warm)] capitalize">
              {currentPlan}
            </span>
          </span>
          {billing?.subscription_status && (
            <StatusBadge
              kind={statusToKind(billing.subscription_status)}
              label={billing.subscription_status}
            />
          )}
        </div>
      </header>

      {billing?.portal_url && (
        <div>
          <a
            href={billing.portal_url}
            target="_blank"
            rel="noopener noreferrer"
            className="btn-primary text-xs"
          >
            Manage subscription
            <span aria-hidden="true" className="ml-1">↗</span>
            <span className="sr-only"> (opens in a new tab)</span>
          </a>
        </div>
      )}

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {plans.map((plan) => {
          const isCurrent = currentPlan.toLowerCase() === plan.name.toLowerCase()
          const isRecommended = plan.name === "Pro"
          return (
            <div
              key={plan.id}
              className={[
                "card flex flex-col",
                isCurrent ? "ring-1 ring-[var(--color-accent-warm)]" : "",
                isRecommended ? "border-[var(--color-accent-warm)]" : "",
              ].join(" ")}
            >
              {isRecommended && (
                <span className="badge-violet self-start">Recommended</span>
              )}

              <h3 className="mt-2 text-lg font-semibold text-[var(--text-primary)]">
                {plan.name}
              </h3>
              <p className="mt-2 stat-value text-2xl">
                {plan.price_display}
              </p>
              {plan.price_cents === 0 && (
                <p className="text-xs text-[var(--text-muted)] mt-1">
                  14-day card-backed trial
                </p>
              )}

              <ul className="mt-5 space-y-2 text-sm text-[var(--text-secondary)] flex-1">
                <li className="flex items-center gap-2">
                  <span className="text-[var(--color-accent-green)]">✓</span>
                  {plan.words_training_limit.toLocaleString("en-US")} training words
                </li>
                <li className="flex items-center gap-2">
                  <span className="text-[var(--color-accent-green)]">✓</span>
                  {plan.responses_month_limit.toLocaleString("en-US")} responses/month
                </li>
                <li className="flex items-center gap-2">
                  <span className="text-[var(--color-accent-green)]">✓</span>
                  {plan.modes_active} mode{plan.modes_active !== 1 ? "s" : ""}
                </li>
                <li className="flex items-center gap-2">
                  <span className={plan.email_triage ? "text-[var(--color-accent-green)]" : "text-[var(--text-muted)]"}>
                    {plan.email_triage ? "✓" : "✗"}
                  </span>
                  Email triage
                </li>
                <li className="flex items-center gap-2">
                  <span className={plan.booking ? "text-[var(--color-accent-green)]" : "text-[var(--text-muted)]"}>
                    {plan.booking ? "✓" : "✗"}
                  </span>
                  Booking + video
                </li>
              </ul>

              <button
                type="button"
                onClick={() => checkout(plan.id)}
                disabled={isCurrent || checkingOut === plan.id}
                aria-current={isCurrent ? "true" : undefined}
                className={[
                  "mt-6 w-full py-2.5 text-sm font-medium rounded-full transition-all",
                  isCurrent
                    ? "bg-[var(--surface-2)] text-[var(--text-muted)] cursor-default"
                    : "btn-primary",
                ].join(" ")}
              >
                {isCurrent
                  ? "Current plan"
                  : checkingOut === plan.id
                  ? "Redirecting..."
                  : "Start trial"}
              </button>
            </div>
          )
        })}
      </div>
    </div>
  )
}
