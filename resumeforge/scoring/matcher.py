from resumeforge.scoring.section_weights import SectionWeights
from resumeforge.scoring.weights import WeightTable
from resumeforge.scoring.synonyms import SynonymTable
import re

class Matcher:
    def __init__(
        self,
        weights=None,
        section_weights=None,
        synonyms=None,
    ):
        self.weights = weights or WeightTable()
        self.section_weights = (
            section_weights or SectionWeights()
        )
        self.synonyms = synonyms or SynonymTable()
    
    def _normalize(self, text: str) -> set[str]:
        words = re.findall(r"[a-z0-9\+\#\.]+", text.lower())
        return set(words)

    def score(self, resume, job_description: str) -> int:
        if not job_description:
            return 0

        job_terms = self._normalize(job_description)
        job_terms = self.synonyms.expand(job_terms)
        
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
                    job_terms,
                    multiplier,
                )

        return score

    def _score_tags(
        self,
        tags,
        job_terms,
        multiplier,
    ):
        # Each matching keyword contributes:
        #     keyword_weight × section_weight
        # This allows experience matches to outrank skills-only matches.
        
        score = 0

        matches = {
            tag.lower()
            for tag in tags
        } & job_terms

        for keyword in matches:
            score += (
                self.weights.get(keyword)
                * multiplier
            )

        return score