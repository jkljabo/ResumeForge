
from resumeforge.tailoring.engine import TailoringEngine
from resumeforge.tailoring.experience_selector import ExperienceSelector
from resumeforge.tailoring.factory import (
    create_selectors,
    create_tailoring_engine,
)
from resumeforge.tailoring.skill_selector import SkillSelector


def test_create_tailoring_engine():

    engine = create_tailoring_engine()

    assert isinstance(
        engine,
        TailoringEngine,
    )

def test_factory_wires_dependencies():

    engine = create_tailoring_engine()

    assert engine.skill_selector is not None
    assert engine.experience_selector is not None
    assert engine.project_selector is not None
    assert engine.certification_selector is not None
    assert engine.summary_selector is not None

def test_create_selectors_returns_all_dependencies():
    selectors = create_selectors()

    assert isinstance(
        selectors["skill_selector"],
        SkillSelector,
    )

    assert isinstance(
        selectors["experience_selector"],
        ExperienceSelector,
    )

