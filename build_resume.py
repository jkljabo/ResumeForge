import argparse

from resumeforge.builder import ResumeBuilder
from resumeforge.loader import load_resume
from resumeforge.templates import DefaultTemplate, ModernTemplate


TEMPLATES = {
    "default": DefaultTemplate,
    "modern": ModernTemplate,
}


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--template",
        default="default",
        choices=TEMPLATES.keys(),
        help="Resume template",
    )

    parser.add_argument(
        "--output",
        default="resume.docx",
        help="Output filename",
    )

    args = parser.parse_args()

    resume = load_resume()

    template = TEMPLATES[args.template]()

    builder = ResumeBuilder(template=template)

    builder.render(resume)

    builder.save(args.output)

    print(f"Resume generated: {args.output}")


if __name__ == "__main__":
    main()