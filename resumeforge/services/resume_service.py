from pathlib import Path

from resumeforge.resume.repository import ResumeRepository


class ResumeService:

    def __init__(
        self,
        repository: ResumeRepository,
    ):
        self.repository = repository

    def load(self, path: Path):
        return self.repository.load(path)