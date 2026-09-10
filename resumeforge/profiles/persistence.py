from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ProfilePersistence:
    """Reads and writes profile JSON documents."""

    def load(
        self,
        resume_path: Path,
    ) -> dict[str, Any]:
        with resume_path.open(
            encoding="utf-8",
        ) as file:
            return json.load(file)

    def save(
        self,
        resume_path: Path,
        data: dict[str, Any],
    ) -> None:
        with resume_path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=2,
                ensure_ascii=False,
            )