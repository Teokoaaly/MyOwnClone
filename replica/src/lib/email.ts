import "server-only";
import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);
const fromEmail = process.env.RESEND_FROM_EMAIL ?? "noreply@replica.tudominio.com";

export async function sendEmail(params: {
  to: string | string[];
  subject: string;
  html: string;
  replyTo?: string;
}) {
  return resend.emails.send({
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
  return sendEmail({
    to: params.to,
    subject: `Confirmación de reunión con ${params.cloneName}`,
    html: `
      <h1>¡Reunión confirmada!</h1>
      <p>Hola ${params.visitorName},</p>
      <p>Tu reunión con <strong>${params.cloneName}</strong> está programada para:</p>
      <p><strong>${params.date}</strong> a las <strong>${params.time}</strong></p>
      ${params.meetingUrl ? `<p>Enlace de la videollamada: <a href="${params.meetingUrl}">${params.meetingUrl}</a></p>` : ""}
      <p>¡Nos vemos pronto!</p>
    `,
  });
}

export async function sendLoginVerificationCode(params: {
  to: string;
  url: string;
}) {
  return sendEmail({
    to: params.to,
    subject: "Accede a tu cuenta de Réplica",
    html: `
      <div style="text-align:center;padding:40px 20px">
        <h1 style="color:#7c3aed">Réplica</h1>
        <p>Haz clic en el botón de abajo para acceder a tu cuenta:</p>
        <a href="${params.url}" style="display:inline-block;padding:12px 24px;background:#7c3aed;color:white;text-decoration:none;border-radius:8px;font-weight:bold;margin:20px 0">
          Acceder a mi cuenta
        </a>
        <p style="color:#888;font-size:12px">Si no solicitaste este enlace, ignora este email.</p>
      </div>
    `,
  });
}
