/**
 * Embed page: /embed/[slug]
 *
 * Renderiza el chat en modo "inline" sin el layout completo del dashboard.
 * Diseñado para ser embebido en webs externas via iframe.
 *
 * Parametros via query string:
 * - mode: teach | support | sales (default: support)
 * - color: hex color para el accent (default: #6366f1)
 */
import { ChatPanel } from "@/components/chat/ChatPanel";

interface EmbedPageProps {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ mode?: string; color?: string }>;
}

export const dynamic = "force-dynamic";

export default async function EmbedPage({ params, searchParams }: EmbedPageProps) {
  const { slug } = await params;
  const { mode, color } = await searchParams;

  // Validar mode
  const validModes = ["teach", "support", "sales"];
  const initialSilo = validModes.includes(mode || "") ? mode! : "support";

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#ffffff",
        padding: "16px",
        fontFamily: "system-ui, -apple-system, sans-serif",
      }}
    >
      <ChatPanel
        slug={slug}
        initialSilo={initialSilo}
      />
    </div>
  );
}