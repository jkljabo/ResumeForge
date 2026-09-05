from pathlib import Path

from resumeforge.loader import load_resume
from resumeforge.builder import ResumeBuilder
from resumeforge.profiles.repository import ProfileRepository

def test_resume_loads():
    repository = ProfileRepository()
    profile = repository.get_default()
    resume = load_resume(profile.resume_path)
    
    assert resume is not None

def test_resume_has_name():
    repository = ProfileRepository()
    profile = repository.get_default()
    resume = load_resume(profile.resume_path)
    
    assert resume.header.name == "Jason Little"

def test_builder_creates_document():
    builder = ResumeBuilder()
    assert builder.document is not None

def test_output_directory_exists():
    assert Path("output").exists()