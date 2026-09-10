import json
import shutil
from pathlib import Path

from resumeforge.constants import DEFAULT_PROFILE_FILE
from resumeforge.profiles.repository import (
    ProfileRepository,
)

class ProfileService:

    def __init__(
        self,
        root: Path | None = None,
    ):
        self.root = (
            Path("profiles")
            if root is None
            else Path(root)
        )

        self.repository = ProfileRepository(root)

    def create(
        self,
        name: str,
    ):

        return self.repository.create(name)

    def list(self) -> list[str]:

        profiles = self.repository.list()

        return [
            profile.name
            for profile in profiles
        ]

    def remove(
        self,
        name: str,
    ) -> None:
        self.repository.remove(name)

    def edit(
        self,
        name: str,
        updates: dict,
    ) -> None:
        self.repository.update(
            name,
            updates,
        )