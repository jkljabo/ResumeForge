from dataclasses import dataclass

from .header import Header
from .summary import Summary


@dataclass(frozen=True)
class ResumeProfile:
    header: Header
    summary: Summary | None = None