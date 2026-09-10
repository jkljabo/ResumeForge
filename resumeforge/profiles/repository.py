import json
import shutil
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

    def create(self, name: str) -> Profile:
        if self.root is None:
            raise ValueError(
                "Cannot create profiles using the default repository."
            )

        profile_dir = self.root / name

        if profile_dir.exists():
            raise FileExistsError(
                f"Profile '{name}' already exists."
            )

        profile_dir.mkdir(
            parents=True,
        )

        resume_file = profile_dir / DEFAULT_PROFILE_FILE

        resume_file.write_text(
            "{}",
            encoding="utf-8",
        )

        return Profile(
            name=name,
            directory=profile_dir,
            is_default=(name == DEFAULT_PROFILE_NAME),
        )

    def remove(self, name: str) -> None:
        if self.root is None:
            raise ValueError(
                "Cannot remove profiles using the default repository."
            )

        profile = self.get(name)

        shutil.rmtree(profile.directory)

    def update(
        self,
        name: str,
        updates: dict,
    ) -> None:
        if self.root is None:
            raise ValueError(
                "Cannot update profiles using the default repository."
            )

        profile = self.get(name)

        resume_file = profile.resume_path

        with resume_file.open(
            "r",
            encoding="utf-8",
        ) as file:
            resume = json.load(file)

        resume.update(updates)

        with resume_file.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                resume,
                file,
                indent=4,
            )

    def list(self) -> list[Profile]:
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
                    directory=resume_file.parent,
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
                    directory=directory,
                    is_default=(directory.name == DEFAULT_PROFILE_NAME),
                )
            )

        return profiles

    def exists(self, name: str) -> bool:
        return any(profile.name == name for profile in self.list())

    def get(self, name: str) -> Profile:
        for profile in self.list():
            if profile.name == name:
                return profile

        raise FileNotFoundError(f"Profile '{name}' not found.")

    def get_default(self) -> Profile:
        for profile in self.list():
            if profile.is_default:
                return profile

        raise FileNotFoundError("Default profile not found.")