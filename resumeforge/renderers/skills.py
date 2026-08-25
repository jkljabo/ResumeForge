from resumeforge.renderers.base import BaseRenderer


class SkillsRenderer(BaseRenderer):

    def render(self, document, resume):

        if not resume.skills:
            return

        document.add_heading("Technical Skills", level=1)

        for group in resume.skills:

            p = document.add_paragraph()

            p.add_run(f"{group.category}: ").bold = True
            p.add_run(", ".join(group.skills))