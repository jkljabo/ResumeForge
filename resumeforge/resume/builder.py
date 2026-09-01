from resumeforge.resume.document import ResumeDocument


class ResumeBuilder:

    def build(self, resume):

        return ResumeDocument(
            summary=resume.summary,
            skills=resume.skills,
            experience=resume.experience,
            education=resume.education,
            certifications=resume.certifications,
            projects=resume.projects,
        )