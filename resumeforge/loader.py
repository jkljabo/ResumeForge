import json
from pathlib import Path

from resumeforge.domain import Header, ResumeProfile

BASE_DIR = Path(__file__).resolve().parent.parent


def load_resume(profile: str = "resume") -> ResumeProfile:
    file = BASE_DIR / "data" / f"{profile}.json"

    with open(file, encoding="utf-8") as f:
        data = json.load(f)

    header = Header(
        name=data.get("name", ""),
        headline=data.get("headline", ""),
        tagline=data.get("tagline", ""),
        location=data.get("location", ""),
        phone=data.get("phone", ""),
        email=data.get("email", ""),
        linkedin=data.get("linkedin", ""),
        github=data.get("github", ""),
        portfolio=data.get("portfolio", ""),
    )

    return ResumeProfile(header=header)