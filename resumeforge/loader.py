import json
from pathlib import Path

from resumeforge.domain import (
    Header,
    ResumeProfile,
    Education,
    Experience,
)

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

    education = [
        Education(
            school=item.get("school", ""),
            degree=item.get("degree", ""),
            field=item.get("field", ""),
            graduation_year=item.get("year", ""),
        )
        for item in data.get("education", [])
    ]

    experience = [
        Experience(
            company=item["company"],
            title=item["title"],
            start=item.get("start", ""),
            end=item.get("end", ""),
            bullets=item.get("bullets", []),
        )
        for item in data.get("experience", [])
    ]

    return ResumeProfile(
        header=header,
        education=education,
        experience=experience,
    )