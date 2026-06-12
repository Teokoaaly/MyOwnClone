import { headers } from "next/headers"

export const dynamic = "force-dynamic"

async function getBaseUrl() {
  const headerList = await headers()
  const protocol = headerList.get("x-forwarded-proto") ?? "http"
  const host = headerList.get("x-forwarded-host") ?? headerList.get("host") ?? "localhost:3000"
  return `${protocol}://${host}`
}

export default async function ApiKeysPage() {
  const serviceKeyConfigured = Boolean(process.env.SERVICE_API_KEY?.trim())
  const baseUrl = await getBaseUrl()
  const endpointUrl = `${baseUrl}/api`

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          API Keys
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Connect your workspace programmatically. The secret key is kept server-side and is never shown in full.
        </p>
      </header>

      <div className="grid grid-cols-1 gap-4 xl:grid-cols-3">
        <div className="card xl:col-span-2">
          <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            API access
          </h3>
          <dl className="space-y-4">
            <div>
              <dt className="stat-label">Base URL</dt>
              <dd className="mt-1 rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 font-mono text-sm text-[var(--text-primary)]">
                {endpointUrl}
              </dd>
            </div>
            <div>
              <dt className="stat-label">Authentication header</dt>
              <dd className="mt-1 rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 font-mono text-sm text-[var(--text-primary)]">
                X-API-Key: &lt;your-secret-key&gt;
              </dd>
            </div>
            <div>
              <dt className="stat-label">Proxy status</dt>
              <dd className="mt-1 flex items-center gap-2 text-sm text-[var(--text-primary)]">
                <span
                  className={[
                    "inline-flex rounded-full px-2 py-1 text-xs font-semibold",
                    serviceKeyConfigured
                      ? "bg-emerald-50 text-emerald-700"
                      : "bg-amber-50 text-amber-700",
                  ].join(" ")}
                >
                  {serviceKeyConfigured ? "Configured" : "Missing"}
                </span>
                <span className="text-[var(--text-muted)]">
                  {serviceKeyConfigured
                    ? "The workspace proxy key is available."
                    : "Set SERVICE_API_KEY in the frontend environment to enable authenticated requests."}
                </span>
              </dd>
            </div>
          </dl>
        </div>

        <div className="card">
          <h3 className="mb-4 text-sm font-semibold text-[var(--text-primary)]">
            Security notes
          </h3>
          <ul className="space-y-3 text-sm text-[var(--text-secondary)]">
            <li>Store keys only in environment variables or a secure secret manager.</li>
            <li>Never expose the full secret in the browser or in client-side bundles.</li>
            <li>Rotate the key after sharing environments, demos, or temporary deployments.</li>
          </ul>
        </div>
      </div>

      <div className="card">
        <h3 className="mb-3 text-sm font-semibold text-[var(--text-primary)]">
          Example request
        </h3>
        <pre className="overflow-x-auto rounded-xl border border-[var(--border-soft)] bg-[var(--surface-2)] p-4 text-xs leading-6 text-[var(--text-primary)]">
{`curl -X POST "${endpointUrl}/clone/analytics/overview" \\
  -H "Content-Type: application/json" \\
  -H "X-API-Key: <your-secret-key>"`}
        </pre>
      </div>
    </div>
  )
}
