from dataclasses import dataclass


@dataclass(frozen=True)
class Summary:
    text: str