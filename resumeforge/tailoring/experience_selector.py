class ExperienceSelector:

    def select(
        self,
        profile,
        match_result,
    ):
        if match_result is None:
            return list(profile.experience)

        matched = {
            keyword.lower()
            for keyword in match_result.matched
        }

        scored = []

        for experience in profile.experience:

            overlap = matched.intersection(
                {
                    keyword.lower()
                    for keyword in experience.keywords
                }
            )

            if overlap:
                scored.append(
                    (
                        len(overlap),
                        experience,
                    )
                )

        scored.sort(
            reverse=True,
            key=lambda item: item[0],
        )

        return [
            item[1]
            for item in scored[:5]
        ]