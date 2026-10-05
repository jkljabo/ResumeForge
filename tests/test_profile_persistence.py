import json

from resumeforge.constants import DEFAULT_PROFILE_FILE, DEFAULT_PROFILE_NAME
from resumeforge.profiles.persistence import (
    ProfilePersistence,
)
from resumeforge.profiles.profile import Profile


def test_load_returns_dictionary(tmp_path):
    resume = tmp_path / "resume.json"

    resume.write_text(
        json.dumps(
            {
                "name": "Jason Little",
                "headline": "Engineer",
            }
        ),
        encoding="utf-8",
    )

    persistence = ProfilePersistence()

    result = persistence.load(resume)

    assert result == {
        "name": "Jason Little",
        "headline": "Engineer",
    }


def test_save_writes_json(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    persistence.save(
        resume,
        {
            "name": "Jason Little",
            "headline": "Engineer",
        },
    )

    data = json.loads(
        resume.read_text(
            encoding="utf-8",
        )
    )

    assert data == {
        "name": "Jason Little",
        "headline": "Engineer",
    }


def test_round_trip(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Senior Engineer",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(
        resume,
    )

    assert loaded == original


def test_unicode_round_trip(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "José García",
        "headline": "Développeur",
        "city": "München",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(
        resume,
    )

    assert loaded == original


def test_round_trip_preserves_color_theme(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "color_theme": "blue",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["color_theme"] == "blue"


def test_round_trip_preserves_description(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "description": "CDC Resume",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["description"] == "CDC Resume"


def test_round_trip_preserves_tags(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "tags": "cdc,federal",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["tags"] == "cdc,federal"


def test_profile_persistence_preserves_notes(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "notes": "Primary resume for CDC applications.",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["notes"] == "Primary resume for CDC applications."


def test_profile_persistence_preserves_category(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "category": "Government",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["category"] == "Government"


def test_profile_persistence_preserves_visibility(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "visibility": "Private",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["visibility"] == "Private"


def test_profile_persistence_preserves_owner(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "owner": "Jason Little",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["owner"] == "Jason Little"


def test_profile_persists_organization(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "organization": "OpenAI",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["organization"] == "OpenAI"


def test_profile_persists_purpose(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "purpose": "Federal Applications",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["purpose"] == "Federal Applications"


def test_profile_persists_target_role(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "target_role": "Senior Software Engineer",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["target_role"] == "Senior Software Engineer"


