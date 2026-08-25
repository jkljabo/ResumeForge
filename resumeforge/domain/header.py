from dataclasses import dataclass


@dataclass(frozen=True)
class Header:
    name: str
    headline: str
    tagline: str
    location: str
    phone: str
    email: str
    linkedin: str
    github: str
    portfolio: str