from pathlib import Path

from .profile import Profile


class ProfileRepository:
    """
    Discovers available resume profiles.
    """

    def __init__(self) -> None:
        self._data_dir = Path(__file__).resolve().parent.parent / "data"

    def list_profiles(self) -> list[Profile]:
        resume_path = self._data_dir / "resume.json"

        if not resume_path.exists():
            return []

        return [
            Profile(
                name="software_engineer",
                path=resume_path,
            )
        ]