from pathlib import Path

from resumeforge.resume.factory import create_resume_service


def load_resume(path: Path):
    return create_resume_service().load(path)