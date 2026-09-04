from pathlib import Path

from resumeforge.builder import ResumeBuilder
from resumeforge.cli import (
    build_parser,
    THEMES,
    TEMPLATES,
)
from resumeforge.filtering import ResumeFilter
from resumeforge.loader import load_resume


def main():

    parser = build_parser()
    args = parser.parse_args()

    resume = load_resume()
    if args.job:
        with open(args.job, encoding="utf-8") as f:
            job_description = f.read()

        resume = ResumeFilter().filter(
            resume,
            job_description,
        )

    template_cls = TEMPLATES[args.template]
    theme_cls = THEMES[args.theme]

    template = template_cls()
    theme = theme_cls()

    builder = ResumeBuilder(
        theme=theme,
        template=template,
    )

    builder.render(resume)

    output = Path("output") / args.output
    output.parent.mkdir(exist_ok=True)

    builder.save(output)

    print(f"Resume generated: {output}")


if __name__ == "__main__":
    main()