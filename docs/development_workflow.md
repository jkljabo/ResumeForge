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

## Scope

This document defines the required workflow for every ResumeForge story.

It governs:

• Story Planning
• RED implementation
• GREEN implementation
• Story Signoff

Project architecture, coding standards, and feature requirements are documented elsewhere.

## Development Philosophy

Story Planning
      ↓
     RED
      ↓
 GREEN Review
      ↓
Full Regression
      ↓
Story Signoff

ResumeForge follows an incremental development model.

Each story should:

- Have a single responsibility.
- Be independently testable.
- Be backward compatible.
- Introduce only the functionality required for the current story.
- Avoid unrelated refactoring.
- Leave the project in a fully releasable state.

Whenever possible, stories should remain small enough to complete in a single Planning → RED → GREEN → Signoff cycle.

## Source of Truth

Every review is based on the uploaded ResumeForge-WIP.zip.

Recommendations must never rely solely on previous conversations or memory.

Project verification always precedes recommendations.

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
- Base all recommendations on the uploaded ResumeForge-WIP.zip rather than prior implementation assumptions.

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
- Produce content that can be copied directly into CHECKPOINT.md with minimal or no editing.
- Use the same heading hierarchy.
- Use the same checklist style (`□`, `✓`).
- Use the same bullet style.
- Use fenced code blocks only where the documentation currently uses them.
- Avoid introducing alternate markdown styles unless specifically requested.
- Minimize prose outside of implementation notes.

The objective is to reduce documentation editing and keep every story planning cycle
consistent with the repository's established format.

Planning should produce a nearly complete story package requiring only minor edits before approval.

The objective is for the resulting story package to be immediately usable with minimal editing.

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
- Documentation updates required by the story have been identified.

### Story Scope Verification

Recommendations should be limited to the approved story.

Do not introduce:

- Future stories
- Nice-to-have features
- Architectural redesigns
- Opportunistic refactoring

Unless explicitly requested by the developer.

## Phase 2 – Implementation Package (RED)

### Developer (Jason's) Input

```text
Review: Implementation Package (RED)

ResumeForge-WIP.zip
```

### ChatGPT (Avery's) Responsibilities

- Review the uploaded ResumeForge-WIP.zip immediately before every review.
    Do not rely on knowledge from previous uploads, previous stories, or earlier conversations if it conflicts with the current project state.

- Write only the tests necessary to drive the new behavior.
- Follow existing project testing patterns.
- Avoid implementation guidance until RED is complete.
- Focus review feedback on the failing tests presented by the developer. Do not speculate about unrelated implementation details.
- Base all recommendations on the uploaded ResumeForge-WIP.zip rather than prior implementation assumptions.

### Required RED Deliverables

Every RED review shall produce a complete RED implementation package.

The package shall contain only failing tests and shall not include production
implementation guidance.

The RED package shall include:

1. Project Audit Summary

   Confirm the documentation, source files, and tests reviewed from the
   uploaded ResumeForge-WIP.zip.

2. Existing Reference

   Identify the current file(s) and exact location where new tests should be
   added.

3. Suggested Test Updates

   For every affected test file provide:

   - Current location
   - Exact insertion point
   - Complete test code
   - Supporting explanation (when needed)

   Tests shall be complete and ready to paste into the project.

4. Expected RED Results

   Identify the expected failing tests and explain why each failure is expected.

No production code or implementation recommendations shall be included during
RED.

### RED Completion Confirmation

Once the developer has executed the RED tests and submitted the failing
results, ChatGPT shall perform a RED Confirmation Review.

The purpose of this review is to verify that:

- every newly added RED test fails only because the feature has not yet
  been implemented;
- no unrelated regressions have been introduced;
- the failures correspond exactly to the approved story scope.

Only after ChatGPT explicitly confirms the RED failures may the workflow
advance to GREEN.

GREEN implementation shall never begin automatically after RED test
creation alone.

### Developer (Jason's) Responsibilities

- Add the RED tests.
- Execute the targeted test suites.
- Submit the failing results.

### Exit Criteria

RED is complete only when:

- Complete RED tests have been produced.
- Every affected test file has been identified.
- Exact insertion locations have been documented.
- Only the newly added tests fail.
- Existing regression tests continue to pass.
- The developer has executed the RED tests.
- ChatGPT has reviewed the failing results.
- The failures are confirmed to represent only the missing functionality.

