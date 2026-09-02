class SummarySelector:

    def select(
        self,
        profile,
        match,
    ):
        if profile is None:
            return []

        if match is None:
            return getattr(profile, "summary_keywords", [])

        matched = {
            item.lower()
            for item in match.matched
        }

        selected = []

        for keyword in profile.summary_keywords:
            if keyword.lower() in matched:
                selected.append(keyword)

        return selected