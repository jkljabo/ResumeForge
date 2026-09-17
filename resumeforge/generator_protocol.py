from pathlib import Path
from typing import Protocol, runtime_checkable

from resumeforge.resume.document import ResumeDocument

@runtime_checkable
class ResumeGeneratorProtocol(Protocol):

    def generate(
        self,
        profile,
        job: str,
        destination: Path,
    ) -> ResumeDocument:
        ...