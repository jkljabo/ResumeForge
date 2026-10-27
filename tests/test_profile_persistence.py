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


def test_profile_persists_experience_level(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "experience_level": "Senior",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["experience_level"] == "Senior"


def test_profile_persists_employment_type(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "employment_type": "Full-time",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["employment_type"] == "Full-time"


def test_profile_persists_work_arrangement(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "work_arrangement": "Hybrid",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["work_arrangement"] == "Hybrid"


def test_profile_persists_work_authorization(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "work_authorization": "U.S. Citizen",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["work_authorization"] == "U.S. Citizen"


def test_profile_persists_security_clearance(tmp_path):
    resume = tmp_path / "resume.json"

    persistence = ProfilePersistence()

    original = {
        "name": "Jason Little",
        "headline": "Engineer",
        "security_clearance": "Secret",
    }

    persistence.save(
        resume,
        original,
    )

    loaded = persistence.load(resume)

    assert loaded["security_clearance"] == "Secret"


def test_profile_persistence_serializes_citizenship(tmp_path):
    persistence = ProfilePersistence()

    profile_data = {
        "name": DEFAULT_PROFILE_NAME,
        "headline": "Engineer",
        "citizenship": "United States",
    }

    profile_file = tmp_path / "resume.json"

    persistence.save(
        profile_file,
        profile_data,
    )

    restored = persistence.load(profile_file)

    assert restored["citizenship"] == "United States"


def test_profile_persistence_defaults_missing_citizenship(tmp_path):
    persistence = ProfilePersistence()

    profile_data = {
        "name": DEFAULT_PROFILE_NAME,
        "headline": "Engineer",
    }

    profile_file = tmp_path / "resume.json"

    persistence.save(
        profile_file,
        profile_data,
    )

    restored = persistence.load(profile_file)

    assert restored.get("citizenship") is None


def test_profile_save_restores_residency(tmp_path):
    profile_file = tmp_path / DEFAULT_PROFILE_FILE

    profile_data = {
        "headline": None,
        "full_name": None,
        "color_theme": None,
        "description": None,
        "tags": [],
        "notes": None,
        "category": None,
        "visibility": None,
        "owner": None,
        "organization": None,
        "purpose": None,
        "target_role": None,
        "experience_level": None,
        "employment_type": None,
        "work_arrangement": None,
        "work_authorization": None,
        "security_clearance": None,
        "citizenship": None,
        "residency": "Georgia",
    }

    profile_service = ProfilePersistence()

    profile_service.save(
        profile_file,
        profile_data,
    )

    loaded = profile_service.load(
        profile_file,
    )

    assert loaded["residency"] == "Georgia"


def test_profile_load_without_residency_defaults_none(tmp_path):
    profile_file = tmp_path / DEFAULT_PROFILE_FILE

    profile_data = {
        "headline": None,
        "full_name": None,
        "color_theme": None,
        "description": None,
        "tags": [],
        "notes": None,
        "category": None,
        "visibility": None,
        "owner": None,
        "organization": None,
        "purpose": None,
        "target_role": None,
        "experience_level": None,
        "employment_type": None,
        "work_arrangement": None,
        "work_authorization": None,
        "security_clearance": None,
        "citizenship": None,
    }

    profile_service = ProfilePersistence()

    profile_service.save(
        profile_file,
        profile_data,
    )

    loaded = profile_service.load(
        profile_file,
    )

    assert "residency" not in loaded


def test_profile_save_restores_languages(tmp_path):
    profile_file = tmp_path / DEFAULT_PROFILE_FILE

    profile_data = {
        "headline": None,
        "full_name": None,
        "color_theme": None,
        "description": None,
        "tags": [],
        "notes": None,
        "category": None,
        "visibility": None,
        "owner": None,
        "organization": None,
        "purpose": None,
        "target_role": None,
        "experience_level": None,
        "employment_type": None,
        "work_arrangement": None,
        "work_authorization": None,
        "security_clearance": None,
        "citizenship": None,
        "languages": "English,Spanish",
    }

    profile_service = ProfilePersistence()

    profile_service.save(
        profile_file,
        profile_data,
    )

    loaded = profile_service.load(
        profile_file,
    )

    assert loaded["languages"] == "English,Spanish"


def test_profile_load_without_languages_defaults_none(tmp_path):
    profile_file = tmp_path / DEFAULT_PROFILE_FILE

    profile_data = {
        "headline": None,
        "full_name": None,
        "color_theme": None,
        "description": None,
        "tags": [],
        "notes": None,
        "category": None,
        "visibility": None,
        "owner": None,
        "organization": None,
        "purpose": None,
        "target_role": None,
        "experience_level": None,
        "employment_type": None,
        "work_arrangement": None,
        "work_authorization": None,
        "security_clearance": None,
        "citizenship": None,
    }

    profile_service = ProfilePersistence()

    profile_service.save(
        profile_file,
        profile_data,
    )

    loaded = profile_service.load(
        profile_file,
    )

    assert loaded.get("languages") is None


def test_profile_save_restores_certifications(tmp_path):
    profile_file = tmp_path / DEFAULT_PROFILE_FILE

    profile_data = {
        "headline": None,
        "full_name": None,
        "color_theme": None,
        "description": None,
        "tags": [],
        "notes": None,
        "category": None,
        "visibility": None,
        "owner": None,
        "organization": None,
        "purpose": None,
        "target_role": None,
        "experience_level": None,
        "employment_type": None,
        "work_arrangement": None,
        "work_authorization": None,
        "security_clearance": None,
        "citizenship": None,
        "languages": None,
        "certifications": "AZ-204,AZ-305",
    }

    profile_service = ProfilePersistence()

    profile_service.save(
        profile_file,
        profile_data,
    )

    loaded = profile_service.load(
        profile_file,
    )

    assert loaded["certifications"] == "AZ-204,AZ-305"


def test_profile_load_without_certifications_defaults_none(tmp_path):
    profile_file = tmp_path / DEFAULT_PROFILE_FILE

    profile_data = {
        "headline": None,
        "full_name": None,
        "color_theme": None,
        "description": None,
        "tags": [],
        "notes": None,
        "category": None,
        "visibility": None,
        "owner": None,
        "organization": None,
        "purpose": None,
        "target_role": None,
        "experience_level": None,
        "employment_type": None,
        "work_arrangement": None,
        "work_authorization": None,
        "security_clearance": None,
        "citizenship": None,
        "languages": None,
    }

    profile_service = ProfilePersistence()

    profile_service.save(
        profile_file,
        profile_data,
    )

    loaded = profile_service.load(
        profile_file,
    )

    assert loaded.get("certifications") is None


def test_profile_save_restores_skills(tmp_path):
    profile_file = tmp_path / DEFAULT_PROFILE_FILE

    profile_data = {
        "headline": None,
        "full_name": None,
        "color_theme": None,
        "description": None,
        "tags": [],
        "notes": None,
        "category": None,
        "visibility": None,
        "owner": None,
        "organization": None,
        "purpose": None,
        "target_role": None,
        "experience_level": None,
        "employment_type": None,
        "work_arrangement": None,
        "work_authorization": None,
        "security_clearance": None,
        "citizenship": None,
        "languages": None,
        "skills": "C#,.NET,Azure",
    }

    profile_service = ProfilePersistence()

    profile_service.save(
        profile_file,
        profile_data,
    )

    loaded = profile_service.load(
        profile_file,
    )

    assert loaded["skills"] == "C#,.NET,Azure"


def test_profile_load_without_skills_defaults_none(tmp_path):
    profile_file = tmp_path / DEFAULT_PROFILE_FILE

    profile_data = {
        "headline": None,
        "full_name": None,
        "color_theme": None,
        "description": None,
        "tags": [],
        "notes": None,
        "category": None,
        "visibility": None,
        "owner": None,
        "organization": None,
        "purpose": None,
        "target_role": None,
        "experience_level": None,
        "employment_type": None,
        "work_arrangement": None,
        "work_authorization": None,
        "security_clearance": None,
        "citizenship": None,
        "languages": None,
    }

    profile_service = ProfilePersistence()

    profile_service.save(
        profile_file,
        profile_data,
    )

    loaded = profile_service.load(
        profile_file,
    )

    assert loaded.get("skills") is None


