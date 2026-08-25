from dataclasses import dataclass, field


@dataclass(frozen=True)
class SkillGroup:
    category: str

    skills: list[str] = field(default_factory=list)