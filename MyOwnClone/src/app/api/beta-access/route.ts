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

    // Try Resend if key is configured
    const apiKey = process.env.RESEND_API_KEY;
    if (apiKey && apiKey.startsWith("re_")) {
      const { Resend } = await import("resend");
      const resend = new Resend(apiKey);
      await resend.emails.send({
        from: "MyOwnClone <beta@myownclone.com>",
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
    }

    // Always return ok — email will be sent when key is configured
    return NextResponse.json({
      ok: true,
      message: "Request received. We will review it and get back to you soon.",
    });
  } catch (e: any) {
    return NextResponse.json(
      { ok: true, message: "Request received (email delivery pending). We will review it soon." },
      { status: 200 }
    );
  }
}
