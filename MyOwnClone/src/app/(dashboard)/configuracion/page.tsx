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

  const embedCode = `<script\n  src="${widgetUrl}"\n  data-clone="${cloneSlug}"\n  async\n></script>`;

  return (
    <div className="space-y-6">
      <header>
        <h1 className="text-2xl font-semibold text-[var(--text-primary)]">
          Embed widget
        </h1>
        <p className="mt-1 text-sm text-[var(--text-muted)]">
          Add your AI clone to any website with a single script tag. No API key needed.
        </p>
      </header>

      <div className="card">
        <h3 className="mb-3 text-sm font-semibold text-[var(--text-primary)]">
          Installation
        </h3>
        <p className="mb-4 text-xs text-[var(--text-muted)]">
          Paste this code right before the closing <code>&lt;/body&gt;</code> tag on your site.
          Replace <code>data-clone</code> with your clone slug from Settings.
        </p>
        <pre className="overflow-x-auto rounded-xl border border-[var(--border-soft)] bg-[var(--surface-2)] p-4 text-xs leading-6 text-[var(--text-primary)]">
{embedCode}
        </pre>
      </div>

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
        <div className="card">
          <h3 className="mb-3 text-sm font-semibold text-[var(--text-primary)]">
            What it does
          </h3>
          <ul className="space-y-2 text-xs text-[var(--text-secondary)]">
            <li>&bull; Adds a floating chat bubble to the bottom-right corner</li>
            <li>&bull; Visitors click to chat with your clone instantly</li>
            <li>&bull; Runs in the browser — no server needed</li>
            <li>&bull; Works on any HTML page, CMS, or site builder</li>
          </ul>
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

      <div className="card">
        <h3 className="mb-3 text-sm font-semibold text-[var(--text-primary)]">
          Customization
        </h3>
        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="border-b border-[var(--border-soft)] text-left">
                <th className="py-2 pr-4 font-semibold text-[var(--text-muted)]">Attribute</th>
                <th className="py-2 pr-4 font-semibold text-[var(--text-muted)]">Description</th>
                <th className="py-2 font-semibold text-[var(--text-muted)]">Default</th>
              </tr>
            </thead>
            <tbody className="text-[var(--text-secondary)]">
              <tr className="border-b border-[var(--border-soft)]">
                <td className="py-2 pr-4 font-mono">data-clone</td>
                <td className="py-2 pr-4">Your clone slug (from Settings)</td>
                <td className="py-2 font-mono">Required</td>
              </tr>
              <tr className="border-b border-[var(--border-soft)]">
                <td className="py-2 pr-4 font-mono">data-position</td>
                <td className="py-2 pr-4">Bubble: bottom-right or bottom-left</td>
                <td className="py-2 font-mono">bottom-right</td>
              </tr>
              <tr>
                <td className="py-2 pr-4 font-mono">data-color</td>
                <td className="py-2 pr-4">Primary color (hex)</td>
                <td className="py-2 font-mono">#7c3aed</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
