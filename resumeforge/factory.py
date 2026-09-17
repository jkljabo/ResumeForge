from resumeforge.generator import ResumeGenerator
from resumeforge.output.factory import (
    create_exporter,
    create_writer,
)
from resumeforge.resume.factory import create_builder
from resumeforge.scoring.factory import create_matcher
from resumeforge.tailoring.factory import create_tailoring_engine
from resumeforge.profiles.repository import ProfileRepository
from resumeforge.services.profile_service import ProfileService
from resumeforge.recommendations.engine import RecommendationEngine


def create_resume_generator() -> ResumeGenerator:
    return ResumeGenerator(
        matcher=create_matcher(),
        recommendation_engine=RecommendationEngine(),
        tailoring_engine=create_tailoring_engine(),
        builder=create_builder(),
        exporter=create_exporter(),
        writer=create_writer(),
    )

def create_profile_service() -> ProfileService:
    repository = ProfileRepository()
    return ProfileService(repository=repository)

def create_profile_repository() -> ProfileRepository:
    return ProfileRepository()