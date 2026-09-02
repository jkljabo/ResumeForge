from types import SimpleNamespace

from resumeforge.tailoring.skill_selector import SkillSelector


def test_returns_list():

    profile = SimpleNamespace(
        skills=[]
    )

    selector = SkillSelector()

    skills = selector.select(
        profile,
        None,
    )

    assert skills == []

def test_returns_profile_skills():

    profile = SimpleNamespace(
        skills=[
            "Python",
            "Azure",
            "Docker",
        ]
    )

    selector = SkillSelector()

    skills = selector.select(
        profile,
        None,
    )

    assert skills == [
        "Python",
        "Azure",
        "Docker",
    ]

def test_returns_only_matching_skills():

    profile = SimpleNamespace(
        skills=[
            "Python",
            "Azure",
            "Docker",
        ]
    )

    match = SimpleNamespace(
        matched=[
            "azure",
            "docker",
        ]
    )

    selector = SkillSelector()

    skills = selector.select(
        profile,
        match,
    )

    assert skills == [
        "Azure",
        "Docker",
    ]

def test_matching_is_case_insensitive():

    profile = SimpleNamespace(
        skills=[
            "Azure",
        ]
    )

    match = SimpleNamespace(
        matched=[
            "AZURE",
        ]
    )

    selector = SkillSelector()

    skills = selector.select(
        profile,
        match,
    )

    assert skills == ["Azure"]

