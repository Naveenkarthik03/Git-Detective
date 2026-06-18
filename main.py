from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from parser import scan_repository
from utils import clone_repo

from documentation_generator import generate_documentation
from code_review import review_repository

from architecture_diagram import generate_diagram
from ai_engine import generate_summary


app = FastAPI()

# -----------------------------
# Templates
# -----------------------------
templates = Jinja2Templates(
    directory="templates"
)

# -----------------------------
# Static folder
# -----------------------------
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# -----------------------------
# Home Page
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# -----------------------------
# Analyze Repository
# -----------------------------
@app.post("/analyze")
def analyze_repository(repo_url: str):

    # Clone repository
    repo_path = clone_repo(repo_url)

    # Scan files
    files = scan_repository(repo_path)

    # Documentation
    try:

        documentation = generate_documentation(
            repo_path
        )

    except Exception as e:

        documentation = f"Error: {e}"

    # Architecture Diagram
    try:

        diagram = generate_diagram(
            repo_path
        )

    except Exception as e:

        diagram = f"Error: {e}"

    # Code Review
    try:

        review_repository(
            repo_path
        )

        code_review = "Completed"

    except Exception as e:

        code_review = f"Error: {e}"

    # AI Summary
    try:

        summary = generate_summary()

    except Exception as e:

        summary = f"AI unavailable: {e}"

    return {

        "status": "success",

        "repository": repo_url,

        "total_files": len(files),

        "files": files,

        "documentation": documentation,

        "architecture_diagram": diagram,

        "code_review": code_review,

        "ai_summary": summary
    }