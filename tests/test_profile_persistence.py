import json

from resumeforge.profiles.persistence import (
    ProfilePersistence,
)


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