from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from app.gemini_flash import generate_outline
from app.gemini_pro import generate_story
from app.exporters import save_pdf

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# Store the latest generated comic
latest_comic = []


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):
    global latest_comic

    # Step 1: Generate 5-panel outline
    outline = generate_outline(
        story_prompt,
        character_name,
        setting,
        tone,
        art_style
    )

    # Step 2: Generate narration and dialogue
    story = generate_story(
        outline,
        character_name,
        tone
    )

    # Step 3: Combine outline + story
    panels = []

    for i, panel in enumerate(outline):
        story_data = story[i] if i < len(story) else {}

        panels.append({
            "panel_number": panel.get(
                "panel_number",
                i + 1
            ),
            "title": panel.get(
                "title",
                f"Panel {i + 1}"
            ),
            "scene_description": panel.get(
                "scene_description",
                ""
            ),
            "image_prompt": panel.get(
                "image_prompt",
                ""
            ),
            "narration": story_data.get(
                "narration",
                ""
            ),
            "dialogue": story_data.get(
                "dialogue",
                ""
            )
        })

    # Save latest generated comic
    latest_comic = panels

    return templates.TemplateResponse(
        request=request,
        name="comic_preview.html",
        context={
            "request": request,
            "panels": panels
        }
    )


@router.get("/download-pdf")
async def download_pdf():
    global latest_comic

    if not latest_comic:
        return {
            "error": "Please generate a comic first."
        }

    pdf_file = save_pdf(latest_comic)

    return FileResponse(
        path=pdf_file,
        filename="comiccraft_export.pdf",
        media_type="application/pdf"
    )


@router.get("/export-success", response_class=HTMLResponse)
async def export_success(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="export_success.html",
        context={
            "request": request
        }
    )


@router.get("/test-image")
async def test_image(
    prompt: str = "comic book scene"
):
    return {
        "message": "Image generation test route",
        "prompt": prompt
    }