# Git-Detective

AI-powered GitHub Repository Analyzer built using FastAPI and Google Gemini API.

Git-Detective helps developers quickly understand unfamiliar repositories by automatically generating architecture diagrams, documentation, AI summaries, and code reviews.

---

## Features

- Analyze public GitHub repositories
- Clone repositories automatically
- Scan and list project files
- Build dependency graphs
- Generate architecture diagrams
- Generate AI summaries
- Generate downloadable documentation
- Perform code reviews
- Display repository insights in a clean web interface

---

## Tech Stack

### Backend

- Python
- FastAPI

### AI

- Google Gemini API

### Visualization

- NetworkX
- Matplotlib

### Repository Analysis

- GitPython
- AST

### Frontend

- HTML
- CSS
- JavaScript

---

## Project Workflow

```text
GitHub Repository URL

↓

Clone Repository

↓

Scan Repository Files

↓

Analyze Dependencies

↓

Generate Architecture Diagram

↓

Generate AI Summary

↓

Generate Documentation

↓

Perform Code Review

↓

Display Results
```

---

## Project Structure

```text
Git-Detective/

static/
templates/

main.py
parser.py
utils.py

dependency_graph.py
architecture_diagram.py

documentation_generator.py

ai_engine.py

repo_reader.py

code_review.py

requirements.txt

README.md

render.yaml
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Git-Detective.git

cd Git-Detective
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## Example Repositories To Test

FastAPI Template

```text
https://github.com/fastapi/full-stack-fastapi-template
```

Flask Project

```text
https://github.com/miguelgrinberg/flasky
```

---

## Future Improvements

- Support multiple programming languages
- Export reports as PDF
- Interactive dependency graphs
- User authentication
- Repository comparison
- Dark mode

---

## Author

**Naveen Karthik**

