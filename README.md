# ResumeForge

ResumeForge is an AI-assisted resume tailoring and generation platform written in Python.

It analyzes a job description, matches it against a resume profile, tailors resume content for Applicant Tracking Systems (ATS), and generates polished resumes using configurable templates, themes, and export formats.

---

## Features

- ATS keyword matching
- Resume scoring
- AI-assisted resume tailoring pipeline
- Markdown resume generation
- DOCX export
- Configurable templates
- Configurable themes
- Command-line interface (CLI)
- Modular architecture
- 185+ automated tests

---

## Requirements

- Python 3.13+
- Virtual environment

---

## Installation

### Clone the repository

```powershell
git clone https://github.com/jkljabo/ResumeForge.git
cd ResumeForge
```

### Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

## Build

```powershell
python build_resume.py
```

---

## Command Line

Display available options:

```powershell
resumeforge --help
```

Generate a tailored resume:

```powershell
resumeforge --job job.txt --output resume.md
```

---

## Run Tests

```powershell
python -m pytest
```

Current status:

- ✅ 185 automated tests passing

---

## Verify Project

```powershell
.\verify-project.ps1
```

---

## Packaging

Build source and wheel distributions:

```powershell
python -m build --no-isolation
```

---

## Project Status

Current release:

**v0.1.1-alpha**

---

## Roadmap

### Completed

- ✅ Resume domain model
- ✅ ATS matching engine
- ✅ Resume tailoring engine
- ✅ Markdown generation
- ✅ DOCX generation
- ✅ Export pipeline
- ✅ Installable CLI
- ✅ Modern Python packaging
- ✅ Modular architecture
- ✅ Comprehensive unit testing

### Planned

- ☐ PDF export improvements
- ☐ HTML export
- ☐ Multiple resume profiles
- ☐ LinkedIn export
- ☐ AI-generated summaries
- ☐ Skill recommendation engine

---

## License

MIT License

Copyright (c) 2026 Jason Little (jkljabo)