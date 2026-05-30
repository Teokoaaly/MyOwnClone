"""Inbound email webhook and inbox management service.

Orchestrates the full email pipeline:
1. Receive email via SendGrid Inbound Parse webhook
2. Parse, classify, and generate draft
3. Store in email_inbound table
4. Expose CRUD API for the inbox UI (list, get, update, send, discard)
"""

import logging
from typing import Any

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import func, select

from controllers.common.schema import register_response_schema_models, register_schema_models
from controllers.console import console_ns
from controllers.console.wraps import account_initialization_required, setup_required
from core.clonify.email_ai import _get_clone_context, classify_email, generate_draft_reply
from core.clonify.email_processor import parse_inbound_email, resolve_clone_by_domain
from extensions.ext_database import db
from fields.base import ResponseModel
from libs.login import current_account_with_tenant, login_required
from models.clonify import (
    CloneConfig,
    EmailInbound,
    EmailInboundStatus,
)

logger = logging.getLogger(__name__)


class EmailListItem(ResponseModel):
    id: str
    clone_id: str
    from_email: str | None = None
    from_name: str | None = None
    subject: str | None = None
    body_text: str | None = None
    status: str
    classification: str | None = None
    has_draft: bool = False
    received_at: int | None = None


class EmailDraftPayload(BaseModel):
    draft_reply: str
    status: str | None = None


class EmailSendPayload(BaseModel):
    draft_reply: str = Field(default="")


register_schema_models(console_ns, EmailDraftPayload, EmailSendPayload)
register_response_schema_models(console_ns, EmailListItem)


@console_ns.route("/clonify/clones/<string:clone_id>/inbox")
class InboxListApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)

        status_filter = request.args.get("status")
        page = int(request.args.get("page", 1))
        limit = min(int(request.args.get("limit", 20)), 50)

        stmt = (
            select(EmailInbound)
            .where(EmailInbound.clone_id == clone_id)
            .order_by(EmailInbound.received_at.desc())
        )
        if status_filter:
            stmt = stmt.where(EmailInbound.status == status_filter)

        stmt = stmt.offset((page - 1) * limit).limit(limit)
        emails = db.session.execute(stmt).scalars().all()

        return [
            {
                "id": e.id,
                "clone_id": e.clone_id,
                "from_email": e.from_email,
                "from_name": e.from_name,
                "subject": e.subject,
                "body_text": _truncate(e.body_text, 200),
                "status": e.status,
                "classification": e.classification,
                "has_draft": bool(e.draft_reply),
                "received_at": int(e.received_at.timestamp()) if e.received_at else None,
            }
            for e in emails
        ], 200


@console_ns.route("/clonify/inbox/<string:email_id>")
class InboxDetailApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, email_id: str):
        account, tenant_id = current_account_with_tenant()
        email = db.session.execute(
            select(EmailInbound).where(EmailInbound.id == email_id)
        ).scalar_one_or_none()
        if not email:
            return {"error": "email not found"}, 404
        _verify_clone_access(email.clone_id, tenant_id)

        return {
            "id": email.id,
            "clone_id": email.clone_id,
            "from_email": email.from_email,
            "from_name": email.from_name,
            "subject": email.subject,
            "body_text": email.body_text,
            "body_html": email.body_html,
            "draft_reply": email.draft_reply,
            "status": email.status,
            "labels": email.labels if isinstance(email.labels, list) else [],
            "classification": email.classification,
            "received_at": int(email.received_at.timestamp()) if email.received_at else None,
        }, 200

    @login_required
    @account_initialization_required
    @setup_required
    def put(self, email_id: str):
        account, tenant_id = current_account_with_tenant()
        email = db.session.execute(
            select(EmailInbound).where(EmailInbound.id == email_id)
        ).scalar_one_or_none()
        if not email:
            return {"error": "email not found"}, 404
        _verify_clone_access(email.clone_id, tenant_id)

        data = EmailDraftPayload.model_validate(request.json)
        if data.draft_reply is not None:
            email.draft_reply = data.draft_reply
        if data.status:
            if data.status == "sent":
                email.responded_at = func.current_timestamp()
            email.status = data.status
        db.session.commit()
        return {"id": email.id, "status": email.status, "has_draft": bool(email.draft_reply)}, 200

    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, email_id: str):
        account, tenant_id = current_account_with_tenant()
        email = db.session.execute(
            select(EmailInbound).where(EmailInbound.id == email_id)
        ).scalar_one_or_none()
        if not email:
            return {"error": "email not found"}, 404
        _verify_clone_access(email.clone_id, tenant_id)
        email.status = EmailInboundStatus.DISCARDED
        db.session.commit()
        return "", 204


@console_ns.route("/clonify/inbox/<string:email_id>/generate-draft")
class InboxGenerateDraftApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self, email_id: str):
        account, tenant_id = current_account_with_tenant()
        email = db.session.execute(
            select(EmailInbound).where(EmailInbound.id == email_id)
        ).scalar_one_or_none()
        if not email:
            return {"error": "email not found"}, 404
        _verify_clone_access(email.clone_id, tenant_id)

        memory_context, template_context = _get_clone_context(email.clone_id)

        def llm_call(prompt: str) -> str:
            from core.model_manager import ModelManager
            from graphon.model_runtime.entities.model_entities import ModelType

            model_manager = ModelManager()
            model_instance = model_manager.get_default_model_instance(
                tenant_id=tenant_id, model_type=ModelType.LLM
            )
            return model_instance.invoke_llm(prompt=prompt)

        result = generate_draft_reply(
            from_name=email.from_name or "",
            from_email=email.from_email or "",
            subject=email.subject or "",
            body_text=email.body_text or "",
            memory_context=memory_context,
            template_context=template_context,
            llm_callable=llm_call,
        )

        email.draft_reply = result.body
        email.classification = "consulta"
        db.session.commit()

        return {
            "subject": result.subject,
            "body": result.body,
        }, 200


def _verify_clone_access(clone_id: str, tenant_id: str) -> None:
    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.id == clone_id,
            CloneConfig.tenant_id == tenant_id,
        )
    ).scalar_one_or_none()
    if not clone:
        from werkzeug.exceptions import NotFound
        raise NotFound("clone not found")


def _truncate(text: str | None, max_len: int) -> str | None:
    if not text:
        return text
    return text[:max_len] + ("..." if len(text) > max_len else "")
