"""Public webhook for SendGrid Inbound Parse — no auth required.

This endpoint receives raw email data from SendGrid's Inbound Parse feature.
SendGrid sends multipart/form-data with the raw email in the "email" field.

Configure SendGrid's Inbound Parse to POST to:
    https://api.replica.tudominio.com/api/myownclone/public/inbound-email

Authentication:
    If `SENDGRID_INBOUND_WEBHOOK_SECRET` is set, the request must include a
    matching `X-Webhook-Secret` header. Comparison is timing-safe. If the
    secret is unset, the endpoint is open (development only — a warning is
    logged on every request).
"""

import hmac
import ipaddress
import logging
import os
import re
from hashlib import sha256
from typing import Optional

from flask import Blueprint, request, jsonify
from sqlalchemy import select

from api.core.myownclone.email_ai import _get_clone_context, classify_email, generate_draft_reply
from api.core.myownclone.email_processor import parse_inbound_email, resolve_clone_by_domain
from api.core.rate_limit import check_rate_limit, RateLimitConfig
from api.core.security_types import RateLimitKeyType
from api.extensions.ext_database import db
from api.models.myownclone import (
    CloneConfig,
    CreatorMemory,
    CreatorMemoryType,
    EmailInbound,
    EmailTemplate,
    MeetingType_,
    Booking,
    Availability,
)

logger = logging.getLogger(__name__)

myownclone_public_bp = Blueprint("myownclone_public", __name__, url_prefix="/api/myownclone/public")

_WINDOW_SECONDS = 60
_CHAT_LIMIT = 20
_CHAT_SIMPLE_LIMIT = 10
_BOOKING_LIMIT = 10
_MAX_PUBLIC_MESSAGE_LENGTH = 2000
_MAX_VISITOR_FIELD_LENGTH = 200
_MAX_EMAIL_LENGTH = 320

# Memory limit: ~4000 tokens max for memories section (≈16000 chars at ~4 chars/token)
_MAX_MEMORY_CHARS = 16000

# Rate limit configs for Redis-based rate limiting
_CHAT_RATE_LIMIT_CONFIG = RateLimitConfig(limit=_CHAT_LIMIT, window_seconds=_WINDOW_SECONDS)
_CHAT_SIMPLE_RATE_LIMIT_CONFIG = RateLimitConfig(limit=_CHAT_SIMPLE_LIMIT, window_seconds=_WINDOW_SECONDS)
_BOOKING_RATE_LIMIT_CONFIG = RateLimitConfig(limit=_BOOKING_LIMIT, window_seconds=_WINDOW_SECONDS)
_INBOUND_EMAIL_RATE_LIMIT_CONFIG = RateLimitConfig(limit=20, window_seconds=_WINDOW_SECONDS)

# ═══════════════════════════════════════════════════════════════════════════════
# Prompt Injection Protection
# ═══════════════════════════════════════════════════════════════════════════════

# Instruction patterns to strip from user input (prevent prompt injection)
# These patterns match the instruction AND any following content up to sentence end
_INSTRUCTION_PATTERNS = [
    # Direct override attempts - capture entire instruction with following content
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
    r"(?i)\b\x08",  # Backspace character
    r"(?i)\b\u200b",  # Zero-width space
    r"(?i)\b\u200c",  # Zero-width non-joiner
    r"(?i)\b\u200d",  # Zero-width joiner
    r"(?i)\b\U000e0001",  # Cancel character
]

# Compile patterns for efficiency
_COMPILED_INSTRUCTION_PATTERNS = [
    (re.compile(pattern), pattern) for pattern in _INSTRUCTION_PATTERNS
]


