from pathlib import Path

from resumeforge.domain.certification import Certification
from resumeforge.domain.education import Education
from resumeforge.domain.experience import Experience
from resumeforge.domain.project import Project
from resumeforge.domain.resume import ResumeProfile
import json

from resumeforge.domain.skills import SkillGroup
from resumeforge.domain.summary import Summary
from resumeforge.resume.repository import ResumeRepository
from resumeforge.resume.repository_protocol import ResumeRepositoryProtocol
from resumeforge.domain.resume import ResumeProfile
from resumeforge.domain.header import Header

def test_repository_implements_protocol():
    repository = ResumeRepository()

    assert isinstance(
        repository,
        ResumeRepositoryProtocol,
    )


def test_load_returns_resume_document():
    repository = ResumeRepository()

    document = repository.load(
        Path("resumeforge/data/resume.json")
    )

    assert isinstance(
        document,
        ResumeProfile,
    )


def test_save_writes_resume_json(tmp_path):
    repository = ResumeRepository()

    resume = ResumeProfile(
        header=Header(
            name="Jason Little",
            headline="Senior Software Engineer",
            tagline="",
            location="",
            phone="",
            email="",
            linkedin="",
            github="",
            portfolio="",
        ),
    )

    output = tmp_path / "resume.json"

    repository.save(
        resume,
        output,
    )

    data = json.loads(
        output.read_text(encoding="utf-8")
    )

    assert data["name"] == "Jason Little"


def test_save_writes_summary(tmp_path):
    repository = ResumeRepository()

    resume = ResumeProfile(
        header=Header(
            name="Jason Little",
            headline="Senior Software Engineer",
            tagline="",
            location="",
            phone="",
            email="",
            linkedin="",
            github="",
            portfolio="",
        ),
        summary=Summary(
            text="Twenty years building enterprise applications.",
        ),
    )

    output = tmp_path / "resume.json"

    repository.save(
        resume,
        output,
    )

    data = json.loads(
        output.read_text(encoding="utf-8")
    )

    assert data["summary"] == (
        "Twenty years building enterprise applications."
    )


def test_save_writes_education(tmp_path):
    repository = ResumeRepository()

    resume = ResumeProfile(
        header=Header(
            name="Jason Little",
            headline="Senior Software Engineer",
            tagline="",
            location="",
            phone="",
            email="",
            linkedin="",
            github="",
            portfolio="",
        ),
        education=[
            Education(
                school="Georgia Tech",
                degree="B.S.",
                field="Computer Science",
                graduation_year="2002",
            )
        ],
    )

    output = tmp_path / "resume.json"

    repository.save(resume, output)

    data = json.loads(
        output.read_text(encoding="utf-8")
    )

    assert data["education"] == [
        {
            "school": "Georgia Tech",
            "degree": "B.S.",
            "field": "Computer Science",
            "year": "2002",
        }
    ]


def test_save_writes_experience(tmp_path):
    repository = ResumeRepository()

    resume = ResumeProfile(
        header=Header(
            name="Jason Little",
            headline="Senior Software Engineer",
            tagline="",
            location="",
            phone="",
            email="",
            linkedin="",
            github="",
            portfolio="",
        ),
        experience=[
            Experience(
                employer="CDC",
                title="Senior Software Engineer",
                location="Atlanta, GA",
                start_date="2024",
                end_date="Present",
                summary="Building enterprise applications.",
                accomplishments=[
                    "Designed REST APIs",
                    "Improved performance",
                ],
                technologies=[
                    "C#",
                    ".NET",
                    "Azure",
                ],
            )
        ],
    )

    output = tmp_path / "resume.json"

    repository.save(
        resume,
        output,
    )

    data = json.loads(
        output.read_text(
            encoding="utf-8",
        )
    )

    assert data["experience"] == [
        {
            "company": "CDC",
            "title": "Senior Software Engineer",
            "location": "Atlanta, GA",
            "start": "2024",
            "end": "Present",
            "summary": "Building enterprise applications.",
            "bullets": [
                "Designed REST APIs",
                "Improved performance",
            ],
            "technologies": [
                "C#",
                ".NET",
                "Azure",
            ],
        }
    ]


