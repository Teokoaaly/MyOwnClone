import "server-only";
import { Resend } from "resend";

let _resend: any = null; const getResend = () => { if (!_resend) _resend = new Resend(process.env.RESEND_API_KEY); return _resend; };
const fromEmail = process.env.RESEND_FROM_EMAIL ?? "noreply@myownclone.com";

function escapeHtml(value: string): string {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function sanitizeMeetingUrl(value: string | undefined): string | null {
  if (!value) return null;
  try {
    const parsed = new URL(value);
    if (parsed.protocol === "http:" || parsed.protocol === "https:") {
      return parsed.toString();
    }
  } catch {
  }
  return null;
}

export async function sendEmail(params: {
  to: string | string[];
  subject: string;
  html: string;
  replyTo?: string;
}) {
  return getResend().emails.send({
    from: fromEmail,
    to: params.to,
    subject: params.subject,
    html: params.html,
    replyTo: params.replyTo,
  });
}

export async function sendBookingConfirmation(params: {
  to: string;
  visitorName: string;
  cloneName: string;
  date: string;
  time: string;
  meetingUrl?: string;
}) {
  const visitorName = escapeHtml(params.visitorName);
  const cloneName = escapeHtml(params.cloneName);
  const date = escapeHtml(params.date);
  const time = escapeHtml(params.time);
  const meetingUrl = sanitizeMeetingUrl(params.meetingUrl);

  return sendEmail({
    to: params.to,
    subject: `Confirmacion de reunion con ${cloneName}`,
    html: `
      <h1>Reunion confirmada</h1>
      <p>Hola ${visitorName},</p>
      <p>Tu reunion con <strong>${cloneName}</strong> esta programada para:</p>
      <p><strong>${date}</strong> a las <strong>${time}</strong></p>
      ${meetingUrl ? `<p>Enlace de la videollamada: <a href="${meetingUrl}">${meetingUrl}</a></p>` : ""}
      <p>Nos vemos pronto.</p>
    `,
  });
}

export async function sendLoginVerificationCode(params: {
  to: string;
  url: string;
}) {
  return sendEmail({
    to: params.to,
    subject: "Accede a tu cuenta de MyOwnClone",
    html: `
      <div style="text-align:center;padding:40px 20px">
        <h1 style="color:#7c3aed">MyOwnClone</h1>
        <p>Haz clic en el botón de abajo para acceder a tu cuenta:</p>
        <a href="${params.url}" style="display:inline-block;padding:12px 24px;background:#7c3aed;color:white;text-decoration:none;border-radius:8px;font-weight:bold;margin:20px 0">
          Acceder a mi cuenta
        </a>
        <p style="color:#888;font-size:12px">Si no solicitaste este enlace, ignora este email.</p>
      </div>
    `,
  });
}
