import { headers } from "next/headers";

export const dynamic = "force-dynamic";

async function getBaseUrl() {
  const headerList = await headers();
  const host = headerList.get("x-forwarded-host") ?? headerList.get("host") ?? "myownclone.com";
  const protocol = headerList.get("x-forwarded-proto") ?? "https";
  return `${protocol}://${host}`;
}

export default async function EmbedPage() {
  const baseUrl = await getBaseUrl();
  const widgetUrl = `${baseUrl}/widget.js`;
  const cloneSlug = "myownclone-demo";
  const publicCloneUrl = `${baseUrl}/${cloneSlug}`;

  const embedSmall = `<script src="${widgetUrl}" data-clone="${cloneSlug}" data-size="small" async></script>`;
  const embedMedium = `<script src="${widgetUrl}" data-clone="${cloneSlug}" async></script>`;
  const embedLarge = `<script src="${widgetUrl}" data-clone="${cloneSlug}" data-size="large" async></script>`;

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Embed widget
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Add your AI clone to any website. Pick a size, paste the code, done.
        </p>
      </header>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        {/* Small */}
        <div className="card">
          <h3 className="mb-2 text-sm font-semibold text-[var(--text-primary)]">Small · 40px</h3>
          <p className="mb-3 text-xs text-[var(--text-muted)]">Discreet corner button</p>
          <pre className="overflow-x-auto rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2.5 text-[11px] leading-5 text-[var(--text-primary)]">
{embedSmall}
          </pre>
          <p className="mt-1.5 text-[10px] text-[var(--text-muted)] font-mono truncate">{widgetUrl}</p>
        </div>

        {/* Medium */}
        <div className="card ring-1 ring-[var(--color-accent-warm)]/30">
          <div className="flex items-center gap-2 mb-2">
            <h3 className="text-sm font-semibold text-[var(--text-primary)]">Medium · 56px</h3>
            <span className="rounded bg-[var(--color-accent-warm)]/10 px-1.5 py-0.5 text-[10px] font-medium text-[var(--color-accent-warm)]">Default</span>
          </div>
          <p className="mb-3 text-xs text-[var(--text-muted)]">Balanced for most sites</p>
          <pre className="overflow-x-auto rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2.5 text-[11px] leading-5 text-[var(--text-primary)]">
{embedMedium}
          </pre>
          <p className="mt-1.5 text-[10px] text-[var(--text-muted)] font-mono truncate">{widgetUrl}</p>
        </div>

        {/* Large */}
        <div className="card">
          <h3 className="mb-2 text-sm font-semibold text-[var(--text-primary)]">Large · 72px</h3>
          <p className="mb-3 text-xs text-[var(--text-muted)]">High visibility</p>
          <pre className="overflow-x-auto rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2.5 text-[11px] leading-5 text-[var(--text-primary)]">
{embedLarge}
          </pre>
          <p className="mt-1.5 text-[10px] text-[var(--text-muted)] font-mono truncate">{widgetUrl}</p>
        </div>
      </div>

      <div className="card">
        <h3 className="mb-3 text-sm font-semibold text-[var(--text-primary)]">
          Customization
        </h3>
        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="border-b border-[var(--border-soft)] text-left">
                <th className="py-2 pr-4 font-semibold text-[var(--text-muted)]">Attribute</th>
                <th className="py-2 pr-4 font-semibold text-[var(--text-muted)]">Values</th>
                <th className="py-2 font-semibold text-[var(--text-muted)]">Default</th>
              </tr>
            </thead>
            <tbody className="text-[var(--text-secondary)]">
              <tr className="border-b border-[var(--border-soft)]">
                <td className="py-2 pr-4 font-mono">data-clone</td>
                <td className="py-2 pr-4">Your clone slug</td>
                <td className="py-2 font-mono text-[var(--color-accent-red)]">Required</td>
              </tr>
              <tr className="border-b border-[var(--border-soft)]">
                <td className="py-2 pr-4 font-mono">data-size</td>
                <td className="py-2 pr-4">small, medium, large</td>
                <td className="py-2 font-mono">medium</td>
              </tr>
              <tr className="border-b border-[var(--border-soft)]">
                <td className="py-2 pr-4 font-mono">data-position</td>
                <td className="py-2 pr-4">bottom-right, bottom-left</td>
                <td className="py-2 font-mono">bottom-right</td>
              </tr>
              <tr>
                <td className="py-2 pr-4 font-mono">data-color</td>
                <td className="py-2 pr-4">Hex color (e.g. #1c1917)</td>
                <td className="py-2 font-mono">#7c3aed</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div className="card">
        <h3 className="mb-3 text-sm font-semibold text-[var(--text-primary)]">
          Public clone page
        </h3>
        <p className="mb-3 text-xs text-[var(--text-muted)]">
          Share this link directly. No embed needed.
        </p>
        <pre className="overflow-x-auto rounded-lg border border-[var(--border-soft)] bg-[var(--surface-2)] px-3 py-2 font-mono text-xs text-[var(--text-primary)]">
{publicCloneUrl}
        </pre>
        <a
          href={publicCloneUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-3 inline-block text-xs text-[var(--color-accent-blue)] hover:underline"
        >
          Open in new tab &nearr;
        </a>
      </div>
    </div>
  );
}
