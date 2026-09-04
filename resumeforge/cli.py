import argparse
from pathlib import Path

from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)
from resumeforge.exporters import MarkdownExporter
from resumeforge.generator import ResumeGenerator
from resumeforge.scoring import Matcher
from resumeforge.tailoring.engine import TailoringEngine
from resumeforge.output.resume_writer import ResumeWriter
from resumeforge.loader import load_resume

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

    return parser

def create_generator() -> ResumeGenerator:
    """Construct the ResumeForge generation pipeline."""
    matcher = Matcher()

    tailoring_engine = TailoringEngine()

    builder = TailoredResumeBuilder()

    exporter = MarkdownExporter()

    writer = ResumeWriter()

    return ResumeGenerator(
        matcher=matcher,
        tailoring_engine=tailoring_engine,
        builder=builder,
        exporter=exporter,
        writer=writer,
    )

def main() -> int:
    parser = build_parser()

    args = parser.parse_args()

    try:
        profile = load_resume()
    except FileNotFoundError:
        print("Error: Resume profile not found.")
        return 1

    job = ""

    if args.job:
        try:
            job = Path(args.job).read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"Error: Job description not found: {args.job}")
            return 1

    generator = create_generator()

    try:
        generator.generate(
            profile,
            job,
            args.output,
        )
    except Exception as ex:
        print(f"Error: {ex}")
        return 1

    print(f"Resume written to {args.output}")

    return 0

    print(f"Resume written to {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())