from resumeforge.renderers.base import BaseRenderer


class SkillsRenderer(BaseRenderer):

    def render(self, layout, resume):

        if not resume.skills:
            return

        layout.heading("Technical Skills", level=1)

        for group in resume.skills:

            p = layout.paragraph()

            p.add_run(f"{group.category}: ").bold = True
            p.add_run(", ".join(group.skills))