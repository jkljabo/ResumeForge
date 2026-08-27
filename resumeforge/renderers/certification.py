from resumeforge.renderers.base import BaseRenderer


class CertificationRenderer(BaseRenderer):
    def render(self, layout, resume):
        if not resume.certifications:
            return

        layout.heading("Certifications", level=1)

        for cert in resume.certifications:
            p = layout.paragraph(style="List Bullet")

            p.add_run(cert.name).bold = True

            if cert.issuer:
                p.add_run(f" — {cert.issuer}")

            if cert.year:
                p.add_run(f" ({cert.year})")