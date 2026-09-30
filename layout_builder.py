def build_comic_layout(panels):
    return [
        {
            "panel_number": p["panel_number"],
            "image_path": p["image_path"],
            "text": p.get("narration", ""),
        }
        for p in panels
    ]
