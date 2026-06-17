from fastapi import FastAPI

from parser import scan_repository
from utils import clone_repo

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CodebaseX API"}


@app.post("/analyze")
def analyze_repository(repo_url: str):

    repo_path = clone_repo(repo_url)

    files = scan_repository(repo_path)

    return {
        "total_files": len(files),
        "files": files
    }