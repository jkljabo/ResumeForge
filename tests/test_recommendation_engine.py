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

def test_recommendations_are_sorted_by_impact():

    result = MatchResult(
        missing=[
            "docker",
            "azure",
        ]
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].impact == max(
        engine.weights.get("docker"),
        engine.weights.get("azure"),
    )

    assert recommendations[1].impact == min(
        engine.weights.get("docker"),
        engine.weights.get("azure"),
    )

def test_recommendations_preserve_input_order_when_impact_is_equal():

    result = MatchResult(
        missing=[
            "docker",
            "imaginarykeyword",
        ]
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].keyword == "docker"
    assert recommendations[1].keyword == "imaginarykeyword"

def test_recommendations_use_keyword_scores_from_match_result():

    result = MatchResult(
        missing=[
            "azure",
            "docker",
        ],
        keyword_scores={
            "azure": SimpleNamespace(
                keyword="azure",
                matched=False,
                score=10,
            ),
            "docker": SimpleNamespace(
                keyword="docker",
                matched=False,
                score=3,
            ),
        },
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].keyword == "azure"
    assert recommendations[0].impact == 10

    assert recommendations[1].keyword == "docker"
    assert recommendations[1].impact == 3

def test_recommendations_match_keyword_scores_case_insensitively():

    result = MatchResult(
        missing=[
            "Azure",
        ],
        keyword_scores={
            "azure": SimpleNamespace(
                keyword="azure",
                matched=False,
                score=10,
            ),
        },
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].keyword == "Azure"
    assert recommendations[0].impact == 10

def test_recommendation_uses_weight_when_keyword_score_is_missing():

    result = MatchResult(
        missing=[
            "azure",
        ],
        keyword_scores={},
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].impact == (
        engine.weights.get("azure")
    )

def test_get_keyword_score_returns_matching_score():

    result = MatchResult(
        keyword_scores={
            "azure": SimpleNamespace(
                keyword="azure",
                matched=False,
                score=10,
            ),
        },
    )

    engine = RecommendationEngine()

    keyword_score = engine._get_keyword_score(
        result,
        "Azure",
    )

    assert keyword_score.score == 10

def test_recommendations_fall_back_for_missing_keyword_score():

    result = MatchResult(
        missing=[
            "azure",
            "docker",
        ],
        keyword_scores={
            "azure": SimpleNamespace(
                keyword="azure",
                matched=False,
                score=10,
            ),
        },
    )

    engine = RecommendationEngine()

    recommendations = engine.recommend(result)

    assert recommendations[0].keyword == "azure"
    assert recommendations[0].impact == 10

    assert recommendations[1].keyword == "docker"
    assert recommendations[1].impact == (
        engine.weights.get("docker")
    )