GREEN shall not begin until all RED Exit Criteria have been satisfied.

Implementation recommendations should explain how each failing test is expected to transition to passing.

Recommendations should remain traceable to the RED failures.

## Phase 3 – Implementation Review (GREEN)

### Developer (Jason's) Input

```text
Review: Implementation Review (GREEN)

ResumeForge-WIP.zip
```

### ChatGPT (Avery's) Responsibilities

- Review the uploaded ResumeForge-WIP.zip immediately before every review.
    Do not rely on knowledge from previous uploads, previous stories, or earlier conversations if it conflicts with the current project state.

- Verify the implementation against the RED tests.
- Recommend only the minimum implementation required.
- Preserve the existing architecture.
- Avoid introducing unnecessary abstractions or refactoring.
- Base all recommendations on the uploaded ResumeForge-WIP.zip rather than prior implementation assumptions.

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
- The implementation shall remain limited to the scope established by the approved RED tests.

### Required GREEN Deliverables

Every GREEN review shall begin with a Project Audit Summary.

The implementation package shall contain:

1. Existing Reference

   Show the verified current implementation.

2. Suggested Update

   Show the exact production code required.

3. Implementation Rationale

   Explain how the implementation satisfies the RED tests.

4. Scope Verification

   Confirm that only the functionality required by the RED tests is being
   implemented.

GREEN shall never introduce functionality beyond the approved story scope.

## GREEN Entry Criteria

### GREEN Implementation Package

When GREEN begins, ChatGPT shall provide a complete implementation package.

The package shall include:

1. Existing Reference

   Verified current implementation.

2. Suggested Update

   Complete replacement or insertion code.

3. Exact Location

   File name and insertion location.

4. Explanation

   Why each modification satisfies one or more RED tests.

Recommendations should be complete enough to paste directly into the
project.

GREEN reviews should not require the developer to infer missing
implementation.

GREEN begins only after RED has been completed.

Specifically:

- RED tests have been delivered.
- RED tests have been executed.
- Expected failures have been confirmed.
- ChatGPT has reviewed the RED failures.
- The implementation is traceable to those failures.

If RED confirmation has not occurred, GREEN shall not begin.

## Phase 4 – Story Signoff

### Documentation Synchronization

Verify:

□ CHECKPOINT.md
□ docs/history.md
□ docs/phases.md
□ docs/testing.md
□ docs/development.md
□ docs/development_workflow.md (if workflow improvements were discovered)

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

Confirm that Planning, RED, and GREEN phase deliverables were completed before approving final signoff.

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

If the current project differs from previous stories, the current project always takes precedence.

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

## Regression

- Implementation should never precede the RED tests.

- Before recommending implementation changes, review nearby source code to
identify recently completed stories that may be affected.

- Recommendations should preserve behavior introduced by previous completed
stories unless the current story explicitly changes that behavior.

- Regression review should verify that new implementation extends existing
behavior rather than unintentionally replacing it.

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

Before every Planning, RED, GREEN, or Signoff review, perform a complete
project audit of the uploaded ResumeForge-WIP.zip.

The uploaded WIP ZIP is the authoritative source for all documentation,
architecture, implementation, naming conventions, and test patterns.

The review shall include verification of:

- Project documentation
- Current story documentation
- Existing implementation
- Existing unit tests
- Existing architectural patterns
- Existing naming conventions
- Existing CLI behavior
- Existing persistence behavior

Recommendations shall be based only on verified project content.

Do not rely on memory from previous stories.
Do not assume architecture.
Verify first, then recommend.

### Project Audit Checklist

Every review begins with a project audit.

The audit should verify:

✓ development_workflow.md
✓ CHECKPOINT.md
✓ README.md
✓ docs/history.md
✓ docs/testing.md
✓ Current story documentation
✓ Related source files
✓ Related unit tests
✓ Previous completed story (for regression context)
✓ Existing implementation patterns
✓ Existing CLI options
✓ Existing persistence implementation
✓ Existing service update patterns

The audit should be completed before producing recommendations.

### Recommendation Format

Whenever practical, recommendations should identify both the current
implementation and the proposed update.

Preferred format:

Verified Current

Provide the verified implementation exactly as it exists in the uploaded WIP.

Suggested Update

Provide the complete replacement or insertion.

Location

Identify the file and approximate insertion point.

Rationale

### Complete Responses

