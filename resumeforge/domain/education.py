from dataclasses import dataclass


@dataclass(frozen=True)
class Education:
    school: str
    degree: str
    field: str
    graduation: str