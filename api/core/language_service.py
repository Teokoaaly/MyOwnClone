"""Language service for MyOwnClone — validates codes and injects language into prompts."""

from __future__ import annotations

SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "pt": "Portuguese",
    "it": "Italian",
    "zh": "Chinese",
    "ja": "Japanese",
    "ar": "Arabic",
    "hi": "Hindi",
    "ko": "Korean",
    "nl": "Dutch",
    "ru": "Russian",
    "tr": "Turkish",
}

DEFAULT_LANGUAGE = "en"


def validate_language_code(code: str) -> str:
    """Validate and normalize ISO 639-1 language code.

    Returns the validated code or DEFAULT_LANGUAGE if invalid.
    """
    if not code or not isinstance(code, str):
        return DEFAULT_LANGUAGE
    code = code.lower().strip()[:2]
    if code not in SUPPORTED_LANGUAGES:
        return DEFAULT_LANGUAGE
    return code


def get_language_name(code: str) -> str:
    """Get human-readable language name from ISO 639-1 code."""
    code = validate_language_code(code)
    return SUPPORTED_LANGUAGES.get(code, "English")


def inject_language_into_prompt(prompt: str, language_code: str) -> str:
    """Append a language instruction to a system prompt.

    This ensures the LLM responds in the configured language.
    """
    code = validate_language_code(language_code)
    lang_name = get_language_name(code)

    if code == DEFAULT_LANGUAGE:
        return prompt  # No injection needed for English

    language_instruction = (
        f"\n\nIMPORTANT: Always respond in {lang_name} ({code}), "
        f"regardless of the language the user writes in. "
        f"All your responses must be in {lang_name}."
    )
    return prompt + language_instruction
