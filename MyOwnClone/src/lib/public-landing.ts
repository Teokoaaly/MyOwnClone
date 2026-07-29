import { readFile } from "node:fs/promises";
import { join } from "node:path";

export async function renderPublicLanding(): Promise<Response> {
  const html = await readFile(
    join(process.cwd(), "public", "landing-alternative-source.html"),
    "utf8",
  );
  const renderedHtml = html.replace(
    /\s*<section id="interactive-demo"[\s\S]*?<\/section>/,
    "",
  );

  return new Response(renderedHtml, {
    headers: {
      "Content-Security-Policy":
        "default-src 'self' https: data: blob:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https:; style-src 'self' 'unsafe-inline' https:; img-src 'self' data: blob: https:; font-src 'self' data: https:; media-src 'self' data: blob: https:; connect-src 'self' https: ws: wss:;",
      "Content-Type": "text/html; charset=utf-8",
    },
  });
}
