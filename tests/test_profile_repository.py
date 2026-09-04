from resumeforge.profiles import ProfileRepository


def test_repository_discovers_default_profile():
    repository = ProfileRepository()

    profiles = repository.list_profiles()

    assert len(profiles) == 1


def test_default_profile_name():
    repository = ProfileRepository()

    profile = repository.list_profiles()[0]

    assert profile.name == "software_engineer"


def test_default_profile_exists():
    repository = ProfileRepository()

    profile = repository.list_profiles()[0]

    assert profile.path.exists()


def test_default_profile_is_resume_json():
    repository = ProfileRepository()

    profile = repository.list_profiles()[0]

    assert profile.path.name == "resume.json"