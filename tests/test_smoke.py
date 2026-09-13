from pathlib import Path

from resumeforge.resume.factory import create_resume_service
from resumeforge.builder import ResumeBuilder
from resumeforge.profiles.repository import ProfileRepository

def test_resume_loads():
    repository = ProfileRepository()
    profile = repository.get_default()
    service = create_resume_service()
    resume = service.load(profile.resume_path)
    
    assert resume is not None

def test_resume_has_name():
    repository = ProfileRepository()
    profile = repository.get_default()
    service = create_resume_service()
    resume = service.load(profile.resume_path)

    assert resume.header.name == "Jason Little"

def test_builder_creates_document():
    builder = ResumeBuilder()
    assert builder.document is not None

def test_output_directory_exists():
    assert Path("output").exists()