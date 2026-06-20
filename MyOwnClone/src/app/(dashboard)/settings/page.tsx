"use client"

export const dynamic = "force-dynamic"

import { useState, useEffect } from "react"
import { useSession, signOut } from "next-auth/react"
import { useRouter } from "@/i18n/navigation"
import { useTranslations } from "next-intl"
import { LoadingState } from "@/components/ui/LoadingState"
import { ThemeToggle } from "@/components/ui/ThemeToggle"

export default function SettingsPage() {
  const { data: session, status } = useSession()
  const router = useRouter()
  const t = useTranslations("settings")

  const [name, setName] = useState("")
  const [email] = useState(session?.user?.email ?? "")
  const [currentPassword, setCurrentPassword] = useState("")
  const [newPassword, setNewPassword] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("")
  const [saving, setSaving] = useState(false)
  const [saved, setSaved] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [deleteConfirm, setDeleteConfirm] = useState("")
  const [deleting, setDeleting] = useState(false)

  useEffect(() => {
    if (status === "unauthenticated") router.push("/login")
  }, [status, router])

  useEffect(() => {
    if (session?.user?.name) setName(session.user.name)
  }, [session?.user?.name])

  const changePassword = async () => {
    if (newPassword !== confirmPassword) {
      setError(t("passwordMismatch"))
      return
    }
    if (newPassword.length < 8) {
      setError(t("passwordTooShort"))
      return
    }
    setSaving(true)
    setSaved(false)
    setError(null)
    try {
      const res = await fetch("/api/auth/change-password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ currentPassword, newPassword }),
      })
      if (!res.ok) {
        const data = await res.json().catch(() => ({}))
        throw new Error(data.error ?? t("passwordChangeError"))
      }
      setSaved(true)
      setCurrentPassword("")
      setNewPassword("")
      setConfirmPassword("")
      setTimeout(() => setSaved(false), 3000)
    } catch (e) {
      setError(e instanceof Error ? e.message : t("passwordChangeError"))
    } finally {
      setSaving(false)
    }
  }

  const deleteAccount = async () => {
    if (deleteConfirm !== email) return
    setDeleting(true)
    setError(null)
    try {
      const res = await fetch("/api/account/delete", {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
      })
      if (!res.ok) {
        const data = await res.json().catch(() => ({}))
        throw new Error(data.error ?? t("deleteError"))
      }
      await signOut({ callbackUrl: "/login" })
    } catch (e) {
      setError(e instanceof Error ? e.message : t("deleteError"))
      setDeleting(false)
    }
  }

  if (status === "loading") {
    return <LoadingState label={t("loading")} rows={4} />
  }

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          {t("title")}
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          {t("subtitle")}
        </p>
      </header>

      {saved && (
        <div role="status" aria-live="polite"
          className="rounded-lg border border-[var(--color-accent-green)]/30 bg-[var(--color-accent-green)]/10 px-4 py-3 text-sm text-[var(--color-accent-green)]">
          {t("saved")}
        </div>
      )}

      {error && (
        <div className="rounded-lg border border-red-300 bg-red-50 px-4 py-3 text-sm text-red-800">
          {error}
        </div>
      )}

      {/* Profile */}
      <section className="card">
        <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
          {t("profile")}
        </h3>
        <div className="space-y-4">
          <div className="flex items-center gap-4">
            <div className="flex h-14 w-14 items-center justify-center rounded-full bg-[var(--surface-3)] text-lg font-semibold text-[var(--text-secondary)]">
              {session?.user?.name?.charAt(0).toUpperCase() ?? "U"}
            </div>
            <div>
              <p className="text-sm font-medium text-[var(--text-primary)]">
                {session?.user?.name ?? "User"}
              </p>
              <p className="text-xs text-[var(--text-muted)]">
                {session?.user?.email}
              </p>
              {session?.user?.role && (
                <span className="mt-1 inline-flex rounded-full bg-[var(--surface-3)] px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wider text-[var(--text-secondary)]">
                  {session.user.role}
                </span>
              )}
            </div>
          </div>

          <div className="grid gap-4 sm:grid-cols-2">
            <div>
              <label className="stat-label" htmlFor="settings-name">{t("name")}</label>
              <input
                id="settings-name"
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
              />
            </div>
            <div>
              <label className="stat-label" htmlFor="settings-email">{t("email")}</label>
              <input
                id="settings-email"
                type="email"
                value={email}
                disabled
                className="mt-1 w-full cursor-not-allowed rounded-lg border border-[var(--border-soft)] bg-[var(--surface-3)] px-3 py-2 text-sm text-[var(--text-muted)]"
              />
              <p className="mt-1 text-[10px] text-[var(--text-muted)]">{t("emailReadOnly")}</p>
            </div>
          </div>
        </div>
      </section>

      {/* Appearance */}
      <section className="card">
        <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
          {t("appearance")}
        </h3>
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm text-[var(--text-primary)]">{t("theme")}</p>
            <p className="text-xs text-[var(--text-muted)]">{t("themeDesc")}</p>
          </div>
          <ThemeToggle showLabel />
        </div>
      </section>

      {/* Connected Accounts */}
      <section className="card">
        <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
          {t("connectedAccounts")}
        </h3>
        <div className="space-y-3">
          <ConnectedAccount provider="Google" icon="G" connected={false} />
          <ConnectedAccount provider="OpenAI" icon="AI" connected={false} />
        </div>
        <p className="mt-3 text-xs text-[var(--text-muted)]">{t("connectedAccountsDesc")}</p>
      </section>

      {/* Change Password */}
      <section className="card">
        <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
          {t("changePassword")}
        </h3>
        <div className="max-w-md space-y-4">
          <div>
            <label className="stat-label" htmlFor="current-pw">{t("currentPassword")}</label>
            <input
              id="current-pw"
              type="password"
              value={currentPassword}
              onChange={(e) => setCurrentPassword(e.target.value)}
              autoComplete="current-password"
              className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
            />
          </div>
          <div>
            <label className="stat-label" htmlFor="new-pw">{t("newPassword")}</label>
            <input
              id="new-pw"
              type="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              autoComplete="new-password"
              className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
            />
          </div>
          <div>
            <label className="stat-label" htmlFor="confirm-pw">{t("confirmPassword")}</label>
            <input
              id="confirm-pw"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              autoComplete="new-password"
              className="mt-1 w-full rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-[var(--color-accent-warm)] focus:outline-none"
            />
          </div>
          <button
            type="button"
            onClick={changePassword}
            disabled={saving || !currentPassword || !newPassword || !confirmPassword}
            className="btn-primary text-xs disabled:opacity-50"
          >
            {saving ? t("saving") : t("updatePassword")}
          </button>
        </div>
      </section>

      {/* Danger Zone */}
      <section className="card border-red-200">
        <h3 className="mb-2 text-sm font-semibold text-red-700">
          {t("dangerZone")}
        </h3>
        <p className="mb-4 text-xs text-red-600/80">
          {t("dangerZoneDesc")}
        </p>
        <div className="flex items-end gap-3">
          <div className="flex-1">
            <label className="stat-label text-red-600" htmlFor="delete-confirm">
              {t("deleteConfirmLabel")}
            </label>
            <input
              id="delete-confirm"
              type="text"
              value={deleteConfirm}
              onChange={(e) => setDeleteConfirm(e.target.value)}
              placeholder={email}
              className="mt-1 w-full rounded-lg border border-red-200 bg-[var(--surface-2)] px-3 py-2 text-sm text-[var(--text-primary)] focus:border-red-400 focus:outline-none"
            />
          </div>
          <button
            type="button"
            onClick={deleteAccount}
            disabled={deleting || deleteConfirm !== email}
            className="rounded-lg bg-red-600 px-5 py-2 text-xs font-semibold text-white hover:bg-red-700 disabled:cursor-not-allowed disabled:opacity-40"
          >
            {deleting ? t("deleting") : t("deleteButton")}
          </button>
        </div>
      </section>
    </div>
  )
}

function ConnectedAccount({ provider, icon, connected }: { provider: string; icon: string; connected: boolean }) {
  return (
    <div className="flex items-center justify-between rounded-lg border border-[var(--border-soft)] px-4 py-3">
      <div className="flex items-center gap-3">
        <div className="flex h-8 w-8 items-center justify-center rounded-full bg-[var(--surface-3)] text-xs font-bold text-[var(--text-secondary)]">
          {icon}
        </div>
        <div>
          <p className="text-sm font-medium text-[var(--text-primary)]">{provider}</p>
          <p className="text-[11px] text-[var(--text-muted)]">
            {connected ? "Connected" : "Not connected"}
          </p>
        </div>
      </div>
      <span className={`inline-flex rounded-full px-2.5 py-0.5 text-[10px] font-semibold ${
        connected ? "bg-emerald-50 text-emerald-700" : "bg-[var(--surface-3)] text-[var(--text-muted)]"
      }`}>
        {connected ? "Connected" : "Disconnected"}
      </span>
    </div>
  )
}
