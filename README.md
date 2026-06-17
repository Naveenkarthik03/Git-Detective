# Git-Detective

Git-Detective is an AI-powered GitHub repository analysis tool that helps developers understand unfamiliar codebases quickly.

It can clone repositories, analyze files, build dependency graphs, answer repository questions using AI, generate documentation, and perform basic code reviews.

---

## Features

Analyze GitHub repositories

Clone repositories automatically

Scan and list project files

Build dependency graphs

AI-powered repository Q&A

Generate architecture diagrams

Generate project documentation

Perform code reviews

---

## Tech Stack

- Python
- FastAPI
- GitPython
- NetworkX
- Google Gemini API
- Python Dotenv
- Matplotlib

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

Generate Architecture Diagram

↓

Generate Documentation

↓

Perform Code Review

---

## Example Questions

- Explain what `main.py` does
- Explain `parser.py`
- Explain `utils.py`
- Which files interact with GitHub?
- What is the workflow of this project?
- Summarize this repository in 5 bullet points

---

## Project Structure

```text
Git-Detective/

README.md
requirements.txt
.gitignore

main.py
parser.py
utils.py

dependency_graph.py

repo_reader.py
ai_engine.py

architecture_diagram.py

documentation_generator.py

code_review.py

PROJECT_DOCUMENTATION.md
architecture_diagram.png
```

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

### Phase 4 - Architecture Diagram

- Visualize project architecture
- Display file relationships

### Phase 5 - Documentation Generator

- Generate repository documentation
- Analyze project files

### Phase 6 - Code Review Assistant

- Analyze code quality
- Detect large files
- Count imports
- Detect TODO comments

### Phase 7 - Deployment

- Deploy Git-Detective to the web

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

Analyze a repository.

Then run:

```bash
python ai_engine.py
```

Optional tools:

```bash
python architecture_diagram.py

python documentation_generator.py

python code_review.py
```

---

## Future Improvements

- Better AI explanations
- Support more programming languages
- Export reports as PDF
- Interactive dashboard
- One-click deployment

---

## Author

Naveen Karthik