import json

import pytest

from resumeforge.configuration.configuration import (
    ApplicationConfiguration,)
from resumeforge.configuration.configuration_repository import (
    ConfigurationRepositoryError,
)
from resumeforge.configuration.json_configuration_repository import (
    JsonConfigurationRepository,
)


def test_load_returns_default_when_configuration_is_missing(tmp_path):
    repository = JsonConfigurationRepository(
        tmp_path / "settings.json"
    )

    configuration = repository.load()

    assert configuration == ApplicationConfiguration.default()


def test_save_creates_configuration_file(tmp_path):
    repository = JsonConfigurationRepository(
        tmp_path / "settings.json"
    )

    configuration = ApplicationConfiguration.default()

    repository.save(configuration)

    assert (tmp_path / "settings.json").exists()


def test_round_trip_configuration(tmp_path):
    repository = JsonConfigurationRepository(
        tmp_path / "settings.json"
    )

    original = ApplicationConfiguration.default()

    repository.save(original)

    loaded = repository.load()

    assert loaded == original


def test_round_trip_custom_configuration(tmp_path):
    configuration = ApplicationConfiguration(
        default_profile="developer",
        default_theme="modern",
        output_directory=tmp_path / "output",
        default_output_filename="resume.docx",
        page_size="A4",
        font_name="Arial",
    )

    repository = JsonConfigurationRepository(
        tmp_path / "settings.json"
    )

    repository.save(configuration)

    loaded = repository.load()

    assert loaded == configuration


def test_load_invalid_json_raises_repository_error(tmp_path):
    """Loading malformed JSON should raise a repository error."""

    configuration_path = tmp_path / "settings.json"

    configuration_path.write_text(
        "{",
        encoding="utf-8",
    )

    repository = JsonConfigurationRepository(configuration_path)

    with pytest.raises(ConfigurationRepositoryError):
        repository.load()


def test_load_missing_required_field_raises_repository_error(tmp_path):
    """Loading an incomplete configuration should raise a repository error."""

    configuration_path = tmp_path / "settings.json"

    configuration_path.write_text(
        json.dumps(
            {
                "default_profile": "resume",
            }
        ),
        encoding="utf-8",
    )

    repository = JsonConfigurationRepository(configuration_path)

    with pytest.raises(ConfigurationRepositoryError):
        repository.load()


def test_load_invalid_output_directory_type_raises_repository_error(tmp_path):
    """Loading a configuration with an invalid output directory should raise a repository error."""

    configuration_path = tmp_path / "settings.json"

    configuration_path.write_text(
        json.dumps(
            {
                "default_profile": "resume",
                "default_theme": "executive",
                "output_directory": 123,
                "default_output_filename": "resume.docx",
                "page_size": "LETTER",
                "font_name": "Calibri",
            }
        ),
        encoding="utf-8",
    )

    repository = JsonConfigurationRepository(configuration_path)

    with pytest.raises(ConfigurationRepositoryError):
        repository.load()


def test_load_empty_configuration_file_raises_repository_error(tmp_path):
    """Loading an empty configuration file should raise a repository error."""

    configuration_path = tmp_path / "settings.json"

    configuration_path.write_text(
        "",
        encoding="utf-8",
    )

    repository = JsonConfigurationRepository(configuration_path)

    with pytest.raises(ConfigurationRepositoryError):
        repository.load()