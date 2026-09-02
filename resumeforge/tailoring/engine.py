from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.experience_selector import (
    ExperienceSelector,
)
from resumeforge.tailoring.skill_selector import (
    SkillSelector,
)
from resumeforge.tailoring.certification_selector import (
    CertificationSelector,
)


class TailoringEngine:

    def __init__(self):
        self.skill_selector = SkillSelector()
        self.experience_selector = ExperienceSelector()
        self.certification_selector = CertificationSelector()

    def build_plan(
        self,
        resume,
        match_result,
    ):
        return TailoringPlan(
            skills=self.select_skills(
                resume,
                match_result,
            ),
            experience=self.select_experience(
                resume,
                match_result,
            ),
            certifications=self.certification_selector.select(
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