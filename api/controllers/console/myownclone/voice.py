"""Voice cloning API endpoints.

Provides CRUD for voice clones and TTS generation.
Requires ELEVENLABS_API_KEY to be configured.
"""

from __future__ import annotations

import logging

from flask import request, send_file
from flask_restx import Resource
from io import BytesIO

from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import login_required

logger = logging.getLogger(__name__)


@console_ns.route("/myownclone/voice/status")
class VoiceStatusApi(Resource):
    """Check if voice cloning is configured and available."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        from api.core.voice import VoiceService
        vs = VoiceService()
        if not vs.is_configured:
            return {
                "configured": False,
                "message": "ELEVENLABS_API_KEY not configured. Add it to backend.env.production.",
            }, 200

        try:
            info = vs.get_subscription_info()
            return {
                "configured": True,
                "tier": info.get("tier", "unknown"),
                "character_count": info.get("character_count", 0),
                "character_limit": info.get("character_limit", 0),
                "voices_limit": info.get("voice_limit", 0),
            }, 200
        except Exception as exc:
            return {
                "configured": True,
                "error": str(exc),
            }, 200


@console_ns.route("/myownclone/voice/voices")
class VoiceListApi(Resource):
    """List all available voices."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        from api.core.voice import VoiceService, VoiceServiceError
        vs = VoiceService()
        if not vs.is_configured:
            return {"error": "Voice service not configured"}, 400

        try:
            voices = vs.list_voices()
            return {
                "voices": [
                    {
                        "voice_id": v.voice_id,
                        "name": v.name,
                        "category": v.category,
                        "description": v.description,
                        "preview_url": v.preview_url,
                        "labels": v.labels,
                    }
                    for v in voices
                ],
                "total": len(voices),
            }, 200
        except VoiceServiceError as exc:
            return {"error": str(exc)}, 502


@console_ns.route("/myownclone/voice/clone")
class VoiceCloneApi(Resource):
    """Clone a voice from audio samples."""

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        from api.core.voice import VoiceService, VoiceServiceError
        vs = VoiceService()
        if not vs.is_configured:
            return {"error": "Voice service not configured"}, 400

        name = request.form.get("name", "").strip()
        if not name:
            return {"error": "name is required"}, 400

        description = request.form.get("description", "")

        files = []
        for key in request.files:
            f = request.files[key]
            if f.filename:
                content = f.read()
                files.append((f.filename, content, f.content_type or "audio/wav"))

        if not files:
            return {"error": "At least one audio file is required"}, 400

        try:
            voice_id = vs.clone_voice(
                name=name,
                files=files,
                description=description,
            )
            return {
                "voice_id": voice_id,
                "name": name,
                "message": "Voice cloned successfully",
            }, 201
        except VoiceServiceError as exc:
            return {"error": str(exc)}, 502


@console_ns.route("/myownclone/voice/tts")
class VoiceTtsApi(Resource):
    """Generate speech from text using a voice."""

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        from api.core.voice import VoiceService, VoiceServiceError
        vs = VoiceService()
        if not vs.is_configured:
            return {"error": "Voice service not configured"}, 400

        data = request.get_json(silent=True) or {}
        voice_id = data.get("voice_id", "").strip()
        text = data.get("text", "").strip()
        model_id = data.get("model_id", "eleven_multilingual_v2")

        if not voice_id:
            return {"error": "voice_id is required"}, 400
        if not text:
            return {"error": "text is required"}, 400

        try:
            audio = vs.text_to_speech(
                voice_id=voice_id,
                text=text,
                model_id=model_id,
            )
            return send_file(
                BytesIO(audio),
                mimetype="audio/mpeg",
                download_name="speech.mp3",
            )
        except VoiceServiceError as exc:
            return {"error": str(exc)}, 502


@console_ns.route("/myownclone/voice/delete/<string:voice_id>")
class VoiceDeleteApi(Resource):
    """Delete a cloned voice."""

    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, voice_id: str):
        from api.core.voice import VoiceService
        vs = VoiceService()
        if not vs.is_configured:
            return {"error": "Voice service not configured"}, 400

        success = vs.delete_voice(voice_id)
        if success:
            return {"message": "Voice deleted"}, 200
        return {"error": "Failed to delete voice"}, 502
