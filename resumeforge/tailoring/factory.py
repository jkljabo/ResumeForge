from resumeforge.tailoring.skill_selector import SkillSelector
from resumeforge.tailoring.experience_selector import ExperienceSelector
from resumeforge.tailoring.project_selector import ProjectSelector
from resumeforge.tailoring.certification_selector import CertificationSelector
from resumeforge.tailoring.summary_selector import SummarySelector

from resumeforge.tailoring.engine import TailoringEngine


def create_tailoring_engine():

    return TailoringEngine(**create_selectors())

def create_selectors():
    return {
        "skill_selector": SkillSelector(),
        "experience_selector": ExperienceSelector(),
        "project_selector": ProjectSelector(),
        "certification_selector": CertificationSelector(),
        "summary_selector": SummarySelector(),
    }