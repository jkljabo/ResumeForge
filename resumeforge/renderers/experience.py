from resumeforge.renderers.base import BaseRenderer


class ExperienceRenderer(BaseRenderer):
    def render(self, document, resume):
        if not resume.experience:
            return

        document.add_heading("Professional Experience", 1)

        for job in resume.experience:
            document.add_paragraph(f"{job.employer} — {job.title}")