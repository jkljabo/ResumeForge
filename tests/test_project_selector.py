from types import SimpleNamespace

from resumeforge.tailoring.project_selector import ProjectSelector


def test_returns_profile_projects():

    profile = SimpleNamespace(
        projects=[
            "ResumeForge",
            "Blazor Expo",
            "MovieTime",
        ]
    )

    selector = ProjectSelector()

    projects = selector.select(
        profile,
        None,
    )

    assert projects == [
        "ResumeForge",
        "Blazor Expo",
        "MovieTime",
    ]

def test_returns_only_matching_projects():

    profile = SimpleNamespace(
        projects=[
            "ResumeForge",
            "Azure Migration",
            "Blazor Expo",
        ]
    )

    match = SimpleNamespace(
        matched=[
            "azure",
            "blazor",
        ]
    )

    selector = ProjectSelector()

    projects = selector.select(
        profile,
        match,
    )

    assert projects == [
        "Azure Migration",
        "Blazor Expo",
    ]

