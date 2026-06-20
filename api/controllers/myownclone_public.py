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
import logging
import os
import time
from collections import defaultdict
from hashlib import sha256

from flask import Blueprint, request, jsonify, current_app
from sqlalchemy import select

from api.core.myownclone.email_ai import _get_clone_context, classify_email, generate_draft_reply
from api.core.myownclone.email_processor import parse_inbound_email, resolve_clone_by_domain
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

# Internal endpoints are mounted under /api/myownclone/internal and are only
# reachable from the Next.js proxy (X-API-Key) or trusted services. They are
# NOT registered under the public prefix to keep the public surface small.
myownclone_internal_bp = Blueprint("myownclone_internal", __name__, url_prefix="/api/myownclone/internal")

_WINDOW_SECONDS = 60
_CHAT_LIMIT = 20
_CHAT_SIMPLE_LIMIT = 10
_BOOKING_LIMIT = 10
_MAX_PUBLIC_MESSAGE_LENGTH = 2000
_MAX_VISITOR_FIELD_LENGTH = 200
_MAX_EMAIL_LENGTH = 320
_public_rate_limit_store: dict[str, list[float]] = defaultdict(list)


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


def _rate_limit_key(scope: str, slug: str | None = None) -> str:
    client_ip = (request.headers.get("X-Forwarded-For", "") or request.remote_addr or "unknown").split(",")[0].strip()
    parts = [scope, client_ip]
    if slug:
        parts.append(slug)
    return ":".join(parts)


def _consume_rate_limit(scope: str, limit: int, slug: str | None = None) -> bool:
    key = _rate_limit_key(scope, slug)
    now = time.time()
    recent = [stamp for stamp in _public_rate_limit_store[key] if now - stamp < _WINDOW_SECONDS]
    if len(recent) >= limit:
        _public_rate_limit_store[key] = recent
        return False
    recent.append(now)
    _public_rate_limit_store[key] = recent
    return True


def _rate_limit_response() -> tuple[dict[str, str], int]:
    return {"error": "rate_limit_exceeded"}, 429


def _visitor_id() -> str:
    raw = (request.headers.get("X-Forwarded-For", "") or request.remote_addr or "unknown").split(",")[0].strip()
    user_agent = request.headers.get("User-Agent", "")
    return sha256(f"{raw}:{user_agent}".encode("utf-8")).hexdigest()[:32]


def _conversation_mode_for_silo(silo_value: str) -> str:
    return "pedagogy" if silo_value == "teach" else silo_value


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


