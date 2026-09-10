from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from resumeforge.profiles.profile import Profile


@runtime_checkable
class ProfileRepositoryProtocol(Protocol):
    def list(self) -> list[Profile]:
        ...

    def create(self, name: str) -> None:
        ...

    def remove(self, name: str) -> None:
        ...

    def update(
        self,
        name: str,
        updates: dict[str, Any],
    ) -> None:
        ...