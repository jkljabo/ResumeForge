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
    parser = argparse.ArgumentParser(
        prog="resumeforge",
    )

    subparsers = parser.add_subparsers(
        dest="command",
    )

    #
    # generate
    #
    generate = subparsers.add_parser(
        "generate",
        help="Generate a tailored resume",
    )

    generate.add_argument(
        "--template",
        choices=TEMPLATES,
        default="default",
    )

    generate.add_argument(
        "--theme",
        choices=THEMES,
        default="default",
    )

    generate.add_argument(
        "--output",
        default="resume.docx",
    )

    generate.add_argument(
        "--job",
        help="Path to a job description text file",
    )

    generate.add_argument(
        "--profile",
        metavar="NAME",
        help="Resume profile to use",
    )

    generate.add_argument(
        "--explain",
        action="store_true",
        help="Display explainability report after tailoring",
    )
    
    #
    # profile
    #
    profile = subparsers.add_parser(
        "profile",
        help="Manage resume profiles",
    )

    profile_commands = profile.add_subparsers(
        dest="profile_command",
    )

    create = profile_commands.add_parser(
        "create",
        help="Create a new profile",
    )

    list = profile_commands.add_parser(
        "list",
        help="List available resume profiles",
    )

    remove = profile_commands.add_parser(
        "remove",
        help="Remove a profile",
    )

    edit_parser = profile_commands.add_parser(
        "edit",
        help="Edit an existing profile",
    )

    edit_parser.add_argument(
        "name",
    )

    edit_parser.add_argument(
        "--headline",
    )

    edit_parser.add_argument(
        "--full-name",
        dest="full_name",
    )

    remove.add_argument(
        "name",
        help="Profile name",
    )

    create.add_argument(
        "name",
        help="Profile name",
    )

    #
    # config
    #
    config_parser = subparsers.add_parser(
        "config",
        help="Manage ResumeForge configuration.",
    )

    config_subparsers = config_parser.add_subparsers(
        dest="config_command",
    )

    config_subparsers.add_parser(
        "show",
        help="Display the current configuration.",
    )

    config_set_parser = config_subparsers.add_parser("set")

    config_set_parser.add_argument("key")

    config_set_parser.add_argument("value")

    default_profile_parser = config_subparsers.add_parser(
        "default-profile",
    )

    default_profile_parser.add_argument(
        "profile",
    )

    theme_parser = config_subparsers.add_parser(
        "theme",
        help="Set the default theme",
    )
    theme_parser.add_argument("theme")

    output_dir_parser = config_subparsers.add_parser(
        "output-dir",
        help="Set the default output directory",
    )
    output_dir_parser.add_argument("directory")

    output_file_parser = config_subparsers.add_parser(
        "output-file",
        help="Set the default output filename",
    )
    output_file_parser.add_argument("filename")

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