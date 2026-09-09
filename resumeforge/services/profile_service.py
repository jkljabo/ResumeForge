from pathlib import Path
import shutil


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

    def create(
        self,
        name: str,
    ):

        profile_dir = self.root / name

        if profile_dir.exists():
            raise FileExistsError(
                f"Profile '{name}' already exists."
            )

        profile_dir.mkdir(
            parents=True,
        )

        (
            profile_dir
            / "resume.json"
        ).write_text(
            "{}",
            encoding="utf-8",
        )

    def list(self) -> list[str]:

        if not self.root.exists():
            return []

        return sorted(
            p.name
            for p in self.root.iterdir()
            if p.is_dir()
        )

    def remove(
        self,
        name: str,
    ) -> None:

        profile_path = self.root / name

        if not profile_path.exists():
            raise FileNotFoundError(
                f"Profile '{name}' does not exist."
            )

        shutil.rmtree(profile_path)