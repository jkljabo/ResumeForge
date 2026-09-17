class TailoringPlan:

    def __init__(
        self,
        skills=None,
        experience=None,
        projects=None,
        certifications=None,
        education=None,
        summary_keywords=None,
        excluded=None,
        recommendations=None,
        promoted=None,
        demoted=None,
        rationale=None,
    ):
        self.skills = skills or []
        self.experience = experience or []
        self.projects = projects or []
        self.certifications = certifications or []
        self.education = education or []
        self.summary_keywords = summary_keywords or []
        self.excluded = excluded or []
        self.recommendations = recommendations or []
        self.promoted = promoted or []
        self.demoted = demoted or []
        self.rationale = rationale or []