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

from flask import Blueprint, request, jsonify

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


@myownclone_public_bp.route("/inbound-email", methods=["POST"])
def inbound_email():
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

    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    silo_str = data.get("silo", "teach")
    context_id = data.get("context_id")

    if not message:
        return jsonify({"error": "message is required"}), 400

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
            from api.core.model_manager import ModelManager, ModelType

            model_manager = ModelManager()
            model_instance = model_manager.get_default_model_instance(
                tenant_id=clone.tenant_id, model_type=ModelType.LLM
            )

            accumulated = ""
            for chunk in model_instance.invoke_llm_stream(prompt=full_prompt):
                accumulated += chunk
                yield f"data: {json.dumps({'content': chunk})}\n\n"

            yield f"data: {json.dumps({'content': '', 'done': True, 'context_found': result.found, 'silo': silo.value, 'confidence': round(result.scores[0], 2) if result.scores else 0, 'sources': [{'content': c[:300], 'score': round(s, 2)} for c, s in zip(result.contents, result.scores)]})}\n\n"
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

    payload = request.get_json(silent=True) or {}
    message = (payload.get("message") or "").strip()
    if not message:
        return jsonify({"error": "message_required"}), 400

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

    data = request.get_json(silent=True) or {}
    meeting_type_id = data.get("meeting_type_id")
    visitor_name = data.get("visitor_name", "")
    visitor_email = data.get("visitor_email", "")
    booking_date = data.get("date")
    start_time = data.get("start_time")

    if not meeting_type_id or not visitor_name or not visitor_email or not booking_date:
        return jsonify({"error": "meeting_type_id, visitor_name, visitor_email, and date are required"}), 400

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
