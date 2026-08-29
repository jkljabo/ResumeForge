from resumeforge.concepts import TechnologyConcepts


class ConceptMatcher:
    def __init__(self):
        self.concepts = TechnologyConcepts()

    def matches(self, left, right):
        return left.lower() == right.lower()