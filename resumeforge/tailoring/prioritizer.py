from typing import Sequence

RATIONALE_REASONS = {
    "skill": "matched requested skills",
    "project": "matched requested projects",
    "certification": "matched requested certifications",
    "education": "matched requested education",
    "experience": "matched relevant experience",
}

class TailoringPrioritizer:

    def prioritize(
        self,
        plan,
        match_result,
    ):

        # Existing recommendation prioritization
        if hasattr(plan, "recommendations"):
            plan.recommendations.sort(
                key=lambda r: r.impact,
                reverse=True,
            )

        # Promote matched experience
        if hasattr(plan, "experience"):

            (
                plan.experience,
                plan.promoted,
            ) = self._promote_items(
                plan.experience,
                self._get_promoted(
                    match_result,
                    "promoted_experience",
                ),
            )
            self._record_rationale(
                plan,
                "experience",
                plan.promoted,
                RATIONALE_REASONS["experience"],
            )

        # Promote matched skills
        if hasattr(plan, "skills"):

            (
                plan.skills,
                plan.promoted_skills,
            ) = self._promote_items(
                plan.skills,
                self._get_promoted(
                    match_result,
                    "promoted_skills",
                ),
            )
            self._record_rationale(
                plan,
                "skill",
                plan.promoted_skills,
                RATIONALE_REASONS["skill"],
            )
            
        # Promote matched projects
        if hasattr(plan, "projects"):

            (
                plan.projects,
                plan.promoted_projects,
            ) = self._promote_items(
                plan.projects,
                self._get_promoted(
                    match_result,
                    "promoted_projects",
                ),
            )
            self._record_rationale(
                plan,
                "project",
                plan.promoted_projects,
                RATIONALE_REASONS["project"],
            )

        # Promote matched certifications
        if hasattr(plan, "certifications"):

            (
                plan.certifications,
                plan.promoted_certifications,
            ) = self._promote_items(
                plan.certifications,
                self._get_promoted(
                    match_result,
                    "promoted_certifications",
                ),
            )
            self._record_rationale(
                plan,
                "certification",
                plan.promoted_certifications,
                RATIONALE_REASONS["certification"],
            )

        # Promote matched education
        if hasattr(plan, "education"):

            (
                plan.education,
                plan.promoted_education,
            ) = self._promote_items(
                plan.education,
                self._get_promoted(
                    match_result,
                    "promoted_education",
                ),
            )
            self._record_rationale(
                plan,
                "education",
                plan.promoted_education,
                RATIONALE_REASONS["education"],
            )

        return plan

    def _promote_items(
        self,
        items: Sequence[str],
        promoted: Sequence[str],
    ) -> tuple[list[str], list[str]]:
        if not items:
            return [], []

        if not promoted:
            return items.copy(), []

        promoted_set = set(promoted)

        promoted_items = [
            item
            for item in items
            if item in promoted_set
        ]

        remaining_items = [
            item
            for item in items
            if item not in promoted_set
        ]

        return (
            promoted_items + remaining_items,
            promoted_items,
        )

    def _get_promoted(
        self,
        match_result,
        attribute: str,
    ) -> list[str]:

        if match_result is None:
            return []

        return getattr(
            match_result,
            attribute,
            [],
        )

    def _record_rationale(
        self,
        plan,
        section: str,
        items: list[str],
        reason: str | None = None,
    ):
        for item in items:
            plan.rationale.append(
                self._build_rationale(
                    section,
                    item,
                    reason,
                )
            )

    def _build_rationale(
        self,
        section: str,
        item: str,
        reason: str | None = None,
    ) -> str:
        message = f"Promoted {section}: {item}"

        if reason:
            message += f" ({reason})"

        return message