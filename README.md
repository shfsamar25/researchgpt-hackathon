ResearchGPT – AI-Powered Literature Review Assistant
ResearchGPT is a web-based assistant that generates structured literature reviews for a given research topic in seconds. It helps students, researchers, and innovators quickly understand the current landscape, identify research gaps, and get ideas for future directions.
​

Features
Automatic literature review outline generation (Introduction, Existing Work, Research Gaps, Future Directions).
​

Research gap detection and suggestion of possible innovations.
​

Fast, lightweight UI that runs in the browser and talks to a FastAPI backend.

Designed for hackathon-style rapid prototyping and demos.

Tech Stack
Frontend: HTML, CSS, JavaScript (single-page UI).

Backend: FastAPI (Python) with Uvicorn server.

AI Model: LLM endpoint (configurable) for summarization and gap detection.
​

Data Sources (future scope): ArXiv, Semantic Scholar, and other research APIs.
​

Project Structure
text
researchgpt-hackathon/
├── backend/
│   ├── main.py          # FastAPI app with /generate_outline endpoint
│   ├── requirements.txt # Backend Python dependencies
│   └── venv/            # Python virtual environment (local)
├── index.html           # Frontend UI
├── styles.css           # Styling for the UI (optional)
└── README.md
Getting Started (Local Setup)
Prerequisites
Python 3.9+ installed

Windows with PowerShell or CMD

A browser (Chrome / Edge)

1. Clone the repository
bash
git clone <your-repo-url> researchgpt-hackathon
cd researchgpt-hackathon
2. Setup and run the backend (FastAPI)
Open PowerShell and run:

powershell
cd "C:\Users\shifa samar\researchgpt-hackathon\backend"

python -m venv venv
cmd /c venv\Scripts\activate.bat

pip install -r requirements.txt
uvicorn main:app --reload
The backend will start on:

text
http://127.0.0.1:8000
Keep this window open while using the app.
​

3. Run the frontend
Open a new PowerShell window and run:

powershell
cd "C:\Users\shifa samar\researchgpt-hackathon"
start index.html
This opens the UI in your default browser.

How to Use
Open the web UI (index.html) in your browser.

Enter a research topic (e.g., "Federated learning for healthcare").

Click Generate outline.

The app will call the backend and generate four sections:

Introduction / Background

Existing Work

Research Gaps

Future Directions / Innovation Ideas

You can tweak the generated text further for your report or presentation.

Roadmap / Future Scope
Integrate real research APIs (ArXiv, Semantic Scholar) to fetch live papers.
​

Multi-language support for non-English researchers.
​

Export structured reviews as PDF / DOCX with proper citations.
​

Team collaboration features and project history.
​

Turn into a SaaS dashboard for universities and research labs.
​

Use Cases
Students writing survey papers or thesis chapters.

Researchers exploring new domains and needing a quick overview.

Startups validating ideas and scanning existing literature.
​

Limitations
This is a hackathon prototype; it may not cover all edge cases.

Quality and depth of summaries depend on the underlying LLM and data sources.

Always verify outputs against original papers before publication.



Team
Developer(s): iqra,zaara,shifa
