"""LLM-powered email classification and draft generation using Claude.

Classifies incoming emails and generates draft replies in the creator's tone,
using their memory, signatures, and templates.
"""

import json
import logging
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


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
    prompt = CLASSIFICATION_PROMPT.format(
        from_name=from_name or "Desconocido",
        from_email=from_email,
        subject=subject or "(sin asunto)",
        body=body_text or "(sin contenido)",
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
    prompt = DRAFT_PROMPT.format(
        from_name=from_name or "Desconocido",
        from_email=from_email,
        subject=subject or "(sin asunto)",
        body=body_text or "(sin contenido)",
        memory_context=memory_context,
        template_context=template_context,
    )

    try:
        response = llm_callable(prompt)
        data = _parse_json_response(response)
        return DraftResult(
            subject=data.get("subject", f"Re: {subject or 'tu mensaje'}"),
            body=data.get("body", ""),
        )
    except Exception:
        logger.exception("Draft generation failed")
        return DraftResult(
            subject=f"Re: {subject or 'tu mensaje'}",
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