Whenever ChatGPT recommends source code or tests, the response shall be
complete.

Avoid responses such as:

- "Add something similar to..."
- "Update this section..."
- "If your project contains..."
- "Looks like..."
- "You probably have..."

Instead provide:

- verified current implementation;
- exact insertion point;
- complete replacement code;
- explanation of the change.

The objective is to eliminate follow-up clarification before coding begins.

Explain why the change is required for the current story.

Every implementation recommendation should be traceable to verified project
content.

Recommendations should be derived from verified project content rather than
memory or assumptions.

### Phase Deliverables Matter

Each review phase produces a different deliverable.

Planning
    Documentation

RED
    Complete failing tests

GREEN
    Production implementation

Signoff
    Verification and approval

Advancing to the next phase without completing the current phase introduces
avoidable review cycles.

ChatGPT should never assume a phase has been completed unless the developer's
submitted results confirm completion.

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

- Planning reviews shall produce planning documentation only.
- RED reviews shall produce complete failing tests only.
- GREEN reviews shall produce production implementation only.
- Signoff reviews shall verify implementation, documentation, regression results, and story completion only.
- A review shall not skip phases or combine RED and GREEN deliverables unless explicitly requested by the developer.

## Guiding Principle

> Build the smallest possible change that satisfies the current story, preserves the verified architecture, maintains backward compatibility, keeps documentation synchronized, and leaves the project in a releasable state.

## AI Collaboration Guidelines

To minimize development cycle time:

- ChatGPT shall complete the Project Audit Checklist before making any recommendations.
- The uploaded ResumeForge-WIP.zip is the authoritative source for all
  documentation and implementation decisions. Review it immediately before
  every Planning, RED, GREEN, or Signoff review. Do not rely on previous
  stories or memory when the current project can be verified.

### Verification Before Recommendation

Never assume:

- class names
- service names
- repository names
- workflow names
- CLI options
- persistence implementations
- documentation structure
- helper utilities
- existing architecture

Every reference included in a recommendation must be verified from the
uploaded ResumeForge-WIP.zip.

Verification extends beyond class names.

ChatGPT shall verify:

- constructor signatures;
- helper methods;
- persistence classes;
- workflow methods;
- CLI argument handling;
- dataclass fields;
- service update patterns;
- repository APIs.

If a recommendation references a symbol that cannot be found in the
uploaded project, the recommendation shall be corrected before being
returned.

Inventing project members is considered a workflow failure.

If a detail cannot be verified, explicitly state that it could not be
verified rather than making an assumption.

- Story Planning begins by proposing the next story when "<new name>" is provided.
- Planning should produce a nearly complete story package.
- RED produces only failing tests.
- GREEN produces only the minimum implementation required.
- Signoff verifies implementation and documentation only.
- Recommendations should follow existing project patterns unless the story explicitly changes them.
- Planning, RED, GREEN, and Signoff responses should mirror the formatting
  used by CHECKPOINT.md whenever practical so content can be copied into
  project documentation with minimal editing.
- Prefer extending existing implementation patterns over introducing new abstractions.
- Verify that new tests follow the conventions already established in the surrounding test file.
- Planning responses shall mirror the current CHECKPOINT.md structure and markdown conventions   exactly. New headings, checklist styles, or formatting conventions should not be introduced unless the repository documentation has first adopted them.
- Implementation (RED/GREEN) reviews must never introduce new classes, services, repositories, or abstractions that are not present in the current WIP unless the story explicitly calls for them. All recommendations must be derived from the uploaded codebase.
- Every review should begin with a brief Project Audit Summary confirming the
  documentation, source files, and tests that were reviewed.
- ChatGPT shall never infer that a previous phase has been completed.
- Completion of a phase is confirmed only by the developer's submitted review results.
- When uncertainty exists, remain in the current phase rather than advancing to the next one.
- Recommendations must reference existing implementation patterns whenever
  practical. New patterns should not be introduced unless required by the
  current story.
- If an implementation detail cannot be verified from the uploaded project,
  explicitly state that it could not be verified rather than making an
  assumption.
- References to project classes, services, repositories, workflows,
  commands, or architecture must originate from the verified project.
  Do not invent or substitute names based on memory or common patterns.
- Planning reviews shall produce documentation updates only.
  Implementation details should not be discussed beyond identifying the
  expected architectural impact.
