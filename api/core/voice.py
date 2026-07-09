"""Voice cloning module — ElevenLabs integration.

Provides voice cloning, TTS, and voice management.
Requires ELEVENLABS_API_KEY environment variable.

Usage:
    from api.core.voice import VoiceService
    vs = VoiceService()
    # Clone voice from audio samples
    voice_id = vs.clone_voice(name="My Voice", files=[...])
    # Generate speech from text
    audio = vs.text_to_speech(voice_id="...", text="Hello world")
    # List available voices
    voices = vs.list_voices()
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import BinaryIO

import requests

logger = logging.getLogger(__name__)

ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1"


@dataclass
class VoiceInfo:
    voice_id: str
    name: str
    category: str | None = None
    description: str | None = None
    preview_url: str | None = None
    labels: dict | None = None


class VoiceServiceError(RuntimeError):
    """Raised when a voice operation fails."""


class VoiceService:
    """ElevenLabs voice cloning and TTS service.

    All methods require a valid ELEVENLABS_API_KEY.
    If the key is not set, methods raise VoiceServiceError.
    """

    def __init__(self, api_key: str | None = None) -> None:
        self._api_key = api_key or os.environ.get("ELEVENLABS_API_KEY", "")
        self._base_url = ELEVENLABS_API_URL

    @property
    def is_configured(self) -> bool:
        return bool(self._api_key)

    def _headers(self) -> dict:
        if not self._api_key:
            raise VoiceServiceError("ELEVENLABS_API_KEY not configured")
        return {
            "xi-api-key": self._api_key,
            "Accept": "application/json",
        }

    def list_voices(self) -> list[VoiceInfo]:
        """List all available voices in the account."""
        resp = requests.get(
            f"{self._base_url}/voices",
            headers=self._headers(),
            timeout=30,
        )
        if resp.status_code >= 400:
            raise VoiceServiceError(
                f"Failed to list voices: {resp.status_code} {resp.text[:200]}"
            )
        data = resp.json()
        voices = []
        for v in data.get("voices", []):
            voices.append(VoiceInfo(
                voice_id=v["voice_id"],
                name=v["name"],
                category=v.get("category"),
                description=v.get("description"),
                preview_url=v.get("preview_url"),
                labels=v.get("labels"),
            ))
        return voices

    def clone_voice(
        self,
        name: str,
        files: list[tuple[str, bytes, str]],
        description: str = "",
    ) -> str:
        """Clone a voice from audio samples.

        Args:
            name: Display name for the cloned voice.
            files: List of (filename, audio_bytes, content_type) tuples.
            description: Optional description.

        Returns:
            The voice_id of the newly created voice.
        """
        if not files:
            raise VoiceServiceError("At least one audio sample is required")

        files_data = []
        for filename, audio_bytes, content_type in files:
            files_data.append(
                ("files", (filename, audio_bytes, content_type))
            )

        form_data = {
            "name": name,
            "description": description,
        }

        resp = requests.post(
            f"{self._base_url}/voices/add",
            headers=self._headers(),
            files=files_data,
            data=form_data,
            timeout=120,
        )
        if resp.status_code >= 400:
            raise VoiceServiceError(
                f"Failed to clone voice: {resp.status_code} {resp.text[:200]}"
            )
        data = resp.json()
        voice_id = data.get("voice_id")
        if not voice_id:
            raise VoiceServiceError("No voice_id in response")
        logger.info("Voice cloned: name=%s voice_id=%s", name, voice_id)
        return voice_id

    def delete_voice(self, voice_id: str) -> bool:
        """Delete a cloned voice by ID."""
        resp = requests.delete(
            f"{self._base_url}/voices/{voice_id}",
            headers=self._headers(),
            timeout=30,
        )
        return resp.status_code < 400

    def text_to_speech(
        self,
        voice_id: str,
        text: str,
        model_id: str = "eleven_multilingual_v2",
        voice_settings: dict | None = None,
    ) -> bytes:
        """Generate speech audio from text.

        Args:
            voice_id: The voice to use.
            text: Text to convert to speech.
            model_id: TTS model (default: multilingual v2).
            voice_settings: Optional voice settings (stability, similarity_boost, etc).

        Returns:
            Raw audio bytes (MP3).
        """
        if not text.strip():
            raise VoiceServiceError("Text cannot be empty")

        payload = {
            "text": text,
            "model_id": model_id,
        }
        if voice_settings:
            payload["voice_settings"] = voice_settings

        resp = requests.post(
            f"{self._base_url}/text-to-speech/{voice_id}",
            headers={**self._headers(), "Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        if resp.status_code >= 400:
            raise VoiceServiceError(
                f"TTS failed: {resp.status_code} {resp.text[:200]}"
            )
        return resp.content

    def get_subscription_info(self) -> dict:
        """Get current subscription usage and limits."""
        resp = requests.get(
            f"{self._base_url}/user/subscription",
            headers=self._headers(),
            timeout=30,
        )
        if resp.status_code >= 400:
            raise VoiceServiceError(
                f"Failed to get subscription: {resp.status_code}"
            )
        return resp.json()
