
import argparse
from argparse import Namespace
from pathlib import Path

from resumeforge.bootstrap import (
    create_generator,
    create_configuration_service,
)
from resumeforge.configuration.configuration_service import ConfigurationService
from resumeforge.profiles.profile import Profile
from resumeforge.profiles.repository import ProfileRepository
from resumeforge.services.profile_service import (
    ProfileService,
)
from resumeforge.services.resume_service import ResumeService
from resumeforge.resume.factory import (
    create_resume_service,
)
from resumeforge.factory import create_profile_repository, create_profile_service
from resumeforge.generator_protocol import ResumeGeneratorProtocol


class CLIWorkflow:
    def __init__(
        self,
        configuration_service: ConfigurationService | None = None,
        repository: ProfileRepository | None = None,
        resume_service: ResumeService | None = None,
        generator: ResumeGeneratorProtocol | None = None,
        profile_service: ProfileService | None = None,
    )-> None:
        if configuration_service is None:
            configuration_service = (
                create_configuration_service()
            )

        self.configuration_service = configuration_service

        self.repository = (
            repository
            if repository is not None
            else create_profile_repository()
        )

        self.resume_service = (
            resume_service
            or create_resume_service()
        )

        self.generator = (
            generator
            or create_generator()
        )

        self.profile_service = (
            profile_service
            or create_profile_service()
        )

    def run(
        self,
        args: Namespace,
    ) -> int:

        if args.command == "profile":
            return self.run_profile(args)

        if args.command == "config":
            return self.run_config(args)
        
        return self.run_generate(args)


    def run_generate(
        self,
        args: Namespace,
    ) -> int:

        profile = resolve_profile(
            self.repository,
            args,
        )

        job = load_job_description(
            args.job,
        )

        resume = self.resume_service.load(
            profile.resume_path,
        )

        self.generator.generate(
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

        service = self.profile_service

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

        if args.profile_command == "import":

            self.profile_service.import_profile(
                args.name,
                args.source,
            )

            print("Profile imported.")

            return 0

        if args.profile_command == "export":

            self.profile_service.export_profile(
                args.name,
                args.destination,
            )

            print("Profile exported.")

            return 0

        if args.profile_command == "clone":
            self.profile_service.clone_profile(
                args.source_name,
                args.destination_name,
            )

            print("Profile cloned.")

            return 0

        if args.profile_command == "rename":
            self.profile_service.rename_profile(
                args.old_name,
                args.new_name,
            )

            print("Profile renamed.")

            return 0

        if args.profile_command == "default":
            self.profile_service.set_default_profile(
                args.profile_name,
            )

            print("Default profile updated.")

            return 0

        print("Unknown profile command.")
        return 1


    def list(self) -> int:
        profiles = self.profile_service.list()

        if not profiles:
            print("No profiles found.")
            return 0

        default_profile = self.profile_service.get_default_profile()

        for profile in profiles:
            if profile == default_profile:
                print(f"* {profile}")
            else:
                print(profile)

        return 0


    def remove_profile(
        self,
        name: str,
    ) -> int:
        self.profile_service.remove(name)

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

        if getattr(args, "color_theme", None) is not None:
            updates["color_theme"] = args.color_theme

        if getattr(args, "description", None) is not None:
            updates["description"] = args.description

        if getattr(args, "tags", None) is not None:
            updates["tags"] = args.tags

        if getattr(args, "notes", None) is not None:
            updates["notes"] = args.notes

        if getattr(args, "category", None) is not None:
            updates["category"] = args.category

        if getattr(args, "visibility", None) is not None:
            updates["visibility"] = args.visibility

        if getattr(args, "owner", None) is not None:
            updates["owner"] = args.owner

        if getattr(args, "organization", None) is not None:
            updates["organization"] = args.organization

        if getattr(args, "purpose", None) is not None:
            updates["purpose"] = args.purpose

        if getattr(args, "target_role", None) is not None:
            updates["target_role"] = args.target_role

        if getattr(args, "experience_level", None) is not None:
            updates["experience_level"] = args.experience_level

        if getattr(args, "employment_type", None) is not None:
            updates["employment_type"] = args.employment_type

        if getattr(args, "work_arrangement", None) is not None:
            updates["work_arrangement"] = args.work_arrangement

        if getattr(args, "work_authorization", None) is not None:
            updates["work_authorization"] = args.work_authorization


        self.profile_service.edit(
            args.name,
            updates,
        )

        print(f"Profile '{args.name}' updated.")

        return 0


    def run_config(self, args: Namespace) -> int:
        if args.config_command == "show":
            configuration = (
                self.configuration_service.get_configuration()
            )

            print("ResumeForge Configuration")
            print("=" * 40)
            print(f"Default Profile         : {configuration.default_profile}")
            print(f"Default Theme           : {configuration.default_theme}")
            print(f"Output Directory        : {configuration.output_directory}")
            print(
                f"Default Output Filename : "
                f"{configuration.default_output_filename}"
            )
            print(f"Page Size               : {configuration.page_size}")
            print(f"Font Name               : {configuration.font_name}")

            return 0

        elif args.config_command == "list":
            configuration = (
                self.configuration_service.get_configuration()
            )

            print("ResumeForge Configuration")
            print("-------------------------")
            print(
                f"default-profile      {configuration.default_profile}"
            )
            print(
                f"default-theme        {configuration.default_theme}"
            )
            print(
                f"output-directory     {configuration.output_directory}"
            )
            print(
                f"default-output-file  "
                f"{configuration.default_output_filename}"
            )
            print(
                f"page-size           {configuration.page_size}"
            )
            print(
                f"font-name           {configuration.font_name}"
            )

            return 0

        elif args.config_command == "set":
            try:
                self.configuration_service.update_configuration(
                    **{
                        args.key.replace("-", "_"): args.value,
                    }
                )

                print("Configuration updated.")

                return 0

            except ValueError as ex:
                print(ex)

                return 1

        elif args.config_command == "reset":
            self.configuration_service.reset_configuration()

            print("Configuration reset.")

            return 0

        elif args.config_command == "help":
            print("ResumeForge Configuration Help")
            print("------------------------------")
            print()
            print("default-profile")
            print("    Default profile used for resume generation.")
            print()
            print("default-theme")
            print("    executive")
            print("    modern")
            print()
            print("page-size")
            print("    LETTER")
            print("    A4")
            print()
            print("font-name")
            print("    Font used when rendering documents.")
            print()

            return 0

        elif args.config_command == "default-profile":
            self.configuration_service.update_default_profile(
                args.profile,
            )

            print("Default profile updated.")

            return 0

        elif args.config_command == "theme":
            self.configuration_service.update_configuration(
                default_theme=args.theme,
            )

            print("Theme updated.")

            return 0

        elif args.config_command == "output-dir":
            self.configuration_service.update_configuration(
                output_directory=Path(args.directory),
            )

            print("Output directory updated.")

            return 0

        elif args.config_command == "output-file":
            self.configuration_service.update_configuration(
                default_output_filename=args.filename,
            )

            print("Output filename updated.")

            return 0

        print(
            f"Unknown config command: {args.config_command}"
        )
        
        return 1


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