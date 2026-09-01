from resumeforge.optimizer.optimization_result import (
    OptimizationResult,
)
from resumeforge.optimizer.optimizer import ResumeOptimizer
from resumeforge.recommendations.recommendation import Recommendation


def test_optimizer_exists():
    optimizer = ResumeOptimizer()

    assert optimizer is not None

def test_optimizer_returns_resume():

    optimizer = ResumeOptimizer()

    resume = object()

    optimized = optimizer.optimize(
        resume,
        [],
    )

    assert optimized.resume is resume

def test_optimizer_returns_optimization_result():

    optimizer = ResumeOptimizer()

    resume = object()

    result = optimizer.optimize(
        resume,
        [],
    )

    assert isinstance(
        result,
        OptimizationResult,
    )

    assert result.resume is resume
    assert result.applied == []
    assert result.skipped == []

def test_optimizer_tracks_applied_recommendations():

    optimizer = ResumeOptimizer()

    resume = object()

    recommendations = [
        Recommendation(
            keyword="docker",
            section="skills",
            impact=5,
            reason="Test recommendation",
        ),
    ]

    result = optimizer.optimize(
        resume,
        recommendations,
    )

    assert len(result.applied) == 1
    assert len(result.skipped) == 0

    assert result.applied[0] is recommendations[0]

def test_optimizer_skips_unapplicable_recommendations():

    class TestOptimizer(ResumeOptimizer):

        def _can_apply(self, recommendation):
            return recommendation.keyword != "terraform"

    optimizer = TestOptimizer()

    recommendations = [
        Recommendation(
            keyword="docker",
            section="skills",
            impact=5,
            reason="",
        ),
        Recommendation(
            keyword="terraform",
            section="projects",
            impact=4,
            reason="",
        ),
    ]

    result = optimizer.optimize(
        object(),
        recommendations,
    )

    assert len(result.applied) == 1
    assert len(result.skipped) == 1

    assert result.applied[0].keyword == "docker"
    assert result.skipped[0].keyword == "terraform"