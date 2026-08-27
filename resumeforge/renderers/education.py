from resumeforge.renderers.base import BaseRenderer


class EducationRenderer(BaseRenderer):

    def render(self, layout, resume):

        if not resume.education:
            return

        layout.heading("Education", level=1)

        for school in resume.education:

            p = layout.paragraph()

            layout.text(p,school.degree).bold = True
            layout.text(p, f"\n{school.school}")

            if school.graduation_year:
                layout.text(p, f" ({school.graduation_year})")