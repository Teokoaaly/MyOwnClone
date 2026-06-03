"use client"

import { useState, useEffect } from "react"
import { useSession } from "next-auth/react"
import { useRouter } from "next/navigation"

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

const FEATURE_ICONS: Record<string, string> = {
  words_training_limit: "📝",
  responses_month_limit: "💬",
  modes_active: "🎯",
  email_triage: "📧",
  booking: "📅",
  api_access: "🔌",
  multi_clone: "👥",
  whitelabel: "🎨",
}

export default function FacturacionPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const [plans, setPlans] = useState<Plan[]>([])
  const [billing, setBilling] = useState<BillingInfo | null>(null)
  const [loading, setLoading] = useState(true)
  const [checkingOut, setCheckingOut] = useState<string | null>(null)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  useEffect(() => {
    async function load() {
      try {
        const [plansRes, billingRes] = await Promise.all([
          fetch("/api/clone/plans"),
          fetch("/api/clone/billing"),
        ])
        if (plansRes.ok) setPlans(await plansRes.json())
        if (billingRes.ok) setBilling(await billingRes.json())
      } catch {
        // Empty
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
    return (
      <div className="flex h-64 items-center justify-center">
        <div className="animate-spin h-6 w-6 border-2 border-purple-600 border-t-transparent rounded-full" />
      </div>
    )
  }

  const currentPlan = billing?.plan || "básico"

  return (
    <div className="p-8">
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          Facturación
        </h1>
        <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
          Plan actual: <span className="font-semibold text-purple-600 dark:text-purple-400 capitalize">{currentPlan}</span>
          {billing?.subscription_status && (
            <span className="ml-2 text-xs px-2 py-0.5 rounded-full bg-green-100 dark:bg-green-950 text-green-700 dark:text-green-300">
              {billing.subscription_status}
            </span>
          )}
        </p>
      </div>

      {billing?.portal_url && (
        <div className="mb-8 flex gap-3">
          <a
            href={billing.portal_url}
            target="_blank"
            rel="noopener noreferrer"
            className="px-4 py-2 bg-purple-600 text-white text-sm font-medium rounded-lg hover:bg-purple-700 transition-colors"
          >
            💳 Gestionar suscripción
          </a>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {plans.map((plan) => {
          const isCurrent = currentPlan.toLowerCase() === plan.name.toLowerCase()
          const isRecommended = plan.name === "Pro"
          return (
            <div
              key={plan.id}
              className={`relative rounded-xl border-2 p-6 transition-all ${
                isCurrent
                  ? "border-purple-500 bg-purple-50/50 dark:bg-purple-950/20"
                  : isRecommended
                  ? "border-purple-400/40 bg-white dark:bg-gray-900"
                  : "border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900"
              }`}
            >
              {isRecommended && (
                <span className="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 text-xs font-bold text-white bg-gradient-to-r from-purple-600 to-pink-600 rounded-full">
                  Recomendado
                </span>
              )}

              <h3 className="text-lg font-bold text-gray-900 dark:text-white mt-2">
                {plan.name}
              </h3>
              <p className="mt-2 text-3xl font-extrabold text-gray-900 dark:text-white">
                {plan.price_display}
              </p>
              {plan.price_cents === 0 && (
                <p className="text-xs text-gray-400 mt-1">14 días de prueba con tarjeta</p>
              )}

              <ul className="mt-5 space-y-2">
                <li className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                  <span>✅</span>
                  {plan.words_training_limit.toLocaleString("es-ES")} palabras training
                </li>
                <li className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                  <span>✅</span>
                  {plan.responses_month_limit.toLocaleString("es-ES")} respuestas/mes
                </li>
                <li className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                  <span>✅</span>
                  {plan.modes_active} modo{plan.modes_active !== 1 ? "s" : ""}
                </li>
                <li className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                  <span>{plan.email_triage ? "✅" : "❌"}</span>
                  Email triage
                </li>
                <li className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                  <span>{plan.booking ? "✅" : "❌"}</span>
                  Booking + video
                </li>
              </ul>

              <button
                onClick={() => checkout(plan.id)}
                disabled={isCurrent || checkingOut === plan.id}
                className={`mt-6 w-full py-2.5 text-sm font-semibold rounded-lg transition-all ${
                  isCurrent
                    ? "bg-gray-100 dark:bg-gray-800 text-gray-400 cursor-default"
                    : "bg-purple-600 text-white hover:bg-purple-500 disabled:opacity-50"
                }`}
              >
                {isCurrent ? "Plan actual" : checkingOut === plan.id ? "Redirigiendo..." : "Comenzar prueba"}
              </button>
            </div>
          )
        })}
      </div>
    </div>
  )
}
