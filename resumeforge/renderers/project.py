from resumeforge.renderers.base import BaseRenderer


class ProjectRenderer(BaseRenderer):
    def render(self, document, resume):
        if not resume.projects:
            return

        document.add_heading("Projects", level=1)

        for project in resume.projects:
            p = document.add_paragraph(style="List Bullet")

            p.add_run(project.name).bold = True

            if project.description:
                p.add_run(f" — {project.description}")