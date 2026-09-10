from argparse import Namespace
from pathlib import Path

import pytest

from resumeforge.cli import (
    build_parser,
    main,
    THEMES,
    TEMPLATES,
)

from resumeforge.bootstrap import create_generator
from resumeforge.generator import ResumeGenerator
from resumeforge.profiles import Profile
from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)

from resumeforge.workflow import CLIWorkflow
from tests.helpers import make_resume_profile

# ---------------------------------------------------------------------
# Test Doubles
# ---------------------------------------------------------------------

class FakeGenerator:

    def __init__(self):
        self.called = False
        self.profile = None
        self.job = None
        self.destination = None

    def generate(
        self,
        profile,
        job,
        destination,
    ):
        self.called = True
        self.profile = profile
        self.job = job
        self.destination = destination


class FailingGenerator:

    def generate(
        self,
        profile,
        job,
        destination,
    ):
        raise RuntimeError("Boom")
    

# ---------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------


def make_fake_profile(name="default", *, default=None):
    if default is None:
        default = name == "default"

    return Profile(
        name=name,
        directory=Path("profiles") / name,
        is_default=default,
    )


def stub_workflow(
    monkeypatch,
    generator=None,
):
    generator = generator or FakeGenerator()

    monkeypatch.setattr(
        "resumeforge.workflow.create_generator",
        lambda: generator,
    )

    monkeypatch.setattr(
        "resumeforge.workflow.load_resume",
        lambda *_: make_resume_profile(),
    )

    return generator


# ---------------------------------------------------------------------
# Parser / Command Routing Tests
# ---------------------------------------------------------------------


def test_job_argument_exists():
    parser = build_parser()

    args = parser.parse_args(
        [
            "generate",
            "--job",
            "jobs/test.txt",
        ]
    )

    assert args.command == "generate"
    assert args.job == "jobs/test.txt"


def test_parser_accepts_profile_argument():
    parser = build_parser()

    args = parser.parse_args(
    [
        "generate",
        "--profile",
        "government",
    ]
)

    assert args.command == "generate"
    assert args.profile == "government"


def test_parser_profile_defaults_to_none():
    parser = build_parser()

    args = parser.parse_args(
    [
        "generate",
    ]
)

    assert args.command == "generate"
    assert args.profile is None


def test_parser_defaults_to_generate():
    parser = build_parser()

    args = parser.parse_args(
    [
        "generate",
    ]
)

    assert args.command == "generate"
    assert args.profile is None


def test_parser_profile_create_command():
    parser = build_parser()

    args = parser.parse_args(
        [
            "profile",
            "create",
            "consulting",
        ]
    )

    assert args.command == "profile"
    assert args.profile_command == "create"
    assert args.name == "consulting"


def test_generate_command_exists():
    parser = build_parser()

    args = parser.parse_args(["generate"])

    assert args.command == "generate"


def test_profile_command_exists():
    parser = build_parser()

    args = parser.parse_args(
        [
            "profile",
            "create",
            "government",
        ]
    )

    assert args.command == "profile"
    assert args.profile_command == "create"
    assert args.name == "government"


def test_profile_list_command():

    parser = build_parser()

    args = parser.parse_args(
        ["profile", "list"]
    )

    assert args.command == "profile"
    assert args.profile_command == "list"

# ----------------------------------
# Generator construction tests
# ----------------------------------

def test_create_generator_returns_resume_generator():
    generator = create_generator()

    assert isinstance(generator, ResumeGenerator)

def test_create_generator_uses_tailored_resume_builder():
    generator = create_generator()

    assert isinstance(
        generator.builder,
        TailoredResumeBuilder,
    )

def test_create_generator_wires_pipeline():

    generator = create_generator()

    assert generator.matcher is not None
    assert generator.tailoring_engine is not None
    assert generator.builder is not None
    assert generator.exporter is not None
    assert generator.writer is not None


# ---------------------------------------------------------------------
# Theme / Template Tests
# ---------------------------------------------------------------------

