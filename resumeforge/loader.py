import json
from pathlib import Path

from resumeforge.domain import (
    Header,
    ResumeProfile,
    Education,
    Experience,
    Summary,
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

    summary = Summary(text=data.get("summary", ""))

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
            employer=item.get("company", ""),
            title=item.get("title", ""),
            location=item.get("location", ""),
            start_date=item.get("start", ""),
            end_date=item.get("end", ""),
            summary=item.get("summary", ""),
            accomplishments=item.get("bullets", []),
            technologies=item.get("technologies", []),
        )
        for item in data.get("experience", [])
    ]

    return ResumeProfile(
        header=header,
        summary=summary,
        education=education,
        experience=experience,
    )