import { ChatPanel } from "@/components/chat/ChatPanel";
import { headers } from "next/headers";

interface PageProps {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ context?: string; silo?: string; q?: string }>;
}

export default async function ClonePage({ params, searchParams }: PageProps) {
  const { slug } = await params;
  const { context, silo, q } = await searchParams;
  const headersList = await headers();
  const contextId = context || headersList.get("x-myownclone-context-id") || undefined;
  const defaultSilo = silo || "teach";
  const initialQuery = q?.trim() || undefined;

  const cloneData = await fetchCloneConfig(slug);

  return (
    <main
      className="mx-auto flex h-dvh max-w-4xl flex-col px-4"
      style={{ background: "var(--bg-page)", color: "var(--text-primary)" }}
    >
      {/* Header with logo */}
      <header
        className="flex items-center gap-3 border-b px-2 py-4"
        style={{ borderColor: "var(--border-soft)" }}
      >
        {/* MyOwnClone logo mark */}
        <div className="shrink-0" style={{ width: 36, height: 36 }}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="36"
            height="36"
            viewBox="0 0 32 32"
            aria-label="MyOwnClone"
          >
            <rect x="2" y="2" width="13" height="13" rx="4" fill="#1c1917" />
            <rect x="17" y="2" width="13" height="13" rx="4" fill="#292524" />
            <rect x="2" y="17" width="13" height="13" rx="4" fill="#292524" />
            <rect x="17" y="17" width="13" height="13" rx="4" fill="#1c1917" />
          </svg>
        </div>

        <div className="min-w-0">
          <h1 className="text-lg font-semibold tracking-tight text-[var(--text-primary)] truncate">
            {cloneData?.name || slug}
          </h1>
          {cloneData?.description && (
            <p className="text-xs text-[var(--text-muted)] truncate">
              {cloneData.description}
            </p>
          )}
        </div>

        {/* Powered by */}
        <div className="ml-auto shrink-0 text-right">
          <p className="text-[10px] text-[var(--text-muted)] leading-tight">
            Powered by
          </p>
          <p className="text-[11px] font-medium text-[var(--text-secondary)] leading-tight">
            MyOwnClone
          </p>
        </div>
      </header>

      {/* Chat area */}
      <ChatPanel
        slug={slug}
        initialSilo={defaultSilo}
        contextId={contextId}
        initialQuery={initialQuery}
      />
    </main>
  );
}

async function fetchCloneConfig(slug: string) {
  try {
    const apiUrl = process.env.MYOWNCLONE_API_URL || "http://localhost:5001";
    const res = await fetch(`${apiUrl}/api/myownclone/public/clones/${slug}`, {
      cache: "no-store",
    });
    if (!res.ok) return null;
    return res.json();
  } catch {
    return null;
  }
}
