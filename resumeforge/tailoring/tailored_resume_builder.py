from resumeforge.resume.document import ResumeDocument


class TailoredResumeBuilder:

    def build(self, profile, plan):
        document = ResumeDocument()

        if profile is not None:
            document.name = getattr(profile, "name", "")
            document.title = getattr(profile, "title", "")
            document.email = getattr(profile, "email", "")
            document.phone = getattr(profile, "phone", "")
            document.location = getattr(profile, "location", "")
            document.linkedin = getattr(profile, "linkedin", "")
            document.github = getattr(profile, "github", "")

        document.summary = " ".join(getattr(plan, "summary_keywords", []))
        document.skills = plan.skills
        document.experience = plan.experience
        document.projects = plan.projects
        document.certifications = plan.certifications

        return document