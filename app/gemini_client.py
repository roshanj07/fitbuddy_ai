from google import genai

from .config import (
    GEMINI_API_KEY,
    AI_REQUIRED
)


_client = None


if GEMINI_API_KEY:
    _client = genai.Client(
        api_key=GEMINI_API_KEY
    )


def generate_text(
    prompt: str,
    model: str,
    fallback: str
) -> str:

    if not _client:

        if AI_REQUIRED:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured."
            )

        return fallback

    try:

        response = _client.models.generate_content(
            model=model,
            contents=prompt
        )

        text = (
            response.text or ""
        ).strip()

        if text:
            return text

        return fallback

    except Exception as exc:

        if AI_REQUIRED:
            raise RuntimeError(
                f"Gemini request failed: {exc}"
            ) from exc

        return fallback