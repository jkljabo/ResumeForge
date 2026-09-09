from pathlib import Path
import pytest

from resumeforge.services.profile_service import (
    ProfileService,
)


def test_create_profile_directory(tmp_path):

    service = ProfileService(tmp_path)

    service.create("government")

    assert (tmp_path / "government").is_dir()


def test_create_resume_file(tmp_path):

    service = ProfileService(tmp_path)

    service.create("government")

    assert (
        tmp_path
        / "government"
        / "resume.json"
    ).exists()


def test_create_existing_profile_raises(tmp_path):

    service = ProfileService(tmp_path)

    service.create("government")

    with pytest.raises(FileExistsError):
        service.create("government")

def test_remove_existing_profile(tmp_path):

    service = ProfileService(tmp_path)

    service.create("government")

    service.remove("government")

    assert not (tmp_path / "government").exists()

def test_remove_missing_profile_raises(tmp_path):

    service = ProfileService(tmp_path)

    with pytest.raises(FileNotFoundError):
        service.remove("government")

def test_remove_preserves_other_profiles(tmp_path):

    service = ProfileService(tmp_path)

    service.create("government")
    service.create("banking")

    service.remove("government")

    assert not (tmp_path / "government").exists()
    assert (tmp_path / "banking").exists()

def test_list_after_remove(tmp_path):

    service = ProfileService(tmp_path)

    service.create("government")
    service.create("banking")

    service.remove("government")

    assert service.list() == ["banking"]

