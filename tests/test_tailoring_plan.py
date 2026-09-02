from resumeforge.tailoring.plan import TailoringPlan


def test_plan_defaults_are_empty():
    plan = TailoringPlan()

    assert plan.skills == []
    assert plan.experience == []
    assert plan.projects == []
    assert plan.certifications == []
    assert plan.summary_keywords == []
    assert plan.excluded == []


def test_plan_stores_values():
    plan = TailoringPlan(
        skills=["Azure"],
        experience=["Microsoft"],
        projects=["ResumeForge"],
        certifications=["AZ-204"],
        summary_keywords=["Cloud"],
        excluded=["React"],
    )

    assert plan.skills == ["Azure"]
    assert plan.experience == ["Microsoft"]
    assert plan.projects == ["ResumeForge"]
    assert plan.certifications == ["AZ-204"]
    assert plan.summary_keywords == ["Cloud"]
    assert plan.excluded == ["React"]