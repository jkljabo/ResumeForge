class MarkdownResumeRenderer:

    def render(self, document):

        if document is None:
            return ""

        lines = []

        if document.name:
            lines.append(f"# {document.name}")
            lines.append("")

        if document.email:
            lines.append(document.email)

        if document.phone:
            lines.append(document.phone)

        if document.summary:
            lines.append("")
            lines.append("## Professional Summary")
            lines.append("")
            lines.append(document.summary)

        if document.skills:
            lines.append("")
            lines.append("## Skills")
            lines.append("")

            for skill in document.skills:
                lines.append(f"- {skill}")

        return "\n".join(lines)