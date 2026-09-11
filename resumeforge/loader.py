
from importlib.resources import files
from pathlib import Path

from resumeforge.resume.repository import ResumeRepository


def load_resume(resume_path: Path):
    repository = ResumeRepository()

    return repository.load(resume_path)