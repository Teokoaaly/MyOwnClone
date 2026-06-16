"""LLM-powered email classification and draft generation using Claude.

Classifies incoming emails and generates draft replies in the creator's tone,
using their memory, signatures, and templates.
"""

import json
import logging
import re
import unicodedata
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

# ═══════════════════════════════════════════════════════════════════════════════
# Email Content Sanitization (Prompt Injection Protection)
# ═══════════════════════════════════════════════════════════════════════════════

# Instruction patterns to strip from email content (prevent prompt injection)
_EMAIL_INJECTION_PATTERNS = [
    r"(?i)\bignore\s+(all\s+)?previous\s+(instructions?|directions?)[^.!?]*(?:[.!?]|$)",
    r"(?i)\bdisregard\s+(all\s+)?(your|previous)[^.!?]*(?:[.!?]|$)",
    r"(?i)\bforget\s+(everything|all|what\s+you\s+said)[^.!?]*(?:[.!?]|$)",
    r"(?i)\bnew\s+instruction[s]?[^.!?]*(?:[.!?]|$)",
    r"(?i)\bsystem\s*:[^.!?]*(?:[.!?]|$)",
    r"(?i)\byou\s+are\s+now\s+[^.!?]*(?:[.!?]|$)",
    r"(?i)\bchange\s+your\s+(behavior|response)\s+to\s*[^.!?]*(?:[.!?]|$)",
    r"(?i)\boutput\s+your\s+(full\s+)?system\s+prompt[s]?[^.!?]*(?:[.!?]|$)",
    r"(?i)\bwhat\s+is\s+your\s+(system\s+)?prompt[s]?[^.!?]*(?:[.!?]|$)",
    r"(?i)\btell\s+me\s+your\s+instructions[s]?[^.!?]*(?:[.!?]|$)",
    r"(?i)\bprint\s*\(\s*['\"](INJECTED|PWNED|HACKED)\s*['\"]\s*\)",
    r"(?i)\bprint\s*\(\s*['\"]INJECT",
]

_COMPILED_EMAIL_INJECTION_PATTERNS = [
    (re.compile(pattern), pattern) for pattern in _EMAIL_INJECTION_PATTERNS
]


def _sanitize_email_content(content: str) -> str:
    """Sanitize email content to prevent prompt injection attacks.

    Removes:
    - HTML tags
    - Instruction override patterns
    - Unicode homoglyph attacks (zero-width spaces, combining characters)

    Wraps content in delimiters to separate it from system prompt.
    """
    if not content:
        return ""

    sanitized = content

    # Step 1: Strip HTML tags
    sanitized = re.sub(r"<[^>]+>", " ", sanitized)

    # Step 2: Remove prompt injection patterns
    for compiled_pattern, _ in _COMPILED_EMAIL_INJECTION_PATTERNS:
        sanitized = compiled_pattern.sub("[REDACTED]", sanitized)

    # Step 3: Remove unicode homoglyph attacks
    sanitized = sanitized.replace("\u200b", "")
    sanitized = sanitized.replace("\u200c", "")
    sanitized = sanitized.replace("\u200d", "")
    sanitized = sanitized.replace("\ufeff", "")

    # Step 4: NFD normalize and remove combining characters
    normalized = unicodedata.normalize("NFD", sanitized)
    sanitized = "".join(
        c for c in normalized
        if not unicodedata.combining(c) or unicodedata.category(c) not in ("Mn", "Mc")
    )

    # Step 5: Clean up excessive whitespace
    sanitized = re.sub(r"\s+", " ", sanitized).strip()

    return sanitized


def _wrap_email_content(content: str) -> str:
    """Wrap sanitized email content in delimiters for LLM prompts."""
    if not content:
        return "(sin contenido)"
    return f"""<<<EMAIL_CONTENT>>>
{content}
<<<END_EMAIL_CONTENT>>>"""


@dataclass
class ClassificationResult:
    category: str = "consulta"
    urgency: str = "normal"
    summary: str = ""
    sentiment: str = "neutral"


@dataclass
class DraftResult:
    subject: str = ""
    body: str = ""
    used_templates: list[str] = field(default_factory=list)


CLASSIFICATION_PROMPT = """Clasifica el siguiente email recibido por un creador de contenido.

Responde ÚNICAMENTE en formato JSON válido, sin texto adicional:
{
  "category": "consulta|queja|venta|soporte|otro",
  "urgency": "baja|normal|alta",
  "summary": "resumen de 1 frase en español",
  "sentiment": "positivo|neutral|negativo"
}

Email:
De: {from_name} <{from_email}>
Asunto: {subject}

{body}"""


