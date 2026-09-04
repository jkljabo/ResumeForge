from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Profile:
    """
    Represents a stored resume profile.
    """

    name: str
    path: Path
    description: str = ""
    is_default: bool = False

    @property
    def resume_file(self) -> Path:
        return self.path / "resume.json"