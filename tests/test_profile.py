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


def test_profile_defaults_to_no_color_theme():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.color_theme is None


def test_profile_stores_color_theme():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        color_theme="blue",
    )

    assert profile.color_theme == "blue"


def test_profile_defaults_to_no_description():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.description is None


def test_profile_stores_description():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        description="CDC Resume",
    )

    assert profile.description == "CDC Resume"


def test_profile_defaults_to_no_tags():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.tags is None


def test_profile_stores_tags():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        tags="cdc,federal",
    )

    assert profile.tags == "cdc,federal"


def test_profile_defaults_to_no_notes():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.notes is None


def test_profile_stores_notes():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        notes="Primary resume for CDC applications.",
    )

    assert profile.notes == "Primary resume for CDC applications."


def test_profile_defaults_to_no_category():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.category is None


def test_profile_stores_category():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        category="Government",
    )

    assert profile.category == "Government"


def test_profile_defaults_to_no_visibility():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.visibility is None


def test_profile_stores_visibility():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        visibility="Private",
    )

    assert profile.visibility == "Private"


def test_profile_defaults_to_no_owner():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.owner is None


def test_profile_stores_owner():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        owner="Jason Little",
    )

    assert profile.owner == "Jason Little"


def test_profile_defaults_to_no_organization():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.organization is None


def test_profile_stores_organization():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        organization="OpenAI",
    )

    assert profile.organization == "OpenAI"


def test_profile_defaults_to_no_purpose():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.purpose is None


def test_profile_stores_purpose():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        purpose="Federal Applications",
    )

    assert profile.purpose == "Federal Applications"


def test_profile_defaults_to_no_target_role():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.target_role is None


def test_profile_stores_target_role():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        target_role="Senior Software Engineer",
    )

    assert profile.target_role == "Senior Software Engineer"


def test_profile_defaults_to_no_experience_level():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.experience_level is None


def test_profile_stores_experience_level():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        experience_level="Senior",
    )

    assert profile.experience_level == "Senior"


def test_profile_defaults_to_no_employment_type():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.employment_type is None


def test_profile_stores_employment_type():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        employment_type="Full-time",
    )

    assert profile.employment_type == "Full-time"


def test_profile_defaults_to_no_work_arrangement():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.work_arrangement is None


def test_profile_stores_work_arrangement():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        work_arrangement="Hybrid",
    )

    assert profile.work_arrangement == "Hybrid"


def test_profile_defaults_to_no_work_authorization():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
    )

    assert profile.work_authorization is None


def test_profile_stores_work_authorization():
    profile = Profile(
        name="government",
        directory=Path("profiles") / "government",
        work_authorization="U.S. Citizen",
    )

    assert profile.work_authorization == "U.S. Citizen"



    