from fastapi import FastAPI

from parser import scan_repository
from utils import clone_repo

from documentation_generator import generate_documentation
from code_review import review_repository


app = FastAPI()


# ---------------------------------
# Home Endpoint
# ---------------------------------
@app.get("/")
def home():

    return {
        "message": "Welcome to Git-Detective 🚀"
    }


# ---------------------------------
# Analyze Repository
# ---------------------------------
@app.post("/analyze")
def analyze_repository(repo_url: str):

    # Clone repository
    repo_path = clone_repo(repo_url)

    # Scan repository files
    files = scan_repository(repo_path)

    # Generate documentation
    generate_documentation(repo_path)

    # Run code review
    review_repository(repo_path)

    return {

        "status": "success",

        "repository": repo_url,

        "total_files": len(files),

        "documentation": "PROJECT_DOCUMENTATION.md generated",

        "code_review": "Completed",

        "message": "Repository analysis completed successfully 🚀"
    }