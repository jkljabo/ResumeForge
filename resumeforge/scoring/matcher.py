from resumeforge.scoring.section_weights import SectionWeights
from resumeforge.scoring.weights import WeightTable
from resumeforge.concepts import ConceptMatcher

import re

class Matcher:
    def __init__(
        self,
        weights=None,
        section_weights=None,
        concepts=None,
    ):
        self.weights = weights or WeightTable()
        self.section_weights = (
            section_weights or SectionWeights()
        )
        self.concepts = (
            concepts or ConceptMatcher()
        )
    
    def _normalize(self, text: str) -> set[str]:
        words = re.findall(r"[a-z0-9\+\#\.]+", text.lower())
        return set(words)

    def _extract_job_phrases(self, text: str) -> set[str]:
        words = re.findall(
            r"[a-z0-9\+\#\.]+",
            text.lower(),
        )

        phrases = set(words)

        for i in range(len(words) - 1):
            phrases.add(
                f"{words[i]} {words[i+1]}"
            )

        return phrases

    def score(self, resume, job_description: str) -> int:
        if not job_description:
            return 0

        job_phrases = self._extract_job_phrases(job_description)

        score = 0

        sections = (
            "skills",
            "experience",
            "projects",
            "certifications",
        )

        for section in sections:
            multiplier = self.section_weights.get(section)

            for item in getattr(resume, section, []):
                score += self._score_tags(
                    getattr(item, "tags", []),
                    job_phrases,
                    multiplier,
                )

        return score

    def _matches(self, tag, job_phrases):
        tag_lower = tag.lower()

        for phrase in job_phrases:

            if tag_lower == phrase:
                return True

            if self.concepts.matches(tag_lower, phrase):
                return True

        return False

    def _score_tags(
        self,
        tags,
        job_phrases,
        multiplier,
    ):
        # Each matching keyword contributes:
        #     keyword_weight × section_weight
        # This allows experience matches to outrank skills-only matches.
        
        score = 0

        for tag in tags:

            if self._matches(tag, job_phrases):

                score += (
                    self.weights.get(tag.lower())
                    * multiplier
                )

        return score
