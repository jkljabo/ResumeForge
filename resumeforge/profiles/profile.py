from dataclasses import dataclass
from pathlib import Path
from resumeforge.constants import (
    DEFAULT_PROFILE_NAME,
    DEFAULT_PROFILE_FILE,
)

@dataclass(frozen=True)
class Profile:
    name: str
    directory: Path
    is_default: bool = False

    @property
    def resume_path(self) -> Path:
        return self.directory / DEFAULT_PROFILE_FILE