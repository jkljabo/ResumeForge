from resumeforge.renderers.base import BaseRenderer


class CertificationRenderer(BaseRenderer):
    def render(self, document, resume):
        if not resume.certifications:
            return

        document.add_heading("Certifications", level=1)

        for cert in resume.certifications:
            p = document.add_paragraph(style="List Bullet")

            p.add_run(cert.name).bold = True

            if cert.issuer:
                p.add_run(f" — {cert.issuer}")

            if cert.year:
                p.add_run(f" ({cert.year})")