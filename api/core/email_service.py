"""Email outbound service using Resend API."""

import logging
import os
from string import Formatter
from typing import Optional

import requests

logger = logging.getLogger(__name__)

# SECURITY (P1.10.01 / H-08): protect against str.format(**kwargs)
# format-string injection. ``str.format`` resolves attribute access and
# item access on kwargs values, so a value like ``{0.__class__}`` would
# leak internals. We pre-escape ``{`` and ``}`` in untrusted values so
# they cannot be re-interpreted as format specifiers. The known safe
# keys (``app_url``, ``token``) are passed through unchanged.
_SAFE_EMAIL_TEMPLATE_KEYS = frozenset({
    "app_url",
    "token",
    "reset_url",
    "first_name",
    "clone_name",
    "lead_name",
    "lead_email",
    "sender_name",
    "team_name",
    "from_name",
})


def _escape_format_injection(value):
    """Escape ``{`` and ``}`` so a user-supplied value cannot be interpreted
    as a format specifier when fed to ``str.format``. Other types (int, etc.)
    pass through unchanged via ``str(value)``."""
    if not isinstance(value, str):
        return value
    return value.replace("{", "{{").replace("}", "}}")

RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = os.environ.get("RESEND_FROM_EMAIL", "noreply@myownclone.com")
APP_URL = os.environ.get("APP_URL", "https://myownclone.com")

# Language templates
TEMPLATES = {
    "en": {
        "welcome_subject": "Welcome to MyOwnClone!",
        "welcome_body": """
<h2>Welcome to MyOwnClone!</h2>
<p>Your account has been created successfully.</p>
<p>You can now create your first AI clone and start building your digital persona.</p>
<p><a href="{app_url}/resumen" style="background:#f97316;color:white;padding:10px 20px;border-radius:6px;text-decoration:none;">Go to Dashboard</a></p>
<p>— The MyOwnClone Team</p>
""",
        "password_reset_subject": "Reset your password",
        "password_reset_body": """
<h2>Password Reset</h2>
<p>We received a request to reset your password.</p>
<p><a href="{app_url}/reset-password?token={token}" style="background:#f97316;color:white;padding:10px 20px;border-radius:6px;text-decoration:none;">Reset Password</a></p>
<p>This link expires in 1 hour.</p>
<p>If you didn't request this, ignore this email.</p>
""",
        "billing_receipt_subject": "Payment receipt — MyOwnClone",
        "billing_receipt_body": """
<h2>Payment Received</h2>
<p>Your payment of <strong>{amount}</strong> for the <strong>{plan}</strong> plan has been processed.</p>
<p>Thank you for your subscription!</p>
""",
        "lead_notification_subject": "New lead captured — {clone_name}",
        "lead_notification_body": """
<h2>New Lead</h2>
<p>A new lead was captured from your clone <strong>{clone_name}</strong>.</p>
<p><strong>Email:</strong> {lead_email}</p>
<p><strong>Summary:</strong> {summary}</p>
<p><a href="{app_url}/inbox" style="background:#f97316;color:white;padding:10px 20px;border-radius:6px;text-decoration:none;">View Conversation</a></p>
""",
    },
    "es": {
        "welcome_subject": "¡Bienvenido a MyOwnClone!",
        "welcome_body": """
<h2>¡Bienvenido a MyOwnClone!</h2>
<p>Tu cuenta ha sido creada exitosamente.</p>
<p>Ahora puedes crear tu primer clone de IA y comenzar a construir tu persona digital.</p>
<p><a href="{app_url}/resumen" style="background:#f97316;color:white;padding:10px 20px;border-radius:6px;text-decoration:none;">Ir al Panel</a></p>
<p>— El equipo de MyOwnClone</p>
""",
        "password_reset_subject": "Restablecer tu contraseña",
        "password_reset_body": """
<h2>Restablecer Contraseña</h2>
<p>Recibimos una solicitud para restablecer tu contraseña.</p>
<p><a href="{app_url}/reset-password?token={token}" style="background:#f97316;color:white;padding:10px 20px;border-radius:6px;text-decoration:none;">Restablecer Contraseña</a></p>
<p>Este enlace expira en 1 hora.</p>
<p>Si no solicitaste esto, ignora este email.</p>
""",
        "billing_receipt_subject": "Recibo de pago — MyOwnClone",
        "billing_receipt_body": """
<h2>Pago Recibido</h2>
<p>Tu pago de <strong>{amount}</strong> para el plan <strong>{plan}</strong> ha sido procesado.</p>
<p>¡Gracias por tu suscripción!</p>
""",
        "lead_notification_subject": "Nuevo lead capturado — {clone_name}",
        "lead_notification_body": """
<h2>Nuevo Lead</h2>
<p>Un nuevo lead fue capturado desde tu clone <strong>{clone_name}</strong>.</p>
<p><strong>Email:</strong> {lead_email}</p>
<p><strong>Resumen:</strong> {summary}</p>
<p><a href="{app_url}/inbox" style="background:#f97316;color:white;padding:10px 20px;border-radius:6px;text-decoration:none;">Ver Conversación</a></p>
""",
    },
}


