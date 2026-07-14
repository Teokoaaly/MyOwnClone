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


def _clone_owned_by_tenant(clone_id: str | None, tenant_id: str | None) -> bool:
    """SECURITY (P0.4 / H-03): verify clone belongs to caller's tenant.

    Returns True only when a CloneConfig row exists with the given clone_id
    scoped to tenant_id. Used by Source CRUD (and reusable by other resources
    that take a clone_id from the request) to prevent cross-tenant IDOR.

    Mirrors ``feedback._clone_owned_by_tenant``; both should converge into a
    single shared helper in P0.4.05 (libs/tenant.py).
    """
    if not clone_id or not tenant_id:
        return False
    found = db.session.execute(
        select(CloneConfig.id).where(
            CloneConfig.id == clone_id,
            CloneConfig.tenant_id == tenant_id,
        )
    ).scalar_one_or_none()
    return found is not None


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

        # Update onboarding status when first clone is created
        try:
            from api.models.account import Account
            account_obj = db.session.get(Account, account.id)
            if account_obj and account_obj.onboarding_status in ("not_started", "wizard_in_progress"):
                account_obj.onboarding_status = "wizard_completed"
                db.session.commit()
        except Exception:
            logger.warning("Failed to update onboarding status for account=%s", account.id)

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
        if not tenant or not getattr(tenant, "id", None):
            return {"error": "tenant not configured for this account"}, 400
        clone_id = request.args.get("clone_id")

        # P0.4 (H-03): scoping por tenant via JOIN a clone_configs, no por
        # prefix-like sobre clone_id (era IDOR: un tenant podia leer fuentes
        # de otro pasando su clone_id exacto).
        clone_ids_subq = select(CloneConfig.id).where(
            CloneConfig.tenant_id == tenant.id
        )
        stmt = select(Source).where(Source.clone_id.in_(clone_ids_subq))
        if clone_id:
            # Si se filtra por clone_id, verificar que pertenece al tenant.
            if not _clone_owned_by_tenant(clone_id, tenant.id):
                return {"error": "clone not found"}, 404
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
        if not tenant or not getattr(tenant, "id", None):
            return {"error": "tenant not configured for this account"}, 400

        # P0.4 (H-03): verificar que el clone_id pertenece al tenant antes
        # de crear la fuente. Sin esto, un tenant podia inyectar fuentes en
        # el knowledge base de otro tenant (cross-tenant source injection).
        if not _clone_owned_by_tenant(payload.clone_id, tenant.id):
            return {"error": "clone not found"}, 404

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

@console_ns.route("/myownclone/clone/<string:clone_id>/avatar")
class CloneAvatarApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id):
        """Upload avatar for a clone."""
        from flask import request, g
        from api.extensions.ext_database import db
        from api.models import CloneConfig
        from api.libs.login import current_account_with_tenant
        import os
        import uuid

        account, tenant_id = current_account_with_tenant()

        # Verify clone exists and belongs to user's tenant
        clone = db.session.get(CloneConfig, clone_id)
        if not clone:
            return {"error": "Clone not found"}, 404
        if tenant_id and clone.tenant_id != tenant_id:
            return {"error": "Access denied"}, 403
        
        # Check file upload
        if 'avatar' not in request.files:
            return {"error": "No file uploaded"}, 400
        
        file = request.files['avatar']
        if file.filename == '':
            return {"error": "No file selected"}, 400
        
        # Validate file type
        allowed_types = {'image/jpeg', 'image/png', 'image/gif', 'image/webp'}
        if file.content_type not in allowed_types:
            return {"error": "Invalid file type. Allowed: JPEG, PNG, GIF, WebP"}, 400

        # Validate file size (max 5MB)
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)
        if file_size > 5 * 1024 * 1024:
            return {"error": "File too large. Maximum 5MB"}, 400

        # P2.8.07: sanitize extension from user-supplied filename.
        # Without an allowlist, ``shellcode.php`` (rsplit('.')[-1] -> "php")
        # would let the extension pass through. Map the content_type to a
        # known-good extension and ignore whatever the client sent.
        content_type_to_ext = {
            "image/jpeg": "jpg",
            "image/png": "png",
            "image/gif": "gif",
            "image/webp": "webp",
        }
        ext = content_type_to_ext[file.content_type]
        filename = f"{uuid.uuid4()}.{ext}"

        # P2.8.07: ensure parent directory exists (fresh deploys would
        # otherwise raise FileNotFoundError on file.save).
        avatars_dir = os.environ.get(
            "AVATARS_DIR", "/opt/myownclone/shared/avatars"
        )
        os.makedirs(avatars_dir, exist_ok=True)
        filepath = os.path.join(avatars_dir, filename)

        # Save file
        file.save(filepath)
        
        # Update clone avatar_url
        avatar_url = f"/avatars/{filename}"
        clone.avatar_url = avatar_url
        db.session.commit()
        
        return {
            "success": True,
            "avatar_url": avatar_url,
            "message": "Avatar uploaded successfully"
        }, 201
    
    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, clone_id):
        """Remove avatar from a clone."""
        from api.extensions.ext_database import db
        from api.models import CloneConfig
        from api.libs.login import current_account_with_tenant
        import os

        account, tenant_id = current_account_with_tenant()

        clone = db.session.get(CloneConfig, clone_id)
        if not clone:
            return {"error": "Clone not found"}, 404
        if tenant_id and clone.tenant_id != tenant_id:
            return {"error": "Access denied"}, 403
        
        if clone.avatar_url:
            # Delete file
            filepath = os.path.join("/opt/myownclone/shared/avatars", 
                                   clone.avatar_url.replace("/avatars/", ""))
            if os.path.exists(filepath):
                os.remove(filepath)
            
            clone.avatar_url = None
            db.session.commit()
        
        return {"success": True, "message": "Avatar removed"}, 200
