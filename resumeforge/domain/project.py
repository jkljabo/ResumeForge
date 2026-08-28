from dataclasses import dataclass, field


@dataclass(frozen=True)
class Project:
    name: str
    description: str
    technologies: list[str] = field(default_factory=list)
    url: str = ""
    tags: list[str] = field(default_factory=list)