def _record_knowledge_gap(clone_id: str, question: str) -> None:
    """Track unanswered questions so the creator can fill knowledge holes.

    Increments count if the same question keeps missing context, so the
    analytics dashboard can surface the most urgent gaps."""
    from api.models.myownclone import AnalyticsGap

    existing = db.session.execute(
        select(AnalyticsGap).where(
            AnalyticsGap.clone_id == clone_id,
            AnalyticsGap.question == question,
            AnalyticsGap.status == "open",
        )
    ).scalar_one_or_none()
    if existing:
        existing.count = (existing.count or 0) + 1
        return
    db.session.add(
        AnalyticsGap(
            clone_id=clone_id,
            question=question,
            count=1,
            status="open",
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

    raw_email = None

    if request.is_json:
        data = request.get_json(silent=True) or {}
        raw_email = data.get("email") or data.get("raw")
    else:
        raw_email = request.form.get("email") or request.data

    if not raw_email:
        logger.warning("No email content in webhook payload")
        return jsonify({"status": "no_content"}), 200

    if isinstance(raw_email, str):
        raw_bytes = raw_email.encode("utf-8")
    else:
        raw_bytes = raw_email if isinstance(raw_email, bytes) else str(raw_email).encode("utf-8")

    try:
        parsed = parse_inbound_email(raw_bytes)
    except Exception:
        logger.exception("Failed to parse inbound email")
        return jsonify({"status": "parse_error"}), 200

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

    if not _consume_rate_limit("chat_public", _CHAT_LIMIT, slug):
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

    if result.found:
        context_block = f"CONTENIDO DE REFERENCIA:\n{context_text}"
    else:
        # Anti-hallucination: when no grounded context exists, force the LLM
        # to admit it lacks information instead of inventing an answer.
        # Also log a knowledge gap so the creator can see what's missing.
        context_block = (
            "No se encontró contenido relevante en la base de conocimiento.\n"
            "IMPORTANTE: Si no dispones de información verificable para "
            "responder, di claramente 'No tengo información sobre eso en "
            "mi contenido' y NO inventes datos."
        )
        _record_knowledge_gap(clone.id, message)

    full_prompt = f"""{system_prompt}

{context_block}

Pregunta del usuario: {message}"""

    # Per-mode temperature override (FASE 3.1). Falls back to env defaults.
    from api.core.model_manager import GenerationParams
    mode_temperature = float(mode_prompt.temperature) if (
        mode_prompt and mode_prompt.temperature is not None
    ) else None
    gen_params = GenerationParams.from_env()
    if mode_temperature is not None:
        gen_params = GenerationParams(
            temperature=max(0.0, min(2.0, mode_temperature)),
            max_tokens=gen_params.max_tokens,
            top_p=gen_params.top_p,
        )

    def generate():
        try:
            from api.core.model_manager import ModelManager, ModelType

            model_manager = ModelManager()
            model_instance = model_manager.get_default_model_instance(
                tenant_id=clone.tenant_id,
                model_type=ModelType.LLM,
                params=gen_params,
            )

            accumulated = ""
            for chunk in model_instance.invoke_llm_stream(prompt=full_prompt):
                accumulated += chunk
                yield f"data: {json.dumps({'content': chunk})}\n\n"

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

            yield f"data: {json.dumps({'content': '', 'done': True, 'conversation_id': persisted_conversation_id, 'context_found': result.found, 'silo': silo.value, 'confidence': confidence, 'sources': sources})}\n\n"
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
    memories = db.session.execute(
        select(CreatorMemory).where(
            CreatorMemory.clone_id == clone_id,
            CreatorMemory.type == CreatorMemoryType.MEMORY,
        ).order_by(CreatorMemory.priority.desc())
    ).scalars().all()

    if memories:
        mem_text = "\n".join(f"- {m.content}" for m in memories)
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

    if not _consume_rate_limit("chat_public_simple", _CHAT_SIMPLE_LIMIT, slug):
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

    if not _consume_rate_limit("booking_public", _BOOKING_LIMIT, slug):
        payload, status = _rate_limit_response()
        return jsonify(payload), status

    data = request.get_json(silent=True) or {}
    meeting_type_id = data.get("meeting_type_id")
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


# ── Internal endpoints (service-to-service: Next.js proxy → backend) ────────
# These are mounted under /api/myownclone/internal and protected by X-API-Key
# (the same SERVICE_API_KEY the proxy already sends). They exist so the
# frontend does NOT need to duplicate the OpenAI key: the backend owns all
# LLM/embedding credentials.


def _require_service_key() -> tuple[dict, int] | None:
    """Validate X-API-Key against SERVICE_API_KEY. Returns an error response
    tuple if invalid, or None if the caller is authorized."""
    import hmac
    import os
    from flask import request

    configured = os.environ.get("SERVICE_API_KEY", "").strip()
    if not configured:
        return {"error": "service key not configured"}, 503
    provided = request.headers.get("X-API-Key", "")
    if not provided or not hmac.compare_digest(provided, configured):
        return {"error": "unauthorized"}, 401
    return None


@myownclone_internal_bp.route("/embed", methods=["POST"])
def embed_texts():
    """Embed a batch of texts using the active EmbeddingService.

    Called by the Next.js ingestion route (MyOwnClone/src/app/api/clone/sources)
    so that the OPENAI_API_KEY only lives on the backend.

    Request:
        Headers: X-API-Key: <SERVICE_API_KEY>
        Body:    {"texts": ["...", "..."], "tenant_id": "<optional>"}

    Response 200:
        {"vectors": [[...1536 floats...], ...],
         "provider": "openai|lexical",
         "model": "text-embedding-3-small",
         "tokens_used": 123}
    """
    err = _require_service_key()
    if err:
        return jsonify(err[0]), err[1]

    data = request.get_json(silent=True) or {}
    texts = data.get("texts") or []
    tenant_id = data.get("tenant_id")

    if not isinstance(texts, list) or not texts:
        return jsonify({"error": "texts must be a non-empty list"}), 400

    if len(texts) > 512:
        return jsonify({"error": "too many texts in one batch (max 512)"}), 413

    # Cap each text to avoid runaway embeddings cost.
    MAX_TEXT_CHARS = 16_000
    truncated = [(t or "")[:MAX_TEXT_CHARS] for t in texts]

    from api.core.embeddings import EmbeddingService

    service = EmbeddingService(tenant_id=tenant_id)
    result = service.embed_texts(truncated)

    return jsonify({
        "vectors": result.vectors,
        "provider": result.provider,
        "model": result.model,
        "tokens_used": result.tokens_used,
    }), 200


@myownclone_internal_bp.route("/embed/status", methods=["GET"])
def embed_status():
    """Report which embedding provider/model is active. Useful for the
    frontend to show 'semantic search on/off' in the UI."""
    err = _require_service_key()
    if err:
        return jsonify(err[0]), err[1]

    from api.core.embeddings import EmbeddingService

    svc = EmbeddingService()
    return jsonify({
        "provider": svc.provider,
        "model": svc.model,
        "dimensions": 1536,
        "semantic": svc.provider == "openai",
    }), 200


@myownclone_internal_bp.route("/ingest", methods=["POST"])
def ingest_source():
    """Run the ingestion pipeline for a source (extract → chunk → embed → persist).

    Called by the Next.js proxy when a source is created/uploaded so that
    PDF/YouTube/web content actually gets indexed (previously stuck at
    status='processing' forever).

    Request:
        Headers: X-API-Key: <SERVICE_API_KEY>
        Body:    {"source_id": "<uuid>", "async": true}

    Response 202 (async mode, default):
        {"status": "accepted", "source_id": "..."}
    Response 200 (sync mode, async=false):
        {"status": "ready|error", "chunks_created": N, "tokens_used": N,
         "embedding_provider": "openai|lexical"}
    """
    err = _require_service_key()
    if err:
        return jsonify(err[0]), err[1]

    data = request.get_json(silent=True) or {}
    source_id = data.get("source_id")
    if not source_id:
        return jsonify({"error": "source_id is required"}), 400

    run_async = data.get("async", True)

    if run_async:
        # Spawn a background thread so the upload request returns immediately.
        # On a larger deployment this would be an rq/celery job; for a single
        # VPS a thread is simpler and good enough.
        import threading

        def _run():
            try:
                with current_app.app_context():
                    from api.core.ingestion_pipeline import IngestionPipeline
                    IngestionPipeline().ingest(source_id=source_id)
            except Exception:
                logger.exception("Background ingestion failed for %s", source_id)

        thread = threading.Thread(target=_run, daemon=True)
        thread.start()
        return jsonify({"status": "accepted", "source_id": source_id}), 202

    # Sync mode: run inline and return the result.
    try:
        from api.core.ingestion_pipeline import IngestionPipeline
        result = IngestionPipeline().ingest(source_id=source_id)
        return jsonify({
            "status": result.status,
            "source_id": result.source_id,
            "chunks_created": result.chunks_created,
            "tokens_used": result.tokens_used,
            "embedding_provider": result.embedding_provider,
            "error": result.error,
        }), 200 if result.status == "ready" else 422
    except Exception as exc:
        logger.exception("Sync ingestion failed for %s", source_id)
        return jsonify({"error": str(exc)}), 500


@myownclone_internal_bp.route("/upload", methods=["POST"])
def upload_file():
    """Accept a PDF upload and store it in a temporary path, returning a
    URL the ingestion pipeline can download later.

    The Next.js proxy sends the file as multipart/form-data with field "file".
    Files are stored under /tmp/myownclone-uploads/ (mapped to a volume in
    docker-compose) and served back as a file:// URL the backend can read.

    Request:
        Headers: X-API-Key: <SERVICE_API_KEY>
        Body:    multipart/form-data with "file" field

    Response 200:
        {"url": "file:///tmp/myownclone-uploads/<uuid>.pdf",
         "filename": "doc.pdf", "size": 12345}
    """
    err = _require_service_key()
    if err:
        return jsonify(err[0]), err[1]

    if "file" not in request.files:
        return jsonify({"error": "file field is required"}), 400

    file = request.files["file"]
    if not file.filename:
        return jsonify({"error": "empty filename"}), 400

    # Only PDF for now (the only binary type the pipeline supports).
    allowed = {".pdf"}
    import os
    import uuid as uuidlib

    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed:
        return jsonify({"error": f"unsupported file type: {ext}"}), 415

    upload_dir = os.environ.get("UPLOAD_DIR", "/tmp/myownclone-uploads")
    os.makedirs(upload_dir, exist_ok=True)
    stored_name = f"{uuidlib.uuid4()}{ext}"
    stored_path = os.path.join(upload_dir, stored_name)
    file.save(stored_path)

    return jsonify({
        "url": f"file://{stored_path}",
        "filename": file.filename,
        "size": os.path.getsize(stored_path),
    }), 200
