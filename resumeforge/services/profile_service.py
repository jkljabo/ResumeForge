
from resumeforge.profiles.repository import (
    ProfileRepository,
)
from resumeforge.profiles.repository_protocol import ProfileRepositoryProtocol

class ProfileService:

    def __init__(
        self,
        repository: ProfileRepositoryProtocol | None = None,
    ):
        self.repository = repository

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