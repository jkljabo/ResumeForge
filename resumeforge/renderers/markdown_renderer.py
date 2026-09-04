class MarkdownRenderer:

    def render(self, document):

        lines = []

        lines.append("# Resume")

        if document.summary:
            lines.append("")
            lines.append("## Summary")
            lines.append("")
            lines.append(document.summary)

        self._render_list_section(
            lines,
            "Skills",
            document.skills,
        )

        self._render_list_section(
            lines,
            "Experience",
            document.experience,
        )

        self._render_list_section(
            lines,
            "Education",
            document.education,
        )

        self._render_list_section(
            lines,
            "Certifications",
            document.certifications,
        )

        self._render_list_section(
            lines,
            "Projects",
            document.projects,
        )

        return "\n".join(lines)

    def _render_list_section(
        self,
        lines,
        title,
        items,
    ):
        if not items:
            return

        lines.append("")
        lines.append(f"## {title}")
        lines.append("")

        for item in items:
            lines.append(f"- {item}")