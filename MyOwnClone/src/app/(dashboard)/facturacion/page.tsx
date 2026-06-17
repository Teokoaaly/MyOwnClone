"use client"

export const dynamic = "force-dynamic"

import { useEffect, useState } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "@/i18n/navigation"
import PublicPricing from "@/components/ui/PublicPricing"

interface BillingInfo {
  has_stripe: boolean
  plan: string | null
  status?: string | null
  subscription_status: string | null
  portal_url: string | null
  error?: string | null
  currency?: string
  balance_cents?: number
  cash_cents?: number
  voucher_cents?: number
  credit_cents?: number
  outstanding_cents?: number
  usage_cost_cents?: number
  balance_alert_enabled?: boolean
  auto_billing_enabled?: boolean
  payment_history?: PaymentRow[]
  voucher_records?: PaymentRow[]
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
  const [billing, setBilling] = useState<BillingInfo | null>(null)
  const [plans, setPlans] = useState<PlanInfo[]>([])
  const [loading, setLoading] = useState(true)
  const [checkoutLoading, setCheckoutLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [activeTab, setActiveTab] = useState<"payments" | "vouchers">("payments")

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
        if (!cancelled) setError(e instanceof Error ? e.message : "Unable to load billing")
      } finally {
        if (!cancelled) setLoading(false)
      }
    }

    loadBilling()
    return () => {
      cancelled = true
    }
  }, [])

  const openPortal = () => {
    if (billing?.portal_url) {
      window.open(billing.portal_url, "_blank", "noopener,noreferrer")
    }
  }

  const startCheckout = async () => {
    const plan = plans.find((item) => item.id === "pro" || item.name.toLowerCase() === "pro") ?? plans.find((item) => item.stripe_price_id) ?? plans[0]
    if (!plan) {
      setError("No billing plan is configured yet.")
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
        setError(data.error === "stripe_not_configured" ? "Stripe is not configured for this environment." : data.error ?? "Unable to start checkout.")
        return
      }
      window.location.assign(data.url)
    } finally {
      setCheckoutLoading(false)
    }
  }

  const handlePlanAction = (planId: string) => {
    if (planId === "enterprise") {
      window.location.href = "mailto:hello@myownclone.com"
      return
    }
    if (planId === "free") {
      router.push("/resumen")
      return
    }
    startCheckout()
  }

  if (status === "loading" || loading) {
    return (
      <div className="space-y-4">
        <div className="h-8 w-40 animate-pulse rounded bg-[var(--surface-3)]" />
        <div className="h-36 animate-pulse rounded-lg bg-[var(--surface-2)]" />
      </div>
    )
  }

  const currency = billing?.currency ?? "usd"
  const paymentHistory = billing?.payment_history ?? []
  const voucherRecords = billing?.voucher_records ?? []
  const currentPlan = plans.find((plan) => plan.id === billing?.plan || plan.name.toLowerCase() === billing?.plan)

  return (
    <div className="space-y-10">
      <section className="space-y-8">
        <div className="flex flex-col gap-6 xl:flex-row xl:items-end xl:justify-between">
          <div>
            <h1 className="text-xl font-semibold text-[var(--text-primary)]">
              Balance
            </h1>
            <p className="mt-2 text-sm text-[var(--text-secondary)]">
              Top up your team balance, manage alerts, and review payment and voucher history.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3 text-sm text-[var(--text-secondary)]">
            <span className="inline-flex items-center gap-2">
              <span className={`h-2 w-2 rounded-full ${billing?.balance_alert_enabled ? "bg-emerald-500" : "bg-[var(--text-faint)]"}`} />
              Balance alert is {billing?.balance_alert_enabled ? "enabled" : "disabled"}
            </span>
            <span className="inline-flex items-center gap-2">
              <span className={`h-2 w-2 rounded-full ${billing?.auto_billing_enabled ? "bg-emerald-500" : "bg-[var(--text-faint)]"}`} />
              Auto-billing is {billing?.auto_billing_enabled ? "enabled" : "disabled"}
            </span>
            <button type="button" className="btn-secondary rounded-md text-sm">
              Enable alert
            </button>
            <button type="button" className="btn-secondary rounded-md text-sm">
              Enable auto-billing
            </button>
          </div>
        </div>

        <div>
          <p className="flex items-center gap-1 text-sm text-[var(--text-muted)]">
            Effective balance
            <span className="inline-flex h-4 w-4 items-center justify-center rounded-full border border-[var(--border-medium)] text-[10px]">
              ?
            </span>
          </p>
          <p className="mt-1 text-3xl font-semibold tracking-normal text-[var(--text-primary)]">
            {money(billing?.balance_cents, currency)}
          </p>
        </div>

        <div className="border-t border-[var(--border-soft)] pt-7">
          <div className="grid max-w-3xl grid-cols-2 gap-6 text-sm md:grid-cols-4">
            <BalancePart label="Cash" value={money(billing?.cash_cents, currency)} />
            <BalancePart label="Voucher" value={money(billing?.voucher_cents, currency)} prefix="+" hint />
            <BalancePart label="Credit" value={money(billing?.credit_cents, currency)} prefix="+" />
            <BalancePart label="Outstanding" value={money(billing?.outstanding_cents, currency)} prefix="-" />
          </div>
        </div>

        <div className="grid gap-3 md:grid-cols-3">
          <StatusTile label="Plan" value={currentPlan?.name ?? billing?.plan ?? "No plan"} />
          <StatusTile label="Subscription" value={billing?.subscription_status ?? billing?.status ?? "Not active"} />
          <StatusTile label="Tracked usage cost" value={money(billing?.usage_cost_cents, currency)} />
        </div>

        {(billing?.error || error) && (
          <div className="rounded-md border border-amber-300 bg-amber-50 px-4 py-3 text-sm text-amber-950">
            {error ?? "Stripe is not configured for this environment, so checkout and portal actions are unavailable."}
          </div>
        )}

        <div className="rounded-md border border-orange-300 bg-orange-50 px-4 py-3 text-sm text-orange-950">
          <span className="mr-2 text-orange-500">△</span>
          Vouchers can only be used for consumption and cannot offset outstanding balances.
        </div>

        <div className="flex flex-wrap gap-3">
          <button
            type="button"
            onClick={startCheckout}
            disabled={checkoutLoading}
            className="rounded-md bg-slate-950 px-7 py-2.5 text-sm font-semibold text-white disabled:cursor-not-allowed disabled:opacity-60"
          >
            {checkoutLoading ? "Opening..." : billing?.has_stripe ? "Manage plan" : "Recharge"}
          </button>
          <button type="button" className="rounded-md border border-[var(--border-medium)] bg-white px-7 py-2.5 text-sm font-medium text-[var(--text-primary)]">
            Support Bank Transfer
          </button>
          <button
            type="button"
            onClick={() => router.push("/configuracion")}
            className="rounded-md border border-[var(--border-medium)] bg-white px-7 py-2.5 text-sm font-medium text-[var(--text-primary)]"
          >
            Get API Key
          </button>
          {billing?.portal_url && (
            <button
              type="button"
              onClick={openPortal}
              className="rounded-md border border-[var(--border-medium)] bg-white px-7 py-2.5 text-sm font-medium text-[var(--text-primary)]"
            >
              View Stripe Portal
            </button>
          )}
        </div>
      </section>

      <section id="plans" className="border-t border-[var(--border-soft)] pt-10">
        <div className="flex flex-col gap-2">
          <p className="section-label">Plans</p>
          <h2 className="text-xl font-semibold text-[var(--text-primary)]">
            Same pricing as the public landing
          </h2>
          <p className="max-w-2xl text-sm leading-6 text-[var(--text-secondary)]">
            The dashboard uses the same commercial tiers shown on the landing page, so upgrades and sales conversations stay consistent.
          </p>
        </div>
        <div className="mt-7">
          <PublicPricing
            mode="dashboard"
            currentPlanId={currentPlan?.id ?? billing?.plan}
            onSelectPlan={handlePlanAction}
          />
        </div>
      </section>

      <section className="border-t border-[var(--border-soft)] pt-10">
        <div className="flex flex-col gap-6 xl:flex-row xl:items-end xl:justify-between">
          <div className="flex gap-8 border-b border-[var(--border-soft)] text-sm font-medium">
            <button
              type="button"
              onClick={() => setActiveTab("payments")}
              className={`pb-3 ${activeTab === "payments" ? "border-b-2 border-slate-950 text-slate-950" : "text-[var(--text-secondary)]"}`}
            >
              Payment History
            </button>
            <button
              type="button"
              onClick={() => setActiveTab("vouchers")}
              className={`pb-3 ${activeTab === "vouchers" ? "border-b-2 border-slate-950 text-slate-950" : "text-[var(--text-secondary)]"}`}
            >
              Voucher Records
            </button>
          </div>

          <div className="flex flex-wrap gap-2">
            <button type="button" className="rounded-md border border-[var(--border-medium)] bg-white px-6 py-2 text-sm font-medium">
              View Invoices
            </button>
            <div className="flex rounded-md border border-[var(--border-medium)] bg-white text-sm text-[var(--text-muted)]">
              <input
                type="text"
                placeholder="Start date"
                className="w-36 bg-transparent px-3 py-2 outline-none"
                aria-label="Start date"
              />
              <span className="px-2 py-2">→</span>
              <input
                type="text"
                placeholder="End date"
                className="w-36 bg-transparent px-3 py-2 outline-none"
                aria-label="End date"
              />
            </div>
          </div>
        </div>

        <div className="mt-8 overflow-hidden rounded-md border border-[var(--border-soft)]">
          {activeTab === "payments" ? (
            <table className="w-full text-sm">
              <thead className="bg-slate-100 text-left text-[var(--text-primary)]">
                <tr>
                  <th className="px-5 py-4 font-semibold">Sequence</th>
                  <th className="px-5 py-4 font-semibold">Date(UTC)</th>
                  <th className="px-5 py-4 font-semibold">Amount(Tax included)</th>
                  <th className="px-5 py-4 font-semibold">Results</th>
                </tr>
              </thead>
              <tbody>
                {paymentHistory.length > 0 ? paymentHistory.map((row) => (
                  <tr key={row.sequence} className="border-t border-[var(--border-soft)]">
                    <td className="px-5 py-5 font-mono">{row.sequence}</td>
                    <td className="px-5 py-5">{row.date}</td>
                    <td className="px-5 py-5">{row.amount}</td>
                    <td className="px-5 py-5">{row.result}</td>
                  </tr>
                )) : (
                  <tr>
                    <td colSpan={4} className="px-5 py-12 text-center text-sm text-[var(--text-muted)]">
                      No local payment records yet. Stripe invoices will appear through the billing portal when configured.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          ) : (
            <div className="px-5 py-12 text-center text-sm text-[var(--text-muted)]">
              {voucherRecords.length === 0 ? "No voucher records yet." : `${voucherRecords.length} voucher records`}
            </div>
          )}
        </div>
      </section>
    </div>
  )
}

function StatusTile({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-md border border-[var(--border-soft)] bg-white px-4 py-3">
      <p className="text-xs text-[var(--text-muted)]">{label}</p>
      <p className="mt-1 text-sm font-semibold capitalize text-[var(--text-primary)]">{value}</p>
    </div>
  )
}

function BalancePart({
  label,
  value,
  prefix,
  hint,
}: {
  label: string
  value: string
  prefix?: string
  hint?: boolean
}) {
  return (
    <div className="flex items-end gap-4">
      {prefix && <span className="pb-1 text-[var(--text-muted)]">{prefix}</span>}
      <div>
        <p className="flex items-center gap-1 text-sm text-[var(--text-muted)]">
          {label}
          {hint && (
            <span className="inline-flex h-4 w-4 items-center justify-center rounded-full border border-[var(--border-medium)] text-[10px]">
              ?
            </span>
          )}
        </p>
        <p className="mt-1 text-base font-medium text-[var(--text-primary)]">
          {value}
        </p>
      </div>
    </div>
  )
}
