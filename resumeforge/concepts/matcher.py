from .technology import TechnologyConcepts


class ConceptMatcher:
    def __init__(self):
        self.technology = TechnologyConcepts()

    def matches(self, left: str, right: str) -> bool:
        left = left.lower().strip()
        right = right.lower().strip()

        if left == right:
            return True

        for aliases in self.technology.aliases.values():
            if left in aliases and right in aliases:
                return True

        return False