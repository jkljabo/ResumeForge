from dataclasses import dataclass


@dataclass(frozen=True)
class Certification:
    name: str
    issuer: str = ""
    year: str = ""