def test_save_writes_skills(tmp_path):
    repository = ResumeRepository()

    resume = ResumeProfile(
        header=Header(
            name="Jason Little",
            headline="Senior Software Engineer",
            tagline="",
            location="",
            phone="",
            email="",
            linkedin="",
            github="",
            portfolio="",
        ),
        skills=[
            SkillGroup(
                category="Languages",
                skills=[
                    "C#",
                    "Python",
                    "SQL",
                ],
            )
        ],
    )

    output = tmp_path / "resume.json"

    repository.save(
        resume,
        output,
    )

    data = json.loads(
        output.read_text(
            encoding="utf-8",
        )
    )

    assert data["skills"] == [
        {
            "category": "Languages",
            "skills": [
                "C#",
                "Python",
                "SQL",
            ],
        }
    ]


def test_save_writes_certifications(tmp_path):
    repository = ResumeRepository()

    resume = ResumeProfile(
        header=Header(
            name="Jason Little",
            headline="Senior Software Engineer",
            tagline="",
            location="",
            phone="",
            email="",
            linkedin="",
            github="",
            portfolio="",
        ),
        certifications=[
            Certification(
                name="Azure Developer Associate",
                issuer="Microsoft",
                year="2025",
                tags=[
                    "Azure",
                    ".NET",
                ],
            )
        ],
    )

    output = tmp_path / "resume.json"

    repository.save(
        resume,
        output,
    )

    data = json.loads(
        output.read_text(
            encoding="utf-8",
        )
    )

    assert data["certifications"] == [
        {
            "name": "Azure Developer Associate",
            "issuer": "Microsoft",
            "year": "2025",
            "tags": [
                "Azure",
                ".NET",
            ],
        }
    ]


def test_save_writes_projects(tmp_path):
    repository = ResumeRepository()

    resume = ResumeProfile(
        header=Header(
            name="Jason Little",
            headline="Senior Software Engineer",
            tagline="",
            location="",
            phone="",
            email="",
            linkedin="",
            github="",
            portfolio="",
        ),
        projects=[
            Project(
                name="ResumeForge",
                description="AI-powered resume tailoring tool.",
                technologies=[
                    "Python",
                    "OpenAI",
                    "Markdown",
                ],
                url="https://github.com/jkljabo/ResumeForge",
                tags=[
                    "AI",
                    "Resume",
                ],
            )
        ],
    )

    output = tmp_path / "resume.json"

    repository.save(
        resume,
        output,
    )

    data = json.loads(
        output.read_text(
            encoding="utf-8",
        )
    )

    assert data["projects"] == [
        {
            "name": "ResumeForge",
            "description": "AI-powered resume tailoring tool.",
            "technologies": [
                "Python",
                "OpenAI",
                "Markdown",
            ],
            "url": "https://github.com/jkljabo/ResumeForge",
            "tags": [
                "AI",
                "Resume",
            ],
        }
    ]


def test_save_then_load_round_trip(tmp_path):
    repository = ResumeRepository()

    resume = ResumeProfile(
        header=Header(
            name="Jason Little",
            headline="Senior Software Engineer",
            tagline="Cloud Modernization",
            location="Atlanta",
            phone="555-555-5555",
            email="jason@example.com",
            linkedin="linkedin",
            github="github",
            portfolio="portfolio",
        ),
        summary=Summary(
            text="Experienced engineer.",
        ),
        education=[
            Education(
                school="Georgia Tech",
                degree="B.S.",
                field="Computer Science",
                graduation_year="2002",
            )
        ],
        experience=[
            Experience(
                employer="CDC",
                title="Senior Software Engineer",
                location="Atlanta",
                start_date="2024",
                end_date="Present",
                summary="Building enterprise software.",
                accomplishments=["Built APIs"],
                technologies=["Python"],
            )
        ],
        skills=[
            SkillGroup(
                category="Languages",
                skills=["Python"],
            )
        ],
        certifications=[
            Certification(
                name="Azure Developer",
                issuer="Microsoft",
                year="2025",
                tags=["Azure"],
            )
        ],
        projects=[
            Project(
                name="ResumeForge",
                description="Resume tool",
                technologies=["Python"],
                url="https://github.com/jkljabo/ResumeForge",
                tags=["AI"],
            )
        ],
    )

    output = tmp_path / "resume.json"

    repository.save(resume, output)

    loaded = repository.load(output)

    assert loaded == resume