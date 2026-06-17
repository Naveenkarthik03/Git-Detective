# Git-Detective

Git-Detective is an AI-powered GitHub repository analysis tool that helps developers understand unfamiliar codebases quickly.

It can clone repositories, analyze files, build dependency graphs, and answer questions about the repository using AI.

---

## Features

Analyze GitHub repositories

Clone repositories automatically

Scan and list project files

Build dependency graphs

Understand file relationships

AI-powered repository Q&A

Summarize repositories

---

## Tech Stack

- Python
- FastAPI
- GitPython
- NetworkX
- Google Gemini API
- Python Dotenv

---

## Project Workflow

GitHub Repository URL

↓

Clone Repository

↓

Scan Files

↓

Build Dependency Graph

↓

Read Repository Files

↓

AI Question Answering

↓

Repository Summary

---

## Example Questions

- Explain what `main.py` does
- Explain `parser.py`
- Explain `utils.py`
- Which files interact with GitHub?
- What is the workflow of this project?
- Summarize this repository in 5 bullet points

---

## Project Progress

### Phase 1 - Repository Parser

- Clone GitHub repositories
- Scan repository files

### Phase 2 - Dependency Graph

- Analyze Python imports
- Build file relationships

### Phase 3 - AI Repository Q&A

- Read repository files
- Ask questions about the codebase
- Generate repository summaries

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Analyze a repository and then run:

```bash
python ai_engine.py
```

---

## Author

Naveen Karthik