- When suggesting code changes, prefer modifying existing files and extending
existing implementations over introducing new files.
- Creation of new source files should occur only when explicitly required by
the approved story.
  
## Workflow Integrity

The workflow itself is considered part of the project's architecture.

Maintaining strict phase boundaries is as important as maintaining code quality.

Each phase should produce a complete, reviewable deliverable before advancing
to the next phase.

Phase progression is developer-controlled.

ChatGPT shall never infer that the next phase should begin.

Progression occurs only after the developer explicitly requests the next
review phase.

Examples:

Story Planning
    ↓
Developer requests RED

RED
    ↓
Developer submits failing tests
    ↓
RED Confirmation
    ↓
Developer requests GREEN

GREEN
    ↓
Developer submits passing tests
    ↓
GREEN Review
    ↓
Developer requests Signoff

## Developer Experience Goals

The workflow is designed to minimize development cycle time.

Every review should strive to eliminate unnecessary iterations by:

- providing complete copy/paste-ready code;
- identifying exact file locations;
- referencing verified project content;
- avoiding assumptions;
- avoiding placeholder guidance;
- minimizing follow-up questions.

A successful review should allow the developer to implement the
recommendations immediately without needing clarification.

## Continuous Improvement

This workflow is a living document.

As new lessons are learned during development, the workflow should be updated to capture improvements that reduce development cycle time, improve code quality, or strengthen project consistency.

Process improvements should be treated with the same discipline as software improvements: review them, document them, and adopt them consistently.

A successful review is one in which the developer can implement the
recommendations without first correcting assumptions about the current
project.

Recommendations should be immediately actionable, traceable to the verified
implementation, and require little or no clarification before development
continues.

Workflow improvements identified during Story Signoff should be incorporated before the story is closed whenever practical.

Incremental refinement is preferred over infrequent large revisions.

## Review Warm-Up

Every review should follow this sequence.

Planning
    ↓
Open ResumeForge-WIP.zip
    ↓
Review documentation
    ↓
Review related source
    ↓
Review related tests
    ↓
Verify architecture
    ↓
Produce recommendations

RED
    ↓
Audit
    ↓
Write failing tests only

GREEN
    ↓
Audit
    ↓
Implement minimum code required

Signoff
    ↓
Audit
    ↓
Verify implementation
    ↓
Verify documentation
    ↓
Verify regression tests

Story Planning Checklist
☐ Documentation reviewed
☐ Existing implementation reviewed
☐ Existing tests reviewed
☐ Story scope confirmed
☐ Existing patterns identified

RED Checklist
☐ Audit complete
☐ Existing tests reviewed
☐ New failing tests complete
☐ No implementation provided
☐ Await developer confirmation

GREEN Checklist
☐ Audit complete
☐ Minimal implementation
☐ Existing patterns followed
☐ Passing story tests
☐ Full regression passes

Story Signoff Checklist
☐ Documentation reviewed
☐ Source reviewed
☐ Tests reviewed
☐ Regression suite passed
☐ Git commit
☐ Git push
☐ Tag created
☐ Story complete

A story is considered complete only when:
✓ Implementation is complete
✓ Tests pass
✓ Documentation is synchronized
✓ Story review is approved

### Project Audit Summary

Every review shall begin with a concise Project Audit Summary before any recommendations are made.

Recommended format:

Project Audit Summary

Documentation Reviewed

✓ development_workflow.md
✓ CHECKPOINT.md
✓ README.md
✓ docs/history.md
✓ docs/testing.md

Implementation Reviewed

✓ Related source files
✓ Related unit tests
✓ Existing implementation patterns

Verification Status

Recommendations below are based solely on the uploaded
ResumeForge-WIP.zip.

Every referenced:

- class
- method
- dataclass field
- helper
- CLI option
- persistence API
- workflow
- documentation section

has been verified before inclusion.

If verification was not possible, the recommendation shall explicitly
state that fact rather than making an assumption.

Verification Confidence

□ Complete

□ Partial

If Partial, recommendations shall be limited to only those areas that could be verified.

## Definition of Success

A review is considered successful when:

- no project symbols were assumed;
- no implementation details were invented;
- recommendations are traceable to the uploaded project;
- responses are complete rather than partial;
- the developer can paste the recommendations directly into the project;
- no additional clarification is required before implementation.

The objective is to reduce development cycles by maximizing accuracy,
verification, and completeness during every review.