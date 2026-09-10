from resumeforge.services.profile_service import ProfileService
from resumeforge.profiles.repository import ProfileRepository
from resumeforge.profiles.repository_protocol import (
    ProfileRepositoryProtocol,
)


def test_repository_implements_protocol():
    repository = ProfileRepository()

    assert isinstance(
        repository,
        ProfileRepositoryProtocol,
    )


def test_service_accepts_protocol_repository():
    repository = ProfileRepository()

    service = ProfileService(
        repository=repository,
    )

    assert service.repository is repository