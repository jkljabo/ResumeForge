class ReportRenderer:

    SECTION_ORDER = (
        "skills",
        "experience",
        "projects",
        "certifications",
    )
    
    def render(self, result):

        lines = []

        lines.append("Resume Match Report")
        lines.append("===================")
        self._blank(lines)
        lines.append(f"Overall Score: {result.score}")
        lines.append(f"Coverage: {result.coverage}%")
        self._blank(lines)
        lines.append("Section Scores")
        lines.append("--------------")

        for section, score in result.section_scores.items():
            lines.append(f"{section.title()}: {score}")

        lines.append("Matched Keywords")
        lines.append("----------------")

        if result.matched:
            for keyword in sorted(result.matched):
                lines.append(f"✓ {keyword}")
        else:
            lines.append("(none)")

        self._blank(lines)

        self._render_keyword_sections(
            lines,
            "Matched Keywords by Section",
            result.matched_by_section,
            "✓",
        )
        
        lines.append("Missing Keywords")
        lines.append("----------------")

        if result.missing:
            for keyword in sorted(result.missing):
                lines.append(f"• {keyword}")
        else:
            lines.append("(none)")

        self._blank(lines)

        self._render_keyword_sections(
            lines,
            "Missing Keywords by Section",
            result.missing_by_section,
            "•",
        )
        
        return "\n".join(lines)

    def _render_keyword_sections(
        self,
        lines,
        title,
        sections,
        bullet,
    ):
        self._blank(lines)
        lines.append(title)
        lines.append("-" * len(title))

        for section in self.SECTION_ORDER:
            keywords = sections.get(section, [])
            self._blank(lines)
            section_title = section.title()

            lines.append(section_title)
            lines.append("-" * len(section_title))

            if keywords:
                for keyword in sorted(keywords):
                    lines.append(
                        f"{bullet} {keyword}"
                    )
            else:
                lines.append("(none)")

    def _blank(self, lines):
        if lines and lines[-1] != "":
            lines.append("")