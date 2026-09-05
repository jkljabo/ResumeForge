from pathlib import Path

from resumeforge.profiles import Profile

from resumeforge.constants import (
    DEFAULT_PROFILE_NAME,
    DEFAULT_PROFILE_FILE,
)

def test_profile_creation():
    profile = Profile(
        name=DEFAULT_PROFILE_NAME,
        resume_path=Path("profiles")
            / DEFAULT_PROFILE_NAME 
            / DEFAULT_PROFILE_FILE,
        is_default=True,
    )

    assert profile.name == DEFAULT_PROFILE_NAME
    assert profile.resume_path == Path("profiles") / DEFAULT_PROFILE_NAME / DEFAULT_PROFILE_FILE

    assert profile.is_default is True


def test_resume_path_property():
    profile = Profile(
        name="default",
        resume_path=Path("profiles") / DEFAULT_PROFILE_NAME / DEFAULT_PROFILE_FILE,
        is_default=True,
    )

    assert profile.resume_path == Path("profiles") / DEFAULT_PROFILE_NAME / DEFAULT_PROFILE_FILE

def test_resume_path():
    profile = Profile(
        name=DEFAULT_PROFILE_NAME,
        resume_path=Path("profiles") / DEFAULT_PROFILE_NAME / DEFAULT_PROFILE_FILE,
        is_default=True,
    )

    assert profile.resume_path == Path("profiles") / DEFAULT_PROFILE_NAME / DEFAULT_PROFILE_FILE
