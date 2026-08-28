from dataclasses import dataclass, field


@dataclass(frozen=True)
class Certification:
    name: str
    issuer: str = ""
    year: str = ""
    tags: list[str] = field(default_factory=list)