"""Gemini integration for structured 5-panel comic outlines."""

import os
import json
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = os.getenv(
    "GEMINI_FLASH_MODEL",
    "gemini-3.8-flash"
)

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_outline(
    story_prompt,
    character_name,
    setting,
    tone,
    art_style
):
    prompt = f"""
Create a 5-panel comic story outline.

Story prompt: {story_prompt}
Character name: {character_name}
Setting: {setting}
Story tone: {tone}
Art style: {art_style}

Return ONLY valid JSON.
Do not add markdown or ```json.

Use exactly this structure:

[
  {{
    "panel_number": 1,
    "title": "Panel title",
    "scene_description": "Detailed scene description",
    "image_prompt": "Detailed image generation prompt"
  }}
]

Create exactly 5 panels.
"""

    last_error = None

    for attempt in range(3):
        try:
            response = client.interactions.create(
                model=GEMINI_MODEL,
                input=prompt
            )

            text = response.output_text.strip()

            if text.startswith("```"):
                text = text.replace("```json", "")
                text = text.replace("```", "")
                text = text.strip()

            return json.loads(text)

        except Exception as error:
            last_error = error

            print(
                f"Gemini request failed "
                f"(attempt {attempt + 1}/3): {error}"
            )

            if attempt < 2:
                time.sleep(5)

    raise RuntimeError(
        "Gemini API is temporarily unavailable. "
        "Please try Generate again after a short wait."
    ) from last_error