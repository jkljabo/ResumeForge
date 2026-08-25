from dataclasses import dataclass, field

from .header import Header
from .summary import Summary
from .experience import Experience
from .education import Education
from .skills import SkillGroup
from .certification import Certification
from .project import Project


@dataclass(frozen=True)
class ResumeProfile:
    header: Header
    summary: Summary | None = None
    experience: list[Experience] = field(default_factory=list)
    education: list[Education] = field(default_factory=list)
    skills: list[SkillGroup] = field(default_factory=list)
    certifications: list[Certification] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)