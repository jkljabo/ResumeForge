from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.experience_selector import (
    ExperienceSelector,
)
from resumeforge.tailoring.project_selector import ProjectSelector
from resumeforge.tailoring.skill_selector import (
    SkillSelector,
)
from resumeforge.tailoring.certification_selector import (
    CertificationSelector,
)
from resumeforge.tailoring.summary_selector import SummarySelector


class TailoringEngine:

    def __init__(self):
        self.skill_selector = SkillSelector()
        self.experience_selector = ExperienceSelector()
        self.project_selector = ProjectSelector()
        self.certification_selector = CertificationSelector()
        self.summary_selector = SummarySelector()

    def build_plan(
        self,
        resume,
        match_result,
    ):
        return TailoringPlan(
            skills=self.skill_selector.select(
                resume,
                match_result,
            ),
            experience=self.experience_selector.select(
                resume,
                match_result,
            ),
            projects=self.project_selector.select(
                resume,
                match_result,
            ),
            certifications=self.certification_selector.select(
                resume,
                match_result,
            ),
            summary_keywords=self.summary_selector.select(
                resume,
                match_result,
            ),
        )

    def select_skills(
        self,
        resume,
        match_result,
    ):
        return self.skill_selector.select(
            resume,
            match_result,
        )

    def select_experience(
        self,
        resume,
        match_result,
    ):
        return self.experience_selector.select(
            resume,
            match_result,
        )