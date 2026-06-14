"use client"

export const dynamic = "force-dynamic"

import { useEffect, useState } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "@/i18n/navigation"

interface BillingInfo {
  plan: string | null
  currency?: string
}

interface PlanInfo {
  id: string
  name: string
  price_cents: number
  price_display?: string
  stripe_price_id?: string | null
  words_training_limit?: number
  responses_month_limit?: number
  modes_active?: number
  email_triage?: boolean
  booking?: boolean
  api_access?: boolean
  multi_clone?: boolean
  whitelabel?: boolean
}

function money(cents = 0, currency = "usd") {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: currency.toUpperCase(),
  }).format(cents / 100)
}

function planFeatures(plan: PlanInfo) {
  const modes = plan.modes_active ?? 1
  const features = [
    `${plan.words_training_limit?.toLocaleString("en-US") ?? "Flexible"} training words`,
    `${plan.responses_month_limit?.toLocaleString("en-US") ?? "Flexible"} monthly responses`,
    `${modes} active mode${modes === 1 ? "" : "s"}`,
  ]

  if (plan.email_triage) features.push("AI email triage")
  if (plan.booking) features.push("Booking workflows")
  if (plan.api_access) features.push("API access")
  if (plan.multi_clone) features.push("Multi-clone workspace")
  if (plan.whitelabel) features.push("White label")

  return features
}

export default function PlanesPage() {
  const { status } = useSession()
  const router = useRouter()
  const [billing, setBilling] = useState<BillingInfo | null>(null)
  const [plans, setPlans] = useState<PlanInfo[]>([])
  const [loading, setLoading] = useState(true)
  const [checkoutLoading, setCheckoutLoading] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  useEffect(() => {
    let cancelled = false

    async function loadPlans() {
      if (status !== "authenticated") return

      try {
        const [billingRes, plansRes] = await Promise.all([
          fetch("/api/clone/billing", { cache: "no-store", credentials: "include" }),
          fetch("/api/clone/plans", { cache: "no-store", credentials: "include" }),
        ])
        if (!cancelled && billingRes.ok) {
          setBilling(await billingRes.json())
        }
        if (!cancelled && plansRes.ok) {
          const data = await plansRes.json()
          setPlans(Array.isArray(data) ? data : [])
        }
      } catch (e) {
        if (!cancelled) setError(e instanceof Error ? e.message : "Unable to load plans")
      } finally {
        if (!cancelled) setLoading(false)
      }
    }

    if (status === "authenticated") {
      loadPlans()
    }

    return () => {
      cancelled = true
    }
  }, [status])

  const startCheckout = async (plan: PlanInfo) => {
    if (!plan.stripe_price_id) {
      setError(`${plan.name} is not available for checkout yet.`)
      return
    }

    setCheckoutLoading(plan.id)
    setError(null)
    try {
      const res = await fetch("/api/clone/stripe/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          plan_id: plan.id,
          success_url: "/planes",
          cancel_url: "/planes",
        }),
      })
      const data = await res.json().catch(() => ({}))
      if (!res.ok || !data.url) {
        setError(
          data.error === "stripe_not_configured"
            ? "Stripe is not configured for this environment."
            : data.error ?? "Unable to start checkout.",
        )
        return
      }
      window.location.assign(data.url)
    } finally {
      setCheckoutLoading(null)
    }
  }

  if (status === "loading" || loading) {
    return (
      <div className="space-y-4">
        <div className="h-8 w-40 animate-pulse rounded bg-[var(--surface-3)]" />
        <div className="h-72 animate-pulse rounded-[32px] bg-[var(--surface-2)]" />
      </div>
    )
  }

  const currency = billing?.currency ?? "usd"

  return (
    <div className="space-y-8">
      <section className="landing-pricing-section !m-0 !rounded-[32px] !px-5 !py-10 md:!px-8">
        <div className="landing-pricing-shell !mx-0 !max-w-none">
          <div className="landing-pricing-head">
            <p className="landing-pricing-kicker">Upgrade</p>
            <h2>Select a plan</h2>
            <p>
              Choose the workspace plan first. Billing details and invoices stay in the Billing page.
            </p>
          </div>

          {error && (
            <div className="mx-auto mb-6 max-w-2xl rounded-xl border border-amber-300 bg-amber-50 px-4 py-3 text-sm text-amber-950">
              {error}
            </div>
          )}

          {plans.length === 0 ? (
            <div className="rounded-2xl border border-[var(--border-soft)] bg-white px-5 py-8 text-center text-sm text-[var(--text-muted)]">
              No plans are configured yet.
            </div>
          ) : (
            <div className="landing-pricing-grid">
              {plans.map((plan, index) => {
                const normalizedCurrent = billing?.plan?.toLowerCase()
                const isCurrent =
                  plan.id.toLowerCase() === normalizedCurrent ||
                  plan.name.toLowerCase() === normalizedCurrent
                const featured = index === 1 || plan.id.toLowerCase().includes("pro")
                const canCheckout = Boolean(plan.stripe_price_id)

                return (
                  <article
                    key={plan.id}
                    className={featured ? "landing-plan-card landing-plan-card-featured" : "landing-plan-card"}
                  >
                    <div className="landing-plan-top">
                      <span className="landing-plan-glyph" aria-hidden="true" />
                      {isCurrent ? (
                        <span className="landing-plan-badge">Current</span>
                      ) : featured ? (
                        <span className="landing-plan-badge">Popular</span>
                      ) : null}
                    </div>

                    <div className="landing-plan-price">
                      <span>{plan.price_display ?? money(plan.price_cents, currency)}</span>
                      <small>/mo</small>
                    </div>

                    <h3>{plan.name}</h3>
                    <p>
                      {isCurrent
                        ? "This is your active plan."
                        : "Upgrade when your clone needs more capacity and workflows."}
                    </p>

                    <button
                      type="button"
                      onClick={() => startCheckout(plan)}
                      disabled={checkoutLoading !== null || isCurrent || !canCheckout}
                      className={featured ? "landing-plan-cta landing-plan-cta-inverse" : "landing-plan-cta"}
                    >
                      {isCurrent
                        ? "Current plan"
                        : checkoutLoading === plan.id
                          ? "Opening checkout..."
                          : canCheckout
                            ? "Select plan"
                            : "Unavailable"}
                    </button>

                    <div className="landing-plan-divider" />
                    <div className="landing-plan-features">
                      <strong>Features</strong>
                      <ul>
                        {planFeatures(plan).map((feature) => (
                          <li key={feature}>{feature}</li>
                        ))}
                      </ul>
                    </div>
                  </article>
                )
              })}
            </div>
          )}
        </div>
      </section>
    </div>
  )
}
