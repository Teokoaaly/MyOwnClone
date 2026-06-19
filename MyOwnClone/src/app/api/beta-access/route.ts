import { NextResponse } from "next/server";

const TO_EMAIL = "info.myownclone@gmail.com";

export async function POST(request: Request) {
  try {
    const { name, email, reason, comment } = await request.json();
    if (!name || !email || !reason) {
      return NextResponse.json({ error: "Name, email and reason are required" }, { status: 400 });
    }
    const apiKey = process.env.RESEND_API_KEY;
    if (!apiKey || !apiKey.startsWith("re_")) {
      return NextResponse.json({ ok: true, message: "Request received." });
    }
    const { Resend } = await import("resend");
    const resend = new Resend(apiKey);
    const result = await resend.emails.send({
      from: "MyOwnClone <beta@myownclone.com>",
      to: TO_EMAIL,
      subject: reason + " — " + name,
      replyTo: email,
      html: "<h2>New beta access request</h2><p><strong>Name:</strong> " + name + "</p><p><strong>Email:</strong> " + email + "</p><p><strong>Reason:</strong> " + reason + "</p><p><strong>Comment:</strong> " + (comment || "(none)") + "</p>",
    });
    console.log("Resend OK:", JSON.stringify(result).slice(0, 200));
    return NextResponse.json({ ok: true, message: "Request received. We'll get back to you soon." });
  } catch (e: any) {
    console.error("Resend error:", e.message);
    return NextResponse.json({ ok: true, message: "Request received." }, { status: 200 });
  }
}
