from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from resumeforge.resume.document import ResumeDocument
from resumeforge.domain.resume import ResumeProfile

@runtime_checkable
class ResumeRepositoryProtocol(Protocol):

    def load(
        self,
        path: Path,
    ) -> ResumeDocument:
        ...

    def save(
        self,
        resume: ResumeProfile,
        path: Path,
    ) -> None:
        ...