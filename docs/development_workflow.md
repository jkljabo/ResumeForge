# ResumeForge Development Workflow

## Purpose

This document defines the standard development workflow for ResumeForge. It establishes a consistent process for planning, implementing, testing, reviewing, and signing off on every story.

The goals of this workflow are to:

- Keep implementation cycles short.
- Follow strict Test-Driven Development (TDD).
- Minimize unnecessary refactoring.
- Preserve architectural consistency.
- Ensure documentation remains synchronized with the codebase.
- Produce small, incremental, high-quality changes.

## Development Philosophy

ResumeForge follows an incremental development model.

Each story should:

- Have a single responsibility.
- Be independently testable.
- Be backward compatible.
- Introduce only the functionality required for the current story.
- Avoid unrelated refactoring.
- Leave the project in a fully releasable state.

Whenever possible, stories should remain small enough to complete in a single Planning → RED → GREEN → Signoff cycle.

## Standard Story Workflow

Every story progresses through four phases:

- Story Planning
- Implementation Package (RED)
- Implementation Review (GREEN)
- Story Signoff

## Phase 1 – Story Planning

### Developer (Jason's) Input

```text
Story G.x.x.xx – <new name>

Review: Story Planning

ResumeForge-WIP.zip
```

### ChatGPT (Avery's) Responsibilities

Before making recommendations:

- Review the uploaded ResumeForge-WIP.zip project.
- Establish the current architecture.
- Verify the project's current implementation patterns.

Then:

- Propose the story title.
- Draft the Story Objective.
- Draft the Acceptance Criteria.
- Update the Definition of Ready.
- Identify the expected implementation files.
- Produce the RED Test Plan.
- Estimate the expected regression test count.
- Recommend documentation updates.

### Response Format

When providing story planning feedback, ChatGPT should mirror the formatting used by
the current project documentation (primarily CHECKPOINT.md).

Responses should:

- Preserve existing section names whenever possible.
- Produce content that can be copied directly into the documentation with minimal editing.
- Use the same heading hierarchy.
- Use the same checklist style (`□`, `✓`).
- Use the same bullet style.
- Use fenced code blocks only where the documentation currently uses them.
- Avoid introducing alternate markdown styles unless specifically requested.
- Minimize prose outside of implementation notes.

The objective is to reduce documentation editing and keep every story planning cycle
consistent with the repository's established format.

Planning should produce a nearly complete story package requiring only minor edits before approval.

### Developer (Jason's) Responsibilities

- Update project documentation.
- Verify story scope.
- Submit the planning package for signoff.

### Exit Criteria

Planning is complete when:

- Story title is finalized.
- Story objective is approved.
- Acceptance criteria are complete.
- Definition of Ready is satisfied.
- Expected files are identified.
- RED Test Plan is documented.
- Expected regression test count is recorded.

## Phase 2 – Implementation Package (RED)

### Developer (Jason's) Input

```text
Review: Implementation Package (RED)

ResumeForge-WIP.zip
```

### ChatGPT (Avery's) Responsibilities

- Review the uploaded ResumeForge-WIP.zip before making recommendations.
- Write only the tests necessary to drive the new behavior.
- Follow existing project testing patterns.
- Avoid implementation guidance until RED is complete.

### Developer (Jason's) Responsibilities

- Add the RED tests.
- Execute the targeted test suites.
- Submit the failing results.

### Exit Criteria

RED is complete when:

- Only the newly added tests fail.
- Existing regression tests continue to pass.
- Failures clearly identify the missing functionality.

## Phase 3 – Implementation Review (GREEN)

### Developer (Jason's) Input

```text
Review: Implementation Review (GREEN)

ResumeForge-WIP.zip
```

### ChatGPT (Avery's) Responsibilities

- Review the uploaded ResumeForge-WIP.zip before making recommendations.
- Verify the implementation against the RED tests.
- Recommend only the minimum implementation required.
- Preserve the existing architecture.
- Avoid introducing unnecessary abstractions or refactoring.

### Developer (Jason's) Responsibilities

- Implement the required functionality.
- Execute targeted tests.
- Execute the full regression suite.

### Exit Criteria

GREEN is complete when:

- All new tests pass.
- Full regression suite passes.
- Acceptance criteria are satisfied.
- No unnecessary code changes were introduced.

## Phase 4 – Story Signoff

### Developer (Jason's) Input

