class TailoringPlan:

    def __init__(
        self,
        skills=None,
        experience=None,
        projects=None,
        certifications=None,
        summary_keywords=None,
        excluded=None,
    ):
        self.skills = skills or []
        self.experience = experience or []
        self.projects = projects or []
        self.certifications = certifications or []
        self.summary_keywords = summary_keywords or []
        self.excluded = excluded or []