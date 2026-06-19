import { NextResponse } from "next/server";

const TO_EMAIL = "info.myownclone@gmail.com";

export async function POST(request: Request) {
  try {
    const { name, email, reason, comment } = await request.json();

    if (!name || !email || !reason) {
      return NextResponse.json(
        { error: "Name, email and reason are required" },
        { status: 400 }
      );
    }

    const apiKey = process.env.RESEND_API_KEY;
    if (!apiKey || !apiKey.startsWith("re_")) {
      console.warn("RESEND_API_KEY not configured");
      return NextResponse.json({
        ok: true,
        message: "Request received. We will review it and get back to you soon.",
      });
    }

    const { Resend } = await import("resend");
    const resend = new Resend(apiKey);

    const result = await resend.emails.send({
      from: "MyOwnClone <onboarding@resend.dev>",
      to: TO_EMAIL,
      subject: "Beta access: " + reason + " - " + name,
      replyTo: email,
      html:
        "<h2>New beta access request</h2>" +
        "<p><strong>Name:</strong> " + name + "</p>" +
        "<p><strong>Email:</strong> " + email + "</p>" +
        "<p><strong>Reason:</strong> " + reason + "</p>" +
        "<p><strong>Comment:</strong> " + (comment || "(none)") + "</p>",
    });

    console.log("Resend email sent:", result.data?.id || result);

    return NextResponse.json({
      ok: true,
      message: "Request received. We will review it and get back to you soon.",
    });
  } catch (e: any) {
    console.error("Beta access email error:", e.message || e);
    return NextResponse.json(
      { ok: true, message: "Request received (email delivery pending). We will review it soon." },
      { status: 200 }
    );
  }
}
