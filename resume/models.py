from dataclasses import dataclass

@dataclass
class ContactInfo:
    name: str
    headline: str
    tagline: str
    location: str
    phone: str
    email: str
    linkedin: str
    github: str
    portfolio: str