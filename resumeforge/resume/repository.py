import json
from pathlib import Path

from resumeforge.domain.certification import Certification
from resumeforge.domain.education import Education
from resumeforge.domain.experience import Experience
from resumeforge.domain.header import Header
from resumeforge.domain.project import Project
from resumeforge.domain.resume import ResumeProfile
from resumeforge.domain.skills import SkillGroup
from resumeforge.domain.summary import Summary
from resumeforge.resume.repository_protocol import ResumeRepositoryProtocol


class ResumeRepository(
    ResumeRepositoryProtocol,
):

    def load(
        self,
        path: Path,
    ) -> ResumeProfile:
        with path.open(
            "r",
            encoding="utf-8",
        ) as f:
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
        
        skills = [
            SkillGroup(
                category=item.get("category", ""),
                skills=item.get("skills", []),
            )
            for item in data.get("skills", [])
        ]

        certifications = [
            Certification(
                name=item.get("name", ""),
                issuer=item.get("issuer", ""),
                year=item.get("year", ""),
                tags=item.get("tags", []),
            )
            for item in data.get("certifications", [])
        ]

        projects = [
            Project(
                name=item.get("name", ""),
                description=item.get("description", ""),
                technologies=item.get("technologies", []),
                url=item.get("url", ""),
                tags=item.get("tags", []),
            )
            for item in data.get("projects", [])
        ]
        
        return ResumeProfile(
            header=header,
            summary=summary,
            education=education,
            experience=experience,
            skills=skills,
            certifications=certifications,
            projects=projects,
        )

    def save(
        self,
        resume: ResumeProfile,
        path: Path,
    ) -> None:

        data = self._to_dict(
            resume,
        )

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
            )

    def _to_dict(
        self,
        resume: ResumeProfile,
    ) -> dict:

        return {
            "name": resume.header.name,
            "headline": resume.header.headline,
            "tagline": resume.header.tagline,
            "location": resume.header.location,
            "phone": resume.header.phone,
            "email": resume.header.email,
            "linkedin": resume.header.linkedin,
            "github": resume.header.github,
            "portfolio": resume.header.portfolio,
            "summary": (
                resume.summary.text
                if resume.summary is not None
                else ""
            ),
            "education": [
                {
                    "school": item.school,
                    "degree": item.degree,
                    "field": item.field,
                    "year": item.graduation_year,
                }
                for item in resume.education
            ],
            "experience": [
                {
                    "company": item.employer,
                    "title": item.title,
                    "location": item.location,
                    "start": item.start_date,
                    "end": item.end_date,
                    "summary": item.summary,
                    "bullets": item.accomplishments,
                    "technologies": item.technologies,
                }
                for item in resume.experience
            ],
            "skills": [
                {
                    "category": item.category,
                    "skills": item.skills,
                }
                for item in resume.skills
            ],
            "certifications": [
                {
                    "name": item.name,
                    "issuer": item.issuer,
                    "year": item.year,
                    "tags": item.tags,
                }
                for item in resume.certifications
            ],
            "projects": [
                {
                    "name": item.name,
                    "description": item.description,
                    "technologies": item.technologies,
                    "url": item.url,
                    "tags": item.tags,
                }
                for item in resume.projects
            ],
        }    