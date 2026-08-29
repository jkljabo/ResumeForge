from resumeforge.scoring.synonyms import SynonymTable
from resumeforge.scoring import (
    Matcher,
    WeightTable,
    SectionWeights,
)
from types import SimpleNamespace


def test_matcher_can_be_created():
    matcher = Matcher()

    assert matcher is not None


def test_score_returns_integer():
    matcher = Matcher()

    score = matcher.score(None, "")

    assert isinstance(score, int)

def test_score_returns_zero_for_empty_job_description():
    matcher = Matcher()
    resume = SimpleNamespace(skills=[], experience=[], projects=[], certifications=[])

    assert matcher.score(resume, "") == 0


def test_score_counts_matching_skill_tags():
    matcher = Matcher()
    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(tags=["azure", ".net"]),
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    score = matcher.score(
        resume,
        "Looking for Azure and .NET experience"
    )

    assert score == 4

def test_weighted_keywords_increase_score():
    weights = WeightTable()
    weights.add("azure", 10)

    matcher = Matcher(weights)

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(tags=["azure"])
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    assert matcher.score(resume, "Azure Engineer") == 20

def test_matcher_accepts_weight_table():
    table = WeightTable()

    matcher = Matcher(table)

    assert matcher.weights is table

def test_matcher_accepts_keyword_weights():
    weights = WeightTable()

    matcher = Matcher(weights=weights)

    assert matcher.weights is weights


def test_matcher_accepts_section_weights():
    section_weights = SectionWeights()

    matcher = Matcher(
        section_weights=section_weights,
    )

    assert matcher.section_weights is section_weights

def test_experience_scores_higher_than_skills():
    weights = WeightTable()
    weights.add("azure", 10)

    sections = SectionWeights()
    sections.add("skills", 1)
    sections.add("experience", 3)

    matcher = Matcher(
        weights=weights,
        section_weights=sections,
    )

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(tags=["azure"])
        ],
        experience=[
            SimpleNamespace(tags=["azure"])
        ],
        projects=[],
        certifications=[],
    )

    assert matcher.score(resume, "Azure") == 40

def test_custom_section_weights():
    weights = WeightTable()
    weights.add("blazor", 5)

    sections = SectionWeights()
    sections.add("projects", 5)

    matcher = Matcher(
        weights=weights,
        section_weights=sections,
    )

    resume = SimpleNamespace(
        skills=[],
        experience=[],
        projects=[
            SimpleNamespace(tags=["blazor"])
        ],
        certifications=[],
    )

    assert matcher.score(resume, "Blazor") == 25

def test_matcher_accepts_synonym_table():
    table = SynonymTable()

    matcher = Matcher(synonyms=table)

    assert matcher.synonyms is table

def test_synonyms_affect_matching():
    matcher = Matcher()

    resume = SimpleNamespace(
        skills=[
            SimpleNamespace(tags=["azure functions"])
        ],
        experience=[],
        projects=[],
        certifications=[],
    )

    score = matcher.score(
        resume,
        "Looking for Function Apps"
    )

    assert score > 0