def _sanitize_user_input(user_input: str) -> str:
    """Strip instruction patterns from user input to prevent prompt injection.

    Uses regex patterns to detect and remove common prompt injection attempts.
    Returns sanitized input with markers delimiting user content.
    """
    import re
    import unicodedata

    sanitized = user_input
    for compiled_pattern, _ in _COMPILED_INSTRUCTION_PATTERNS:
        sanitized = compiled_pattern.sub("[REDACTED]", sanitized)

    # Normalize unicode homoglyphs that might be used to evade detection
    # Remove combining characters that create visual homoglyphs
    sanitized = sanitized.replace("\u200b", "")  # Remove zero-width spaces
    sanitized = sanitized.replace("\u200c", "")
    sanitized = sanitized.replace("\u200d", "")
    sanitized = sanitized.replace("\u200e", "")  # Left-to-right mark
    sanitized = sanitized.replace("\u200f", "")  # Right-to-left mark
    sanitized = sanitized.replace("\u2028", "")  # Line separator
    sanitized = sanitized.replace("\u2029", "")  # Paragraph separator
    sanitized = sanitized.replace("\ufeff", "")  # BOM
    sanitized = sanitized.replace("\u0335", "")  # Combining short stroke overlay
    sanitized = sanitized.replace("\u0336", "")  # Combining long stroke overlay
    sanitized = sanitized.replace("\u0337", "")  # Combining short solidus overlay
    sanitized = sanitized.replace("\u0338", "")  # Combining long solidus overlay
    sanitized = sanitized.replace("\u0340", "")  # Combining grave tone mark
    sanitized = sanitized.replace("\u0341", "")  # Combining acute tone mark
    sanitized = sanitized.replace("\u0342", "")  # Combining Greek perispomeni
    sanitized = sanitized.replace("\u0343", "")  # Combining Greek koronis
    sanitized = sanitized.replace("\u0344", "")  # Combining Greek dialytika
    sanitized = sanitized.replace("\u0345", "")  # Combining Greek ypogegrammeni
    sanitized = sanitized.replace("\u0346", "")  # Combining Greek rough breathing
    sanitized = sanitized.replace("\u0347", "")  # Combining Greek smooth breathing
    sanitized = sanitized.replace("\u0348", "")  # Combining Greek rough breathing
    sanitized = sanitized.replace("\u0349", "")  # Combining Greek smooth breathing
    sanitized = sanitized.replace("\u0350", "")  # Combining right half ring
    sanitized = sanitized.replace("\u0351", "")  # Combining left half ring
    sanitized = sanitized.replace("\u0352", "")  # Combining fermata
    sanitized = sanitized.replace("\u0353", "")  # Combining X below
    sanitized = sanitized.replace("\u0354", "")  # Combining left arrowhead
    sanitized = sanitized.replace("\u0355", "")  # Combining right arrowhead
    sanitized = sanitized.replace("\u0356", "")  # Combining right half ring above
    sanitized = sanitized.replace("\u0357", "")  # Combining right half ring below
    sanitized = sanitized.replace("\u0358", "")  # Combining dot above right
    sanitized = sanitized.replace("\u0359", "")  # Combining left half ring above
    sanitized = sanitized.replace("\u035a", "")  # Combining left half ring below
    sanitized = sanitized.replace("\u035b", "")  # Combining Greek zeta
    sanitized = sanitized.replace("\u035c", "")  # Combining double acute accent
    sanitized = sanitized.replace("\u035d", "")  # Combining double grave accent
    sanitized = sanitized.replace("\u035e", "")  # Combining candrabindu
    sanitized = sanitized.replace("\u035f", "")  # Combining caron below
    sanitized = sanitized.replace("\u0360", "")  # Combining double tilde
    sanitized = sanitized.replace("\u0361", "")  # Combining double inverted breve
    sanitized = sanitized.replace("\u0362", "")  # Combining double rightwards arrowhead

    # NFD normalize to separate combining characters from base characters
    # then remove any remaining combining marks in the pattern range
    normalized = unicodedata.normalize("NFD", sanitized)
    # Filter out combining characters that could be used for homoglyph attacks
    sanitized = "".join(
        c for c in normalized
        if not unicodedata.combining(c) or unicodedata.category(c) not in ("Mn", "Mc")
    )

    return sanitized


def _filter_output_for_leakage(response_text: str) -> str:
    """Detect and redact memory data leakage in LLM responses.

    Scans response for patterns that might indicate the model is outputting
    internal system information, memories, or prompt content.
    """
    import re

    # Patterns indicating potential memory/prompt leakage
    leakage_patterns = [
        r"Información importante que debes recordar",
        r"(?i)\binformación\s+importante",
        r"(?i)\bmemoria\s+anterior",
        r"(?i)\brecuerda\s+que",
        r"(?i)\bsystem\s+prompt",
        r"(?i)\binstrucciones\s+internas",
        r"(?i)\bprompt\s+original",
        r"(?i)\bconfiguración\s+interna",
    ]

  ***REMOVED***ltered = response_text
    for pattern in leakage_patterns:
        compiled = re.compile(pattern)
        if compiled.search(filtered):
          ***REMOVED***ltered = compiled.sub("[MEMORY-LEAK-REJECTED]", filtered)

    return filtered


