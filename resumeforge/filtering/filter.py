from copy import deepcopy

from resumeforge.scoring.factory import create_matcher
from resumeforge.keywords import KeywordExtractor


class ResumeFilter:
    def __init__(
        self,
        matcher=None,
        extractor=None,
    ):
        self.matcher = (
            matcher
            if matcher is not None
            else create_matcher()
        )

        self.extractor = (
            extractor
            if extractor is not None
            else KeywordExtractor()
        )

    def filter(self, resume, job_description):
        if not job_description.strip():
            return resume

        filtered = deepcopy(resume)

        filtered.experience = self.sort_by_relevance(
            filtered.experience,
            job_description,
        )

        keywords = {
            keyword.lower()
            for keyword in self.extractor.extract(job_description)
        }

        filtered.skills = [
            skill
            for skill in filtered.skills
            if self.has_matching_tags(skill, keywords)
        ]

        return filtered

    def sort_by_relevance(self, items, job_description):
        scored = [
            (
                self.matcher.score(item, job_description),
                item,
            )
            for item in items
        ]

        scored.sort(
            reverse=True,
            key=lambda item: item[0],
        )

        return [
            item
            for _, item in scored
        ]

    def has_matching_tags(self, item, keywords):
        return any(
            tag.lower() in keywords
            for tag in getattr(item, "tags", [])
        )
    