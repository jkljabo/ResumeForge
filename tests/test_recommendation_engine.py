from types import SimpleNamespace

from resumeforge import recommendations
from resumeforge.recommendations.engine import RecommendationEngine
from resumeforge.scoring.match_result import MatchResult
from resumeforge.scoring.weights import WeightTable


def test_engine_creates_recommendations():
    result = MatchResult(
        missing=[
            "imaginarykeyword",
        ]
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert len(recommendations) == 1

    # assert recommendations[0].keyword == "docker"
    # assert recommendations[1].keyword == "terraform"

    assert recommendations[0].keyword == "imaginarykeyword"
    assert recommendations[0].impact == 1

    assert (
        recommendations[0].reason
        == "Missing keyword from job description."
    )

def test_recommendations_use_keyword_weights():
    result = SimpleNamespace(
        missing=[
            "azure",
            "docker",
        ]
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].keyword == "azure"
    assert recommendations[0].impact > 0

    assert recommendations[1].keyword == "docker"
    assert recommendations[1].impact > 0

def test_engine_recommends_best_section():
    result = MatchResult(
        missing=[
            "docker",
            "terraform",
            "microservices",
        ]
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].section == "skills"
    assert recommendations[1].section == "projects"
    assert recommendations[2].section == "experience"

def test_engine_provides_recommendation_reason():
    result = MatchResult(
        missing=["docker"]
    )

    engine = RecommendationEngine()

    recommendation = engine.recommend(result)[0]

    assert recommendation.reason != ""
    assert recommendation.reason != (
        "Missing keyword from job description."
    )

def test_known_keywords_use_descriptive_reasons():

    result = MatchResult(
        missing=[
            "docker",
            "terraform",
        ]
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].reason.startswith(
        "Common DevOps"
    )

    assert recommendations[1].reason.startswith(
        "Infrastructure-as-Code"
    )