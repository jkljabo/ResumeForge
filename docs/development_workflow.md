# ResumeForge Development Workflow

## Purpose

This document defines the standard development workflow for ResumeForge. It establishes a consistent process for planning, implementing, verifying, documenting, and signing off on every story.

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
• Implementation Package (RED)
• RED Verification
• Implementation Package (GREEN)
• GREEN Verification
• Story Signoff

Project architecture, coding standards, and feature requirements are documented elsewhere.

## Development Philosophy

Story Planning
      ↓
Implementation Package (RED)
      ↓
RED Verification
      ↓
Implementation Package (GREEN)
      ↓
GREEN Verification
      ↓
Story Signoff

Engineering Contract

ResumeForge follows strict Test-Driven Development (TDD).

Each workflow phase must produce a verifiable engineering artifact before the
next phase may begin.

Story Planning produces the complete Story Planning Package.

The Story Planning Package is the engineering specification for the entire
story.

Story Planning shall establish the baseline against which every subsequent
workflow phase is verified.

Implementation Package (RED), Implementation Package (GREEN), GREEN
Verification, and Story Signoff shall validate conformance to the approved
Story Planning Package rather than redefining story requirements.

It shall contain every piece of information required to complete all remaining
workflow phases without introducing assumptions.

At a minimum, the Story Planning Package shall define:

• Story objective
• Business purpose
• Scope
• Acceptance criteria
• Files expected to change
• RED test suite
• Expected RED failures
• GREEN implementation plan
• Regression expectations
• Documentation updates
• Story completion criteria

Testing Planning Package

Story Planning shall define the complete testing strategy.

The testing plan shall include:

• new unit tests
• modified unit tests
• persistence tests
• CLI tests
• regression expectations
• expected test count increase

Each planned test shall be identified by name whenever practical.

Each planned test shall identify the existing test family it extends.

Story Planning shall verify that new tests follow the established testing
pattern already present within the corresponding test file.

If no established pattern exists, Story Planning shall explicitly document the
reason a new testing pattern is being introduced.

Testing shall distinguish between:

• tests expected to fail because implementation is missing
• tests expected to pass because existing architecture already satisfies the
  requirement

Both outcomes shall be documented during Story Planning.

Implementation Package (RED) implements this approved testing plan.

Later workflow phases shall not determine additional testing requirements
unless Story Planning is formally reopened.

No later workflow phase shall be required to determine missing story
requirements.

Every workflow phase shall produce objective evidence supporting its conclusions.

Review conclusions shall be traceable to the current ResumeForge-WIP Source Authority.

General statements such as:

• "Looks correct"
• "Documentation appears synchronized"
• "Implementation follows the pattern"

are insufficient unless accompanied by evidence derived from the current Source Authority.

Evidence shall identify:

• artifact reviewed
• location reviewed
• observation
• conclusion

Source Authority Verification

Every workflow phase shall begin by validating the current ResumeForge-WIP
Source Authority.

Source Authority validation shall confirm:

• current ResumeForge-WIP reviewed
• CHECKPOINT.md reviewed
• current workflow phase confirmed
• current story confirmed

Recommendations shall be based on the current ResumeForge-WIP Source Authority.

Conversational memory shall never replace current project review.