def test_default_template_exists():
    assert "default" in TEMPLATES


def test_modern_template_exists():
    assert "modern" in TEMPLATES


def test_executive_template_exists():
    assert "executive" in TEMPLATES


def test_corporate_theme_exists():
    assert "corporate" in THEMES


def test_dark_theme_exists():
    assert "dark" in THEMES


# ----------------------------------
# CLI Success Tests
# ----------------------------------

def test_main_invokes_generator(monkeypatch):
    workflow = stub_workflow(monkeypatch)

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "generate",
            "--output",
            "resume.md",
        ],
    )

    exit_code = main()

    assert exit_code == 0
    assert workflow.called
    assert workflow.destination == "resume.md"
    assert workflow.profile is not None
    assert workflow.job == ""


def test_main_reads_job_file(monkeypatch, tmp_path):
    generator = stub_workflow(monkeypatch)

    job_file = tmp_path / "job.txt"
    job_file.write_text(
        "Python Azure Developer",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "generate",
            "--job",
            str(job_file),
            "--output",
            "resume.md",
        ],
    )

    exit_code = main()

    assert exit_code == 0
    assert generator.job == "Python Azure Developer"
    assert generator.destination == "resume.md"


def test_main_uses_selected_profile(monkeypatch):
    calls = []

    fake_profile = make_fake_profile("government")

    class FakeRepository:
        def get(self, name):
            calls.append(name)
            return fake_profile

        def get_default(self):
            raise AssertionError()

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileRepository",
        lambda: FakeRepository(),
    )

    stub_workflow(monkeypatch)

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "generate",
            "--profile",
            "government",
        ],
    )

    assert main() == 0

    assert calls == ["government"]


def test_main_uses_default_profile(monkeypatch):

    default_called = False

    fake_profile = make_fake_profile()

    class FakeRepository:
        def get_default(self):
            nonlocal default_called
            default_called = True
            return fake_profile

        def get(self, name):
            raise AssertionError(
                "Named profile should not be requested."
            )

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileRepository",
        lambda: FakeRepository(),
    )

    stub_workflow(monkeypatch)

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "generate",
        ],
    )

    assert main() == 0

    assert default_called


# ---------------------------------------------------------------------
# CLI Error Handling Tests
# ---------------------------------------------------------------------

def test_main_missing_resume(monkeypatch, capsys):
    def missing(path):
        raise FileNotFoundError("Resume profile not found")

    monkeypatch.setattr(
        "resumeforge.workflow.load_resume",
        missing,
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "generate",
        ],
    )

    exit_code = main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Resume profile not found" in captured.out


def test_main_missing_job_file(monkeypatch, capsys):
    monkeypatch.setattr(
        "resumeforge.workflow.load_resume",
        lambda *_: make_resume_profile(),
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "generate",
            "--job",
            "missing.txt",
        ],
    )

    exit_code = main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Job description not found" in captured.out


def test_main_unknown_profile(monkeypatch, capsys):
    class FakeRepository:
        def get(self, name):
            raise FileNotFoundError(
                f"Profile '{name}' not found."
            )

        def get_default(self):
            raise AssertionError()

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileRepository",
        lambda: FakeRepository(),
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "generate",
            "--profile",
            "missing",
        ],
    )

    exit_code = main()

    captured = capsys.readouterr()

    assert exit_code == 1

    assert "Profile 'missing' not found." in captured.out


def test_main_generator_failure(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "resumeforge.workflow.create_generator",
        lambda: FailingGenerator(),
    )

    monkeypatch.setattr(
        "resumeforge.workflow.load_resume",
        lambda *_: make_resume_profile(),
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "generate",
        ],
    )

    exit_code = main()

    out = capsys.readouterr().out

    assert exit_code == 1
    assert "Boom" in out
    assert "Resume written" not in out


