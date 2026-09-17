from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.experience_selector import (
    ExperienceSelector,
)
from resumeforge.tailoring.prioritizer import TailoringPrioritizer
from resumeforge.tailoring.project_selector import ProjectSelector
from resumeforge.tailoring.skill_selector import (
    SkillSelector,
)
from resumeforge.tailoring.certification_selector import (
    CertificationSelector,
)
from resumeforge.tailoring.summary_selector import SummarySelector


class TailoringEngine:

    def __init__(
        self,
        skill_selector=None,
        experience_selector=None,
        project_selector=None,
        certification_selector=None,
        summary_selector=None,
        prioritizer=None,
    ):
        self.skill_selector = (
            skill_selector or SkillSelector()
        )
        self.experience_selector = (
            experience_selector or ExperienceSelector()
        )
        self.project_selector = (
            project_selector or ProjectSelector()
        )
        self.certification_selector = (
            certification_selector or CertificationSelector()
        )
        self.summary_selector = (
            summary_selector or SummarySelector()
        )
        self.prioritizer = (
            prioritizer
            or TailoringPrioritizer()
        )

    def create_plan(
        self,
        resume,
        match_result,
    ):
        plan = TailoringPlan(
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
            recommendations=getattr(
                match_result,
                "recommendations",
                [],
            ),
        )
        return self.prioritizer.prioritize(
            plan,
            match_result,
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