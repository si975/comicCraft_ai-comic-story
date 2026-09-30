"""PDF export for ComicCraft."""

from pathlib import Path
from fpdf import FPDF

EXPORT_DIR = Path("static/exports")
EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def save_pdf(comic):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 12, "ComicCraft - AI Comic Story", ln=True)

    pdf.ln(5)

    for panel in comic:
        panel_number = panel.get("panel_number", "")
        title = panel.get("title", "")
        scene = panel.get("scene_description", "")
        narration = panel.get("narration", "")
        dialogue = panel.get("dialogue", "")

        pdf.set_font("Arial", "B", 15)
        pdf.cell(
            0,
            10,
            f"Panel {panel_number}: {title}",
            ln=True
        )

        pdf.set_font("Arial", "", 11)

        if scene:
            pdf.multi_cell(
                0,
                7,
                f"Scene: {scene}"
            )
            pdf.ln(2)

        if narration:
            pdf.multi_cell(
                0,
                7,
                f"Narration: {narration}"
            )
            pdf.ln(2)

        if dialogue:
            pdf.multi_cell(
                0,
                7,
                f"Dialogue: {dialogue}"
            )
            pdf.ln(5)

    output = EXPORT_DIR / "comiccraft_export.pdf"

    pdf.output(str(output))

    return str(output)