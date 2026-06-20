"use client"

export const dynamic = "force-dynamic"

import { useEffect, useState } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "@/i18n/navigation"
import { useTranslations } from "next-intl"

interface BillingInfo {
  has_stripe: boolean
  plan: string | null
  status?: string | null
  subscription_status: string | null
  portal_url: string | null
  error?: string | null
  currency?: string
  stripe_customer_id?: string | null
  stripe_subscription_id?: string | null
  usage_cost_cents?: number
  payment_history?: PaymentRow[]
}

interface PaymentRow {
  sequence: string
  date: string
  amount: string
  result: string
}

interface PlanInfo {
  id: string
  name: string
  price_cents: number
  price_display?: string
  stripe_price_id?: string | null
}

function money(cents = 0, currency = "usd") {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: currency.toUpperCase(),
  }).format(cents / 100)
}

export default function FacturacionPage() {
  const { status } = useSession()
  const router = useRouter()
  const t = useTranslations("billing")
  const [billing, setBilling] = useState<BillingInfo | null>(null)
  const [plans, setPlans] = useState<PlanInfo[]>([])
  const [loading, setLoading] = useState(true)
  const [checkoutLoading, setCheckoutLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  useEffect(() => {
    let cancelled = false

    async function loadBilling() {
      try {
        const [billingRes, plansRes] = await Promise.all([
          fetch("/api/clone/billing", { cache: "no-store" }),
          fetch("/api/clone/plans", { cache: "no-store" }),
        ])
        if (!cancelled && billingRes.ok) {
          setBilling(await billingRes.json())
        }
        if (!cancelled && plansRes.ok) {
          const data = await plansRes.json()
          setPlans(Array.isArray(data) ? data : [])
        }
      } catch (e) {
        if (!cancelled) setError(e instanceof Error ? e.message : t("loadError"))
      } finally {
        if (!cancelled) setLoading(false)
      }
    }

    if (status === "authenticated") {
      loadBilling()
    }
    return () => {
      cancelled = true
    }
  }, [status])

  const openPortal = () => {
    if (billing?.portal_url) {
      window.open(billing.portal_url, "_blank", "noopener,noreferrer")
    }
  }

  const startCheckout = async (planId?: string) => {
    const plan = plans.find((p) => p.id === planId)
      ?? plans.find((p) => p.stripe_price_id)
      ?? plans[0]
    if (!plan) {
      setError(t("noPlanConfigured"))
      return
    }

    setCheckoutLoading(true)
    setError(null)
    try {
      const res = await fetch("/api/clone/stripe/checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          plan_id: plan.id,
          success_url: "/facturacion",
          cancel_url: "/facturacion",
        }),
      })
      const data = await res.json().catch(() => ({}))
      if (!res.ok || !data.url) {
        setError(
          data.error === "stripe_not_configured"
            ? t("stripeNotConfigured")
            : data.error ?? t("checkoutError")
        )
        return
      }
      window.location.assign(data.url)
    } finally {
      setCheckoutLoading(false)
    }
  }

  if (status === "loading" || loading) {
    return (
      <div className="space-y-4">
        <div className="h-8 w-48 animate-pulse rounded bg-[var(--surface-3)]" />
        <div className="h-40 animate-pulse rounded-lg bg-[var(--surface-2)]" />
      </div>
    )
  }

  const currency = billing?.currency ?? "usd"
  const currentPlan = plans.find(
    (p) => p.id === billing?.plan || p.name.toLowerCase() === billing?.plan?.toLowerCase()
  )
  const subStatus = billing?.subscription_status ?? billing?.status ?? null
  const isActive = subStatus === "active" || subStatus === "trialing"
  const paymentHistory = billing?.payment_history ?? []

  return (
    <div className="space-y-8">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          {t("title")}
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          {t("subtitle")}
        </p>
      </header>

      {(error || billing?.error) && (
        <div className="rounded-lg border border-amber-300 bg-amber-50 px-4 py-3 text-sm text-amber-950">
          {error ?? billing?.error ?? t("stripeNotConfigured")}
        </div>
      )}

      {/* Subscription Status */}
      <section className="card">
        <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
          {t("subscription")}
        </h3>

        <div className="grid gap-4 sm:grid-cols-3">
          <div className="rounded-lg border border-[var(--border-soft)] bg-[var(--surface-1)] px-4 py-3">
            <p className="text-xs text-[var(--text-muted)]">{t("currentPlan")}</p>
            <p className="mt-1 text-sm font-semibold text-[var(--text-primary)]">
              {currentPlan?.name ?? billing?.plan ?? t("noPlan")}
            </p>
          </div>

          <div className="rounded-lg border border-[var(--border-soft)] bg-[var(--surface-1)] px-4 py-3">
            <p className="text-xs text-[var(--text-muted)]">{t("status")}</p>
            <div className="mt-1 flex items-center gap-2">
              <span className={`h-2 w-2 rounded-full ${
                isActive ? "bg-emerald-500" : subStatus === "past_due" ? "bg-amber-500" : "bg-[var(--text-faint)]"
              }`} />
              <p className="text-sm font-semibold capitalize text-[var(--text-primary)]">
                {subStatus ?? t("notActive")}
              </p>
            </div>
          </div>

          <div className="rounded-lg border border-[var(--border-soft)] bg-[var(--surface-1)] px-4 py-3">
            <p className="text-xs text-[var(--text-muted)]">{t("usageCost")}</p>
            <p className="mt-1 text-sm font-semibold text-[var(--text-primary)]">
              {money(billing?.usage_cost_cents, currency)}
            </p>
            <p className="text-[10px] text-[var(--text-muted)]">{t("currentPeriod")}</p>
          </div>
        </div>

        {/* Payment Method */}
        <div className="mt-4 flex items-center justify-between rounded-lg border border-[var(--border-soft)] bg-[var(--surface-1)] px-4 py-3">
          <div>
            <p className="text-sm font-medium text-[var(--text-primary)]">
              {t("paymentMethod")}
            </p>
            <p className="text-xs text-[var(--text-muted)]">
              {billing?.has_stripe && billing?.stripe_customer_id
                ? t("paymentMethodManaged")
                : t("noPaymentMethod")}
            </p>
          </div>
          {billing?.portal_url && (
            <button
              type="button"
              onClick={openPortal}
              className="btn-secondary text-xs"
            >
              {t("updatePaymentMethod")}
            </button>
          )}
        </div>

        {/* Actions */}
        <div className="mt-4 flex flex-wrap gap-3">
          {billing?.portal_url ? (
            <button
              type="button"
              onClick={openPortal}
              className="btn-primary text-xs"
            >
              {t("manageInStripe")}
            </button>
          ) : (
            <button
              type="button"
              onClick={() => startCheckout()}
              disabled={checkoutLoading}
              className="btn-primary text-xs disabled:opacity-50"
            >
              {checkoutLoading ? t("opening") : t("subscribe")}
            </button>
          )}
        </div>
      </section>

      {/* Invoices */}
      <section className="card">
        <div className="flex items-center justify-between">
          <h3 className="text-sm font-semibold text-[var(--text-primary)]">
            {t("invoices")}
          </h3>
          {billing?.portal_url && (
            <button
              type="button"
              onClick={openPortal}
              className="text-xs font-medium text-[var(--color-accent-warm)] hover:underline"
            >
              {t("viewAllInvoices")}
            </button>
          )}
        </div>
        <p className="mb-4 text-xs text-[var(--text-muted)]">{t("invoicesDesc")}</p>

        {paymentHistory.length > 0 ? (
          <div className="overflow-hidden rounded-lg border border-[var(--border-soft)]">
            <table className="w-full text-sm">
              <thead className="bg-[var(--surface-2)] text-left text-[var(--text-primary)]">
                <tr>
                  <th className="px-4 py-3 text-xs font-semibold">{t("invoiceDate")}</th>
                  <th className="px-4 py-3 text-xs font-semibold">{t("invoiceAmount")}</th>
                  <th className="px-4 py-3 text-xs font-semibold">{t("invoiceStatus")}</th>
                </tr>
              </thead>
              <tbody>
                {paymentHistory.map((row) => (
                  <tr key={row.sequence} className="border-t border-[var(--border-soft)]">
                    <td className="px-4 py-3">{row.date}</td>
                    <td className="px-4 py-3 font-mono">{row.amount}</td>
                    <td className="px-4 py-3">
                      <span className="inline-flex rounded-full bg-emerald-50 px-2 py-0.5 text-[10px] font-medium text-emerald-700">
                        {row.result}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="rounded-lg border border-dashed border-[var(--border-soft)] px-4 py-10 text-center text-sm text-[var(--text-muted)]">
            {billing?.has_stripe ? t("noInvoices") : t("noInvoicesNoStripe")}
          </div>
        )}
      </section>
    </div>
  )
}
