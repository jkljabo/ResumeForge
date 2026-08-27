import argparse
from pathlib import Path

from resumeforge.builder import ResumeBuilder
from resumeforge.loader import load_resume
from resumeforge.templates import DefaultTemplate, ModernTemplate, ExecutiveTemplate

from resumeforge.themes import (
    DefaultTheme,
    CorporateTheme,
)

THEMES = {
    "default": DefaultTheme,
    "corporate": CorporateTheme,
}

TEMPLATES = {
    "default": DefaultTemplate,
    "modern": ModernTemplate,
    "executive": ExecutiveTemplate,
}


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--theme",
        default="default",
        choices=THEMES.keys(),
        help="Resume theme",
    )
    
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

    theme = THEMES[args.theme]()

    builder = ResumeBuilder(
        template=template,
        theme=theme,
    )

    builder.render(resume)

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    output = output_dir / args.output

    builder.save(output)

    print(f"Resume generated: {output}")


if __name__ == "__main__":
    main()