_SENDGRID_SECRET = os.environ.get("SENDGRID_INBOUND_WEBHOOK_SECRET", "")
if not _SENDGRID_SECRET:
    logger.warning(
        "SENDGRID_INBOUND_WEBHOOK_SECRET is not set — /inbound-email will accept "
        "unauthenticated requests. Set the secret in production."
    )


def _check_sendgrid_signature() -> bool:
    """Validate the X-Webhook-Secret header against the configured secret.

    Returns True if the secret matches or if no secret is configured (dev mode).
    """
    if not _SENDGRID_SECRET:
        return True
    provided = request.headers.get("X-Webhook-Secret", "")
    if not provided:
        return False
    return hmac.compare_digest(provided, _SENDGRID_SECRET)


def _is_production() -> bool:
    return os.environ.get("FLASK_ENV", "production") == "production"


def _get_trusted_proxy_nets() -> list[ipaddress.IPv4Network | ipaddress.IPv6Network]:
    """Parse TRUSTED_PROXY_IPS env var into a list of networks.

    Expected format: comma-separated CIDR notation, e.g. "10.0.0.0/8,172.16.0.0/12,192.168.0.0/16"
    """
    raw = os.environ.get("TRUSTED_PROXY_IPS", "")
    if not raw:
        return []
    networks = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            networks.append(ipaddress.ip_network(part, strict=False))
        except ValueError:
            logger.warning("Invalid trusted proxy network: %s", part)
    return networks


def _is_from_trusted_proxy(remote_addr: str) -> bool:
    """Check if remote_addr belongs to a trusted proxy network."""
    if not remote_addr or remote_addr == "unknown":
        return False
    trusted_nets = _get_trusted_proxy_nets()
    if not trusted_nets:
        # No trusted proxies configured - assume direct connection
        return False
    try:
        addr = ipaddress.ip_address(remote_addr)
        return any(addr in net for net in trusted_nets)
    except ValueError:
        return False


def _get_validated_client_ip() -> str:
    """Get client IP with proper X-Forwarded-For validation.

    Only trusts X-Forwarded-For header when the request comes from a trusted proxy.
    Otherwise falls back to request.remote_addr.

    Returns:
        The validated client IP address.
    """
    remote_addr = request.remote_addr or "unknown"

    if _is_from_trusted_proxy(remote_addr):
        forwarded_for = request.headers.get("X-Forwarded-For", "")
        if forwarded_for:
            # X-Forwarded-For can be a comma-separated list, take the first (original client)
            client_ip = forwarded_for.split(",")[0].strip()
            if client_ip:
                return client_ip

    # Not from trusted proxy or no X-Forwarded-For - use remote_addr
    return remote_addr


def _rate_limit_response() -> tuple[dict[str, str], int]:
    return {"error": "rate_limit_exceeded"}, 429


def _rate_limit_service_unavailable() -> tuple[dict[str, str], int]:
    """Return 503 when Redis is unavailable (fail-closed)."""
    return {"error": "rate_limit_service_unavailable"}, 503


def _check_rate_limit_public(scope: str, config: RateLimitConfig, slug: str | None = None) -> tuple[bool, int | None]:
    """Check rate limit using Redis with fail-closed behavior.

    Args:
        scope: The endpoint scope (e.g., 'chat_public')
        config: Rate limit configuration
        slug: Optional slug for endpoint-specific limiting

    Returns:
        Tuple of (allowed, remaining): allowed=True if request is allowed,
        allowed=False if rate limited or Redis unavailable. remaining=None
        when Redis is unavailable (fail-closed).
    """
    client_ip = _get_validated_client_ip()
    endpoint = f"/{scope}" if not slug else f"/{scope}/{slug}"

    allowed, remaining, _ = check_rate_limit(
        identifier=client_ip,
        endpoint=endpoint,
        key_type=RateLimitKeyType.PUBLIC,
        config=config,
    )
    return allowed, remaining


