class ResumeDocument:

    def __init__(
        self,
        summary="",
        skills=None,
        experience=None,
        education=None,
        certifications=None,
        projects=None,
    ):
        self.summary = summary
        self.skills = skills or []
        self.experience = experience or []
        self.education = education or []
        self.certifications = certifications or []
        self.projects = projects or []