def send_email(
    to: str,
    template_key: str,
    language: str = "en",
    **kwargs,
) -> bool:
    """Send an email using Resend API.

    Returns True on success, False on failure.
    """
    if not RESEND_API_KEY:
        logger.warning("RESEND_API_KEY not configured, skipping email to %s", to)
        return False

    lang = language if language in TEMPLATES else "en"
    templates = TEMPLATES[lang]
    fallback = TEMPLATES["en"]

    subject_tpl = templates.get(f"{template_key}_subject", fallback.get(f"{template_key}_subject", ""))
    body_tpl = templates.get(f"{template_key}_body", fallback.get(f"{template_key}_body", ""))

    if not subject_tpl or not body_tpl:
        logger.warning("Unknown email template: %s", template_key)
        return False

    # P1.10.01 (H-08): escape braces in caller-supplied values so an
    # attacker-controlled string like ``{0.__class__}`` cannot escape into
    # str.format spec resolution. ``app_url`` is a server-controlled
    # constant, so it does not need escaping.
    safe_kwargs = {k: _escape_format_injection(v) for k, v in kwargs.items()}
    # Surface unexpected keys for visibility (mitigate typos like
    # ``leadEmail`` vs ``lead_email`` that would silently render empty).
    unexpected = set(safe_kwargs) - _SAFE_EMAIL_TEMPLATE_KEYS
    if unexpected:
        logger.warning(
            "Email template %s received unexpected keys: %s",
            template_key, sorted(unexpected),
        )

    subject = subject_tpl.format(**safe_kwargs) if safe_kwargs else subject_tpl
    html_body = (
        body_tpl.format(app_url=APP_URL, **safe_kwargs)
        if safe_kwargs
        else body_tpl.format(app_url=APP_URL)
    )

    try:
        resp = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "from": FROM_EMAIL,
                "to": [to],
                "subject": subject,
                "html": html_body,
            },
            timeout=10,
        )
        if resp.status_code in (200, 201):
            logger.info("Email sent to %s: %s", to, subject)
            return True
        else:
            logger.error("Resend API error %s: %s", resp.status_code, resp.text)
            return False
    except Exception:
        logger.exception("Failed to send email to %s", to)
        return False


def send_welcome_email(to: str, language: str = "en") -> bool:
    return send_email(to, "welcome", language=language)


def send_password_reset(to: str, token: str, language: str = "en") -> bool:
    return send_email(to, "password_reset", language=language, token=token)


def send_billing_receipt(to: str, amount: str, plan: str, language: str = "en") -> bool:
    return send_email(to, "billing_receipt", language=language, amount=amount, plan=plan)


def send_lead_notification(
    to: str,
    clone_name: str,
    lead_email: str,
    summary: str,
    language: str = "en",
) -> bool:
    return send_email(
        to, "lead_notification", language=language,
        clone_name=clone_name, lead_email=lead_email, summary=summary,
    )
