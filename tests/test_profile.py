from pathlib import Path

from resumeforge.profiles import Profile

from resumeforge.constants import (
    DEFAULT_PROFILE_NAME,
    DEFAULT_PROFILE_FILE,
)

def test_profile_creation():
    profile = Profile(
        name=DEFAULT_PROFILE_NAME,
        directory=Path("profiles") / DEFAULT_PROFILE_NAME,
        is_default=True,
    )

    assert profile.name == DEFAULT_PROFILE_NAME
    assert profile.resume_path == (
        Path("profiles")
        / DEFAULT_PROFILE_NAME
        / DEFAULT_PROFILE_FILE
    ) 
    assert profile.is_default is True


def test_resume_path_property():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.resume_path == (
        Path("profiles")
        / "government"
        / DEFAULT_PROFILE_FILE
    )


def test_default_profile_flag():
    profile = Profile(
        name=DEFAULT_PROFILE_NAME,
        directory=Path("profiles") / DEFAULT_PROFILE_NAME,
        is_default=True,
    )

    assert profile.is_default is True


def test_non_default_profile():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.is_default is False


