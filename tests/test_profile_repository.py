import json
from pathlib import Path

import pytest

from resumeforge.profiles import ProfileRepository

from resumeforge.constants import (
    DEFAULT_PROFILE_NAME,
    DEFAULT_PROFILE_FILE,
)


def test_repository_discovers_default_profile():
    repository = ProfileRepository()

    profiles = repository.list()

    assert len(profiles) == 1


def test_default_profile_name():
    repository = ProfileRepository()

    profile = repository.list()[0]

    assert profile.is_default


def test_default_profile_exists():
    repository = ProfileRepository()

    profile = repository.list()[0]

    assert profile.resume_path.exists()


def test_profile_path_points_to_resume_json():
    repository = ProfileRepository()

    profile = repository.list()[0]

    assert profile.resume_path.name == DEFAULT_PROFILE_FILE


def create_profile(root: Path, name: str):
    directory = root / name
    directory.mkdir()
    (directory / DEFAULT_PROFILE_FILE).write_text("{}")


def test_empty_repository(tmp_path):
    repo = ProfileRepository(tmp_path)

    assert repo.list() == []


def test_list(tmp_path):
    create_profile(tmp_path, DEFAULT_PROFILE_NAME)
    create_profile(tmp_path, "government")

    repo = ProfileRepository(tmp_path)

    profiles = repo.list()

    assert len(profiles) == 2
    assert profiles[0].name == DEFAULT_PROFILE_NAME
    assert profiles[1].name == "government"


def test_exists(tmp_path):
    create_profile(tmp_path, DEFAULT_PROFILE_NAME)

    repo = ProfileRepository(tmp_path)

    assert repo.exists(DEFAULT_PROFILE_NAME)
    assert not repo.exists("missing")


def test_get_profile(tmp_path):
    create_profile(tmp_path, DEFAULT_PROFILE_NAME)

    repo = ProfileRepository(tmp_path)

    profile = repo.get(DEFAULT_PROFILE_NAME)

    assert profile.name == DEFAULT_PROFILE_NAME


def test_get_missing_profile(tmp_path):
    repo = ProfileRepository(tmp_path)

    with pytest.raises(FileNotFoundError):
        repo.get("missing")


def test_get_default(tmp_path):
    create_profile(tmp_path, DEFAULT_PROFILE_NAME)
    create_profile(tmp_path, "government")

    repo = ProfileRepository(tmp_path)

    profile = repo.get_default()

    assert profile.name == DEFAULT_PROFILE_NAME


def test_create_profile(tmp_path):
    repo = ProfileRepository(tmp_path)

    repo.create("government")

    assert (tmp_path / "government").exists()
    assert (tmp_path / "government" / DEFAULT_PROFILE_FILE).exists()


def test_create_duplicate_profile_raises(tmp_path):
    repo = ProfileRepository(tmp_path)

    repo.create("government")

    with pytest.raises(FileExistsError):
        repo.create("government")


def test_created_profile_is_discoverable(tmp_path):
    repo = ProfileRepository(tmp_path)

    repo.create("government")

    profiles = repo.list()

    assert len(profiles) == 1
    assert profiles[0].name == "government"


def test_remove_profile(tmp_path):

    repo = ProfileRepository(tmp_path)

    repo.create("government")

    repo.remove("government")

    assert not (
        tmp_path
        / "government"
    ).exists()


def test_remove_missing_profile_raises(tmp_path):

    repo = ProfileRepository(tmp_path)

    with pytest.raises(FileNotFoundError):
        repo.remove("government")


def test_remove_preserves_other_profiles(tmp_path):

    repo = ProfileRepository(tmp_path)

    repo.create("government")
    repo.create("banking")

    repo.remove("government")

    assert not (
        tmp_path
        / "government"
    ).exists()

    assert (
        tmp_path
        / "banking"
    ).exists()


def test_update_profile(tmp_path):

    repo = ProfileRepository(tmp_path)

    repo.create("government")

    resume = (
        tmp_path
        / "government"
        / DEFAULT_PROFILE_FILE
    )

    resume.write_text(
        '{"name": "Jason Little", "headline": "Engineer"}',
        encoding="utf-8",
    )

    repo.update(
        "government",
        {
            "headline": "Senior Engineer",
        },
    )

    data = json.loads(
        resume.read_text(
            encoding="utf-8",
        )
    )

    assert data["headline"] == "Senior Engineer"


def test_update_missing_profile_raises(tmp_path):

    repo = ProfileRepository(tmp_path)

    with pytest.raises(FileNotFoundError):
        repo.update(
            "government",
            {
                "headline": "Senior Engineer",
            },
        )


def test_update_preserves_existing_fields(tmp_path):

    repo = ProfileRepository(tmp_path)

    repo.create("government")

    resume = (
        tmp_path
        / "government"
        / DEFAULT_PROFILE_FILE
    )

    resume.write_text(
        json.dumps(
            {
                "name": "Jason Little",
                "headline": "Engineer",
                "location": "Georgia",
            }
        ),
        encoding="utf-8",
    )

    repo.update(
        "government",
        {
            "headline": "Senior Engineer",
        },
    )

    data = json.loads(
        resume.read_text(
            encoding="utf-8",
        )
    )

    assert data["name"] == "Jason Little"
    assert data["location"] == "Georgia"
    assert data["headline"] == "Senior Engineer"


def test_update_multiple_fields(tmp_path):

    repo = ProfileRepository(tmp_path)

    repo.create("government")

    resume = (
        tmp_path
        / "government"
        / DEFAULT_PROFILE_FILE
    )

    resume.write_text(
        json.dumps(
            {
                "name": "Jason Little",
                "headline": "Engineer",
            }
        ),
        encoding="utf-8",
    )

    repo.update(
        "government",
        {
            "headline": "Lead Engineer",
            "name": "Jason K. Little",
        },
    )

    data = json.loads(
        resume.read_text(
            encoding="utf-8",
        )
    )

    assert data["headline"] == "Lead Engineer"
    assert data["name"] == "Jason K. Little"