def test_profile_list_prints_profiles(
    monkeypatch,
    capsys,
):
    class StubProfileService:
        def list(self):
            return [
                "default",
                "government",
            ]

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileService",
        StubProfileService,
    )

    workflow = CLIWorkflow()

    args = Namespace(
        command="profile",
        profile_command="list",
    )

    exit_code = workflow.run(args)

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "default" in captured.out
    assert "government" in captured.out


def test_profile_list_when_empty(
    monkeypatch,
    capsys,
):
    class StubProfileService:
        def list(self):
            return []

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileService",
        StubProfileService,
    )

    workflow = CLIWorkflow()

    args = Namespace(
        command="profile",
        profile_command="list",
    )

    exit_code = workflow.run(args)

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "No profiles found." in captured.out


def test_profile_remove_command():

    parser = build_parser()

    args = parser.parse_args(
        [
            "profile",
            "remove",
            "government",
        ]
    )

    assert args.command == "profile"
    assert args.profile_command == "remove"
    assert args.name == "government"


def test_remove_profile_calls_service(monkeypatch):

    called = {}

    class FakeService:

        def remove(self, name):
            called["name"] = name

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileService",
        FakeService,
    )

    workflow = CLIWorkflow()

    args = Namespace(
        command="profile",
        profile_command="remove",
        name="government",
    )

    assert workflow.run(args) == 0
    assert called["name"] == "government"


def test_remove_missing_profile(monkeypatch):

    class FakeService:

        def remove(self, name):
            raise FileNotFoundError(name)

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileService",
        FakeService,
    )

    workflow = CLIWorkflow()

    args = Namespace(
        command="profile",
        profile_command="remove",
        name="missing",
    )

    with pytest.raises(FileNotFoundError):
        workflow.run(args)


def test_profile_edit_command():

    parser = build_parser()

    args = parser.parse_args(
        [
            "profile",
            "edit",
            "government",
            "--headline",
            "Senior Software Engineer",
        ]
    )

    assert args.command == "profile"
    assert args.profile_command == "edit"
    assert args.name == "government"
    assert args.headline == "Senior Software Engineer"


def test_edit_profile_calls_service(monkeypatch):

    called = {}

    class FakeService:

        def edit(
            self,
            name,
            updates,
        ):
            called["name"] = name
            called["updates"] = updates

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileService",
        FakeService,
    )

    workflow = CLIWorkflow()

    args = Namespace(
        command="profile",
        profile_command="edit",
        name="government",
        headline="Senior Software Engineer",
        full_name=None,
    )

    assert workflow.run(args) == 0

    assert called["name"] == "government"

    assert called["updates"] == {
        "headline": "Senior Software Engineer",
    }


def test_edit_profile_updates_multiple_fields(monkeypatch):

    called = {}

    class FakeService:

        def edit(
            self,
            name,
            updates,
        ):
            called["updates"] = updates

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileService",
        FakeService,
    )

    workflow = CLIWorkflow()

    args = Namespace(
        command="profile",
        profile_command="edit",
        name="government",
        headline="Lead Engineer",
        full_name="Jason K. Little",
    )

    assert workflow.run(args) == 0

    assert called["updates"] == {
        "headline": "Lead Engineer",
        "name": "Jason K. Little",
    }


def test_edit_missing_profile(monkeypatch):

    class FakeService:

        def edit(
            self,
            name,
            updates,
        ):
            raise FileNotFoundError(name)

    monkeypatch.setattr(
        "resumeforge.workflow.ProfileService",
        FakeService,
    )

    workflow = CLIWorkflow()

    args = Namespace(
        command="profile",
        profile_command="edit",
        name="missing",
        headline="Engineer",
        full_name=None,
    )

    with pytest.raises(FileNotFoundError):
        workflow.run(args)


def test_profile_help_contains_edit(capsys):

    parser = build_parser()

    with pytest.raises(SystemExit):
        parser.parse_args(
            [
                "profile",
                "--help",
            ]
        )

    out = capsys.readouterr().out

    assert "edit" in out