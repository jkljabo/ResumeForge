from resumeforge.renderers.base import BaseRenderer


class ProjectRenderer(BaseRenderer):
    def render(self, layout, resume):
        if not resume.projects:
            return

        layout.heading("Projects")

        for project in resume.projects:
            p = layout.bullet()

            layout.bold(p, project.name)

            if project.description:
                p.add_run(f" — {project.description}")