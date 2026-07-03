"""MyOwnClone clone configuration API — CRUD for clone identity, personality, and mode prompts."""

import logging
from datetime import datetime
from uuid import uuid4

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from api.controllers.common.schema import register_response_schema_models, register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.core.contracts import normalize_silo, normalize_silo_list
from api.extensions.ext_database import db
from api.fields.base import ResponseModel
from api.libs.login import current_account_with_tenant, login_required
from api.models.knowledge import Source
from api.models.myownclone import CloneConfig, CloneModePrompt, CloneSilo

logger = logging.getLogger(__name__)
myownclone_ns = console_ns  # Reuse the console namespace


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


@console_ns.route("/myownclone/clones")
class CloneConfigListApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.doc("myownclone_list_clones")
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
    @console_ns.doc("myownclone_create_clone")
    @console_ns.expect(CloneConfigPayload, location="json", validate=True)
    @console_ns.response(201, "Created", CloneConfigResponse)
    def post(self):
        account, tenant_id = current_account_with_tenant()
        if not tenant_id:
            return {"error": "tenant not configured for this account"}, 400

        data = CloneConfigPayload.model_validate(request.json)
        existing = db.session.execute(
            select(CloneConfig).where(CloneConfig.slug == data.slug)
        ).scalar_one_or_none()
        if existing:
            return {"error": f"A clone with slug '{data.slug}' already exists"}, 409

        clone = CloneConfig(
            tenant_id=tenant_id,
            name=data.name,
            slug=data.slug,
            description=data.description,
            avatar_url=data.avatar_url,
            personality_tone=data.personality_tone,
            language=data.language,
            active_modes=normalize_silo_list(data.active_modes),
            is_active=data.is_active,
        )
        db.session.add(clone)
        db.session.flush()

        for silo in CloneSilo.__members__.values():
            prompt = CloneModePrompt(
                clone_id=clone.id,
                mode=silo.value,
                system_prompt=DEFAULT_PROMPTS.get(silo, ""),
                is_active=silo.value in normalize_silo_list(data.active_modes),
            )
            db.session.add(prompt)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"error": f"A clone with slug '{data.slug}' already exists"}, 409
        except Exception:
            db.session.rollback()
            logger.exception("Failed to create clone for tenant=%s slug=%s", tenant_id, data.slug)
            return {"error": "failed to create clone"}, 500

        return _serialize_clone(clone), 201


@console_ns.route("/myownclone/clones/<string:clone_id>")
class CloneConfigApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    @console_ns.doc("myownclone_get_clone")
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
    @console_ns.doc("myownclone_update_clone")
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
            clone.active_modes = normalize_silo_list(data.active_modes)
        if data.is_active is not None:
            clone.is_active = data.is_active
        db.session.commit()
        return _serialize_clone(clone), 200


@console_ns.route("/myownclone/clones/<string:clone_id>/prompts")
class CloneModePromptApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def put(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        data = CloneModePromptPayload.model_validate(request.json)
        mode = normalize_silo(data.mode)
        prompt = db.session.execute(
            select(CloneModePrompt).where(
                CloneModePrompt.clone_id == clone_id,
                CloneModePrompt.mode == mode,
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
            prompt = CloneModePrompt(clone_id=clone_id, mode=mode)
            db.session.add(prompt)
        prompt.system_prompt = data.system_prompt
        prompt.is_active = data.is_active
        db.session.commit()
        return {
            "id": str(prompt.id),
            "mode": normalize_silo(prompt.mode),
            "system_prompt": prompt.system_prompt,
        }, 200


def _serialize_clone(clone: CloneConfig) -> dict:
    prompts = db.session.execute(
        select(CloneModePrompt).where(CloneModePrompt.clone_id == clone.id)
    ).scalars().all()
    return {
        "id": str(clone.id),
        "tenant_id": str(clone.tenant_id),
        "name": clone.name,
        "slug": clone.slug,
        "description": clone.description,
        "avatar_url": clone.avatar_url,
        "personality_tone": clone.personality_tone,
        "language": clone.language,
        "active_modes": normalize_silo_list(clone.active_modes if isinstance(clone.active_modes, list) else []),
        "is_active": clone.is_active if clone.is_active is not None else True,
        "created_at": int(clone.created_at.timestamp()) if clone.created_at else None,
        "updated_at": int(clone.updated_at.timestamp()) if clone.updated_at else None,
        "mode_prompts": [
            {
                "id": str(p.id),
                "mode": normalize_silo(p.mode),
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


# === T2.1: Sources (knowledge base) ===

class SourceCreatePayload(BaseModel):
    clone_id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1, max_length=255)
    type: str = Field(default="text", pattern=r"^(text|url|pdf|youtube)$")
    url: str | None = None  # para url/pdf/youtube: la URL; para text: el contenido
    content: str | None = None  # alias para texto plano (no choca con `url`)


class _SourceListItem(ResponseModel):
    id: str
    clone_id: str
    type: str
    title: str
    url: str | None
    status: str
    metadata: dict | None
    created_at: int | None
    updated_at: int | None


@console_ns.route("/myownclone/sources")
class SourceListApi(Resource):
    @setup_required
    @login_required
    @account_initialization_required
    @console_ns.doc("list_sources")
    def get(self):
        """Lista fuentes de conocimiento del tenant."""
        account, tenant = current_account_with_tenant()
        clone_id = request.args.get("clone_id")
        stmt = select(Source).where(Source.clone_id.like(f"{tenant.id}%"))
        if clone_id:
            stmt = stmt.where(Source.clone_id == clone_id)
        sources = db.session.execute(stmt.order_by(Source.created_at.desc())).scalars().all()
        return {"items": [_serialize_source(s) for s in sources]}

    @setup_required
    @login_required
    @account_initialization_required
    @console_ns.doc("create_source")
    def post(self):
        """Crea una fuente de conocimiento y dispara ingestion."""
        payload = SourceCreatePayload(**request.get_json(force=True))
        account, tenant = current_account_with_tenant()

        # Texto plano puede venir en `url` (legacy) o `content`
        if payload.type == "text":
            text = payload.content or payload.url or ""
        else:
            text = payload.url

        source = Source(
            id=str(uuid4()),
            clone_id=payload.clone_id,
            type=payload.type,
            title=payload.title,
            url=text,
            status="processing",
            chunk_metadata={"content": text} if payload.type == "text" else None,
        )
        db.session.add(source)
        db.session.commit()

        # T3.5: ingestion ASYNC para no bloquear el request HTTP.
        # Para text/URL cortos, sigue siendo rápido (síncrono).
        # Para PDF/YouTube, va a la cola RQ (worker procesa en background).
        job_id = None
        if payload.type in ("pdf", "youtube"):
            from api.core.queue import enqueue_ingestion
            job_id = enqueue_ingestion(source.id, timeout=600)
        else:
            from api.core.ingestion import ingest_source
            ingest_source(source.id)

        # Refrescar tras ingestion
        db.session.refresh(source)
        response = _serialize_source(source)
        if job_id:
            response["job_id"] = job_id  # cliente puede consultar status
        return response, 202 if job_id else 201


def _serialize_source(source: Source) -> dict:
    return {
        "id": str(source.id),
        "clone_id": source.clone_id,
        "type": source.type,
        "title": source.title,
        "url": source.url if source.type != "text" else None,
        "content": (source.chunk_metadata or {}).get("content") if source.type == "text" else None,
        "status": source.status,
        "metadata": source.chunk_metadata,
        "created_at": int(source.created_at.timestamp()) if source.created_at else None,
        "updated_at": int(source.updated_at.timestamp()) if source.updated_at else None,
    }
