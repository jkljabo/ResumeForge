from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from resumeforge.resume.document import ResumeDocument


@runtime_checkable
class ResumeRepositoryProtocol(Protocol):

    def load(
        self,
        path: Path,
    ) -> ResumeDocument:
        ...