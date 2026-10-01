from dataclasses import dataclass
from pathlib import Path
from resumeforge.constants import (
    DEFAULT_PROFILE_NAME,
    DEFAULT_PROFILE_FILE,
)

@dataclass
class Profile:
    name: str
    directory: Path

    is_default: bool = False

    headline: str | None = None
    full_name: str | None = None
    color_theme: str | None = None
    description: str | None = None
    tags: str | None = None
    notes: str | None = None
    category: str | None = None
    visibility: str | None = None
    owner: str | None = None

    @property
    def resume_path(self) -> Path:
        return self.directory / DEFAULT_PROFILE_FILE