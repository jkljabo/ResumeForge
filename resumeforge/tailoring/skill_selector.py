class SkillSelector:

    def select(
        self,
        profile,
        match_result,
    ):
        # If no match information exists yet,
        # return all profile skills.
        if match_result is None:
            return list(profile.skills)

        matched = {
            keyword.lower()
            for keyword in match_result.matched
        }

        return [
            skill
            for skill in profile.skills
            if skill.lower() in matched
        ]   