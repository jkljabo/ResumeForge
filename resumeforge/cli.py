import argparse

from resumeforge.templates import (
    DefaultTemplate,
    ModernTemplate,
    ExecutiveTemplate,
)

from resumeforge.themes import (
    DefaultTheme,
    CorporateTheme,
    DarkTheme,
)

from resumeforge.workflow import CLIWorkflow


THEMES = {
    "default": DefaultTheme,
    "corporate": CorporateTheme,
    "dark": DarkTheme,
}

TEMPLATES = {
    "default": DefaultTemplate,
    "modern": ModernTemplate,
    "executive": ExecutiveTemplate,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--template",
        choices=TEMPLATES,
        default="default",
    )

    parser.add_argument(
        "--theme",
        choices=THEMES,
        default="default",
    )

    parser.add_argument(
        "--output",
        default="resume.docx",
    )

    parser.add_argument(
        "--job",
        help="Path to a job description text file",
    )

    parser.add_argument(
        "--profile",
        metavar="NAME",
        help="Resume profile to use",
    )

    return parser

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    workflow = CLIWorkflow()

    try:
        return workflow.run(args)

    except FileNotFoundError as ex:
        print(f"Error: {ex}")
        return 1

    except Exception as ex:
        print(f"Error: {ex}")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())