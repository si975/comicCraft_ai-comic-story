🎨 ComicCraft – AI Comic Story Creator

ComicCraft is a web-based AI application that transforms user-provided story ideas into complete comic stories with AI-generated illustrations.

It uses FastAPI, Google Gemini models, and Stable Diffusion to generate comic outlines, narration, character dialogues, panel illustrations, and a downloadable PDF comic.

✨ Features

- 📝 Generate comic stories from custom prompts
- 👤 Customize the main character name
- 🌍 Choose the story setting
- 🎭 Select the story tone
- 🎨 Select an art style
- 📖 Generate a structured 5-panel comic outline
- 💬 Generate narration and character dialogues
- 🖼️ Generate comic illustrations using Stable Diffusion
- 👀 Preview the generated comic panel-by-panel
- 📄 Export the complete comic as a PDF
- 🔌 REST API support through FastAPI
- 📚 Interactive API documentation with Swagger

🤖 AI Models

ComicCraft uses multiple AI models for different tasks:

Model| Purpose
Gemini Flash| Generates the structured 5-panel comic outline
Gemini Pro| Generates detailed narration and character dialogues
Stable Diffusion| Generates comic-style illustrations

The project uses "models/gemini-1.5-flash", "models/gemini-1.5-pro", and "runwayml/stable-diffusion-v1-5" as described in the project documentation.

🏗️ Architecture

ComicCraft consists of three major components:

┌───────────────────────────┐
│        Frontend           │
│ HTML + CSS + Jinja2       │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│        FastAPI            │
│        Backend            │
└─────────────┬─────────────┘
              │
       ┌──────┴──────┐
       ▼             ▼
┌─────────────┐ ┌────────────────┐
│ Gemini AI   │ │ Stable Diffusion│
│ Story/Text  │ │ Comic Images   │
└─────────────┘ └────────────────┘
              │
              ▼
       ┌──────────────┐
       │ PDF Export   │
       │    FPDF      │
       └──────────────┘

The frontend collects the user's story information, FastAPI manages processing and routing, and the AI services generate the story and illustrations.

📂 Project Components

The main project components include:

ComicCraft/
│
├── app/
│   ├── main.py
│   └── routes.py
│
├── templates/
│   ├── index.html
│   ├── comic_preview.html
│   └── export_success.html
│
├── static/
│   ├── panels/
│   └── exports/
│
├── gemini_flash.py
├── gemini_pro.py
├── image_generator.py
├── layout_builder.py
├── exporters.py
├── requirements.txt
└── README.md

The documented application uses separate modules for outline generation, story generation, image generation, layout building, and PDF exporting.

🔄 How It Works

User enters story details
          ↓
     Gemini Flash
          ↓
  5-panel comic outline
          ↓
      Gemini Pro
          ↓
 Narration + Dialogues
          ↓
   Stable Diffusion
          ↓
   Panel Illustrations
          ↓
  Comic Layout Builder
          ↓
      PDF Export
          ↓
   Downloadable Comic

1. User Input

Users provide:

- Story Prompt
- Main Character Name
- Setting
- Story Tone
- Art Style

2. Generate Outline

"generate_outline()" creates a structured 5-panel comic outline.

3. Generate Story

"generate_story()" expands the outline into narration and character dialogue.

4. Generate Images

"generate_image()" creates comic-style illustrations for each panel and stores them in "static/panels".

5. Build Layout

"build_comic_layout()" combines the generated images with the corresponding story content.

6. Export PDF

"save_pdf()" creates a multi-page PDF containing the comic panels and narration.

🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- Jinja2
- Google Gemini AI
- Hugging Face Diffusers
- Stable Diffusion
- PyTorch
- FPDF
- Pillow
- HTML
- CSS
- Pydantic

📦 Installation

1. Clone the repository

git clone <your-repository-url>
cd ComicCraft

2. Create a virtual environment

Windows

python -m venv env
env\Scripts\activate

macOS/Linux

python -m venv env
source env/bin/activate

3. Install dependencies

pip install -r requirements.txt

The project documentation also lists the required packages including FastAPI, Uvicorn, Jinja2, Google Generative AI, Diffusers, Transformers, FPDF, Pillow, and Accelerate.

🔑 Environment Variables

Create a ".env" file in the project root:

GEMINI_API_KEY=your_gemini_api_key_here
HF_API_KEY=your_huggingface_api_key_here

Keep your API keys private and do not upload ".env" to GitHub. The project documentation specifies Gemini and Hugging Face credentials as environment variables.

Add this to ".gitignore":

.env
env/
venv/
__pycache__/
*.pyc

▶️ Run the Application

Start the FastAPI server:

uvicorn app.main:app --reload

The project documentation specifies this command for local development.

Open:

http://127.0.0.1:8000

API Documentation

FastAPI Swagger documentation:

http://127.0.0.1:8000/docs

🔌 API Routes

Route| Method| Description
"/"| GET| Opens the homepage
"/generate"| POST| Generates a comic from form input
"/generate-comic/json"| POST| Generates a comic using JSON input
"/test-image"| POST| Tests image generation
"/export-success"| GET| Displays export success page

These routes correspond to the documented FastAPI workflow.

🖥️ User Interface

Home Page

The homepage allows users to enter their:

- Story idea
- Character name
- Setting
- Story tone
- Art style

Supported examples in the project documentation include settings such as school, forest, space, and city, and styles such as anime, pixel art, comic book, and realistic.

Comic Preview

The preview page displays each generated panel with:

- Panel number
- Panel title
- AI-generated image
- Scene description
- Caption
- Narration
- Image prompt reference

PDF Export

Users can download the generated comic as a PDF containing the images, panel titles, descriptions, captions, and narration.

🎯 Example

Input:

Story Prompt: A brave fox exploring an enchanted forest
Character Name: Leo
Setting: Enchanted Forest
Tone: Dramatic
Art Style: Anime

ComicCraft processes the input through the AI pipeline and generates:

5-Panel Story Outline
        ↓
Narration + Dialogue
        ↓
5 Comic Illustrations
        ↓
Comic Preview
        ↓
Downloadable PDF

🚀 Future Enhancements

The current project focuses on single-comic generation without user account management. The documented architecture could be extended with:

- 👤 User profiles
- 📚 Personal comic libraries
- 📖 Multi-page story arcs
- 💾 Saved comics
- 🎨 More art styles
- 🧑‍🎨 Character customization
- ☁️ Cloud deployment
- 🔐 Authentication and authorization

The project documentation specifically identifies user profiles, comic libraries, and multi-page story arcs as possible future enhancements.

📌 Project Status

Status: Local development / deployment ready

ComicCraft provides an end-to-end workflow from story prompt to AI-generated comic and downloadable PDF.

👨‍💻 Development

Built using:

FastAPI
Google Gemini
Stable Diffusion
Hugging Face Diffusers
Jinja2
FPDF
Python

📄 License

Add your preferred license here, for example:

MIT License

---

⭐ ComicCraft — Turn your imagination into a comic with AI.