def _visitor_id() -> str:
    raw = _get_validated_client_ip()
    user_agent = request.headers.get("User-Agent", "")
    return sha256(f"{raw}:{user_agent}".encode("utf-8")).hexdigest()[:32]


def _conversation_mode_for_silo(silo_value: str) -> str:
    return "pedagogy" if silo_value == "teach" else silo_value


def safe_int(value, default=None):
    """Safely parse integer, return default or raise ValueError."""
    try:
        return int(value)
    except (ValueError, TypeError):
        if default is not None:
            return default
        raise


def _record_question(clone_id: str, question: str) -> None:
    from api.models.myownclone import AnalyticsQuestion

    existing = db.session.execute(
        select(AnalyticsQuestion).where(
            AnalyticsQuestion.clone_id == clone_id,
            AnalyticsQuestion.question == question,
        )
    ).scalar_one_or_none()
    if existing:
        existing.count = (existing.count or 0) + 1
        return

    db.session.add(
        AnalyticsQuestion(
            clone_id=clone_id,
            question=question,
            count=1,
        )
    )


def _persist_chat_turn(
    *,
    clone_id: str,
    conversation_id: str | None,
    silo: str,
    user_message: str,
    assistant_message: str,
    confidence: float,
    sources: list[dict],
) -> str:
    from api.models import Conversation, Message

    conversation = None
    if conversation_id:
        conversation = db.session.execute(
            select(Conversation).where(
                Conversation.id == conversation_id,
                Conversation.clone_id == clone_id,
            )
        ).scalar_one_or_none()

    if not conversation:
        conversation = Conversation(
            clone_id=clone_id,
            visitor_id=_visitor_id(),
            mode=_conversation_mode_for_silo(silo),
        )
        db.session.add(conversation)
        db.session.flush()

    db.session.add(
        Message(
            conversation_id=conversation.id,
            role="user",
            content=user_message,
        )
    )
    db.session.add(
        Message(
            conversation_id=conversation.id,
            role="assistant",
            content=assistant_message,
            confidence=f"{confidence:.2f}",
            sources=sources,
        )
    )
    _record_question(clone_id, user_message)
    db.session.commit()
    return conversation.id


@myownclone_public_bp.route("/inbound-email", methods=["POST"])
def inbound_email():
    if _is_production() and not _SENDGRID_SECRET:
        logger.error("Rejected /inbound-email in production: webhook secret is not configured")
        return jsonify({"error": "webhook secret not configured"}), 503

    if not _check_sendgrid_signature():
        logger.warning(
            "Rejected /inbound-email from %s — invalid or missing X-Webhook-Secret",
            request.remote_addr,
        )
        return jsonify({"error": "unauthorized"}), 401

    # Parse email first to get recipient domain for rate limiting
    raw_email = None

    if request.is_json:
        data = request.get_json(silent=True) or {}
        raw_email = data.get("email") or data.get("raw")
  ***REMOVED***:
        raw_email = request.form.get("email") or request.data

    if not raw_email:
        logger.warning("No email content in webhook payload")
        return jsonify({"status": "no_content"}), 200

    if isinstance(raw_email, str):
        raw_bytes = raw_email.encode("utf-8")
  ***REMOVED***:
        raw_bytes = raw_email if isinstance(raw_email, bytes) else str(raw_email).encode("utf-8")

    try:
        parsed = parse_inbound_email(raw_bytes)
    except Exception:
        logger.exception("Failed to parse inbound email")
        return jsonify({"status": "parse_error"}), 200

    # Rate limit check: per sender IP AND per recipient domain
    # This prevents both individual attackers and mass-emailing to a single domain
    client_ip = _get_validated_client_ip()

    # Check rate limit by sender IP
    allowed, remaining, _ = check_rate_limit(
        identifier=client_ip,
        endpoint="inbound-email",
        key_type=RateLimitKeyType.PUBLIC,
        config=_INBOUND_EMAIL_RATE_LIMIT_CONFIG,
    )
    if not allowed:
        if remaining is None:
            # Redis unavailable - fail closed
            payload, status = _rate_limit_service_unavailable()
      ***REMOVED***:
            payload, status = _rate_limit_response()
        return jsonify(payload), status

    # Check rate limit by recipient domain (prevents mass-emailing to single domain)
    allowed, remaining, _ = check_rate_limit(
        identifier=parsed.to_domain,
        endpoint="inbound-email",
        key_type=RateLimitKeyType.PUBLIC,
        config=_INBOUND_EMAIL_RATE_LIMIT_CONFIG,
    )
    if not allowed:
        if remaining is None:
            # Redis unavailable - fail closed
            payload, status = _rate_limit_service_unavailable()
      ***REMOVED***:
            payload, status = _rate_limit_response()
        return jsonify(payload), status

    clone_id = resolve_clone_by_domain(parsed.to_domain)

    if not clone_id:
        logger.warning("No clone found for domain=%s", parsed.to_domain)
        return jsonify({"status": "no_clone"}), 200

    email = EmailInbound(
        clone_id=clone_id,
        from_email=parsed.from_email,
        from_name=parsed.from_name,
        subject=parsed.subject,
        body_text=parsed.body_text,
        body_html=parsed.body_html,
        status="pending",
    )

    _classify_and_draft(email, clone_id)

    db.session.add(email)
    db.session.commit()

    logger.info(
        "Email stored: id=%s clone=%s from=%s status=%s",
        email.id,
        clone_id,
        parsed.from_email,
        email.status,
    )

    return jsonify({"status": "received", "id": email.id}), 200


