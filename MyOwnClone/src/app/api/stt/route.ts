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

    if (!process.env.OPENAI_API_KEY) {
      return NextResponse.json(
        { error: "Speech service unavailable" },
        { status: 503 },
      );
    }

    const openai = await fetch(
      "https://api.openai.com/v1/audio/transcriptions",
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
        },
        body: (() => {
          const fd = new FormData();
          fd.append("file", audioFile);
          fd.append("model", "whisper-1");
          fd.append("language", "es");
          return fd;
        })(),
      }
    );

    const data = await openai.json();

    if (!openai.ok) {
      return NextResponse.json(
        { error: "Error transcribing audio" },
        { status: openai.status || 502 },
      );
    }

    return NextResponse.json({ text: data.text });
  } catch (error) {
    console.error("STT error:", error);
    return NextResponse.json(
      { error: "Error transcribing audio" },
      { status: 500 }
    );
  }
}
