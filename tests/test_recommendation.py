from resumeforge.recommendations.recommendation import Recommendation


def test_recommendation_properties():
    recommendation = Recommendation(
        keyword="docker",
        section="experience",
        impact=10,
        reason="Missing keyword from job description.",
    )

    assert recommendation.keyword == "docker"
    assert recommendation.section == "experience"
    assert recommendation.impact == 10
    assert (
        recommendation.reason
        == "Missing keyword from job description."
    )