@myownclone_public_bp.route("/clones/<string:slug>", methods=["GET"])
def get_clone_public(slug: str):
    """Public endpoint — no auth — returns basic clone info for the public chat page."""
    from sqlalchemy import select
    from api.models.myownclone import CloneConfig

    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.slug == slug,
            CloneConfig.is_active.is_(True),
        )
    ).scalar_one_or_none()

    if not clone:
        return jsonify({"error": "clone not found"}), 404

    return jsonify({
        "id": clone.id,
        "name": clone.name,
        "slug": clone.slug,
        "description": clone.description,
        "avatar_url": clone.avatar_url,
        "personality_tone": clone.personality_tone,
        "language": clone.language,
        "active_modes": clone.active_modes if isinstance(clone.active_modes, list) else [],
        "is_active": clone.is_active,
    }), 200


@myownclone_public_bp.route("/clones/<string:slug>/chat", methods=["POST"])
def chat_public(slug: str):
    """Public chat endpoint — streaming SSE response."""
    import json
    from flask import Response, stream_with_context
    from sqlalchemy import select

    from api.core.retrieval import retrieve_from_silo
    from api.core.myownclone.silos import CloneSilo
    from api.core.rag.retrieval.retrieval_methods import RetrievalMethod
    from api.models.myownclone import CloneConfig, CloneModePrompt

    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.slug == slug,
            CloneConfig.is_active.is_(True),
        )
    ).scalar_one_or_none()

    if not clone:
        return jsonify({"error": "clone not found"}), 404

    allowed, remaining = _check_rate_limit_public("chat_public", _CHAT_RATE_LIMIT_CONFIG, slug)
    if not allowed:
        if remaining is None:
            # Redis unavailable - fail closed
            payload, status = _rate_limit_service_unavailable()
      ***REMOVED***:
            payload, status = _rate_limit_response()
        return jsonify(payload), status

    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    silo_str = data.get("silo", "teach")
    context_id = data.get("context_id")
    conversation_id = data.get("conversation_id")

    if not message:
        return jsonify({"error": "message is required"}), 400

    if len(message) > _MAX_PUBLIC_MESSAGE_LENGTH:
        return jsonify({"error": "message too long"}), 413

    if silo_str not in [s.value for s in CloneSilo]:
        return jsonify({"error": f"invalid silo: {silo_str}"}), 400

    silo = CloneSilo(silo_str)

    mode_prompt = db.session.execute(
        select(CloneModePrompt).where(
            CloneModePrompt.clone_id == clone.id,
            CloneModePrompt.mode == silo.value,
            CloneModePrompt.is_active.is_(True),
        )
    ).scalar_one_or_none()

    system_prompt = mode_prompt.system_prompt if mode_prompt else (
        "Eres un asistente útil. Responde basándote en el contenido proporcionado."
    )

    system_prompt = _add_memories_to_prompt(clone.id, system_prompt)

    result = retrieve_from_silo(
        session=db.session,
        tenant_id=clone.tenant_id,
        clone_id=clone.id,
        query=message,
        silo=silo,
        context_id=context_id,
        top_k=5,
        score_threshold=0.7,
        retrieval_method=RetrievalMethod.SEMANTIC_SEARCH,
    )

    context_text = result.to_context_string() if result.found else ""

    # Sanitize user input to prevent prompt injection
    sanitized_message = _sanitize_user_input(message)

    full_prompt = f"""{system_prompt}

{"CONTENIDO DE REFERENCIA:" if context_text else "No se encontró contenido relevante en la base de conocimiento."}
{context_text}

<<<USER_INPUT>>>
{sanitized_message}
<<<END_USER_INPUT>>>

Pregunta del usuario:"""

    def generate():
        try:
            from api.core.model_manager import ModelManager, ModelType

            model_manager = ModelManager()
            model_instance = model_manager.get_default_model_instance(
                tenant_id=clone.tenant_id, model_type=ModelType.LLM
            )

            accumulated = ""
            for chunk in model_instance.invoke_llm_stream(prompt=full_prompt):
                # Apply output filter to detect memory data leakage
              ***REMOVED***ltered_chunk = _filter_output_for_leakage(chunk)
                accumulated += filtered_chunk
                yield f"data: {json.dumps({'content': filtered_chunk})}\n\n"

            confidence = round(result.scores[0], 2) if result.scores else 0
            sources = [
                {
                    "content": c[:300],
                    "score": round(s, 2),
                    "chunkId": getattr(segment, "metadata", {}).get("segment_id"),
                    "sourceId": getattr(segment, "metadata", {}).get("source_id"),
                    "title": getattr(segment, "metadata", {}).get("source_title"),
                }
                for segment, c, s in zip(result.segments, result.contents, result.scores)
            ]
            persisted_conversation_id = _persist_chat_turn(
                clone_id=clone.id,
                conversation_id=conversation_id,
                silo=silo.value,
                user_message=message,
                assistant_message=accumulated,
                confidence=confidence,
                sources=sources,
            )

            yield f"data: {json.dumps({'content': '', '***REMOVED***': True, 'conversation_id': persisted_conversation_id, 'context_found': result.found, 'silo': silo.value, 'confidence': confidence, 'sources': sources})}\n\n"
            yield "data: [DONE]\n\n"

        except Exception:
            logger.exception("Chat streaming failed for clone=%s", clone.id)
            error_msg = "Lo siento, ha ocurrido un error al procesar tu mensaje. Inténtalo de nuevo."
            yield f"data: {json.dumps({'content': error_msg, 'error': True})}\n\n"
            yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        content_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


