class ProjectSelector:

    def select(
        self,
        profile,
        match_result,
    ):
        if not getattr(profile, "projects", None):
            return []

        if match_result is None:
            return profile.projects

        matched = {
            keyword.lower()
            for keyword in match_result.matched
        }

        selected = []

        for project in profile.projects:
            project_lower = project.lower()

            if any(
                keyword in project_lower
                for keyword in matched
            ):
                selected.append(project)

        return selected