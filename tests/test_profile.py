from pathlib import Path

from resumeforge.profiles import Profile


def test_profile_creation():
    profile = Profile(
        name="default",
        path=Path("profiles/default"),
    )

    assert profile.name == "default"
    assert profile.path == Path("profiles/default")
    assert profile.description == ""
    assert profile.is_default is False


def test_resume_file_property():
    profile = Profile(
        name="default",
        path=Path("profiles/default"),
    )

    assert profile.resume_file == Path("profiles/default/resume.json")