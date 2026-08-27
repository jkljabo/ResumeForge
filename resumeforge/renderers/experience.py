from resumeforge.renderers.base import BaseRenderer


class ExperienceRenderer(BaseRenderer):
    def render(self, layout, resume):
        if not resume.experience:
            return

        layout.heading("Professional Experience", 1)

        for job in resume.experience:
            layout.paragraph(f"{job.employer} — {job.title}")