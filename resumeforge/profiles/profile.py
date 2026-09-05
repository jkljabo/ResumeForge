from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Profile:
    name: str
    resume_path: Path
    is_default: bool = False