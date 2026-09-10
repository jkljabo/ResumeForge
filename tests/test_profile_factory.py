from pathlib import Path

from resumeforge.constants import DEFAULT_PROFILE_FILE
from resumeforge.profiles.factory import ProfileFactory


def test_create_profile():
    factory = ProfileFactory()

    profile = factory.create(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.name == "government"
    assert profile.directory == Path("profiles") / "government"
    assert profile.resume_path == (
        Path("profiles") / "government" / DEFAULT_PROFILE_FILE
    )
    assert profile.is_default is False


def test_create_default_profile():
    factory = ProfileFactory()

    profile = factory.create(
        name="default",
        directory=Path("profiles") / "default",
        is_default=True,
    )

    assert profile.is_default is True