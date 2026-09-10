
import argparse
from pathlib import Path
from argparse import Namespace

from resumeforge.bootstrap import create_generator
from resumeforge.loader import load_resume
from resumeforge.profiles.profile import Profile
from resumeforge.profiles.repository import ProfileRepository
from resumeforge.services.profile_service import (
    ProfileService,
)

class CLIWorkflow:

    def run(
        self,
        args: Namespace,
    ) -> int:

        if args.command == "profile":
            return self.run_profile(args)

        return self.run_generate(args)


    def run_generate(
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
            resume,
            job,
            args.output,
        )

        print(f"Resume written to {args.output}")

        return 0


    def run_profile(
        self,
        args: Namespace,
    ) -> int:

        repository = ProfileRepository()

        service = ProfileService(
            repository=repository,
        )

        if args.profile_command == "create":

            service.create(args.name)

            print(
                f"Profile '{args.name}' created."
            )

            return 0

        if args.profile_command == "list":
            return self.list()

        if args.profile_command == "remove":
            return self.remove_profile(args.name)

        if args.profile_command == "edit":
            return self.edit_profile(args)

        print("Unknown profile command.")
        return 1


    def list(self) -> int:
        service = ProfileService(
            repository=ProfileRepository(),
        )

        profiles = service.list()

        if not profiles:
            print("No profiles found.")
            return 0

        for profile in profiles:
            print(profile)

        return 0


    def remove_profile(
        self,
        name: str,
    ) -> int:
        service = ProfileService(
            repository=ProfileRepository(),
        )

        service.remove(name)

        print(f"Profile '{name}' removed.")

        return 0


    def edit_profile(
        self,
        args: Namespace,
    ) -> int:

        updates = {}

        if args.headline is not None:
            updates["headline"] = args.headline

        if args.full_name is not None:
            updates["name"] = args.full_name

        service = ProfileService(
            repository=ProfileRepository(),
        )

        service.edit(
            args.name,
            updates,
        )

        print(f"Profile '{args.name}' updated.")

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