DRAFT_PROMPT = """Eres el asistente de IA de un creador de contenido. Tu trabajo es redactar
una respuesta profesional a este email en el tono y estilo del creador.

{memory_context}

{template_context}

Email recibido:
De: {from_name} <{from_email}>
Asunto: {subject}

{body}

Redacta una respuesta en español. Sé amable, directo/a y profesional.
Usa la firma proporcionada al final SIEMPRE.

Responde ÚNICAMENTE con JSON:
{{
  "subject": "Re: asunto original",
  "body": "cuerpo de la respuesta en texto plano (máximo 500 palabras)"
}}
NO incluyas markdown ni HTML en el body."""


def classify_email(
    from_name: str,
    from_email: str,
    subject: str,
    body_text: str,
    llm_callable,
) -> ClassificationResult:
    # Sanitize all email content to prevent prompt injection
    sanitized_body = _sanitize_email_content(body_text or "")
    sanitized_subject = _sanitize_email_content(subject or "")

    prompt = CLASSIFICATION_PROMPT.format(
        from_name=from_name or "Desconocido",
        from_email=from_email,
        subject=sanitized_subject or "(sin asunto)",
        body=_wrap_email_content(sanitized_body),
    )

    try:
        response = llm_callable(prompt)
        data = _parse_json_response(response)
        return ClassificationResult(
            category=data.get("category", "consulta"),
            urgency=data.get("urgency", "normal"),
            summary=data.get("summary", ""),
            sentiment=data.get("sentiment", "neutral"),
        )
    except Exception:
        logger.exception("Email classification failed")
        return ClassificationResult()


def generate_draft_reply(
    from_name: str,
    from_email: str,
    subject: str,
    body_text: str,
    memory_context: str,
    template_context: str,
    llm_callable,
) -> DraftResult:
    # Sanitize all email content to prevent prompt injection
    sanitized_body = _sanitize_email_content(body_text or "")
    sanitized_subject = _sanitize_email_content(subject or "")

    prompt = DRAFT_PROMPT.format(
        from_name=from_name or "Desconocido",
        from_email=from_email,
        subject=sanitized_subject or "(sin asunto)",
        body=_wrap_email_content(sanitized_body),
        memory_context=memory_context,
        template_context=template_context,
    )

    try:
        response = llm_callable(prompt)
        data = _parse_json_response(response)
        return DraftResult(
            subject=data.get("subject", f"Re: {sanitized_subject or 'tu mensaje'}"),
            body=data.get("body", ""),
        )
    except Exception:
        logger.exception("Draft generation failed")
        return DraftResult(
            subject=f"Re: {sanitized_subject or 'tu mensaje'}",
            body="Gracias por tu mensaje. Lo revisaré y te responderé en breve.\n\nSaludos cordiales.",
        )


def _parse_json_response(text: str) -> dict:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    if "```json" in text:
        start = text.index("```json") + 7
        end = text.index("```", start)
        return json.loads(text[start:end].strip())
    if "```" in text:
        start = text.index("```") + 3
        end = text.index("```", start)
        return json.loads(text[start:end].strip())
    brace_start = text.find("{")
    brace_end = text.rfind("}")
    if brace_start != -1 and brace_end != -1:
        return json.loads(text[brace_start:brace_end + 1])
    raise ValueError(f"Cannot parse JSON from: {text[:200]}")


def _get_clone_context(clone_id: str) -> tuple[str, str]:
    from sqlalchemy import select

    from extensions.ext_database import db
    from models.myownclone import CreatorMemory, CreatorMemoryType, EmailTemplate

    memories = db.session.execute(
        select(CreatorMemory).where(
            CreatorMemory.clone_id == clone_id,
            CreatorMemory.type.in_([CreatorMemoryType.MEMORY, CreatorMemoryType.SIGNATURE]),
        ).order_by(CreatorMemory.priority.desc())
    ).scalars().all()

    memory_parts: list[str] = []
    signature_parts: list[str] = []

    for m in memories:
        if m.type == CreatorMemoryType.MEMORY:
            memory_parts.append(f"- {m.content}")
        elif m.type == CreatorMemoryType.SIGNATURE:
            signature_parts.append(m.content)

    memory_context = ""
    if memory_parts:
        memory_context = (
            "Información relevante sobre el creador (úsala para contextualizar):\n"
            + "\n".join(memory_parts)
        )

    signature_text = "\n\n---\n" + "\n".join(signature_parts) if signature_parts else ""
    template_context = f"FIRMA A USAR: {signature_text}" if signature_text else ""

    templates = db.session.execute(
        select(EmailTemplate).where(EmailTemplate.clone_id == clone_id)
    ).scalars().all()
    if templates:
        template_context += "\n\nPlantillas disponibles (úsalas si son relevantes):\n"
        for t in templates:
            template_context += f"[{t.name}]: {t.body}\n"

    return memory_context, template_context
