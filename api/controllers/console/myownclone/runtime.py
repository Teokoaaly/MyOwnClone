"""Runtime integration endpoints for configurable AI services."""

from __future__ import annotations

from flask import request
from flask_restx import Resource

from api.controllers.console import console_ns
from api.core.embeddings import EmbeddingService
from api.core.providers.base import ModelInvocationError
from api.core.stt import SpeechToTextService
from api.libs.login import current_account_with_tenant, login_required


@console_ns.route("/myownclone/embeddings")
class RuntimeEmbeddingsApi(Resource):
    @login_required
    def post(self):
        _account, tenant_id = current_account_with_tenant()
        payload = request.get_json(silent=True) or {}
        texts = payload.get("texts") or []
        if not isinstance(texts, list) or not texts or not all(isinstance(text, str) for text in texts):
            return {"error": "texts must be a non-empty list of strings"}, 400

        try:
            vectors = EmbeddingService().embed_texts(texts, tenant_id=tenant_id)
        except (ModelInvocationError, ValueError) as exc:
            return {"error": str(exc)}, 422

        return {
            "vectors": vectors,
            "count": len(vectors),
            "tenant_id": tenant_id,
        }, 200


@console_ns.route("/myownclone/stt/transcribe")
class RuntimeSpeechToTextApi(Resource):
    @login_required
    def post(self):
        _account, tenant_id = current_account_with_tenant()
        audio = request.files.get("audio")
        if audio is None:
            return {"error": "audio is required"}, 400

        try:
            text = SpeechToTextService().transcribe(
                tenant_id=tenant_id,
                audio_bytes=audio.read(),
                filename=audio.filename or "audio.webm",
                content_type=audio.mimetype,
                language=request.form.get("language") or "es",
            )
        except ModelInvocationError as exc:
            return {"error": str(exc)}, 422

        return {"text": text}, 200
