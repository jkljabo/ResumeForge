from resumeforge.recommendations.recommendation import Recommendation
from resumeforge.scoring.weights import WeightTable


class RecommendationEngine:

    SECTION_MAP = {
        # Skills
        "azure": "skills",
        "aws": "skills",
        "docker": "skills",
        "kubernetes": "skills",
        "blazor": "skills",
        "c#": "skills",
        ".net": "skills",
        "sql": "skills",

        # Experience
        "microservices": "experience",
        "leadership": "experience",
        "mentoring": "experience",
        "architecture": "experience",

        # Projects
        "terraform": "projects",
        "github": "projects",

        # Certifications
        "aws certified": "certifications",
        "azure fundamentals": "certifications",
    }

    REASON_MAP = {
        "azure":
            "Core cloud platform skill.",

        "aws":
            "Widely requested cloud platform skill.",

        "docker":
            "Common DevOps technology for containerized applications.",

        "kubernetes":
            "Industry-standard container orchestration platform.",

        "terraform":
            "Infrastructure-as-Code technology used for cloud provisioning.",

        "microservices":
            "Frequently requested enterprise architecture pattern.",

        "blazor":
            "Modern .NET web UI framework.",
    }
    
    def __init__(self, weights=None):
        self.weights = weights or WeightTable()

    def recommend(self, result):
        recommendations = []

        for keyword in result.missing:
            keyword_score = self._get_keyword_score(
                result,
                keyword,
            )

            impact = (
                keyword_score.score
                if keyword_score is not None
                else self.weights.get(keyword)
            )

            recommendations.append(
                Recommendation(
                    keyword=keyword,
                    section=self._recommend_section(keyword),
                    impact=impact,
                    reason=self._recommend_reason(keyword),
                )
            )

        recommendations.sort(
            key=lambda recommendation: recommendation.impact,
            reverse=True,
        )

        return recommendations

    def _get_keyword_score(self, result, keyword):
        keyword_scores = getattr(
            result,
            "keyword_scores",
            {},
        )

        return keyword_scores.get(
            keyword.lower()
        )

    def _recommend_section(self, keyword):
        return self.SECTION_MAP.get(
            keyword.lower(),
            "skills",
        )

    def _recommend_reason(self, keyword):
        return self.REASON_MAP.get(
            keyword.lower(),
            "Missing keyword from job description.",
        )