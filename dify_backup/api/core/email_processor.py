"""Email processing pipeline for the Clonify inbox triage system.

Handles incoming emails from SendGrid Inbound Parse:
1. Parse the raw email (from, subject, body)
2. Classify with Claude (consulta, queja, venta, soporte)
3. Generate draft reply using creator's tone + memory + templates
4. Store in email_inbound table with status=pending
5. Creator reviews and sends via the inbox UI
"""

import json
import logging
import re
from dataclasses import dataclass, field
from email.message import EmailMessage
from email.parser import BytesParser
from email.policy import default as email_default_policy

from sqlalchemy import select

from extensions.ext_database import db
from models.myownclone import CloneConfig, EmailInbound, EmailInboundStatus
from models.myownclone.clone import CloneSilo

logger = logging.getLogger(__name__)


@dataclass
class ParsedEmail:
    from_email: str = ""
    from_name: str = ""
    subject: str = ""
    body_text: str = ""
    body_html: str = ""
    to_domain: str = ""
    clone_id: str | None = None


def parse_inbound_email(raw_body: bytes, content_type: str | None = None) -> ParsedEmail:
    msg = BytesParser(policy=email_default_policy).parsebytes(raw_body)
    result = ParsedEmail()

    result.from_email = str(msg.get("From", ""))
    result.subject = str(msg.get("Subject", ""))

    if result.from_email:
        name_part = result.from_email.split("<")[0].strip().strip('"')
        email_part = result.from_email
        if "<" in result.from_email:
            result.from_email = result.from_email.split("<")[1].split(">")[0].strip()
            result.from_name = name_part if name_part else ""

    result.body_text, result.body_html = _extract_body(msg)

    to_header = str(msg.get("To", ""))
    if "@" in to_header:
        result.to_domain = to_header.split("@")[1].strip()

    return result


def _extract_body(msg: EmailMessage) -> tuple[str, str]:
    text_body = ""
    html_body = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    text_body = payload.decode("utf-8", errors="replace")
            elif content_type == "text/html":
                payload = part.get_payload(decode=True)
                if payload:
                    html_body = payload.decode("utf-8", errors="replace")
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            content = payload.decode("utf-8", errors="replace")
            if msg.get_content_type() == "text/html":
                html_body = content
            else:
                text_body = content

    text_body = text_body.strip()
    html_body = html_body.strip()

    # If only HTML, extract plain text from it
    if not text_body and html_body:
        text_body = _strip_html(html_body)

    # Truncate very long emails to avoid excessive LLM costs
    if text_body and len(text_body) > 4000:
        text_body = text_body[:4000] + "\n\n[... mensaje truncado por longitud]"

    return text_body, html_body


def _strip_html(html: str) -> str:
    text = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = "\n".join(line.strip() for line in text.split("\n") if line.strip())
    return text


def resolve_clone_by_domain(to_domain: str) -> str | None:
    stmt = select(CloneConfig).where(
        CloneConfig.custom_domain == to_domain,
        CloneConfig.is_active.is_(True),
    )
    clone = db.session.execute(stmt).scalar_one_or_none()
    if clone:
        return clone.id
    return None