def _classify_and_draft(email: EmailInbound, clone_id: str) -> None:
    try:
        from api.core.model_manager import ModelManager, ModelType

        clone = db.session.execute(
            select(CloneConfig).where(CloneConfig.id == clone_id)
        ).scalar_one_or_none()

        if not clone:
            return

        model_manager = ModelManager()

        def llm_call(prompt: str) -> str:
            model_instance = model_manager.get_default_model_instance(
                tenant_id=clone.tenant_id, model_type=ModelType.LLM
            )
            return model_instance.invoke_llm(prompt=prompt)

        classification = classify_email(
            from_name=email.from_name or "",
            from_email=email.from_email or "",
            subject=email.subject or "",
            body_text=email.body_text or "",
            llm_callable=llm_call,
        )
        email.classification = classification.category
        email.labels = [classification.category]

        memory_context, template_context = _get_clone_context(clone_id)

        draft = generate_draft_reply(
            from_name=email.from_name or "",
            from_email=email.from_email or "",
            subject=email.subject or "",
            body_text=email.body_text or "",
            memory_context=memory_context,
            template_context=template_context,
            llm_callable=llm_call,
        )
        email.draft_reply = draft.body

    except Exception:
        logger.exception("Classification/draft failed for email=%s", email.id)
        email.draft_reply = None
        email.classification = "consulta"


