from types import SimpleNamespace

from resumeforge.tailoring.experience_selector import (
    ExperienceSelector,
)


def test_returns_empty_when_no_experience():

    profile = SimpleNamespace(
        experience=[]
    )

    selector = ExperienceSelector()

    experience = selector.select(
        profile,
        None,
    )

    assert experience == []

def test_returns_profile_experience():

    profile = SimpleNamespace(
        experience=[
            "Senior Engineer",
            "Software Engineer",
        ]
    )

    selector = ExperienceSelector()

    experience = selector.select(
        profile,
        None,
    )

    assert experience == [
        "Senior Engineer",
        "Software Engineer",
    ]

def test_returns_matching_experience():

    profile = SimpleNamespace(
        experience=[
            SimpleNamespace(
                title="Senior Engineer",
                keywords=[
                    "azure",
                    "docker",
                ],
            ),
            SimpleNamespace(
                title="Database Developer",
                keywords=[
                    "oracle",
                ],
            ),
        ]
    )

    match = SimpleNamespace(
        matched=[
            "docker",
        ]
    )

    selector = ExperienceSelector()

    experience = selector.select(
        profile,
        match,
    )

    assert len(experience) == 1
    assert experience[0].title == "Senior Engineer"

def test_best_match_comes_first():

    profile = SimpleNamespace(
        experience=[
            SimpleNamespace(
                title="Developer",
                keywords=[
                    "sql",
                ],
            ),
            SimpleNamespace(
                title="Cloud Engineer",
                keywords=[
                    "azure",
                    "docker",
                    "kubernetes",
                ],
            ),
        ]
    )

    match = SimpleNamespace(
        matched=[
            "azure",
            "docker",
        ]
    )

    selector = ExperienceSelector()

    experience = selector.select(
        profile,
        match,
    )

    assert experience[0].title == "Cloud Engineer"

def test_limits_number_of_experience_entries():

    profile = SimpleNamespace(
        experience=[
            SimpleNamespace(
                title=f"Job {i}",
                keywords=["azure"],
            )
            for i in range(10)
        ]
    )

    match = SimpleNamespace(
        matched=[
            "azure",
        ]
    )

    selector = ExperienceSelector()

    experience = selector.select(
        profile,
        match,
    )

    assert len(experience) == 5

