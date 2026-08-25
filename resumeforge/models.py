"""
Temporary compatibility layer.

This module exists so older imports continue to work while the
codebase is migrated to the new domain package.
"""

from resumeforge.domain import *


# from dataclasses import dataclass


# @dataclass(frozen=True)
# class Header:
#     name: str
#     headline: str
#     tagline: str
#     location: str
#     phone: str
#     email: str
#     linkedin: str
#     github: str
#     portfolio: str


# @dataclass(frozen=True)
# class ResumeProfile:
#     header: Header