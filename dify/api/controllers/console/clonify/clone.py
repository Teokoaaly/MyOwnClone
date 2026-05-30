"""Clonify clone configuration API — CRUD for clone identity, personality, and mode prompts."""

import logging
from datetime import datetime
from uuid import uuid4

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import select

from controllers.common.schema import register_response_schema_models, register_schema_models
from controllers.console import console_ns
from controllers.console.wraps import account_initialization_required, setup_required
from extensions.ext_database import db
from fields.base import ResponseModel
from libs.login import current_account_with_tenant, login_required
from models.clonify import CloneConfig, CloneModePrompt, CloneSilo

logger = logging.getLogger(__name__)
clonify_ns = console_ns  # Reuse the console namespace


class CloneConfigPayload(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    slug: str = Field(..., min_length=2, max_length=100)
    description: str | None = None
    avatar_url: str | None = None
    personality_tone: str | None = None
    language: str = Field(default="es")
    active_modes: list[str] | None = Field(default_factory=lambda: ["teach"])
    is_active: bool = True


class CloneConfigUpdatePayload(BaseModel):
    name: str | None = None
    description: str | None = None
    personality_tone: str | None = None
    language: str | None = None
    active_modes: list[str] | None = None
    is_active: bool | None = None


class CloneModePromptPayload(BaseModel):
    mode: str
    system_prompt: str
    is_active: bool = True


class CloneConfigResponse(ResponseModel):
    id: str
    tenant_id: str
    name: str
    slug: str
    description: str | None = None
    avatar_url: str | None = None
    personality_tone: str | None = None
    language: str
    active_modes: list | None = None
    is_active: bool
    created_at: int | None = None
    updated_at: int | None = None
    mode_prompts: list | None = None


register_schema_models(
    console_ns,
    CloneConfigPayload,
    CloneConfigUpdatePayload,
    CloneModePromptPayload,
)

register_response_schema_models(
    console_ns,
    CloneConfigResponse,
)


@console_ns.route("/clonify/clones")
class CloneConfigListApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.doc("clonify_list_clones")
    @console_ns.response(200, "Success", [CloneConfigResponse])
    def get(self):
        account, tenant_id = current_account_with_tenant()
        stmt = (
            select(CloneConfig)
            .where(CloneConfig.tenant_id == tenant_id)
            .order_by(CloneConfig.created_at.desc())
        )
        clones = db.session.execute(stmt).scalars().all()
        return [_serialize_clone(c) for c in clones], 200

    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.doc("clonify_create_clone")
    @console_ns.expect(CloneConfigPayload, location="json", validate=True)
    @console_ns.response(201, "Created", CloneConfigResponse)
    def post(self):
        account, tenant_id = current_account_with_tenant()
        data = CloneConfigPayload.model_validate(request.json)
        clone = CloneConfig(
            tenant_id=tenant_id,
            name=data.name,
            slug=data.slug,
            description=data.description,
            avatar_url=data.avatar_url,
            personality_tone=data.personality_tone,
            language=data.language,
            active_modes=data.active_modes,
            is_active=data.is_active,
        )
        db.session.add(clone)
        db.session.flush()

        for silo in CloneSilo:
            prompt = CloneModePrompt(
                clone_id=clone.id,
                mode=silo.value,
                system_prompt=DEFAULT_PROMPTS.get(silo, ""),
                is_active=silo.value in (data.active_modes or []),
            )
            db.session.add(prompt)

        db.session.commit()
        return _serialize_clone(clone), 201


@console_ns.route("/clonify/clones/<string:clone_id>")
class CloneConfigApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.doc("clonify_get_clone")
    @console_ns.response(200, "Success", CloneConfigResponse)
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        clone = db.session.execute(
            select(CloneConfig).where(
                CloneConfig.id == clone_id,
                CloneConfig.tenant_id == tenant_id,
            )
        ).scalar_one_or_none()
        if not clone:
            return {"error": "clone not found"}, 404
        return _serialize_clone(clone), 200

    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.doc("clonify_update_clone")
    @console_ns.response(200, "Success", CloneConfigResponse)
    def put(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        clone = db.session.execute(
            select(CloneConfig).where(
                CloneConfig.id == clone_id,
                CloneConfig.tenant_id == tenant_id,
            )
        ).scalar_one_or_none()
        if not clone:
            return {"error": "clone not found"}, 404

        data = CloneConfigUpdatePayload.model_validate(request.json)
        if data.name is not None:
            clone.name = data.name
        if data.description is not None:
            clone.description = data.description
        if data.personality_tone is not None:
            clone.personality_tone = data.personality_tone
        if data.language is not None:
            clone.language = data.language
        if data.active_modes is not None:
            clone.active_modes = data.active_modes
        if data.is_active is not None:
            clone.is_active = data.is_active
        db.session.commit()
        return _serialize_clone(clone), 200


@console_ns.route("/clonify/clones/<string:clone_id>/prompts")
class CloneModePromptApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def put(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        data = CloneModePromptPayload.model_validate(request.json)
        prompt = db.session.execute(
            select(CloneModePrompt).where(
                CloneModePrompt.clone_id == clone_id,
                CloneModePrompt.mode == data.mode,
            )
        ).scalar_one_or_none()
        if not prompt:
            clone = db.session.execute(
                select(CloneConfig).where(
                    CloneConfig.id == clone_id,
                    CloneConfig.tenant_id == tenant_id,
                )
            ).scalar_one_or_none()
            if not clone:
                return {"error": "clone not found"}, 404
            prompt = CloneModePrompt(clone_id=clone_id, mode=data.mode)
            db.session.add(prompt)
        prompt.system_prompt = data.system_prompt
        prompt.is_active = data.is_active
        db.session.commit()
        return {"id": prompt.id, "mode": prompt.mode, "system_prompt": prompt.system_prompt}, 200


def _serialize_clone(clone: CloneConfig) -> dict:
    prompts = db.session.execute(
        select(CloneModePrompt).where(CloneModePrompt.clone_id == clone.id)
    ).scalars().all()
    return {
        "id": clone.id,
        "tenant_id": clone.tenant_id,
        "name": clone.name,
        "slug": clone.slug,
        "description": clone.description,
        "avatar_url": clone.avatar_url,
        "personality_tone": clone.personality_tone,
        "language": clone.language,
        "active_modes": clone.active_modes if isinstance(clone.active_modes, list) else [],
        "is_active": clone.is_active if clone.is_active is not None else True,
        "created_at": int(clone.created_at.timestamp()) if clone.created_at else None,
        "updated_at": int(clone.updated_at.timestamp()) if clone.updated_at else None,
        "mode_prompts": [
            {
                "id": p.id,
                "mode": p.mode,
                "system_prompt": p.system_prompt,
                "is_active": p.is_active,
            }
            for p in prompts
        ],
    }


DEFAULT_PROMPTS = {
    CloneSilo.TEACH: (
        "Eres un asistente pedagógico amable y paciente. Tu objetivo es ayudar a los "
        "estudiantes a comprender el contenido del curso. Explica los conceptos de forma "
        "clara, usa ejemplos y anima a hacer preguntas. Basa tus respuestas ÚNICAMENTE "
        "en el contenido proporcionado. Si no tienes suficiente información, di claramente "
        "'No tengo suficiente información para responder a eso'."
    ),
    CloneSilo.SUPPORT: (
        "Eres un agente de soporte eficiente y resolutivo. Tu objetivo es resolver dudas "
        "y problemas de los clientes de forma rápida y profesional. Si la consulta requiere "
        "atención humana, indícalo claramente y ofrece derivar al equipo de soporte. "
        "Basas tus respuestas en la documentación proporcionada."
    ),
    CloneSilo.SALES: (
        "Eres un asesor de ventas entusiasta pero no agresivo. Tu objetivo es ayudar a "
        "los clientes a encontrar el producto o servicio que mejor se adapte a sus necesidades. "
        "Destaca los beneficios, responde objeciones con honestidad y recomienda productos "
        "basándote en la información de catálogo proporcionada."
    ),
}
