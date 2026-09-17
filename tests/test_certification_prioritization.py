from types import SimpleNamespace

from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.prioritizer import TailoringPrioritizer


def test_prioritize_promotes_certifications():

    plan = TailoringPlan(
        certifications=[
            "AZ-900",
            "AWS CCP",
            "Security+",
        ]
    )

    match = SimpleNamespace(
        promoted_certifications=[
            "AWS CCP",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.certifications == [
        "AWS CCP",
        "AZ-900",
        "Security+",
    ]

    assert result.promoted_certifications == [
        "AWS CCP",
    ]

def test_prioritize_leaves_certifications_unchanged_without_promotions():

    certifications = [
        "AZ-900",
        "AWS CCP",
        "Security+",
    ]

    plan = TailoringPlan(
        certifications=certifications.copy(),
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match_result=None,
    )

    assert result.certifications == certifications
    assert result.promoted_certifications == []

def test_prioritize_promotes_multiple_certifications():

    plan = TailoringPlan(
        certifications=[
            "AZ-900",
            "AWS CCP",
            "Security+",
            "AZ-204",
        ]
    )

    match = SimpleNamespace(
        promoted_certifications=[
            "AZ-204",
            "AWS CCP",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.certifications == [
        "AWS CCP",
        "AZ-204",
        "AZ-900",
        "Security+",
    ]

    assert result.promoted_certifications == [
        "AWS CCP",
        "AZ-204",
    ]

def test_prioritize_ignores_unknown_certifications():

    original = [
        "AZ-900",
        "AWS CCP",
    ]

    plan = TailoringPlan(
        certifications=original.copy(),
    )

    match = SimpleNamespace(
        promoted_certifications=[
            "CISSP",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.certifications == original
    assert result.promoted_certifications == []

def test_prioritize_handles_empty_certification_list():

    plan = TailoringPlan(
        certifications=[],
    )

    match = SimpleNamespace(
        promoted_certifications=[
            "AWS CCP",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.certifications == []
    assert result.promoted_certifications == []