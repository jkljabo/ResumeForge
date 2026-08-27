from resumeforge.renderers.base import BaseRenderer


class CertificationRenderer(BaseRenderer):
    def render(self, layout, resume):
        if not resume.certifications:
            return

        layout.heading("Certifications", level=1)

        for cert in resume.certifications:
            p = layout.paragraph(style="List Bullet")

            layout.text(p, cert.name).bold = True

            if cert.issuer:
                layout.text(p, f" — {cert.issuer}")

            if cert.year:
                layout.text(p, f" ({cert.year})")