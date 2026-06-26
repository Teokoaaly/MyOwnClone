import { NextResponse } from "next/server";
import { auth } from "@/lib/auth";

const MAX_AUDIO_BYTES = 10 * 1024 * 1024;
const ALLOWED_AUDIO_TYPES = new Set([
  "audio/mpeg",
  "audio/mp3",
  "audio/mp4",
  "audio/wav",
  "audio/webm",
  "audio/ogg",
  "audio/x-m4a",
  "audio/m4a",
]);

function isLocalDevHost(hostname: string): boolean {
  return (
    hostname === "localhost" ||
    hostname.startsWith("localhost:") ||
    hostname === "127.0.0.1" ||
    hostname.startsWith("127.0.0.1:")
  );
}

function getServiceApiKey(hostname: string): string | null {
  const configured = process.env.SERVICE_API_KEY?.trim();
  if (configured) return configured;
  if (
    process.env.NODE_ENV !== "production" &&
    (process.env.ALLOW_DEV_SERVICE_KEY === "true" || isLocalDevHost(hostname))
  ) {
    return "dev-api-key-for-proxy";
  }
  return null;
}

function getBackendUrl(hostname: string): string | null {
  const configured = process.env.MYOWNCLONE_API_URL?.trim();
  if (configured) return configured.replace(/\/+$/, "");
  if (process.env.NODE_ENV !== "production" && isLocalDevHost(hostname)) {
    return "http://127.0.0.1:5001";
  }
  return null;
}

export async function POST(request: Request) {
  try {
    const session = await auth();
    if (!session?.user) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const formData = await request.formData();
    const audioFile = formData.get("audio") as File;

    if (!audioFile) {
      return NextResponse.json({ error: "No audio file" }, { status: 400 });
    }

    if (audioFile.size > MAX_AUDIO_BYTES) {
      return NextResponse.json(
        { error: "Audio file too large" },
        { status: 413 },
      );
    }

    if (audioFile.type && !ALLOWED_AUDIO_TYPES.has(audioFile.type)) {
      return NextResponse.json(
        { error: "Unsupported audio type" },
        { status: 415 },
      );
    }

    const url = new URL(request.url);
    const backendUrl = getBackendUrl(url.hostname);
    const serviceApiKey = getServiceApiKey(url.hostname);
    if (!backendUrl || !serviceApiKey) {
      return NextResponse.json(
        { error: "Speech service unavailable" },
        { status: 503 },
      );
    }

    const fd = new FormData();
    fd.append("audio", audioFile);
    fd.append("language", "es");

    const response = await fetch(`${backendUrl}/console/api/myownclone/stt/transcribe`, {
      method: "POST",
      headers: {
        "X-API-Key": serviceApiKey,
        "X-User-Id": String((session.user as any).id || ""),
        "X-User-Email": String(session.user.email || ""),
        "X-User-Role": String((session.user as any).role || ""),
        "X-Tenant-Id": String((session.user as any).tenantId || ""),
      },
      body: fd,
    });

    const data = await response.json().catch(() => ({ error: "Error transcribing audio" }));
    if (!response.ok) {
      return NextResponse.json(
        { error: data.error || "Error transcribing audio" },
        { status: response.status || 502 },
      );
    }

    return NextResponse.json({ text: data.text || "" });
  } catch (error) {
    console.error("STT error:", error);
    return NextResponse.json(
      { error: "Error transcribing audio" },
      { status: 500 }
    );
  }
}
