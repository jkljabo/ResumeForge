from pathlib import Path

from resume.loader import load_resume
from resume.builder import ResumeBuilder

def test_resume_loads():
    resume = load_resume()
    assert resume is not None

def test_resume_has_name():
    resume = load_resume()
    assert resume["name"] == "Jason Little"

def test_builder_creates_document():
    builder = ResumeBuilder()
    assert builder.document is not None

def test_output_directory_exists():
    assert Path("output").exists()