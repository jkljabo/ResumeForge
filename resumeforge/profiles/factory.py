from pathlib import Path

from resumeforge.profiles.profile import Profile


class ProfileFactory:

    def create(
        self,
        *,
        name: str,
        directory: Path,
        is_default: bool = False,
    ) -> Profile:

        return Profile(
            name=name,
            directory=directory,
            is_default=is_default,
        )
