
from pathlib import Path
import json
import pytest

from resumeforge.cli import build_parser
from resumeforge.services.profile_service import (
    ProfileService,
)
from resumeforge.profiles.repository import (
    ProfileRepository,
)


def test_create_profile_directory(tmp_path):

    repo = ProfileRepository(tmp_path)

    service = ProfileService(
        repository=repo,
    )

    service.create("government")

    assert (tmp_path / "government").is_dir()


def test_create_resume_file(tmp_path):

    repo = ProfileRepository(tmp_path)
    
    service = ProfileService(
        repository=repo,
    )

    service.create("government")

    assert (
        tmp_path
        / "government"
        / "resume.json"
    ).exists()


def test_create_existing_profile_raises(tmp_path):

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    service.create("government")

    with pytest.raises(FileExistsError):
        service.create("government")


def test_create_delegates_to_repository(tmp_path, monkeypatch):

    calls = []

    def fake_create(self, name):
        calls.append(name)

    monkeypatch.setattr(
        ProfileRepository,
        "create",
        fake_create,
    )

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    service.create("government")

    assert calls == ["government"]


def test_remove_existing_profile(tmp_path):

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    service.create("government")

    service.remove("government")

    assert not (tmp_path / "government").exists()


def test_remove_delegates_to_repository(
    tmp_path,
    monkeypatch,
):

    calls = []

    def fake_remove(self, name):
        calls.append(name)

    monkeypatch.setattr(
        ProfileRepository,
        "remove",
        fake_remove,
    )

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    service.create("government")
    service.remove("government")

    assert calls == ["government"]


def test_remove_missing_profile_raises(tmp_path):

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    with pytest.raises(FileNotFoundError):
        service.remove("government")


def test_remove_preserves_other_profiles(tmp_path):

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    service.create("government")
    service.create("banking")

    service.remove("government")

    assert not (tmp_path / "government").exists()
    assert (tmp_path / "banking").exists()


def test_list_after_remove(tmp_path):

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    service.create("government")
    service.create("banking")

    service.remove("government")

    assert service.list() == ["banking"]


def test_list_delegates_to_repository(
    tmp_path,
    monkeypatch,
):

    calls = []

    def fake_list(self):
        calls.append(True)

        return [
            type(
                "FakeProfile",
                (),
                {"name": "government"},
            )(),
        ]

    monkeypatch.setattr(
        ProfileRepository,
        "list",
        fake_list,
    )

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    result = service.list()

    assert calls == [True]
    assert result == ["government"]

def test_edit_delegates_to_repository(
    tmp_path,
    monkeypatch,
):

    calls = []

    def fake_update(self, name, updates):
        calls.append(
            (name, updates)
        )

    monkeypatch.setattr(
        ProfileRepository,
        "update",
        fake_update,
    )

    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    service.create("government")

    updates = {
        "headline": "Senior Software Engineer",
    }

    service.edit(
        "government",
        updates,
    )

    assert calls == [
        (
            "government",
            updates,
        )
    ]

def test_edit_existing_profile(tmp_path):
    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

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
    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

    with pytest.raises(FileNotFoundError):
        service.edit(
            "government",
            {
                "headline": "Senior Engineer",
            },
        )


def test_edit_preserves_existing_fields(tmp_path):
    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

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
    repo = ProfileRepository(tmp_path)
        
    service = ProfileService(
        repository=repo,
    )

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


def test_service_uses_injected_repository(monkeypatch):
    repository = ProfileRepository()

    service = ProfileService(
        repository=repository,
    )

    assert service.repository is repository


def test_service_create_uses_injected_repository(monkeypatch):
    calls = []

    class FakeRepository:
        def create(self, name):
            calls.append(name)

    repository = FakeRepository()

    service = ProfileService(
        repository=repository,
    )

    service.create("government")

    assert calls == ["government"]


def test_service_can_be_constructed_with_defaults():
    service = ProfileService(
        repository=ProfileRepository(),
    )

    assert service.repository is not None


def test_service_can_be_constructed_without_root():
    service = ProfileService(
        repository=ProfileRepository(),
    )

    assert service.repository is not None