def _add_memories_to_prompt(clone_id: str, base_prompt: str) -> str:
    """Add memories to prompt with size limit to prevent unbounded prompt growth.

    Memories are added in priority order (highest first) until the character limit
    is reached. If total memories exceed ~4000 tokens (16000 chars), older/lower
    priority memories are dropped.
    """
    memories = db.session.execute(
        select(CreatorMemory).where(
            CreatorMemory.clone_id == clone_id,
            CreatorMemory.type == CreatorMemoryType.MEMORY,
        ).order_by(CreatorMemory.priority.desc())
    ).scalars().all()

    if not memories:
        return base_prompt

    # Build memories text, respecting character limit
    # Reserve space for the header (~60 chars) and buffer (~200 chars)
    available_chars = _MAX_MEMORY_CHARS - 260

    mem_lines: list[str] = []
    total_chars = 0

    for m in memories:
        line = f"- {m.content}"
        line_chars = len(line) + 1  # +1 for newline

        if total_chars + line_chars > available_chars:
            # Stop adding more memories if we can't fit this one
            break

        mem_lines.append(line)
        total_chars += line_chars

    if mem_lines:
        mem_text = "\n".join(mem_lines)
        base_prompt += f"\n\nInformación importante que debes recordar:\n{mem_text}"

    return base_prompt


@myownclone_public_bp.route("/clones/<string:slug>/chat-simple", methods=["POST"])
def chat_public_simple(slug: str):
    """Public chat endpoint — non-streaming JSON response.

    Simple non-RAG endpoint that delegates to ModelManager.invoke_non_streaming.
    Phase 0.4 — CloneService + ModelInvocationError + clean response shape.
    """
    from flask import current_app

    from api.services.clone_service import CloneService
    from api.core.model_manager import ModelManager, ModelInvocationError

    clone = CloneService.get_public_clone_by_slug(slug)
    if not clone:
        return jsonify({"error": "clone_not_found"}), 404

    allowed, remaining = _check_rate_limit_public("chat_public_simple", _CHAT_SIMPLE_RATE_LIMIT_CONFIG, slug)
    if not allowed:
        if remaining is None:
            # Redis unavailable - fail closed
            payload, status = _rate_limit_service_unavailable()
      ***REMOVED***:
            payload, status = _rate_limit_response()
        return jsonify(payload), status

    payload = request.get_json(silent=True) or {}
    message = (payload.get("message") or "").strip()
    if not message:
        return jsonify({"error": "message_required"}), 400
    if len(message) > _MAX_PUBLIC_MESSAGE_LENGTH:
        return jsonify({"error": "message_too_long"}), 413

    # Reuse the same path as the streaming endpoint, but collect the full reply.
    try:
        reply = ModelManager.invoke_non_streaming(
            tenant_id=clone.tenant_id,
            clone_id=clone.id,
            message=message,
            session_id=payload.get("session_id"),
        )
    except ModelInvocationError as exc:
        current_app.logger.warning("chat_public_simple failed: %s", exc)
        return jsonify({"error": "model_unavailable"}), 502

    return jsonify({
        "slug": slug,
        "reply": reply.text,
        "usage": reply.usage.as_dict() if reply.usage else None,
    })


@myownclone_public_bp.route("/clones/<string:slug>/meeting-types", methods=["GET"])
def get_meeting_types_public(slug: str):
    """Public endpoint — returns active meeting types for a clone."""
    from sqlalchemy import select
    from api.models.myownclone import CloneConfig, MeetingType_

    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.slug == slug,
            CloneConfig.is_active.is_(True),
        )
    ).scalar_one_or_none()
    if not clone:
        return jsonify({"error": "clone not found"}), 404

    types = db.session.execute(
        select(MeetingType_).where(
            MeetingType_.clone_id == clone.id,
            MeetingType_.active.is_(True),
        )
    ).scalars().all()

    return jsonify([
        {
            "id": t.id,
            "name": t.name,
            "duration_minutes": t.duration_minutes,
            "price_cents": t.price_cents,
            "description": t.description,
            "color": t.color,
        }
        for t in types
    ]), 200


