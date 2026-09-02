from types import SimpleNamespace

from resumeforge.tailoring.certification_selector import (
    CertificationSelector,
)


def test_returns_profile_certifications():

    profile = SimpleNamespace(
        certifications=[
            "Microsoft Azure Developer Associate",
            "AWS Cloud Practitioner",
        ]
    )

    selector = CertificationSelector()

    certifications = selector.select(
        profile,
        None,
    )

    assert certifications == [
        "Microsoft Azure Developer Associate",
        "AWS Cloud Practitioner",
    ]

def test_returns_only_matching_certifications():

    profile = SimpleNamespace(
        certifications=[
            "AWS Certified Developer",
            "Azure Fundamentals",
            "Scrum Master",
        ]
    )

    match = SimpleNamespace(
        matched=[
            "azure",
        ]
    )

    selector = CertificationSelector()

    certifications = selector.select(
        profile,
        match,
    )

    assert certifications == [
        "Azure Fundamentals",
    ]

def test_matching_is_case_insensitive():

    profile = SimpleNamespace(
        certifications=[
            "Azure Fundamentals",
        ]
    )

    match = SimpleNamespace(
        matched=[
            "AZURE",
        ]
    )

    selector = CertificationSelector()

    certifications = selector.select(
        profile,
        match,
    )

    assert certifications == [
        "Azure Fundamentals",
    ]

def test_empty_profile_returns_empty_list():

    profile = SimpleNamespace(
        certifications=[]
    )

    selector = CertificationSelector()

    certifications = selector.select(
        profile,
        None,
    )

    assert certifications == []

