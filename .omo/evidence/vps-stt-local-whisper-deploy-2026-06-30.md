Context
- Phase B: STT was broken on VPS because no OPENAI_API_KEY is configured
  and the runtime only supported {openai, openai_compatible}. Decision:
  ship an in-process faster-whisper runtime that needs no external key
  and runs on CPU.

Plan
- Add a new provider ``local_whisper`` (faster-whisper / CTranslate2,
  whisper ``tiny`` int8 = ~75 MB on disk, ~400 MB RSS).
- Refactor SpeechToTextService to dispatch through a registry map of
  provider classes (mirrors ModelManager pattern).
- When no OPENAI_API_KEY is set, the legacy fallback path now resolves
  ``local_whisper`` instead of returning None.
- Source SHA: codex/backend-admin-vps-exec @ f875774
- VPS release: /opt/myownclone/releases/20260629144355-frontend-i18n-selector
- /opt/myownclone/current -> that release
- Container: myownclone_api rebuilt and restarted with env sourced.

Live verification (in-container)
- python -c 'from api.core.providers.local_whisper import LocalWhisperAdapter; print(LocalWhisperAdapter.provider_name)'
  -> local_whisper
- _ensure_model() cold-start: 3.69s (downloads tiny model to /tmp/whisper)
- _ensure_model() warm: < 1ms (cached)
- transcribe(4.3s Spanish WAV, language=es): 1.18s
    output: "Esto es un problema en el sistema metancripción de voz."
  (The exact wording differs from the original espeak-ng input —
  whisper ``tiny`` is the smallest size and trades accuracy for
  speed. ``base`` is one notch up and fits the same memory budget.)

Endpoint sanity
- POST /console/api/myownclone/stt/transcribe (no auth) -> 401
  (correctly protected by @login_required)
- Same endpoint via test_client -> 401 (no 500s, route registered)

Cost / resources
- Container memory usage after model load: ~600 MB RSS (within budget)
- Whisper tiny CPU: ~1x realtime on 2 vCPUs
- HuggingFace download: ~75 MB int8 (one-time)

Tests
- 18 new unit tests (all pass):
  - LocalWhisperAdapter shape (provider_name, supports, generate/stream raises)
  - _ensure_model lazy load + cache reuse
  - transcribe happy path, empty result
  - test_connection ok + fail
  - SpeechToTextService routing to local_whisper
  - SpeechToTextService legacy openai fallback for unknown provider
  - SpeechToTextService raises when provider lacks transcribe (anthropic)
  - ModelRegistry detects local_whisper as STT fallback when OPENAI_API_KEY absent
  - ModelRegistry prefers openai when OPENAI_API_KEY present
  - ModelRegistry resolves local_whisper config block
- Combined i18n + stt suite: 41/41 passing locally.

Rollback target
- /opt/myownclone/releases/20260629124000-local-embeddings-dynamic
  (last known-good backend).