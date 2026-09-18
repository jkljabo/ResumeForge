from types import SimpleNamespace

from resumeforge.tailoring.plan import TailoringPlan
from resumeforge.tailoring.prioritizer import TailoringPrioritizer


def test_records_skill_promotion_rationale():

    plan = TailoringPlan(
        skills=[
            "Azure",
            "SQL Server",
        ]
    )

    match = SimpleNamespace(
        promoted_skills=[
            "Azure",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert len(result.rationale) == 1

    assert result.rationale[0] == (
        "Promoted skill: Azure"
    )

def test_records_multiple_skill_rationale():

    plan = TailoringPlan(
        skills=[
            "Azure",
            "C#",
            "SQL Server",
        ]
    )

    match = SimpleNamespace(
        promoted_skills=[
            "Azure",
            "C#",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.rationale == [
        "Promoted skill: Azure",
        "Promoted skill: C#",
    ]

def test_records_no_rationale_when_nothing_promoted():

    plan = TailoringPlan(
        skills=[
            "Azure",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        None,
    )

    assert result.rationale == []

def test_records_project_rationale():

    plan = TailoringPlan(
        projects=[
            "ResumeForge",
            "Legacy POS",
        ]
    )

    match = SimpleNamespace(
        promoted_projects=[
            "ResumeForge",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.rationale == [
        "Promoted project: ResumeForge",
    ]

def test_records_certification_rationale():

    plan = TailoringPlan(
        certifications=[
            "AZ-204",
            "AWS CCP",
        ]
    )

    match = SimpleNamespace(
        promoted_certifications=[
            "AZ-204",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.rationale == [
        "Promoted certification: AZ-204",
    ]

def test_records_education_rationale():

    plan = TailoringPlan(
        education=[
            "B.S. Computer Science",
            "Azure Learning Path",
        ]
    )

    match = SimpleNamespace(
        promoted_education=[
            "Azure Learning Path",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.rationale == [
        "Promoted education: Azure Learning Path",
    ]

def test_records_experience_rationale():

    plan = TailoringPlan(
        experience=[
            "Legacy VB",
            "Azure Migration",
        ]
    )

    match = SimpleNamespace(
        promoted_experience=[
            "Azure Migration",
        ]
    )

    result = TailoringPrioritizer().prioritize(
        plan,
        match,
    )

    assert result.rationale == [
        "Promoted experience: Azure Migration",
    ]

