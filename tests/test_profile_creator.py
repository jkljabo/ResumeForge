
from pathlib import Path
import json
import pytest

from resumeforge.cli import build_parser
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


def test_edit_existing_profile(tmp_path):
    service = ProfileService(tmp_path)

    service.create("government")

    resume = tmp_path / "government" / "resume.json"

    resume.write_text(
        json.dumps(
            {
                "name": "Jason Little",
                "headline": "Software Engineer",
            }
        ),
        encoding="utf-8",
    )

    service.edit(
        "government",
        {
            "headline": "Senior Software Engineer",
        },
    )

    updated = json.loads(resume.read_text(encoding="utf-8"))

    assert updated["headline"] == "Senior Software Engineer"


def test_edit_missing_profile_raises(tmp_path):
    service = ProfileService(tmp_path)

    with pytest.raises(FileNotFoundError):
        service.edit(
            "government",
            {
                "headline": "Senior Engineer",
            },
        )


def test_edit_preserves_existing_fields(tmp_path):
    service = ProfileService(tmp_path)

    service.create("government")

    resume = tmp_path / "government" / "resume.json"

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

    service.edit(
        "government",
        {
            "headline": "Senior Engineer",
        },
    )

    updated = json.loads(resume.read_text(encoding="utf-8"))

    assert updated["name"] == "Jason Little"
    assert updated["location"] == "Georgia"
    assert updated["headline"] == "Senior Engineer"


def test_edit_updates_multiple_fields(tmp_path):
    service = ProfileService(tmp_path)

    service.create("government")

    resume = tmp_path / "government" / "resume.json"

    resume.write_text(
        json.dumps(
            {
                "name": "Jason Little",
                "headline": "Engineer",
            }
        ),
        encoding="utf-8",
    )

    service.edit(
        "government",
        {
            "headline": "Lead Engineer",
            "name": "Jason K. Little",
        },
    )

    updated = json.loads(resume.read_text(encoding="utf-8"))

    assert updated["headline"] == "Lead Engineer"
    assert updated["name"] == "Jason K. Little"


