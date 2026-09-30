"""Stable Diffusion image-generation integration."""

from pathlib import Path

OUTPUT_DIR = Path("static/panels")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def generate_image(image_prompt, panel_number):
    # Replace this placeholder with Hugging Face Diffusers/Stable Diffusion
    # generation when the required model and credentials are configured.
    return f"/static/panels/panel_{panel_number}.png"