@myownclone_public_bp.route("/clones/<string:slug>/bookings", methods=["POST"])
def create_booking_public(slug: str):
    """Public endpoint — creates a booking for a clone."""
    from sqlalchemy import select
    from api.models.myownclone import CloneConfig, Booking, MeetingType_

    allowed, remaining = _check_rate_limit_public("booking_public", _BOOKING_RATE_LIMIT_CONFIG, slug)
    if not allowed:
        if remaining is None:
            # Redis unavailable - fail closed
            payload, status = _rate_limit_service_unavailable()
      ***REMOVED***:
            payload, status = _rate_limit_response()
        return jsonify(payload), status

    data = request.get_json(silent=True) or {}
    try:
        meeting_type_id = safe_int(data.get("meeting_type_id"))
    except ValueError:
        return jsonify({"error": "invalid meeting_type_id"}), 400
    visitor_name = (data.get("visitor_name") or "").strip()
    visitor_email = (data.get("visitor_email") or "").strip().lower()
    booking_date = data.get("date")
    start_time = data.get("start_time")

    if not meeting_type_id or not visitor_name or not visitor_email or not booking_date:
        return jsonify({"error": "meeting_type_id, visitor_name, visitor_email, and date are required"}), 400
    if len(visitor_name) > _MAX_VISITOR_FIELD_LENGTH:
        return jsonify({"error": "visitor_name too long"}), 400
    if len(visitor_email) > _MAX_EMAIL_LENGTH or "@" not in visitor_email:
        return jsonify({"error": "invalid visitor_email"}), 400

    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.slug == slug,
            CloneConfig.is_active.is_(True),
        )
    ).scalar_one_or_none()
    if not clone:
        return jsonify({"error": "clone not found"}), 404

    mt = db.session.execute(
        select(MeetingType_).where(
            MeetingType_.id == meeting_type_id,
            MeetingType_.clone_id == clone.id,
            MeetingType_.active.is_(True),
        )
    ).scalar_one_or_none()
    if not mt:
        return jsonify({"error": "meeting type not found"}), 404

    from datetime import date as date_type, time as time_type
    try:
        bd = date_type.fromisoformat(booking_date)
    except (ValueError, TypeError):
        return jsonify({"error": "invalid date format"}), 400

    st = None
    if start_time:
        try:
            st = time_type.fromisoformat(start_time)
        except (ValueError, TypeError):
            pass

    if bd and st:
        conflict = db.session.execute(
            select(Booking).where(
                Booking.meeting_type_id == meeting_type_id,
                Booking.date == bd,
                Booking.start_time == st,
                Booking.status != "cancelled",
            )
        ).scalar_one_or_none()
        if conflict:
            return jsonify({"error": "Time slot already booked"}), 409

    booking = Booking(
        meeting_type_id=meeting_type_id,
        visitor_name=visitor_name,
        visitor_email=visitor_email,
        date=bd,
        start_time=st,
        status="confirmed",
    )
    db.session.add(booking)
    db.session.commit()

    return jsonify({
        "id": booking.id,
        "status": booking.status,
        "meeting_type": mt.name,
        "visitor_name": visitor_name,
    }), 201


# ═══════════════════════════════════════════════════════════════════════════════
# AI Feedback
# ═══════════════════════════════════════════════════════════════════════════════


@myownclone_public_bp.route("/ai/feedback", methods=["POST"])
def post_ai_feedback():
    """Record feedback on an AI response.

    Request body (JSON):
        invocation_id: str — the ai_invocations.id
        rating: int — +1 (thumbs up) or -1 (thumbs down)
        comment: str (optional) — user comment

    Returns:
        201: {"message": "feedback recorded"}
        400: {"error": "invalid rating"} / {"error": "missing invocation_id"}
        404: {"error": "invocation not found"}
    """
    data = request.get_json() or {}

    invocation_id = data.get("invocation_id")
    if not invocation_id:
        return jsonify({"error": "missing invocation_id"}), 400

    rating = data.get("rating")
    if rating not in (-1, 1):
        return jsonify({"error": "invalid rating, must be +1 or -1"}), 400

    comment = data.get("comment")

    # Get tenant_id from header if provided
    tenant_id = request.headers.get("X-Tenant-Id")

    try:
        from api.core.feedback_collector import get_feedback_collector
        collector = get_feedback_collector()
        collector.record(
            tenant_id=tenant_id,
            invocation_id=invocation_id,
            rating=rating,
            comment=comment,
        )
        return jsonify({"message": "feedback recorded"}), 201
    except Exception as exc:
        logger.exception("Failed to record feedback: %s", exc)
        return jsonify({"error": "failed to record feedback"}), 500

