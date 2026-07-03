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

from flask import Blueprint, request, jsonify
from sqlalchemy import select

from api.core.myownclone.email_ai import _get_clone_context, classify_email, generate_draft_reply
from api.core.myownclone.email_processor import parse_inbound_email, resolve_clone_by_domain
from api.extensions.ext_database import db
from api.models.ai_models import AITask
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

    full_prompt = f"""{system_prompt}

{"CONTENIDO DE REFERENCIA:" if context_text else "No se encontró contenido relevante en la base de conocimiento."}
{context_text}

Pregunta del usuario: {message}"""

    def generate():
        try:
            from api.core.model_manager import ModelManager

            model_manager = ModelManager()

            accumulated = ""
            tokens_in_est = len(full_prompt.split())  # aproximado
            for chunk in model_manager.invoke_for_task_stream(
                tenant_id=clone.tenant_id,
                clone_id=clone.id,
                task=AITask.CHAT,
                message=full_prompt,
            ):
                accumulated += chunk
                yield f"data: {json.dumps({'content': chunk})}\n\n"
            tokens_out_est = len(accumulated.split())  # aproximado

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

            # T2.11: registrar coste de IA en ai_invocations (Defecto #2 Sisyphus)
            try:
                from api.core.model_manager import record_llm_cost, estimate_cost_cents
                from api.core.model_registry import ModelRegistry
                from api.core.metrics import LLM_TOKENS, LLM_COST_CENTS, EMBEDDINGS

                reg = ModelRegistry()
                m = reg.get_model_for_task(tenant_id=clone.tenant_id, task=AITask.CHAT)
                cost = estimate_cost_cents(m.model_id, m.provider, tokens_in_est, tokens_out_est)
                record_llm_cost(
                    tenant_id=clone.tenant_id,
                    clone_id=str(clone.id),
                    model=m.model_id,
                    provider=m.provider,
                    tokens_in=tokens_in_est,
                    tokens_out=tokens_out_est,
                    cost_cents=cost,
                    task="chat",
                )
                # T3.6: actualizar contadores Prometheus
                LLM_TOKENS.labels(model=m.model_id, provider=m.provider, direction="in").inc(tokens_in_est)
                LLM_TOKENS.labels(model=m.model_id, provider=m.provider, direction="out").inc(tokens_out_est)
                LLM_COST_CENTS.labels(model=m.model_id, provider=m.provider).inc(cost)
            except Exception as exc:
                logger.warning("T2.11: cost tracking falló (no-fatal): %s", exc)

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
        from api.core.model_manager import ModelManager

        clone = db.session.execute(
            select(CloneConfig).where(CloneConfig.id == clone_id)
        ).scalar_one_or_none()

        if not clone:
            return

        model_manager = ModelManager()

        def classify_llm_call(prompt: str) -> str:
            return model_manager.invoke_for_task(
                tenant_id=clone.tenant_id,
                clone_id=clone.id,
                task=AITask.EMAIL_CLASSIFICATION,
                message=prompt,
            ).text

        classification = classify_email(
            from_name=email.from_name or "",
            from_email=email.from_email or "",
            subject=email.subject or "",
            body_text=email.body_text or "",
            llm_callable=classify_llm_call,
        )
        email.classification = classification.category
        email.labels = [classification.category]

        memory_context, template_context = _get_clone_context(clone_id)

        def draft_llm_call(prompt: str) -> str:
            return model_manager.invoke_for_task(
                tenant_id=clone.tenant_id,
                clone_id=clone.id,
                task=AITask.EMAIL_DRAFT,
                message=prompt,
            ).text

        draft = generate_draft_reply(
            from_name=email.from_name or "",
            from_email=email.from_email or "",
            subject=email.subject or "",
            body_text=email.body_text or "",
            memory_context=memory_context,
            template_context=template_context,
            llm_callable=draft_llm_call,
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
