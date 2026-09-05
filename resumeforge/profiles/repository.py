from pathlib import Path

from .profile import Profile

from resumeforge.constants import (
    DEFAULT_PROFILE_NAME,
    DEFAULT_PROFILE_FILE,
)

class ProfileRepository:
    """
    Discovers and retrieves resume profiles.

    When no root is supplied, the repository exposes the project's existing
    resume.json as a single "default" profile. When a root directory is
    supplied (typically by tests), it discovers profile directories that
    contain a resume.json file.
    """

    def __init__(self, root: Path | None = None):
        self.root = root

    def list_profiles(self) -> list[Profile]:
        #
        # Default application profile
        #
        if self.root is None:
            data_dir = Path(__file__).resolve().parent.parent / "data"
            resume_file = data_dir / DEFAULT_PROFILE_FILE

            if not resume_file.exists():
                return []

            return [
                Profile(
                    name=DEFAULT_PROFILE_NAME,
                    resume_path=resume_file,
                    is_default=True,
                )
            ]

        #
        # Filesystem discovery (used by tests and future multi-profile support)
        #
        if not self.root.exists():
            return []

        profiles: list[Profile] = []

        for directory in sorted(self.root.iterdir()):
            if not directory.is_dir():
                continue

            resume_file = directory / DEFAULT_PROFILE_FILE

            if not resume_file.exists():
                continue

            profiles.append(
                Profile(
                    name=directory.name,
                    resume_path=directory / DEFAULT_PROFILE_FILE,
                    is_default=(directory.name == DEFAULT_PROFILE_NAME),
                )
            )

        return profiles

    def exists(self, name: str) -> bool:
        return any(profile.name == name for profile in self.list_profiles())

    def get(self, name: str) -> Profile:
        for profile in self.list_profiles():
            if profile.name == name:
                return profile

        raise FileNotFoundError(f"Profile '{name}' not found.")

    def get_default(self) -> Profile:
        for profile in self.list_profiles():
            if profile.is_default:
                return profile

        raise FileNotFoundError("Default profile not found.")