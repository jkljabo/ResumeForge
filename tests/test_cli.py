
from email import generator

from resumeforge.cli import (
    build_parser,
    create_generator,
    TEMPLATES,
    THEMES,
)
from resumeforge.tailoring.tailored_resume_builder import (
    TailoredResumeBuilder,
)

from resumeforge.generator import ResumeGenerator
from tests.helpers import make_resume_profile
from resumeforge.cli import main

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
    
def test_corporate_theme_exists():
    assert "corporate" in THEMES


def test_dark_theme_exists():
    assert "dark" in THEMES


def test_default_template_exists():
    assert "default" in TEMPLATES


def test_modern_template_exists():
    assert "modern" in TEMPLATES


def test_executive_template_exists():
    assert "executive" in TEMPLATES


def test_job_argument_exists():
    parser = build_parser()

    args = parser.parse_args(
        ["--job", "jobs/test.txt"]
    )

    assert args.job == "jobs/test.txt"

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

def test_main_invokes_generator(monkeypatch,):
    generator = FakeGenerator()

    monkeypatch.setattr(
        "resumeforge.cli.create_generator",
        lambda: generator,
    )

    monkeypatch.setattr(
        "resumeforge.cli.load_resume",
        lambda *_: make_resume_profile(),
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "--output",
            "resume.md",
        ],
    )

    exit_code = main()

    assert exit_code == 0
    assert generator.called
    assert generator.destination == "resume.md"
    assert generator.profile is not None
    assert generator.job == ""

def test_main_reads_job_file(monkeypatch, tmp_path):
    generator = FakeGenerator()

    job_file = tmp_path / "job.txt"
    job_file.write_text(
        "Python Azure Developer",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "resumeforge.cli.create_generator",
        lambda: generator,
    )

    monkeypatch.setattr(
        "resumeforge.cli.load_resume",
        lambda *_: make_resume_profile(),
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
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

def test_main_missing_job_file(monkeypatch, capsys):
    monkeypatch.setattr(
        "resumeforge.cli.load_resume",
        lambda *_: make_resume_profile(),
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
            "--job",
            "missing.txt",
        ],
    )

    exit_code = main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Job description not found" in captured.out

def test_main_missing_resume(monkeypatch, capsys):
    def missing(path):
        raise FileNotFoundError

    monkeypatch.setattr(
        "resumeforge.cli.load_resume",
        missing,
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
        ],
    )

    exit_code = main()

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Resume profile not found" in captured.out

def test_main_generator_failure(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "resumeforge.cli.create_generator",
        lambda: FailingGenerator(),
    )

    monkeypatch.setattr(
        "resumeforge.cli.load_resume",
        lambda *_: make_resume_profile(),
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "resumeforge",
        ],
    )

    exit_code = main()

    out = capsys.readouterr().out

    assert exit_code == 1
    assert "Boom" in out
    assert "Resume written" not in out

