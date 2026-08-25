from resumeforge.domain import SkillGroup


def test_skill_group_model():
    group = SkillGroup(
        category="Cloud",
        skills=["Azure", "AWS", "Docker"]
    )

    assert group.category == "Cloud"
    assert "AWS" in group.skills