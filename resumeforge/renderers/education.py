from resumeforge.renderers.base import BaseRenderer


class EducationRenderer(BaseRenderer):

    def render(self, layout, resume):

        if not resume.education:
            return

        layout.heading("Education", level=1)

        for school in resume.education:

            p = layout.paragraph()

            p.add_run(school.degree).bold = True
            p.add_run(f"\n{school.school}")

            if school.graduation_year:
                p.add_run(f" ({school.graduation_year})")