import re


class Matcher:
    def _normalize(self, text: str) -> set[str]:
        words = re.findall(r"[a-z0-9\+\#\.]+", text.lower())
        return set(words)

    def score(self, resume, job_description: str) -> int:
        if not job_description:
            return 0

        job_terms = self._normalize(job_description)
        score = 0

        for skill_group in getattr(resume, "skills", []):
            group_tags = {tag.lower() for tag in getattr(skill_group, "tags", [])}
            score += len(job_terms & group_tags)

        for experience in getattr(resume, "experience", []):
            exp_tags = {tag.lower() for tag in getattr(experience, "tags", [])}
            score += len(job_terms & exp_tags)

        for project in getattr(resume, "projects", []):
            project_tags = {tag.lower() for tag in getattr(project, "tags", [])}
            score += len(job_terms & project_tags)

        for cert in getattr(resume, "certifications", []):
            cert_tags = {tag.lower() for tag in getattr(cert, "tags", [])}
            score += len(job_terms & cert_tags)

        return score