from pathlib import Path

import pytest

from resumeforge.profiles import ProfileRepository

from resumeforge.constants import (
    DEFAULT_PROFILE_NAME,
    DEFAULT_PROFILE_FILE,
)


def test_repository_discovers_default_profile():
    repository = ProfileRepository()

    profiles = repository.list_profiles()

    assert len(profiles) == 1


def test_default_profile_name():
    repository = ProfileRepository()

    profile = repository.list_profiles()[0]

    assert profile.is_default


def test_default_profile_exists():
    repository = ProfileRepository()

    profile = repository.list_profiles()[0]

    assert profile.resume_path.exists()


def test_profile_path_points_to_resume_json():
    repository = ProfileRepository()

    profile = repository.list_profiles()[0]

    assert profile.resume_path.name == DEFAULT_PROFILE_FILE

def create_profile(root: Path, name: str):
    directory = root / name
    directory.mkdir()
    (directory / DEFAULT_PROFILE_FILE).write_text("{}")

def test_empty_repository(tmp_path):
    repo = ProfileRepository(tmp_path)

    assert repo.list_profiles() == []

def test_list_profiles(tmp_path):
    create_profile(tmp_path, DEFAULT_PROFILE_NAME)
    create_profile(tmp_path, "government")

    repo = ProfileRepository(tmp_path)

    profiles = repo.list_profiles()

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

