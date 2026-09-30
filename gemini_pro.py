"""Gemini integration for comic narration and dialogue."""

import os
import json
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = os.getenv(
    "GEMINI_PRO_MODEL",
    "gemini-3.8-flash"
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_story(outline, character_name, tone):

    prompt = f"""
Create narration and dialogue for this 5-panel comic.

Character: {character_name}
Tone: {tone}

Comic outline:
{json.dumps(outline, indent=2)}

Return ONLY valid JSON.

Use exactly this format:

[
  {{
    "panel_number": 1,
    "narration": "Narration text",
    "dialogue": "Dialogue text"
  }}
]

Create exactly one entry for every panel.
"""

    last_error = None

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )

            text = response.text.strip()

            if text.startswith("```"):
                text = text.replace("```json", "")
                text = text.replace("```", "")
                text = text.strip()

            return json.loads(text)

        except Exception as error:

            last_error = error

            print(
                f"Gemini story request failed "
                f"(attempt {attempt + 1}/3): {error}"
            )

            if attempt < 2:
                time.sleep(10)

    raise RuntimeError(
        "Gemini API is temporarily unavailable. "
        "Please try again after some time."
    ) from last_error