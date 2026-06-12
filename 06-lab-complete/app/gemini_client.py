from google import genai
from google.genai import types

from app.config import settings


def ask_gemini(prompt: str) -> str:
    if not settings.gemini_api_key:
        raise RuntimeError("Missing GEMINI_API_KEY or GOOGLE_API_KEY")

    client = genai.Client(api_key=settings.gemini_api_key)
    response = client.models.generate_content(
        model=settings.llm_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=settings.temperature,
            max_output_tokens=settings.max_output_tokens,
        ),
    )

    return response.text or "Gemini khong tra ve noi dung."
