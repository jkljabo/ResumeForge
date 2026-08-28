from dataclasses import dataclass, field


@dataclass(frozen=True)
class Experience:
    employer: str
    title: str
    location: str
    start_date: str
    end_date: str
    summary: str = ""
    accomplishments: list[str] = field(default_factory=list)
    technologies: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)