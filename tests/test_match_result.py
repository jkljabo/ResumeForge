from types import SimpleNamespace
import pytest

from resumeforge.scoring import MatchResult
from resumeforge.scoring.matcher import Matcher
from resumeforge.scoring.weights import WeightTable


def test_match_result_defaults():
    result = MatchResult()

    assert result.score == 0
    assert result.matched == []
    assert result.missing == []
    assert result.section_scores == {}
    assert result.coverage == 0.0

def test_match_returns_match_result():
    matcher = Matcher()

    result = matcher.match(None, "")

    assert isinstance(result, MatchResult)

def test_match_collects_matches():
    matcher = Matcher()

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(
                tags=["azure", "blazor"]
            )
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    result = matcher.match(
        resume,
        "Azure Developer"
    )

    assert "azure" in result.matched
    assert "blazor" not in result.matched

def test_match_collects_missing_keywords():
    matcher = Matcher()

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(
                tags=["azure"]
            )
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    result = matcher.match(
        resume,
        "Azure Kubernetes Docker"
    )

    assert "azure" in result.matched
    assert "kubernetes" in result.missing
    assert "docker" in result.missing

def test_match_reports_section_scores():
    matcher = Matcher()

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(tags=["azure"])
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    result = matcher.match(
        resume,
        "Azure"
    )

    assert result.section_scores == {
        "skills": 2,
        "experience": 0,
        "projects": 0,
        "certifications": 0,
    }

def test_match_calculates_coverage():
    matcher = Matcher()

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(
                tags=["azure", "blazor"]
            )
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    result = matcher.match(
        resume,
        "Azure Blazor Kubernetes Docker"
    )

    assert result.coverage == 50.0

def test_match_coverage_is_zero_when_no_job_description():
    matcher = Matcher()

    result = matcher.match(None, "")

    assert result.coverage == 0.0

def test_missing_keywords_are_ranked():
    weights = WeightTable()

    weights.add("kubernetes", 8)
    weights.add("docker", 6)
    weights.add("terraform", 4)

    matcher = Matcher(weights=weights)

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(tags=["azure"])
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    result = matcher.match(
        resume,
        "Azure Docker Terraform Kubernetes"
    )

    assert result.missing == [
        "kubernetes",
        "docker",
        "terraform",
    ]

def test_match_result_defaults_matched_by_section():
    result = MatchResult()

    assert result.matched_by_section == {}

def test_match_reports_matches_by_section():
    matcher = Matcher()

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(tags=["azure", "blazor"])
        ],
        experience=[
            SimpleNamespace(tags=["microservices"])
        ],
        projects=[],
        certifications=[],
    )

    result = matcher.match(
        resume,
        "Azure Microservices Docker"
    )

    assert result.matched_by_section == {
        "skills": ["azure"],
        "experience": ["microservices"],
        "projects": [],
        "certifications": [],
    }

def test_match_result_missing_by_section_defaults():
    result = MatchResult()

    assert result.missing_by_section == {}

def test_match_result_defaults_new_fields():
    result = MatchResult()

    assert result.recommendations == []
    assert result.keyword_scores == {}
    assert result.total_keywords == 0

def test_match_result_statistics():
    result = MatchResult(
        matched=["azure", ".net"],
        missing=["terraform"],
    )

    assert result.matched_count == 2
    assert result.missing_count == 1
    assert result.total_matches == 3
    assert result.percent_matched == pytest.approx(66.67, rel=1e-2)