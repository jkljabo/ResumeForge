from unittest.mock import Mock

import pytest

from resumeforge.configuration.configuration import (
    ApplicationConfiguration,
)
from resumeforge.configuration.configuration_repository import (
    ConfigurationRepository,
)
from resumeforge.configuration.configuration_service import (
    ConfigurationService,
)


def test_get_configuration_returns_repository_configuration():
    configuration = ApplicationConfiguration.default()

    repository = Mock(spec=ConfigurationRepository)
    repository.load.return_value = configuration

    service = ConfigurationService(repository)

    result = service.get_configuration()

    assert result == configuration


def test_get_configuration_calls_repository_once():
    repository = Mock(spec=ConfigurationRepository)
    repository.load.return_value = ApplicationConfiguration.default()

    service = ConfigurationService(repository)

    service.get_configuration()

    repository.load.assert_called_once_with()


def test_save_configuration_calls_repository_once():
    repository = Mock(spec=ConfigurationRepository)

    service = ConfigurationService(repository)

    configuration = ApplicationConfiguration.default()

    service.save_configuration(configuration)

    repository.save.assert_called_once_with(configuration)


def test_save_configuration_passes_configuration_to_repository():
    repository = Mock(spec=ConfigurationRepository)

    service = ConfigurationService(repository)

    configuration = ApplicationConfiguration(
        default_profile="developer",
        default_theme="modern",
        output_directory=ApplicationConfiguration.default().output_directory,
        default_output_filename="resume.docx",
        page_size="A4",
        font_name="Arial",
    )

    service.save_configuration(configuration)

    saved_configuration = repository.save.call_args.args[0]

    assert saved_configuration == configuration


def test_reset_configuration_returns_default_configuration():
    repository = Mock(spec=ConfigurationRepository)

    service = ConfigurationService(repository)

    configuration = service.reset_configuration()

    assert configuration == ApplicationConfiguration.default()


def test_reset_configuration_saves_default_configuration():
    repository = Mock(spec=ConfigurationRepository)

    service = ConfigurationService(repository)

    expected = ApplicationConfiguration.default()

    service.reset_configuration()

    repository.save.assert_called_once_with(expected)


def test_update_default_profile_returns_updated_configuration():
    repository = Mock(spec=ConfigurationRepository)

    original = ApplicationConfiguration.default()

    repository.load.return_value = original

    service = ConfigurationService(repository)

    updated = service.update_default_profile("developer")

    assert updated.default_profile == "developer"
    assert updated.default_theme == original.default_theme
    assert updated.output_directory == original.output_directory
    assert updated.default_output_filename == original.default_output_filename
    assert updated.page_size == original.page_size
    assert updated.font_name == original.font_name

    assert updated is not original


def test_update_default_profile_persists_updated_configuration():
    repository = Mock(spec=ConfigurationRepository)

    original = ApplicationConfiguration.default()

    repository.load.return_value = original

    service = ConfigurationService(repository)

    updated = service.update_default_profile("developer")

    repository.save.assert_called_once_with(updated)


def test_update_configuration_updates_multiple_fields():
    repository = Mock(spec=ConfigurationRepository)

    original = ApplicationConfiguration.default()
    repository.load.return_value = original

    service = ConfigurationService(repository)

    updated = service.update_configuration(
        default_profile="developer",
        default_theme="modern",
    )

    assert updated.default_profile == "developer"
    assert updated.default_theme == "modern"

    assert updated.output_directory == original.output_directory
    assert updated.default_output_filename == original.default_output_filename
    assert updated.page_size == original.page_size
    assert updated.font_name == original.font_name


def test_update_configuration_returns_new_configuration_instance():
    repository = Mock(spec=ConfigurationRepository)

    original = ApplicationConfiguration.default()
    repository.load.return_value = original

    service = ConfigurationService(repository)

    updated = service.update_configuration(
        default_profile="developer",
    )

    assert updated is not original


def test_update_configuration_persists_updated_configuration():
    repository = Mock(spec=ConfigurationRepository)

    original = ApplicationConfiguration.default()
    repository.load.return_value = original

    service = ConfigurationService(repository)

    updated = service.update_configuration(
        default_profile="developer",
    )

    repository.save.assert_called_once_with(updated)


def test_update_configuration_rejects_invalid_theme():
    repository = Mock(spec=ConfigurationRepository)

    repository.load.return_value = (
        ApplicationConfiguration.default()
    )

    service = ConfigurationService(repository)

    with pytest.raises(ValueError):
        service.update_configuration(
            default_theme="banana",
        )

    repository.save.assert_not_called()


def test_update_configuration_rejects_invalid_page_size():
    repository = Mock(spec=ConfigurationRepository)

    repository.load.return_value = (
        ApplicationConfiguration.default()
    )

    service = ConfigurationService(repository)

    with pytest.raises(ValueError):
        service.update_configuration(
            page_size="A0",
        )

    repository.save.assert_not_called()


def test_update_configuration_rejects_empty_default_profile():
    repository = Mock(spec=ConfigurationRepository)

    repository.load.return_value = (
        ApplicationConfiguration.default()
    )

    service = ConfigurationService(repository)

    with pytest.raises(ValueError):
        service.update_configuration(
            default_profile="",
        )

    repository.save.assert_not_called()


def test_update_configuration_does_not_persist_invalid_changes():
    repository = Mock(spec=ConfigurationRepository)

    original = ApplicationConfiguration.default()

    repository.load.return_value = original

    service = ConfigurationService(repository)

    with pytest.raises(ValueError):
        service.update_configuration(
            default_theme="banana",
        )

    repository.save.assert_not_called()

    assert repository.load.return_value is original


def test_update_configuration_accepts_valid_theme():
    repository = Mock(spec=ConfigurationRepository)

    repository.load.return_value = (
        ApplicationConfiguration.default()
    )

    service = ConfigurationService(repository)

    updated = service.update_configuration(
        default_theme="modern",
    )

    assert updated.default_theme == "modern"

    repository.save.assert_called_once_with(updated)


