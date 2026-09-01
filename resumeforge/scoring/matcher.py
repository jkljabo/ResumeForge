from resumeforge.scoring.section_weights import SectionWeights
from resumeforge.scoring.weights import WeightTable
from resumeforge.concepts import ConceptMatcher
from resumeforge.scoring.match_result import MatchResult

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

            score += self._score_section(
                getattr(resume, section, []),
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

    def _score_section(
        self,
        items,
        job_phrases,
        multiplier,
    ):
        score = 0

        for item in items:
            score += self._score_tags(
                getattr(item, "tags", []),
                job_phrases,
                multiplier,
            )

        return score

    def match(self, resume, job_description):
        score = self.score(resume, job_description)

        # Keywords used for reporting (coverage, matched, missing)
        job_terms = self._normalize(job_description)

        # Single words + multi-word phrases used for semantic matching
        job_phrases = self._extract_job_phrases(job_description)

        matched = self._collect_matches(
            resume,
            job_terms,
        )

        matched_by_section = self._collect_matches_by_section(
            resume,
            job_terms,
        )
        
        missing = self._collect_missing(
            resume,
            job_terms,
        )

        section_scores = self._collect_section_scores(
            resume,
            job_phrases,
        )

        coverage = self._calculate_coverage(
            matched,
            missing,
        )

        return MatchResult(
            score=score,
            matched=matched,
            missing=missing,
            section_scores=section_scores,
            coverage=coverage,
            matched_by_section=matched_by_section,
        )

    def _collect_matches(self, resume, job_terms):
        matched = set()

        sections = (
            "skills",
            "experience",
            "projects",
            "certifications",
        )

        for section in sections:
            for item in getattr(resume, section, []):
                for tag in getattr(item, "tags", []):
                    if self._matches(tag, job_terms):
                        matched.add(tag.lower())

        return sorted(matched)

    def _collect_matches_by_section(
        self,
        resume,
        job_terms,
    ):
        matches = {}

        sections = (
            "skills",
            "experience",
            "projects",
            "certifications",
        )

        for section in sections:

            section_matches = []

            for item in getattr(resume, section, []):

                for tag in getattr(item, "tags", []):

                    if self._matches(tag, job_terms):

                        section_matches.append(tag.lower())

            matches[section] = sorted(section_matches)

        return matches
        
    def _collect_missing(
        self,
        resume,
        job_terms,
    ):
        missing = set()

        for term in job_terms:
            found = False

            sections = (
                "skills",
                "experience",
                "projects",
                "certifications",
            )

            for section in sections:
                for item in getattr(resume, section, []):
                    for tag in getattr(item, "tags", []):
                        if self._matches(tag, {term}):
                            found = True
                            break

                    if found:
                        break

                if found:
                    break

            if not found:
                missing.add(term)

        return sorted(
            missing,
            key=lambda keyword: self.weights.get(keyword),
            reverse=True,
        )

    def _collect_section_scores(
        self,
        resume,
        job_phrases,
    ):
        section_scores = {}

        sections = (
            "skills",
            "experience",
            "projects",
            "certifications",
        )

        for section in sections:
            multiplier = self.section_weights.get(section)

            section_scores[section] = self._score_section(
                getattr(resume, section, []),
                job_phrases,
                multiplier,
            )

        return section_scores

    def _calculate_coverage(self, matched, missing):
        total = len(matched) + len(missing)

        if total == 0:
            return 0.0

        return round(
            len(matched) / total * 100,
            1,
        )