If the current ResumeForge-WIP Source Authority cannot support a recommendation,
ChatGPT (Avery's) shall explicitly report that verification could not be completed.

Review Evidence Checklist

Every workflow review shall explicitly identify the evidence reviewed before
producing recommendations.

At a minimum, ChatGPT (Avery's) shall confirm review of:

• ResumeForge-WIP Source Authority
• CHECKPOINT.md
• current story documentation
• relevant implementation files
• relevant test files
• affected project documentation

If any required artifact was not reviewed, ChatGPT (Avery's) shall explicitly state
that limitation before making recommendations.

ChatGPT (Avery) is the development lead for the Story Planning phase and is
responsible for producing the complete planning package from the current
ResumeForge-WIP Source Authority.

The developer (Jason) reviews, challenges, approves, and applies the planning
package to the project documentation.

During Story Planning, ChatGPT (Avery) is responsible for leading story
definition.

This responsibility includes producing:

• Complete implementation strategy
• Complete RED testing strategy
• Complete GREEN implementation strategy
• Complete documentation update package

The developer shall never be required to infer missing implementation details
during any later workflow phase.

If a workflow phase identifies a missing functional requirement,
documentation requirement, acceptance criterion, or implementation scope,
the workflow shall pause.

The missing requirement shall be incorporated into Story Planning and
approved before subsequent workflow phases continue.

Later workflow phases shall not independently expand the approved Story
Planning Package.

Story Planning is therefore not limited to reviewing a story that has already
been fully defined elsewhere.

When the story definition is incomplete, ChatGPT (Avery) shall complete the
story definition during Story Planning using the current project architecture,
existing implementation patterns, project roadmap, established story
sequence, and documented scope.

Documentation Contract

Story Planning establishes the documentation authority for the active story.

Every affected project document shall be reviewed before Story Planning may be
approved.

Documentation review shall be exhaustive.

ChatGPT (Avery's) shall inspect every project document that could reasonably be
affected by the approved story, regardless of whether changes are ultimately
required.

A document shall never be omitted because changes appear unlikely or minor.

If a document requires no modifications, that conclusion shall result from an
explicit review of the current document rather than assumption.

For each document, ChatGPT shall provide:

For implementation-related documentation, recommendations shall also identify:

• existing implementation pattern
• related implementation pattern (if applicable)
• justification for any deviation from existing patterns

Document

Location

Current

Suggested

Reason for change

Location shall identify the exact heading, section, subsection, table,
example, or command being reviewed.

General locations such as:

"README"

"Later in the document"

"Documentation examples"

or similar descriptions are not acceptable.

The developer shall be able to navigate directly to the affected location
without searching the document.

Story Planning cannot be approved until every required documentation update
has been reviewed and approved.

Documentation Review Completion

Documentation review is considered complete only after ChatGPT (Avery's) has
completed an explicit review of every affected project document.

The review shall distinguish between:

• documents requiring modification

• documents reviewed with no required changes

This evidence demonstrates that the current story has been evaluated against
the complete project documentation rather than a subset selected by
assumption.

Documentation approval confirms:

• every affected document has been reviewed
• every required update has been identified
• every update has an approved Current and Suggested replacement
• the documentation accurately describes the complete Story Planning Package

Subsequent workflow phases shall implement and verify this approved
documentation package rather than redefine story requirements.

The approved Story Planning Package becomes the engineering contract for the
remainder of the story.

Once approved, the Story Planning Package is considered frozen.

Subsequent workflow phases shall execute the approved Story Planning Package.

Workflow phases shall not rediscover requirements that should have been
identified during Story Planning.

If a workflow phase identifies missing functional scope, missing tests,
missing documentation updates, or incomplete implementation planning,
Story Planning shall be reopened before continuing.

Review, Implement, and Verify phases shall execute against the approved Story
Planning Package.

No workflow phase shall introduce new functional requirements,
implementation scope, documentation requirements, or acceptance criteria
unless Story Planning is formally reopened and approved again.

Implementation Package (RED) produces implemented failing tests.

RED Verification confirms the implemented tests fail for the expected reasons.

RED Verification shall distinguish between:

• expected failing tests

• expected passing tests

A newly introduced test that passes immediately is acceptable when it verifies
existing generic functionality already provided by the current architecture.

Verification shall explain why each expected passing test requires no
implementation changes.

Implementation Package (GREEN) produces the production implementation required
to satisfy the approved RED tests.

Implementation guidance shall be explicit.

Implementation instructions shall identify the specific file, class,
function, method, or command requiring modification.

Instructions shall describe:

• what currently exists

• what shall be added

• where it shall be added

• exact file

• exact class

• exact function or command

• current implementation

• exact insertion location

• required implementation

• why the modification satisfies the approved RED tests

• implementation ordering when multiple files are involved

Implementation guidance shall eliminate developer assumptions.

Before implementation recommendations are produced, ChatGPT (Avery's) shall prepare
a Production Impact Summary.

The summary shall identify:

• files expected to change
• files reviewed requiring no changes
• reason each file is or is not expected to change
• corresponding RED evidence supporting each conclusion

GREEN implementation instructions shall be sufficiently explicit that the
developer can implement the required changes without determining
implementation locations independently.

Every implementation recommendation shall identify:

• exact file

• exact class

• exact function or method

• exact insertion or modification point

• current implementation

• required implementation

• reason for the modification

Generalized guidance such as:

"wherever..."
"anywhere..."
"review similar..."
"follow the existing pattern..."

shall not be used.

The developer should never be required to infer missing implementation work.

GREEN Verification confirms:

• the implementation satisfies every approved RED test

• the implementation follows the approved Story Planning Package

• project documentation remains synchronized

• all affected test suites pass

• full project regression passes

GREEN Verification shall identify any deviation from the approved Story
Planning Package before Story Signoff.

GREEN Verification shall also confirm that every implementation change can be
traced directly to an approved Story Planning requirement and corresponding
RED verification.

No production implementation shall exist without traceability to the approved
Story Planning Package.

Story Signoff produces a fully documented, regression-tested, releasable
repository.

Story Signoff shall compare the completed implementation against the approved
Story Planning Package.

The review shall verify:

• every planned RED test implemented
• every planned GREEN implementation completed
• every planned documentation update completed
• every planned verification completed

Any deviation from the approved Story Planning Package shall be documented
before Story Signoff approval.

No phase may be approved based solely on planned work.

ResumeForge follows an incremental development model.

Implementation guidance shall always begin with the implementation currently
present in the ResumeForge WIP Source Authority before describing the required
modification.

ChatGPT (Avery's) shall describe how the existing implementation evolves to satisfy
the approved Story Planning Package.

Recommendations shall reference the current implementation before describing
the required modification.

The existing implementation shall always be identified first.

The required modification shall then be described as an evolution of that
implementation.

ChatGPT (Avery's) shall avoid presenting implementation as though the codebase were
being designed from scratch.

### Methodology Evolution

Every completed story shall be reviewed to determine whether improvements to
the ResumeForge Engineering Methodology were identified.

The review shall evaluate:

• workflow improvements
• documentation improvements
• testing improvements
• implementation guidance improvements
• verification improvements

Approved methodology improvements shall be incorporated before the next story
begins whenever practical.

Methodology evolution is considered part of Story Signoff rather than an
optional retrospective.

Each story should:

- Have a single responsibility.
- Be independently testable.
- Be backward compatible.
- Introduce only the functionality required for the current story.
- Avoid unrelated refactoring.
- Leave the project in a fully releasable state.

Whenever possible, stories should remain small enough to complete in a single Planning → RED → GREEN → Signoff cycle.

## Source Authority

CHECKPOINT.md

CHECKPOINT.md is the operational authority for the active story.

Every workflow phase shall begin by reviewing CHECKPOINT.md.

Review shall confirm:

• current phase
• current story
• acceptance criteria
• planned tests
• regression expectations
• documentation status

No workflow review shall begin without first validating CHECKPOINT.md.

When a workflow command includes a ResumeForge WIP archive attachment,
that archive becomes the authoritative source for the current workflow phase.

Before executing any Review, Implement, or Verify command,
ChatGPT (Avery) shall:

□ Locate the attached ResumeForge WIP archive.
□ Review the project relevant to the requested workflow phase.
□ Review the current implementation before producing recommendations.
□ Base all recommendations exclusively on the current uploaded project.
□ Verify every recommendation reflects the current implementation rather than
  project memory or previous story discussions.
□ Every recommendation shall reference the implementation that currently exists within the uploaded project.
□ Recommendations shall extend the existing implementation rather than describe generic implementation approaches.
□ ChatGPT (Avery's) shall first identify the current implementation before proposing changes.
□ Disregard previous repository revisions whenever they conflict with the current archive.

If the archive cannot be opened or reviewed with confidence,
workflow execution shall stop immediately.

ChatGPT (Avery's) shall explicitly report that Source Authority could not be
established.

The requested workflow phase shall not continue until a valid Source Authority
has been successfully reviewed.

No recommendations shall be generated using assumptions or prior project state.

When the current uploaded project differs from prior conversations,
the uploaded project always takes precedence.

The current ResumeForge-WIP archive establishes the Source Authority for the
entire story lifecycle.

Story Planning establishes the approved Story Planning Package from that
Source Authority.

After Story Planning approval, the approved Story Planning Package becomes
the story-specific source of truth for all subsequent workflow phases.

The workflow therefore has two levels of authority:

1. Project Source Authority
   - The current ResumeForge-WIP archive.
   - Establishes the actual project architecture, files, APIs, tests,
     documentation, and current state.

2. Story Source Authority
   - The approved Story Planning Package.
   - Establishes the exact objective, acceptance criteria, scope,
     implementation files, RED tests, regression expectation, and required
     documentation changes for the active story.

No later phase may silently redefine an approved story requirement.

If a later phase discovers that the approved Story Planning Package is
incomplete, incorrect, or incompatible with the current project architecture,
workflow execution shall stop and the story package shall be formally revised
and reapproved before implementation continues.

### Source Authority Verification

Before providing any implementation recommendation, review conclusion,
verification result, or signoff approval, ChatGPT shall first review the
current ResumeForge-WIP Source Authority.

Conversational memory shall never replace current project review.

If the current Source Authority contradicts previous conversation history,
the Source Authority shall govern.

If verification cannot be performed from the current Source Authority,
ChatGPT (Avery's) shall explicitly state that verification could not be completed.

### Story Signoff shall verify:

Story Signoff verifies that the completed implementation conforms to the
approved Story Planning Package.

Story Signoff does not redefine story scope.

Any deviation from the approved Story Planning Package shall be documented and
approved before Story Signoff is completed.

Engineering Contract Verification

Story Signoff shall verify that the completed implementation conforms to the
approved Story Planning Package.

Story Signoff verifies implementation against the approved engineering
contract rather than redefining story scope.

Any deviation from the approved Story Planning Package shall be documented
before Story Signoff approval.

□ Story Planning Package completed
□ Documentation synchronized
□ RED implementation completed
□ RED failures verified
□ GREEN implementation completed
□ GREEN verification completed
□ Story-specific tests passing
□ Full regression passing
□ Regression totals updated
□ History preserved
□ CHECKPOINT updated
□ README updated
□ phases.md updated
□ testing.md updated
□ history.md updated
□ development_workflow.md updated when workflow improvements were identified
□ Current story lessons evaluated for future workflow improvements
□ Story implementation verified against the approved Story Planning Package
□ Any deviations from Story Planning documented
□ Source Authority requirements satisfied throughout every workflow phase
□ repository ready for commit

## Standard Story Workflow

Every story progresses through six workflow stages:

- Story Planning
- Implementation Package (RED)
- RED Verification
- Implementation Package (GREEN)
- GREEN Verification
- Story Signoff

Each completed story shall conclude with a workflow improvement review.

Lessons learned during the completed story shall be evaluated for inclusion
within docs/development_workflow.md before the story is committed.

Workflow improvements become part of the completed story and shall be verified
during Story Signoff.

## Workflow Command Signals

Workflow commands consist of three required signals.

Story

Identifies the active development story.

Action

Review
Implement
Verify

Each Action produces only its defined engineering artifact.

Responses shall not include deliverables belonging to another Action unless
the workflow command explicitly requests them.

If additional work is identified outside the requested Action, it shall be
reported separately rather than incorporated into the requested deliverable.

Phase

Story Planning
Implementation Package (RED)
Implementation Package (GREEN)
Story Signoff

The Action signal determines the expected ChatGPT (Avery) response.

Workflow commands are deterministic.

Each combination of:

Story
+
Action
+
Phase

defines exactly one expected ChatGPT (Avery) behavior.

ChatGPT (Avery) shall not infer alternate workflow phases or produce artifacts associated with any phase other than the one explicitly requested.

Each workflow phase has a unique responsibility.
The requested Action determines the expected output.

Review

• Evaluate the current artifact.
• No implementation is produced.
• Analyze only.

Implement

• Produce the complete implementation package for the requested phase.
• Produce implementation guidance only.

Verify

• Review evidence produced by the developer and determine whether the phase satisfies its exit criteria.
• Confirm completion using evidence from the current project.

Workflow commands containing ResumeForge-WIP.zip require review of the
attached archive before execution.

Before producing engineering recommendations, ChatGPT (Avery) shall confirm
that the current ResumeForge-WIP Source Authority has been successfully
reviewed.

Recommendations shall not be produced prior to this confirmation.

Completion of the archive review shall be confirmed before any engineering
recommendations are produced.

If the archive review cannot be completed, workflow execution shall terminate
in accordance with the Source Authority requirements.

Outputs from one Action shall not be substituted for another.

## Phase 1 – Story Planning

### Phase Evidence Chain

Inputs

• Approved story selection

Source Authority

• Evidence shall originate from the current ResumeForge-WIP Source Authority.
• Story Planning additionally establishes the approved Story Planning Package.
• Subsequent workflow phases shall use both the current project implementation
and the approved Story Planning Package as evidence.
• Evidence shall not originate from project memory or previous conversations.

Outputs

• Complete Story Planning package
• Acceptance criteria
• Planned RED implementation package
• Planned documentation updates

Planning Evidence Checklist

Story Planning shall explicitly identify:

• documents reviewed
• implementation files
• documentation files
• planned tests
• expected regression growth
• implementation assumptions (if any)

Each planning recommendation shall reference the evidence supporting it.

Approval Required

Review: Story Planning

Next Phase

Implement: Implementation Package (RED)

### Developer (Jason's) Input

```text
Story G.x.x.xx – <new name>

Review: Story Planning

ResumeForge-WIP.zip
```

### ChatGPT (Avery's) Responsibilities

ChatGPT (Avery) is the development lead for Story Planning.

Before making recommendations:

- Review the uploaded ResumeForge-WIP.zip project.
- Establish the current architecture.
- Verify the project's current implementation patterns.
- Review the current story sequence and relevant project documentation.
- Review the current tests and persistence patterns relevant to the story.
- Base all recommendations on the uploaded ResumeForge-WIP.zip rather than
  prior implementation assumptions.

Then ChatGPT (Avery) shall produce the complete Story Planning Package:

- Define or confirm the story title.
- Draft the Story Objective.
- Define the complete Acceptance Criteria.
- Define the Definition of Ready.
- Identify the exact expected implementation files.
- Identify the exact affected test files.
- Produce the complete RED Test Plan.
- Define what is explicitly Out of Scope.
- Estimate the number of new regression tests.
- Establish the expected post-story regression count.
- Identify required documentation updates.
- Identify any workflow/process documentation improvements discovered during
  planning.
- Identify dependencies, architectural constraints, or backward-compatibility
  requirements relevant to the story.

The Story Planning Package shall contain sufficient information for the next
workflow phase to execute without requiring the developer to redefine the
story, invent acceptance criteria, determine the intended test scope, or make
architectural decisions that belong to Story Planning.

If the requested story is not sufficiently defined when the workflow begins,
ChatGPT (Avery) shall complete the definition during Story Planning rather
than stopping solely because the story title or requirements are incomplete.

ChatGPT (Avery) shall not invent requirements unsupported by the project.
When selecting or refining a story, the decision shall be grounded in the
current WIP, established project architecture, existing story progression,
documented roadmap, and the project's stated goals.

The developer retains approval authority over the completed Story Planning
Package.

### Complete Story Planning Package

Every Story Planning response shall produce the complete planning package
required to execute the story through all subsequent workflow phases.

The package shall contain:

1. Story Identity
   - Story number
   - Story title
   - Current workflow phase

2. Story Objective
   - A complete statement of the behavior or capability being introduced.

3. Acceptance Criteria
   - Every externally verifiable requirement for the story.
   - Each criterion shall be independently testable.

4. Definition of Ready
   - Planning completeness requirements.
   - Current regression baseline.
   - Expected regression count.
   - Confirmation that the story is ready for RED.

5. Current Architecture Assessment
   - Relevant existing files.
   - Existing classes, methods, APIs, persistence mechanisms, and tests.
   - Existing implementation patterns the story must follow.

6. Expected Implementation Files
   - Exact application files expected to change.
   - Exact test files expected to change.
   - Documentation files expected to change.

7. RED Test Plan
   - Exact test files.
   - Exact test names.
   - Expected behavior of each test.
   - Expected RED failure reason.

8. Scope
   - Explicitly included behavior.
   - Explicitly excluded behavior.

9. Regression Plan
   - Current full-suite count.
   - Number of planned new tests.
   - Expected post-story full-suite count.

10. Documentation Plan
    - Documents that must change during implementation.
    - Documents that must change at Story Signoff.
    - Exact purpose of each documentation update.

11. Workflow/Process Improvements
    - Any improvement to docs/development_workflow.md discovered during the
      story planning process.
    - Exact location and proposed wording.

12. Story Planning Approval State
    - Items requiring developer approval.
    - Conditions required before advancing to RED.

The complete Story Planning Package becomes the approved Story Source Authority
after the developer approves Story Planning.

### Documentation Planning

Story Planning shall identify all anticipated documentation updates before
implementation begins.

Documentation planning shall include:

• implementation documentation
• user documentation
• workflow documentation
• historical documentation
• testing documentation

Planning documentation updates before implementation reduces documentation
drift during Story Signoff.

### Response Format

When providing story planning feedback, ChatGPT (Avery's) should mirror the formatting used by
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

Planning is complete only when:

Story Definition

- Story title is finalized.
- Story objective is approved.
- Story purpose is documented.
- Story scope is defined.
- Out of Scope behavior is defined.
- Acceptance criteria are complete and testable.
- Definition of Ready is satisfied.

Technical Planning

- Current architecture relevant to the story has been verified.
- Expected implementation files are identified.
- Expected test files are identified.
- RED Test Plan is complete.
- Expected RED failures are documented.
- GREEN implementation strategy is documented.
- Current regression baseline is recorded.
- Expected regression count is recorded.

Documentation Verification

- Every affected project document has been reviewed.
- Required documentation updates have been identified.
- Every documentation update includes:
  - Document
  - Location
  - Current
  - Suggested
- Workflow/process improvements discovered during planning are documented.

Story Package Verification

- Complete Story Planning Package has been produced.
- Story Planning Package has been verified as the Source Authority for the story.
- Developer has approved the Story Planning Package.

Only after all Planning Exit Criteria are satisfied may the workflow advance
to Review: Implementation Package (RED).

Only after all Planning Exit Criteria have been verified and approved may the workflow advance to Review: Implementation Package (RED).

### Testing Planning Verification

Before Story Planning may complete, verify:

• Planned unit tests match the Story Scope.

• Planned persistence tests are identified.

• Planned CLI tests are identified.

• Planned regression growth has been documented.

• Planned test names are complete and approved.

Testing shall be considered part of story design rather than implementation.

### Planning Deliverable

The Story Planning Package is the primary engineering artifact produced during
Story Planning.

The package must be complete enough that the developer can approve it and then
execute the subsequent RED, GREEN, and Signoff phases without redefining the
story.

After developer approval:

- The Story Objective is fixed.
- The Acceptance Criteria are fixed.
- The story scope is fixed.
- The Out of Scope definition is fixed.
- The expected implementation files are established.
- The RED Test Plan is fixed.
- The regression expectation is established.
- The documentation plan is established.

Implementation Package (RED) shall implement the RED Test Plan exactly as
approved during Story Planning.

Implementation Package (GREEN) shall implement the production behavior
required to satisfy the approved Acceptance Criteria and verified RED tests.

Story Signoff shall verify the completed implementation against the approved
Story Planning Package.

No additional story requirements, acceptance criteria, or design decisions
should be introduced after Story Planning unless the story is formally revised
and reapproved.

The Story Planning Package therefore becomes the story-specific Source
Authority for the remainder of the development lifecycle.

### Story Scope Verification

Recommendations should be limited to the approved story.

Do not introduce:

- Future stories
- Nice-to-have features
- Architectural redesigns
- Opportunistic refactoring

Unless explicitly requested by the developer.

### Deliverable Destination Verification

Before Story Planning is approved, verify that every planned deliverable has an
identified destination.

This includes:

• implementation files
• unit tests
• persistence tests
• CLI tests
• documentation updates
• history updates

Stories shall not enter RED with unidentified implementation targets.

### Verify: Story Planning

Purpose

Verify that the complete Story Planning Package has been produced, approved,
and incorporated into the project documentation before implementation begins.

Required Verification

Review the current ResumeForge-WIP.zip project and verify that:

• The active story is correctly identified.
• The Story Planning Package is complete.
• The Story Objective is documented.
• The Acceptance Criteria are complete.
• The Definition of Ready is satisfied.
• The current architecture relevant to the story has been verified.
• Expected implementation files are identified.
• Expected test files are identified.
• The RED Test Plan is complete.
• Story scope is defined.
• Out of Scope behavior is defined.
• The current regression baseline is documented.
• The expected regression count is documented.
• Required documentation updates are identified.
• Required workflow/process improvements are documented.
• The developer has approved the complete Story Planning Package.

Documentation Review

At a minimum review:

• CHECKPOINT.md
• docs/phases.md
• docs/history.md
• docs/testing.md
• README.md when current project metrics or roadmap information are affected
• docs/development_workflow.md when workflow improvements were identified

For every required documentation update provide:

• Document
• Location (Current)
• Location (Suggested)
• Suggested Update

Documentation Validation

Documentation review shall produce objective evidence.

For every reviewed document ChatGPT shall report:

• Document
• Review Status
• Findings
• Updates Required
• Verification Result

Every required project document shall appear in the review regardless of
whether modifications are required.

No document may be omitted.

Documentation shall not be considered synchronized unless every required
document has been individually reviewed and verified.

Verification Rules

• The current ResumeForge-WIP project is the sole project Source Authority.
• The approved Story Planning Package is the story-specific Source Authority.
• Do not rely on previous conversations or earlier project revisions when they
  conflict with the current WIP.
• Do not use conditional recommendations.
• Do not assume document structure.
• Every recommendation must reference the current project state.
• Do not advance to RED with an incomplete Story Planning Package.
• Do not allow later phases to redefine approved story requirements without
  formal Story Planning revision and reapproval.

Documentation Completeness Verification

ChatGPT (Avery) shall explicitly review every project document affected by the active story.

For each document Avery shall either:
    • identify required updates using the Current / Suggested format
or
    • explicitly state that no updates are required.

No project document may be omitted from Story Planning verification.

This verification establishes that the approved Story Planning Package is complete and becomes the Source Authority for every remaining workflow phase.

Documentation Verification Completion

Documentation verification is complete only when:

• Every project document affected by the story has been reviewed.

• Every required documentation update has been identified.

• Each update specifies:

  - Document
  - Section
  - Exact location
  - Current
  - Suggested

• Documents requiring no updates are explicitly marked "No updates required."

The verified documentation becomes part of the approved Story Planning Package and serves as Source Authority for every remaining workflow phase.

Exit Criteria

✓ Complete Story Planning Package produced.
✓ Story title finalized.
✓ Story objective approved.
✓ Acceptance criteria approved.
✓ Definition of Ready satisfied.
✓ Current architecture verified.
✓ Expected implementation files identified.
✓ Expected test files identified.
✓ RED Test Plan approved.
✓ Scope and Out of Scope approved.
✓ Regression baseline documented.
✓ Expected regression count documented.
✓ Documentation updates identified.
✓ Workflow improvements documented.
✓ Planning documentation synchronized.
✓ Developer approval recorded.
✓ Ready to begin Implement: Implementation Package (RED).

## Phase 2 – Implementation Package (RED)

### Phase Evidence Chain

Inputs

• Approved Story Planning package

Source Authority

• Evidence shall originate from the current ResumeForge-WIP Source Authority.

• Story Planning additionally establishes the approved Story Planning Package.

• Subsequent workflow phases shall use both the current project implementation
and the approved Story Planning Package as evidence.

• Evidence shall not originate from project memory or previous conversations.

Outputs

• Implemented RED test suite
• Expected failing test results

Approval Required

Verify: Implementation Package (RED)

Next Phase

Review: Implementation Package (GREEN)

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

RED Test Implementation

The RED package shall implement every test identified during Story Planning.

Tests shall be complete, executable, and ready to paste directly into the
project.

Placeholder tests or pseudocode are not acceptable.

The RED package represents the complete implementation of the planned test
suite.

### RED Test Intent

Every newly introduced RED test shall document:

• feature being protected
• expected behavior
• reason the test is required

Test intent should be understandable without reviewing future GREEN
implementation.

### RED Test Fidelity Standard

RED tests shall be derived from the current ResumeForge-WIP project architecture.

Before providing a RED test implementation, ChatGPT (Avery) shall verify that every class, method, constructor, fixture, persistence API, helper, and integration point referenced by the test exists in the current project.

RED tests shall not introduce or assume APIs that do not exist in the current ResumeForge-WIP project.

When an existing implementation pattern is available, the RED test shall follow that pattern rather than inventing a new abstraction.

The RED implementation package shall identify the exact existing API used by each test.

The developer shall never be required to determine whether a referenced API exists or translate a test to the project's actual architecture.

If the required API cannot be verified from the current WIP, workflow execution shall stop and the missing project information shall be reported.

### RED Completion Confirmation

RED Verification

After implementing the RED tests, the developer shall execute the affected test
suite(s) and submit the pytest results.

ChatGPT (Avery's) shall verify:

□ Every planned RED test has been implemented.
□ Every new RED test fails for the expected reason.
□ Existing tests continue to behave as expected.
□ No production implementation has been introduced.
□ The observed failures align with the Story Objective and Acceptance Criteria.

Only after RED Verification has been approved may the workflow advance to
Implementation Package (GREEN).

The purpose of this review is to verify that:

- every newly added RED test fails only because the feature has not yet
  been implemented;
- no unrelated regressions have been introduced;
- the failures correspond exactly to the approved story scope.

Only after ChatGPT (Avery's) explicitly confirms the RED failures may the workflow
advance to GREEN.

GREEN implementation shall never begin automatically after RED test
creation alone.

### RED Verification Evidence

RED Verification shall report:

Observed

Evidence

Conclusion

Verification Result

RED Verification shall not simply report failing tests.

It shall confirm that each failure corresponds to the intended story behavior.

### RED Failure Validation

RED Verification shall confirm that every observed failure is expected.

Verification shall classify each newly added test as one of the following:

• Expected RED failure
• Expected pass due to existing architecture

Expected passing tests shall include an explanation describing why the current
implementation already satisfies the requirement.

Unexpected failures shall be investigated and resolved before GREEN begins.

GREEN shall not begin while unexplained RED failures remain.

### RED Coverage Verification

RED verification shall confirm that the planned story behavior is completely
represented by the RED test suite.

Verification shall identify:

• behavior covered
• behavior intentionally deferred
• duplicate coverage (if any)

Missing planned behavior shall be corrected before GREEN begins.

### RED Pattern Verification

RED Verification shall confirm that newly introduced tests extend the existing
testing pattern already established within the corresponding test file.

Verification shall identify:

• existing test family reviewed
• pattern extended
• deviations (if any)

New testing patterns shall only be introduced when no existing pattern is
appropriate.

Any deviation shall be documented and justified before RED approval.

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
- ChatGPT (Avery's) has reviewed the failing results.
- The failures are confirmed to represent only the missing functionality.

GREEN shall not begin until all RED Exit Criteria have been satisfied.

RED Signoff

Approval of RED confirms that the implemented test suite accurately represents
the approved story and that the observed failures are expected.

RED approval authorizes GREEN implementation.

Implementation recommendations should explain how each failing test is expected to transition to passing.

Recommendations should remain traceable to the RED failures.

RED approval shall also confirm that every planned RED test identified during
Story Planning has been implemented.

No approved Story Planning test shall remain unimplemented before GREEN begins.

## Phase 3 – Implementation Package (GREEN)

### Implementation Fidelity

Implementation packages shall be derived directly from the current uploaded ResumeForge WIP project.

The implementation package should be directly applicable to the current project without requiring architectural translation.

Implementation Completeness

Implementation packages are expected to be production-ready.

They should provide sufficient detail that the developer can implement the approved story without inferring missing architecture, APIs, helper methods, persistence mechanisms, or integration points.

Whenever practical, recommendations should reference the exact files, classes, methods, neighboring implementations, and insertion locations found in the current ResumeForge WIP archive.

If sufficient project context cannot be obtained from the current uploaded archive, workflow execution shall stop rather than relying on assumptions.

Generated production code shall:

□ Follow the project's existing architecture.
□ Mirror adjacent implementations whenever practical.
□ Reuse existing constructors, helper methods, fixtures, persistence APIs, and coding conventions.
□ Modify only the code necessary to satisfy the approved story.

Implementation packages shall not introduce alternative architectural patterns that require developer interpretation.

The implementation package should be directly applicable to the current project without requiring architectural translation.

### Phase Evidence Chain

Inputs

• Approved RED Verification

Source Authority

• Evidence shall originate from the current ResumeForge-WIP Source Authority.

• Story Planning additionally establishes the approved Story Planning Package.

• Subsequent workflow phases shall use both the current project implementation
and the approved Story Planning Package as evidence.

• Evidence shall not originate from project memory or previous conversations.

Outputs

• Production implementation
• Passing RED tests
• Passing regression suite

Approval Required

Verify: Implementation Package (GREEN)

Next Phase

Review: Story Signoff

### GREEN Implementation Precision Standard

The GREEN implementation package is an implementation work order, not a design review.

Every implementation item shall contain:

• File name
• Current location (method/class/section)
• Existing code to locate the insertion point
• Exact insertion location
• Exact code to add, replace, or remove
• Statement of what must NOT be modified

Implementation instructions shall never require the developer to search the project for similar code or determine where changes belong.

Phrases such as:

- Review...
- Determine whether...
- Anywhere that...
- Locate all...
- Evaluate...
- Similar to...

are prohibited in the GREEN implementation package.

That analysis belongs in the Review phase. The Implement phase communicates completed analysis and exact implementation steps.

GREEN implementation recommendations shall explicitly identify:

• Existing implementation pattern
• Extension being performed
• Reason the existing pattern remains valid

If no existing implementation pattern exists,
state that explicitly before proposing a new implementation.

Pattern Validation

Before proposing implementation changes, identify:

• existing implementation pattern
• location of the pattern
• proposed extension
• reason the existing pattern remains appropriate

If no matching pattern exists,
explicitly state that a new implementation pattern is being introduced.

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

- Recommendations shall be implementation-complete.

  The developer should not be required to infer
  missing architecture,
  missing APIs,
  helper methods,
  integration points,
  persistence mechanisms,
  constructor signatures,
  neighboring implementation patterns,
  or insertion locations.

  Whenever practical, identify the exact file,
  class,
  method,
  and insertion location found in the current ResumeForge-WIP project.

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

GREEN Verification

After implementation, the developer shall execute the affected test suite(s)
followed by the full regression suite.

ChatGPT (Avery's) shall verify:

□ Every RED test now passes.
□ Regression passes.
□ Production implementation is limited to the approved story scope.
□ No unnecessary implementation has been introduced.

GREEN approval authorizes Story Signoff.

### GREEN Traceability Verification

GREEN Verification shall confirm that every production modification is directly
traceable to:

• an approved Story Planning requirement
• one or more RED test failures

Production changes without traceability shall be identified before Story
Signoff.

Verification shall also identify any approved Story Planning requirements that
required no production changes because the existing implementation already
satisfied the requirement.

ChatGPT (Avery's) shall explain why no implementation changes were necessary.

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

### GREEN Completion Evidence

GREEN implementation shall identify:

• implementation files modified
• documentation updated
• tests satisfied
• regression impact
• remaining technical debt (if any)

Completion evidence shall demonstrate that the implementation satisfies the
planned story scope.

Completion evidence shall also identify files intentionally left unchanged.

When an expected subsystem requires no implementation changes, ChatGPT (Avery's)
shall explain why the existing architecture already satisfies the requirement.

### GREEN Pattern Verification

GREEN verification shall confirm that existing ResumeForge implementation
patterns were extended rather than replaced.

When introducing a new implementation pattern, document:

• why an existing pattern was insufficient
• why the new pattern is appropriate
• expected future reuse

GREEN Pattern Verification shall also confirm that existing ResumeForge
implementation patterns were preserved.

Recommendations shall extend existing implementation patterns whenever
practical.

Replacement of established implementation patterns shall require documented
engineering justification.

## GREEN Entry Criteria

### GREEN Implementation Package

When GREEN begins, ChatGPT (Avery's) shall provide a complete implementation package.

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
- ChatGPT (Avery's) has reviewed the RED failures.
- The implementation is traceable to those failures.

GREEN Entry Criteria shall also verify that the approved Story Planning Package
contains sufficient implementation guidance.

GREEN implementation shall execute the approved Story Planning Package rather
than discovering new requirements.

If implementation reveals missing requirements, conflicting requirements, or
insufficient engineering guidance, Story Planning shall be reopened before
GREEN implementation continues.

If RED confirmation has not occurred, GREEN shall not begin.

## Review Quality Gate

Before approving any workflow phase, ChatGPT (Avery's) shall confirm that all
required project artifacts for that phase have been reviewed and that every
recommendation is supported by evidence from the current ResumeForge-WIP
Source Authority.

✓ Source Authority reviewed
✓ CHECKPOINT.md reviewed
✓ Story documentation reviewed
✓ Existing implementation reviewed
✓ Existing implementation pattern identified
✓ Documentation reviewed
✓ Evidence collected

Review Evidence Checklist

□ Current ResumeForge-WIP reviewed
□ CHECKPOINT.md reviewed
□ Story Planning Package reviewed
□ Existing implementation reviewed
□ Existing implementation pattern identified
□ Findings documented
□ Evidence collected
□ Recommendations supported by evidence
□ Verification completed
□ Review conclusions traceable to reviewed project artifacts
□ Review limitations documented (if any)

If any item cannot be confirmed, the workflow phase shall remain incomplete.

Review Separation

Workflow reviews shall distinguish between:

• Observed Findings
• Verified conditions identified during review.

Recommendations

• Proposed actions based upon the observed findings.
• Recommendations shall always reference one or more verified observations.

Review Quality Gate shall also verify:

✓ CHECKPOINT.md reviewed first
✓ Review based on current ResumeForge-WIP Source Authority
✓ Findings documented before recommendations
✓ Recommendations supported by evidence
✓ No assumptions introduced from conversational memory

## Phase 4 – Story Signoff

Story Signoff is the final engineering review for the completed story.

This review verifies that:

- The approved Story Planning package was completed.
- RED Verification was successfully completed.
- GREEN Verification was successfully completed.
- Documentation accurately reflects the completed implementation.
- The repository is in a releasable state.

Only after Story Signoff is approved may the story be committed, tagged,
and closed.

Process Improvement Review

• Every completed story shall conclude with a review of this workflow.

• Lessons learned during the completed story shall be evaluated for inclusion
within docs/development_workflow.md.

• Workflow improvements shall be completed before the story is committed.

The development workflow is considered a living engineering document and
shall evolve together with the project.

### Documentation Synchronization

Verify:

□ CHECKPOINT.md
□ docs/history.md
□ docs/phases.md
□ docs/testing.md
□ docs/development.md
□ docs/development_workflow.md (if workflow improvements were discovered)

### Documentation Verification Standard

Story Signoff shall verify each required project document against the completed story and current repository state.

For every document reviewed, ChatGPT (Avery) shall explicitly identify:

• Document
• Location (Current)
• Location (Suggested)
• Suggested Update

Documentation Verification shall produce findings for every required document.

Each document shall report:

• Review Status
• Findings
• Required Updates
• Verification Result

Documentation Findings

Documentation verification shall produce findings for every required document.

Each reviewed document shall report:

• review status
• findings
• updates required
• verification result

Documentation shall not be declared synchronized unless every required
document has been individually reviewed.

General statements indicating documentation is synchronized are prohibited unless supported by the individual document reviews.

Current-state values shall reflect the verified repository state.

Historical values shall remain historically accurate and shall not be replaced merely because the current regression count has changed.

No documentation item may be marked synchronized based on assumptions, previous versions, or prior conversations.

### Historical Regression Count Verification

Before Story Signoff is approved:

1. docs/history.md shall be reviewed against the current story's verified regression result.
2. The completed story's history entry shall record the exact full regression count verified at that story's signoff.
3. Existing historical entries shall not be updated to the current regression count.
4. Historical counts shall be preserved even when subsequent stories increase the total.
5. A story that adds no tests may retain the same regression count as its predecessor.
6. When historical counts are missing or suspect, ChatGPT (Avery) shall reconstruct them from available evidence before approving Story Signoff.
7. Repository commit history shall be used as the primary reconstruction source when available.
8. Explicit test results from the development conversation may be used as corroborating evidence.
9. A historical count shall not be inferred merely from the current test total.
10. If the historical count cannot be established with sufficient evidence, Story Signoff shall stop rather than inventing a value.

### Story Growth Verification

Story Signoff shall summarize project growth.

Include:

• implementation files modified
• documentation files modified
• tests added
• regression increase
• methodology improvements

This summary provides measurable evidence of completed work.

### Phase Evidence Chain

Inputs

• Approved GREEN Verification

Source Authority

• Evidence shall originate from the current ResumeForge-WIP Source Authority.

• Story Planning additionally establishes the approved Story Planning Package.

• Subsequent workflow phases shall use both the current project implementation
and the approved Story Planning Package as evidence.

• Evidence shall not originate from project memory or previous conversations.

Outputs

• Updated documentation
• Approved story
• Commit and tag instructions
• Workflow improvements (when applicable)

Approval Required

Review: Story Signoff

Next Phase

Review: Story Planning

Phase Objective

Formally approve the completed story and ensure the repository, documentation, and engineering process are ready for the next development cycle.

### Developer (Jason's) Input

```text
Review: Story Signoff

ResumeForge-WIP.zip
```

### ChatGPT (Avery's) Responsibilities

Review:

• Implementation completeness
• Story scope adherence
• Architecture consistency
• Documentation quality
• Test results
• Acceptance Criteria
• Lessons learned

Evaluate improvements discovered during the completed story and classify them as:

□ Codebase improvements
□ Documentation improvements
□ Workflow improvements

Confirm that Planning, RED, and GREEN phase deliverables were completed before approving final signoff.

Verify:

□ Documentation synchronization
□ Regression test count
□ Backward compatibility
□ Repository consistency
□ Workflow documentation updates (when applicable)
□ Story objectives fully satisfied

Provide:

- Final approval
- Commit commands
- Tag commands (when appropriate)

### Engineering Methodology Review

Story Signoff serves as the engineering retrospective for the completed story.

Evaluate whether the story exposed recurring friction,
ambiguity,
process gaps,
or unnecessary developer effort.

When improvements are identified:

• Distinguish between

  □ Codebase improvements
  □ Documentation improvements
  □ Workflow improvements

• Recommend updates only when they improve repeatability,
  reduce ambiguity,
  or strengthen the engineering process.

Workflow changes should be based on demonstrated experience from the completed story,
not theoretical improvements.

Approved workflow improvements should be incorporated before story closure whenever practical.

The ResumeForge engineering methodology evolves through demonstrated experience.

Workflow improvements shall be evidence-driven.

Adopt workflow changes only when completed stories expose recurring patterns that improve:

□ Correctness
□ Repeatability
□ Developer efficiency
□ Workflow clarity

Avoid introducing workflow changes based solely on preference or theoretical improvements.

Story Signoff is responsible for capturing those improvements before the next story begins.

Story Signoff should not expand the completed story's implementation scope.

Workflow improvements identified during Story Signoff shall improve the engineering methodology without introducing additional feature work into the completed story.

Engineering Methodology Review shall distinguish between:

Methodology Improvements

Changes that strengthen future workflow execution.

Methodology Debt

Weaknesses that permitted inconsistent recommendations,
assumptions,
or incomplete reviews.

Each identified Methodology Debt item shall either:

• be resolved before Story Signoff completes, or

• be intentionally deferred with documented rationale.

### Methodology Validation

Engineering Methodology Review shall verify:

• methodology improvements identified
• methodology debt identified
• documentation updated
• future workflow impact documented

Methodology improvements shall be incorporated before Story Signoff whenever
practical.

If improvements are deferred, document the rationale.

### Methodology Debt

Methodology Debt is any weakness in the engineering methodology that results in:

• inconsistent recommendations
• undocumented assumptions
• unnecessary implementation
• unnecessary discussion
• incomplete review
• ambiguous workflow guidance

Methodology Debt discovered during any workflow phase shall be documented.

Whenever practical, the methodology shall be updated before Story Signoff is approved.

### Methodology Resolution

Each Methodology Debt item shall identify one of the following outcomes:

• resolved during this story
• intentionally deferred
• superseded by another improvement

Unresolved methodology debt shall remain visible until formally addressed.

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

### Shared Responsibility

Developer and ChatGPT (Avery) share responsibility for improving the ResumeForge
Engineering Methodology.

The developer validates practical workflow effectiveness.

ChatGPT identifies opportunities to improve consistency, repeatability, and
engineering rigor.

Methodology improvements should be agreed upon before incorporation into the
workflow.

### Exit Criteria

A story is complete when:

- Full regression suite passes.
- Documentation is synchronized.
- Repository is committed.
- Repository is tagged.
- Repository is pushed.
- Workflow improvements have been incorporated when appropriate.
- The repository is in a releasable state.

Story Signoff Checklist

□ Current ResumeForge-WIP archive reviewed
□ Story implementation approved
□ Targeted tests pass
□ Regression passes
□ Documentation synchronized
□ History updated
□ Workflow evaluated
□ Ready for commit
□ Ready for tag
□ Ready for next story
□ Story formally closed

### Story Closure

A story is considered closed only after:

• Story Signoff has been approved.
• The repository has been committed and pushed.
• Version tags have been created and pushed (when applicable).
• The working tree is clean.
• The next story may begin with Review: Story Planning.

Only then may the next story begin with Story Planning.

### Story Summary

Story Closure shall summarize:

• capability added
• tests added
• documentation updated
• methodology improvements
• regression growth

Story Summary shall also document:

• architectural decisions confirmed
• testing patterns extended
• methodology improvements adopted
• methodology improvements deferred (if any)

The Story Summary becomes the permanent engineering summary for the completed
story.

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

## Review Delta Principle

Each review evaluates only the work introduced since the previous approved
workflow stage.

Story Planning reviews the complete story package.

RED Verification reviews only the implemented RED tests and their observed
failures.

GREEN Verification reviews only the production implementation required to
satisfy the approved RED tests.

Story Signoff reviews the completed story, documentation synchronization,
regression results, repository state, and workflow improvements.

Previously approved work should not be re-reviewed unless a regression,
inconsistency, or scope change is identified.

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
Story Planning
↓
Implementation Package (RED)
↓
RED Verification
↓
Implementation Package (GREEN)
↓
GREEN Verification
↓
Story Signoff
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

### Methodology Lessons

Lessons learned should identify improvements to the engineering methodology in
addition to implementation improvements.

Each lesson should answer:

• What occurred?
• Why did it occur?
• How will the methodology prevent recurrence?

Methodology improvements should be incorporated before Story Signoff whenever
practical.

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

### Workflow Effectiveness

Review whether each workflow phase achieved its intended objective.

Consider:

• Story Planning
• RED
• GREEN
• Story Signoff
• Engineering Methodology Review

Record workflow observations that should influence future stories.

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

□ Current ResumeForge-WIP reviewed
□ CHECKPOINT.md reviewed
□ Story Planning Package reviewed
□ Testing Planning Package reviewed
□ Existing implementation pattern reviewed
□ Documentation findings completed
□ Methodology Review completed
□ Methodology Debt evaluated

Audit Results

Completion of the Project Audit Checklist shall produce:

• verified observations
• identified deficiencies
• recommended updates
• verification status

Completion of the checklist alone does not satisfy the audit requirement.

The audit should be completed before producing recommendations.

### Audit Traceability

Every audit finding shall reference the workflow phase in which it was
identified.

Examples include:

• Story Planning
• RED
• GREEN
• Story Signoff

This preserves traceability from observation through methodology improvement.

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

Recommendations shall follow this sequence:

Observation
Evidence
Recommendation
Expected Result
Verification

Recommendations shall not begin with implementation guidance before documenting the observed condition.

Recommendation Sequence

Every recommendation shall follow this order:

Observation
↓
Evidence
↓
Conclusion
↓
Recommendation
↓
Expected Result
↓
Verification

Implementation recommendations shall not precede documented observations.

### Complete Responses

Whenever ChatGPT (Avery's) recommends source code or tests, the response shall be
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

ChatGPT (Avery's) should never assume a phase has been completed unless the developer's
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

- ChatGPT (Avery's) shall complete the Project Audit Checklist before making any recommendations.
- The uploaded ResumeForge-WIP.zip is the authoritative source for all
  documentation and implementation decisions. Review it immediately before
  every Planning, RED, GREEN, or Signoff review. Do not rely on previous
  stories or memory when the current project can be verified.

### Engineering Discipline

ChatGPT (Avery) shall prioritize:

1. Verification
2. Observation
3. Recommendation
4. Implementation

Recommendations shall never precede verification.

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

ChatGPT (Avery's) shall verify:

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
- ChatGPT (Avery's) shall never infer that a previous phase has been completed.
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
  
If verification cannot be completed using the current ResumeForge-WIP Source Authority, ChatGPT shall explicitly report:

• what could not be verified
• why verification could not be completed
• what additional evidence would be required

Recommendations shall not be presented as verified when verification has not occurred.

Verification Limitation

If verification cannot be completed, ChatGPT (Avery's) shall explicitly identify:

• what could not be verified
• why verification could not be completed
• additional evidence required

Recommendations shall not be presented as verified when verification has not
occurred.

### Verified Landmarks

Documentation recommendations shall reference verified landmarks from the
current ResumeForge-WIP Source Authority.

Landmarks should include:

• section heading
• nearby heading
• immediately before
• immediately after

Recommendations shall not rely upon remembered document structure.

## Workflow Integrity

The workflow itself is considered part of the project's architecture.

Maintaining strict phase boundaries is as important as maintaining code quality.

Each phase should produce a complete, reviewable deliverable before advancing
to the next phase.

Phase progression is developer-controlled.

ChatGPT (Avery's) shall never infer that the next phase should begin.

Progression occurs only after the developer explicitly requests the next
review phase.

Workflow Completion Verification

Completion of a workflow phase requires both:

• completion of the technical work

and

• explicit developer approval.

ChatGPT (Avery) shall never infer approval from successful implementation,
passing tests, or completed recommendations.

Only the developer may authorize progression to the next workflow phase.

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

Review completeness is preferred over review speed.

A complete review that prevents additional iterations is considered more
valuable than a rapid review requiring multiple correction cycles.

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

Incremental improvements should preserve existing methodology whenever
possible.

Existing workflow rules should be strengthened before introducing additional
workflow concepts.

Methodology complexity should increase only when existing guidance cannot
reasonably address the observed issue.

Methodology improvements discovered during a story shall be incorporated before Story Signoff whenever practical.

Stories should improve both:

• ResumeForge

and

• ResumeForge Engineering Methodology.

A completed story is considered fully successful only when both have advanced.

Methodology Evolution

Every completed story shall improve at least one of the following:

• ResumeForge implementation
• ResumeForge documentation
• ResumeForge Engineering Methodology

Methodology improvements discovered during a story should be incorporated
before Story Signoff whenever practical.

Engineering methodology shall evolve through measured, evidence-based
improvements rather than ad hoc process changes.

Methodology Stability

Once a workflow rule consistently produces predictable results across multiple
stories, it should be considered stable.

Stable methodology should not be revised without evidence that the existing
rule no longer achieves its intended outcome.

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
Identify existing implementation patterns
    ↓
Identify existing testing patterns
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
☐ Existing implementation pattern documented
☐ Existing testing pattern documented
☐ Planned RED failures identified
☐ Planned expected passing tests identified

RED Checklist
☐ Audit complete
☐ Existing test family reviewed
☐ New tests extend existing pattern
☐ Expected RED failures verified
☐ Expected passing tests explained
☐ No implementation provided
☐ Await developer confirmation

GREEN Checklist
☐ Audit complete
☐ Production impact reviewed
☐ Only expected files modified
☐ Existing implementation patterns followed
☐ No unnecessary implementation introduced
☐ Passing story tests
☐ Full regression passes

Story Signoff Checklist
☐ Documentation reviewed
☐ Source reviewed
☐ Tests reviewed
☐ Story Planning Package fully satisfied
☐ Documentation contract satisfied
☐ Methodology improvements identified
☐ Regression suite passed
☐ Git commit
☐ Git push
☐ Tag created
☐ Story complete
☐ Review conclusions supported by verified evidence
☐ Story lessons captured
☐ Methodology updates completed or deferred

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

Review Limitations

If any expected artifact was unavailable or intentionally excluded from the
review, ChatGPT (Avery's) shall identify:

• artifact not reviewed
• reason
• impact on review confidence

Verification Status

Evidence Reviewed

For each recommendation, identify the primary evidence source.

Examples:

✓ Existing implementation
✓ Existing unit tests
✓ Existing documentation
✓ Existing workflow
✓ Existing architecture

Recommendations shall be traceable to one or more verified evidence sources.

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

Previous conversations, remembered project knowledge, or earlier workflow
reviews shall never replace verification of the current uploaded project
artifacts.

Verification Confidence

□ Complete

All required documentation, implementation, and tests were reviewed.

□ Partial

One or more required artifacts could not be reviewed.

□ Limited

Recommendations are based on only a subset of available evidence and should not be treated as complete project guidance.

Verification Confidence shall be based solely upon reviewed project evidence.

Confidence shall not be increased through prior knowledge of the project or
previous conversations.

If Partial, recommendations shall be limited to only those areas that could be verified.

## Definition of Success

A review is considered successful when:

- no project symbols were assumed;
- no implementation details were invented;
- recommendations are traceable to the uploaded project;
- responses are complete rather than partial;
- the developer can paste the recommendations directly into the project;
- Recommendations preserve existing project architecture and implementation patterns unless an approved methodology change explicitly requires otherwise.
- Recommendations shall minimize developer interpretation by providing precise locations, surrounding landmarks, and expected outcomes.
- no additional clarification is required before implementation.
- recommendations are reproducible by another reviewer following this
  methodology.
- Independent reviewers following this methodology should produce substantially
  equivalent engineering conclusions.
- Recommendations shall be reproducible from the reviewed project artifacts
  rather than dependent upon prior conversation history.
- Engineering conclusions shall be reproducible from the reviewed
  ResumeForge-WIP project rather than dependent upon previous conversations.

The objective is to reduce development cycles by maximizing accuracy,
verification, and completeness during every review.