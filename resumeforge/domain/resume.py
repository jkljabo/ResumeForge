from dataclasses import dataclass

from .header import Header


@dataclass(frozen=True)
class ResumeProfile:
    header: Header