```text
Review: Story Signoff

ResumeForge-WIP.zip
```

### ChatGPT (Avery's) Responsibilities

Review:

- Implementation
- Architecture
- Documentation
- Test results
- Acceptance Criteria

Verify:

- Documentation updates
- Regression test count
- Backward compatibility
- Project consistency

Provide:

- Final approval
- Commit commands
- Tag commands (when appropriate)

### Developer (Jason's) Responsibilities

Execute:

```bash
python -m pytest -q
git add .
git commit -m "Complete Story G.x.x.xx - <Story Name>"
git push origin main
git tag -a v0.x.xx -m "Story G.x.x.xx - <Story Name>"
git push origin v0.x.xx
```

### Exit Criteria

A story is complete when:

- Full regression suite passes.
- Documentation is synchronized.
- Repository is committed.
- Repository is pushed.
- Version tag is created.
- Version tag is pushed.
- Story receives final signoff.

## Architecture Review Requirements

Every review begins by verifying the current project state.

The uploaded WIP is considered the authoritative source.

Before making recommendations, review the current implementation of:

- CHECKPOINT.md
- README.md
- docs/history.md
- docs/testing.md
- Files affected by the current story
- Relevant tests

Recommendations should always follow the verified architecture rather than assumptions from previous stories.

## Story Design Guidelines

Stories should:

- Remain small.
- Have a single responsibility.
- Be independently testable.
- Maintain backward compatibility.
- Reuse existing architectural patterns.
- Avoid introducing unrelated features.

Whenever possible, stories should require:

- 2–5 implementation edits
- 3–5 new tests
- One RED cycle
- One GREEN cycle
- One Signoff cycle

## Test-Driven Development

ResumeForge follows strict Test-Driven Development.

Every story progresses through:

```text
Planning
    ↓
RED
    ↓
GREEN
    ↓
Regression
    ↓
Signoff
```

Implementation should never precede the RED tests.

## Continuous Documentation

Each completed story updates project documentation.

Typical updates include:

- CHECKPOINT.md
- README.md
- docs/history.md
- docs/testing.md

Documentation should always reflect the current implementation and regression test count.

## Lessons Learned

The following practices have consistently reduced development cycle time.

### Review the Current Architecture

Always review the uploaded ResumeForge-WIP.zip before making recommendations.

The current implementation is authoritative.

Do not assume the architecture based on previous stories.

### Extend Existing Patterns

Prefer extending existing code over introducing new patterns.

Examples include:

- Dataclasses
- Existing workflow update patterns
- Existing test structure
- Existing service interfaces

### Keep Stories Small

Small stories produce:

- Faster reviews
- Simpler implementations
- Easier testing
- Lower regression risk

### Minimize Implementation

During GREEN, implement only the functionality required to satisfy the RED tests.

Avoid unrelated improvements.

### Keep Reviews Focused

Each review should focus only on the current phase.

- Planning reviews should not discuss GREEN implementation.
- RED reviews should focus on failing tests.
- GREEN reviews should focus on the minimal implementation.
- Signoff reviews should verify completion and consistency.

## Guiding Principle

> Build the smallest possible change that satisfies the current story, preserves the verified architecture, maintains backward compatibility, keeps documentation synchronized, and leaves the project in a releasable state.

## AI Collaboration Guidelines

To minimize development cycle time:

- ChatGPT reviews the uploaded WIP before making recommendations.
- The uploaded ResumeForge-WIP.zip is the authoritative source for implementation decisions.
- Story Planning begins by proposing the next story when "<new name>" is provided.
- Planning should produce a nearly complete story package.
- RED produces only failing tests.
- GREEN produces only the minimum implementation required.
- Signoff verifies implementation and documentation only.
- Recommendations should follow existing project patterns unless the story explicitly changes them.
- Planning, RED, GREEN, and Signoff responses should mirror the formatting
  used by CHECKPOINT.md whenever practical so content can be copied into
  project documentation with minimal editing.
- Review the current WIP ZIP before proposing implementation changes.
- Prefer extending existing implementation patterns over introducing new abstractions.
- Verify that new tests follow the conventions already established in the surrounding test file.
  
## Continuous Improvement

This workflow is a living document.

As new lessons are learned during development, the workflow should be updated to capture improvements that reduce development cycle time, improve code quality, or strengthen project consistency.

Process improvements should be treated with the same discipline as software improvements: review them, document them, and adopt them consistently.