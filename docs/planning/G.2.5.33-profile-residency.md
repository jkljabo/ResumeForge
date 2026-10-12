# Story: G.2.5.33 – Profile Residency

Status: Complete

Current Phase: Complete

---

## Business Value

Employment eligibility frequently depends on residency independently of citizenship. Recording residency enables ResumeForge to accurately represent candidate information for employers, recruiters, and government organizations while preserving the separation between Citizenship, Residency, and Work Authorization.

---

## Objective

Introduce an optional Profile Residency attribute that may be independently maintained, persisted, edited, and displayed without affecting existing profile compatibility.

---

## Scope

Included:

- Profile model
- Profile persistence
- CLI profile create
- CLI profile edit
- CLI profile show
- Serialization
- Regression tests
- Documentation

---

## Out of Scope

- Multiple residencies
- Visa tracking
- Residency expiration
- Immigration history
- Tax residency
- Country validation

---

## Acceptance Criteria

- Optional residency field exists.
- Existing profiles remain compatible.
- Residency persists correctly.
- CLI supports create/edit/show.
- Regression suite passes.
- Documentation updated.

---

## Technical Design

Add an optional `residency` attribute following the same architectural pattern established for Citizenship.

The implementation will include:

- Profile object
- Persistence layer
- Profile service
- CLI workflow
- CLI display
- Tests

---

## Repository Artifacts

Implementation:

- resumeforge/profiles/profile.py
- resumeforge/workflow.py
- profile persistence components
- CLI command definitions

Tests:

- tests/test_profile.py
- tests/test_profile_persistence.py
- tests/test_cli.py

Documentation:

- CHECKPOINT.md
- docs/history.md
- docs/phases.md
- docs/planning/G.2.5.33-profile-residency.md

---

## Test Strategy

RED

Introduce failing tests covering:

- default residency
- constructor support
- persistence
- backward compatibility
- CLI create
- CLI edit
- CLI display

GREEN

Implement production code until all RED tests pass while maintaining full regression success.

---

## Risks

Low.

This story follows the established implementation pattern successfully used by previous profile metadata stories.

---

## Dependencies

Requires completion of:

- G.2.5.32 – Profile Citizenship

---

## Story Completion Criteria

The story is complete when:

- Acceptance Criteria satisfied
- RED complete
- GREEN complete
- Full regression suite passes
- Documentation synchronized
- Repository successfully closed

---

## Story Status

Status: Repository Closeout

Engineering Status

- Story Planning Complete
- RED Complete
- GREEN Complete
- ResumeForge Engineering Methodology Complete
- Story Signoff Complete
- Repository Closeout In Progress

## Implementation Readiness

Repository implementation is complete.

The repository has entered Repository Closeout.

Remaining work consists of repository synchronization, repository verification, commit preparation, tag preparation, and final release verification.