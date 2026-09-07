
import argparse
from pathlib import Path
from argparse import Namespace

from resumeforge.bootstrap import create_generator
from resumeforge.loader import load_resume
from resumeforge.profiles.profile import Profile
from resumeforge.profiles.repository import ProfileRepository


class CLIWorkflow:

    def run(
        self,
        args: Namespace,
    ) -> int:

        repository = ProfileRepository()

        profile = resolve_profile(
            repository,
            args,
        )

        resume = load_resume(profile.resume_path)

        job = load_job_description(args.job)

        generator = create_generator()

        generator.generate(
            profile,
            job,
            args.output,
        )

        print(f"Resume written to {args.output}")

        return 0

def resolve_profile(
    repository: ProfileRepository,
    args: argparse.Namespace,
) -> Profile:
    """
    Resolve the requested resume profile.
    """
    if args.profile:
        return repository.get(args.profile)

    return repository.get_default()

def load_job_description(path: str | None) -> str:
    """
    Load the job description from disk.

    Returns an empty string when no job file is supplied.
    """
    if path is None:
        return ""

    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError as ex:
        raise FileNotFoundError(
            f"Job description not found: {path}"
        ) from ex