# ResumeForge Development Workflow

## Purpose

This document defines the standard engineering workflow for ResumeForge.

It establishes the authoritative engineering methodology used to plan,
implement, verify, document, and sign off every ResumeForge story.

All development workflow phases shall conform to this methodology unless an
approved project decision explicitly authorizes a deviation.

The goals of this workflow are to:

- Keep implementation cycles short.
- Follow strict Test-Driven Development (TDD).
- Minimize unnecessary refactoring.
- Preserve architectural consistency.
- Ensure documentation remains synchronized with the codebase.
- Produce small, incremental, high-quality changes.

## Scope

This document defines the required engineering workflow for every ResumeForge
story.

It governs how every story is planned, reviewed, implemented, verified,
documented, and approved.

It governs:

• Environment State Audit
• Story Planning
• Implementation Package (RED)
• RED Verification
• Implementation Package (GREEN)
• GREEN Verification
• Story Signoff

This document does not define project architecture, coding standards,
feature requirements, or implementation details.

Those engineering artifacts are maintained in their respective project
documentation.

## Engineering Session Startup Validation

## Engineering Workflow Governance

### Purpose

Engineering Workflow Governance defines the authoritative engineering workflow for ResumeForge Engineering Methodology (REM).

This section is the single authoritative source governing engineering workflow execution, repository evolution, repository patch management, implementation sequencing, and engineering verification.

No duplicate top-level Engineering Workflow Governance sections shall exist within the repository.

### Workflow Lifecycle

Every engineering story progresses through:

- Initiate
- Review
- Implement
- Verify
- Story Signoff
- Repository Closeout

Each phase establishes the approved engineering baseline for the next phase.

### Repository State First

Every repository modification begins with Repository State Validation.

Repository state—not implementation intent—determines the required repository operation.

### Repository Boundary First

Before any Replace or Consolidate operation, repository boundaries shall be identified and verified.

Boundary Specification shall include:

- Beginning Boundary
- Ending Boundary
- Repository Scope
- Removal Targets
- Expected Repository Outcome

Repository boundaries shall never rely upon developer interpretation.

### Repository Artifact Completeness

Every repository-modifying Repository Patch Update shall contain one complete Repository-ready Replacement Text.

Implementation descriptions, summaries, placeholders, or deferred work do not satisfy this requirement.

### Repository Advancement

Implementation State advances only after:

- Repository State Validation
- Repository Boundary Verification
- Repository Artifact Verification
- Repository Outcome Verification

Intent alone shall never advance repository state.

### Repository Verification

Repository Patch Verification shall validate:

- repository state;
- repository boundaries;
- repository artifact completeness;
- repository delta;
- repository outcome.

### Repository Consolidation

When duplicate authoritative sections exist:

1. designate the canonical section;
2. consolidate all unique guidance;
3. remove duplicate sections;
4. verify that exactly one authoritative section remains.

### Engineering Traceability

Every Repository Patch Update shall maintain complete traceability between:

- Repository State
- Repository Operation
- Repository Boundary
- Repository Artifact
- Repository Verification
- Repository Outcome

Engineering decisions shall be reproducible from repository evidence.

The ResumeForge Engineering Methodology (REM) follows a deterministic engineering workflow.

Every engineering story progresses through explicit workflow states.

```text
Initiate
    ↓
Review
    ↓
Implement
    ↓
Verify
```

Workflow progression shall never skip a workflow state.

Each workflow state has one primary engineering responsibility.

Progression to the next workflow state is authorized only after successful completion of the current workflow state.

### Workflow Responsibilities

#### Initiate

Produces the initial engineering definition and Story Planning foundation.

#### Review

Produces engineering specifications describing **what** will be implemented.

#### Implement

Produces repository-ready engineering artifacts describing **how** approved specifications are realized.

#### Verify

Validates implementation correctness, completeness, traceability, and repository readiness.

Only Verify authorizes progression to the next workflow state.

## Nested Workflow Governance

### Purpose

Nested Workflows provide a structured mechanism for temporarily suspending a parent engineering workflow in order to complete a dependent engineering activity before returning to the parent workflow.

Nested Workflows shall be used only when completion of the parent workflow is blocked by work that is logically subordinate to the current engineering activity.

### Workflow Preservation

When entering a Nested Workflow, the parent workflow shall be preserved.

The Nested Workflow shall:

- identify the parent workflow;
- identify the blocking condition;
- define its own acceptance criteria;
- complete its own Review, Implement, Verify, Signoff, and Repository Closeout activities as applicable.

### Parent Workflow Restoration

Upon successful completion of a Nested Workflow:

1. the parent workflow shall be restored;
2. repository state shall be revalidated;
3. Remaining Work Validation shall be performed;
4. engineering execution shall resume at the next unfinished parent workflow step.

Nested Workflows shall not alter completed parent workflow decisions unless a repository validation identifies a defect requiring correction.

### Repository Authority

Nested Workflows remain subject to Repository Authority.

Both parent and nested workflows shall recover engineering artifacts from the repository rather than conversational history or engineering memory.

## ResumeForge Engineering Methodology Execution Model

The ResumeForge Engineering Methodology (REM) governs every engineering
response produced for the ResumeForge project.

Before producing any engineering response, the engineer shall execute the
following methodology sequence.

1. Command Validation
2. Story State Validation
3. Workflow Transition Validation
4. Source Authority Validation
5. Methodology Validation
6. Deliverable Audit
7. Response Generation
8. Self Verification
9. Response Publication

Each stage shall complete successfully before the next stage begins.

Engineering responses shall be generated from the ResumeForge Engineering
Methodology rather than engineering memory, personal preference, or previous
response patterns.

If any validation stage fails, engineering execution shall immediately stop.

The engineer shall report the validation failure and request clarification
before continuing.

The ResumeForge Engineering Methodology governs both the engineering process
and every engineering response produced during that process.

### Methodology Architecture

The ResumeForge Engineering Methodology is organized into the following
governance domains:

1. Engineering Principles
2. Engineering Governance
3. Engineering Workflow
4. Story Lifecycle
5. Engineering Standards
6. Engineering Artifact Specifications
7. Verification Standards
8. Engineering Command Contracts
9. Continuous Improvement

Future methodology enhancements shall be incorporated into the appropriate
governance domain rather than extending unrelated sections.

When a governance domain becomes excessively large or contains multiple
independent responsibilities, it shall be refactored into smaller,
well-defined sections while preserving deterministic navigation.

## Development Philosophy

ResumeForge follows a disciplined, incremental engineering methodology based
on small, verifiable changes.

Every story progresses through a consistent sequence of planning,
implementation, verification, documentation, and signoff.

The workflow emphasizes:

- Evidence-based engineering decisions.
- Pattern-driven implementation.
- Strict Test-Driven Development (TDD).
- Small, incremental changes.
- Continuous verification.
- Documentation that evolves with the software.

The objective is to produce predictable, repeatable, and maintainable
engineering outcomes while minimizing unnecessary complexity and regression
risk.

## ResumeForge Engineering Methodology Execution Model

The ResumeForge Engineering Methodology (REM) governs every engineering
response generated for the project.

Before producing any engineering response, the engineer shall execute the
following methodology sequence.

1. Command Validation
2. Story State Validation
3. Workflow Transition Validation
4. Source Authority Validation
5. Methodology Validation
6. Deliverable Audit
7. Response Generation
8. Self Verification
9. Response Publication

The engineer shall complete each stage before advancing to the next.

Engineering responses shall not be generated from engineering experience,
historical memory, or personal preference.

Engineering responses shall be generated from the ResumeForge Engineering
Methodology.

If any validation stage fails, engineering execution shall immediately stop.

The engineer shall report the validation failure and request developer
clarification before continuing.

The ResumeForge Engineering Methodology governs the engineering process and
the engineering responses produced during that process.

### Engineering Evidence Principle

Engineering claims shall be supported by engineering evidence.

Statements such as "reviewed", "verified", "implemented", "confirmed",
or "inspected" shall be based upon the current Source Authority and
supported by identifiable project artifacts.

Responses shall distinguish between:

- Verified observations from the current Source Authority.
- Engineering conclusions derived from those observations.
- Recommendations or design guidance.

Engineering claims shall never be based upon historical memory when the
current Source Authority is available.

### Repository-first Engineering Principle

Implementation shall always extend the current repository.

Engineering responses shall not invent:

- APIs
- constructors
- helper functions
- fixtures
- command patterns
- repository architecture

Repository implementation patterns shall be reviewed before implementation
guidance is produced.

Repository artifacts always take precedence over remembered conversation
history or assumed implementation.

## Universal Engineering Phase Lifecycle

Every ResumeForge engineering phase follows the same lifecycle.

Every Implement response shall follow a consistent execution structure:

1. Source Authority
2. Deliverable Audit
3. Implementation Updates
4. Expected Verification Result

This structure minimizes engineering ambiguity while reducing unnecessary
workflow iterations.

### Phase Contracts

Every engineering phase is governed by a Phase Contract.

A Phase Contract defines:

- Objective
- Required Inputs
- Required Deliverables
- Exit Criteria

No engineering phase shall begin until its Required Inputs have been satisfied.

No engineering phase shall conclude until all Required Deliverables have been produced and its Exit Criteria have been met.

Phase Contracts provide deterministic execution boundaries for all Engineering (`E.x`) and Development (`G.x`) stories.

The Environment State Audit establishes the engineering baseline for every
ResumeForge session and shall be completed before the Review phase begins.

### Deliverable Audit

Every Implement phase begins with a Deliverable Audit.

Before implementation work begins, identify:

- Required project artifacts.
- Existing implementation.
- Missing implementation.
- Incomplete implementation.
- Required synchronization updates.

The resulting implementation package shall address every missing deliverable
identified for the current workflow phase.

Deliverable Audit precedes implementation work and establishes the scope of the
implementation package.

### Phase Deliverable Requirements

#### Review Deliverables

- Findings
- Deficiencies
- Evidence
- Required implementation work

#### Implement Deliverables

- Complete implementation updates
- Exact replacement code
- Exact replacement tests
- Exact insertion locations
- Documentation updates

### Implementation Update Specification

Every Implementation Update contained within an Implementation Package shall
follow the standardized structure defined below.

Each Implementation Update shall contain:

1. Implementation Identifier

A unique identifier that provides traceability throughout Story Planning,
Verification, Repository Closeout, and Story Signoff.

2. Primary Section

The exact existing ## heading within the repository document.

3. Secondary Section

The exact existing ### or #### heading.

If no subsection exists, the engineer shall explicitly state that a new
subsection is to be inserted.

4. Anchor Location

The exact insertion point.

Permitted anchor descriptions include:

- Insert before
- Insert after
- Immediately preceding
- Immediately following
- Replace

Paragraph anchors may also be used when required.

5. Implementation Action

Exactly one action shall be specified.

Permitted actions include:

- Insert
- Replace
- Remove
- Rename
- Move

6. Exact Text

The complete text to be inserted or used as the replacement.

Summaries, recommendations, descriptions, and pseudocode are prohibited.

7. Synchronization Updates

Every repository artifact requiring corresponding modification shall be
identified.

8. Implementation Rationale

A concise explanation describing why the update is required.

Implementation Updates shall contain sufficient information for another
engineer to complete the modification without requesting additional
clarification.

#### Verify Deliverables

- Test audit
- Repository audit
- Evidence chain
- Completion assessment
- Signoff recommendation

#### Repository Closeout Commands

Verify: Repository Closeout shall produce the complete Repository Closeout
command sequence required to complete repository closure.

The generated commands shall:

- be presented in execution order;
- be ready for copy/paste execution;
- reflect the current repository state;
- include repository verification commands;
- include staging commands;
- include commit commands;
- include push commands;
- include tag commands;
- include final repository verification commands.

The Verify step prepares repository closure.

It shall not assume that any repository commands have been executed.

### Environment State Audit

Purpose

The Environment State Audit verifies that the engineering environment is
prepared to begin work on the current story.

Responsibilities

• Verify repository availability.
• Verify required engineering documentation.
• Verify Story Continuity.
• Verify engineering environment readiness.
• Verify conditional engineering integrations.

The audit shall conclude with one of the following outcomes:

• Ready
• Ready with Warnings
• Blocked

Environment State Audit shall not:

• Modify project artifacts.
• Perform story planning.
• Produce implementation updates.
• Perform verification.

#### Engineer Responsibilities

Before producing any engineering output, the engineer shall:

1. Refresh Source Authority using the current ResumeForge-WIP repository.
2. Review the governing engineering methodology applicable to the requested phase.
3. Establish the current repository state.
4. Identify repository changes since the previous engineering phase.
5. Base all findings on the current repository rather than conversational memory.

Repository artifacts always supersede conversational context whenever a
difference exists.

### Review

Review begins only after a successful Environment State Audit.

#### Phase Contract

**Objective**

Evaluate the requested engineering work and establish an approved implementation direction.

**Required Inputs**

- Successful Environment State Audit
- Current ResumeForge-WIP repository
- Active Story
- Current engineering methodology

**Required Deliverables**

- Repository Findings
- Engineering Assessment
- Artifact Inventory
- Engineering Recommendations
- Approved Implementation Direction

**Exit Criteria**

Review concludes only when:

- Repository findings are complete.
- Engineering recommendations have been approved.
- Required implementation artifacts have been identified.
- Implementation may begin.

#### Repository Reconciliation

Before beginning Review, compare the current repository against the approved
engineering baseline.

Review shall identify:

- Completed work.
- Remaining work.
- Repository deviations.
- Newly discovered engineering artifacts.

Review findings shall always reflect the current repository state.

The Review step is used to analyze the current artifact, discuss possible
improvements, evaluate alternatives, justify proposed changes, and reach
agreement on the implementation approach.

No artifact modifications occur during Review.

Review concludes only when:

- Requirements are agreed upon.
- Scope is agreed upon.
- Questions are resolved.
- Expected implementation is clearly defined.

---

### Implement

The Implement step applies the approved changes identified during Review.

Implement focuses solely on executing the agreed implementation.

No new requirements, design decisions, or scope changes are introduced during Implement.

Implement concludes only when:

- All approved changes have been applied.
- The artifact reflects the Review agreement.
- No unintended modifications have been introduced.

#### Phase Contract

**Objective**

Execute the implementation approved during Review without introducing new engineering decisions.

**Required Inputs**

- Approved Review
- Current ResumeForge-WIP repository
- Repository reconciliation
- Artifact Inventory

**Required Deliverables**

- Complete Artifact Inventory
- Detailed Implementation Updates
- Repository Anchors
- Implementation Summary

**Exit Criteria**

Implement concludes only when:

- Every required artifact has been updated.
- Every implementation update contains repository-derived anchors.
- No approved implementation work remains incomplete.

#### Artifact Inventory

Every implementation package shall begin with an Artifact Inventory.

The inventory shall identify:

### Artifacts Requiring Modification

List every repository artifact requiring implementation.

### Artifacts Reviewed

List every repository artifact reviewed that requires no modification.

### Deferred Artifacts

List repository artifacts intentionally deferred to future engineering stories.

Implementation Updates shall not begin until the Artifact Inventory has been
completed.

### Required Implementation Update Structure

Every Implement response shall consist of one or more deterministic
Implementation Updates.

Each Implementation Update shall contain, at a minimum:

• File
• Section Reference
• Purpose
• Location Anchor
• Current Text (when replacing existing content)
• Implementation Update
• Expected Result
• Repository Verification
• Repository Location Anchor
• Current Repository State
• Verification Target

Repository anchors shall be derived from the current Source Authority.

Previously generated implementation updates shall not be reused without first
verifying that the repository state remains unchanged.

Location Anchors shall reference text that currently exists within the
Source Authority.

Implementation Updates shall never reference inferred, historical, or
assumed document locations.

When replacing existing content, the Current Text shall be included so
the modification can be applied deterministically.

The term "Suggested Update" shall not be used during any Implement phase.
All approved modifications shall be communicated as Implementation Updates.

Implementation Updates shall describe the exact modification to be
performed.

Implementation Updates shall not contain recommendations, discussion,
design alternatives, or review commentary.

Each Implementation Update shall describe one logical modification.

When multiple unrelated modifications are required, they shall be expressed as
separate Implementation Updates.

Implementation Updates shall remain atomic to simplify implementation,
verification, review history, and corrective iterations.

---

### Verify

Verify confirms that the implementation matches the approved Review.

Verification includes reviewing the implementation, validating supporting evidence, identifying defects, and completing signoff.

Verify concludes only when:

- Implementation matches the approved design.
- Supporting evidence has been reviewed.
- Outstanding issues have been resolved.
- Phase signoff is complete.

#### Phase Contract

**Objective**

Confirm implementation correctness, completeness, and repository synchronization.

**Required Inputs**

- Completed implementation
- Current ResumeForge-WIP repository
- Approved Review

**Required Deliverables**

- Verification Report
- Repository Verification Results
- Completeness Assessment
- Correctness Assessment
- Workflow Disposition

**Exit Criteria**

Verify concludes only when:

- All implementation updates have been verified.
- Artifact Inventory has been reconciled.
- Repository synchronization has been confirmed.

Otherwise the workflow returns to Implement.

#### Completeness Verification

Verify shall evaluate both implementation correctness and implementation
completeness.

Verification shall confirm:

- Every approved implementation update has been completed.
- Every artifact identified in the Artifact Inventory has been evaluated.
- No approved engineering work remains unimplemented.
- Repository documentation remains synchronized.

If implementation is incomplete, the workflow shall return to Implement.

---

### Phase Boundaries

Each engineering phase has exclusive responsibilities.

Environment State Audit shall:

• Verify repository availability.
• Verify Source Authority.
• Verify required engineering documentation.
• Verify story continuity.
• Verify engineering environment readiness.
• Identify conditional engineering integrations.

Environment State Audit shall not:

• Modify project artifacts.
• Perform engineering review.
• Produce implementation updates.
• Perform verification.
• Introduce engineering decisions.

Review shall:

• Analyze the current artifact.
• Discuss improvements.
• Evaluate alternatives.
• Reach engineering agreement.

Review shall not:

• Modify project artifacts.
• Produce implementation instructions.
• Perform verification.

Implement shall:

• Execute the approved engineering agreement.
• Produce deterministic Implementation Updates.

Implement shall not:

• Introduce new requirements.
• Introduce new design decisions.
• Recommend alternative implementations.
• Perform verification.
• Reopen engineering discussions.
• Provide implementation recommendations.
• Suggest optional engineering changes.
• Reevaluate previously approved architectural decisions.
• Generate implementation updates that cannot be directly applied to the
  current Source Authority.

Verify shall:

• Validate completed implementation.
• Identify implementation defects.
• Confirm engineering evidence.
• Approve or reject the phase.

Verify shall not:

• Redesign approved work.
• Expand story scope.
• Produce implementation changes except by returning the workflow to Implement.

### Phase Responsibilities

#### Review

Purpose

Determine the current repository state.

Deliverables

- Findings.
- Deficiencies.
- Evidence.
- Required implementation work.

The Review phase shall not perform implementation.

---

#### Implement

Purpose

Produce all implementation work identified during Review.

Deliverables

- Complete implementation updates.
- Complete replacement code.
- Complete replacement tests.
- Documentation updates.
- Exact insertion locations.

The Implement phase shall not continue the Review phase.

---

#### Verify

Purpose

Validate the completed implementation.

Deliverables

- Test execution audit.
- Repository audit.
- Evidence chain.
- Signoff recommendation.

The Verify phase shall not introduce additional implementation work unless the
workflow returns to Review.

### Verification Failure Rules

Verification determines where the workflow returns when defects are discovered.

Implementation defect

Return to:

Implement

Examples:

- Missing implementation
- Incorrect implementation
- Typographical mistakes
- Missing documentation updates
- Missing tests
- Incorrect code changes

Design or planning defect

Return to:

Review

Examples:

- Scope changes
- Incorrect requirements
- Missing acceptance criteria
- Design changes
- New implementation decisions

The workflow never skips phases.

Every verification failure returns only to the earliest phase required to resolve the identified issue.

### Corrective Workflow

When Verify identifies one or more failures:

1. Record all verification findings.
2. Return only to the earliest required phase.
3. Complete that phase.
4. Repeat Verify for the same engineering phase.
5. Continue this cycle until Verify passes.
6. Advance to the next workflow phase only after successful signoff.

No workflow phase may be skipped during corrective iterations.

If the Environment State Audit concludes with a status of **Blocked**, the
engineering workflow shall not advance to Review until the blocking condition
has been resolved and the audit has been successfully repeated.

### Architectural Decision Finality

When Review identifies multiple valid implementation approaches and one
approach is approved, that decision becomes the authoritative
implementation baseline for the remainder of the story.

Implement and Verify shall evaluate work against the approved
architecture.

The workflow shall not return to Review unless:

- Story requirements change.
- Story scope changes.
- New engineering evidence invalidates the approved architecture.

## Engineering Artifact Types

ResumeForge manages two classes of artifacts.

### Engineering Artifacts

Engineering artifacts define and control the engineering process.

Examples include:

- Story Planning
- Implementation Package (RED)
- Implementation Package (GREEN)
- ResumeForge Engineering Methodology
- Story Signoff

Engineering artifacts always follow the Universal Engineering Phase Lifecycle.

---

### Project Artifacts

Project artifacts describe or support the ResumeForge project itself.

Examples include:

- README.md
- CHECKPOINT.md
- history.md
- testing.md
- phases.md

Project artifacts are updated during engineering phases but are not engineering phases themselves.

## Engineering Artifact Quality Standards

Every engineering artifact shall satisfy the following standards.

### Complete

Contains all information required to perform the work.

### Deterministic

A qualified developer following the artifact should independently produce functionally equivalent results without requiring additional clarification.

### Deterministic Location Identification

Every Location (Current) shall identify the modification point using
sufficient engineering landmarks.

Examples include:

• section heading
• nearby text
• surrounding paragraph
• existing method
• existing class
• existing function
• existing property
• existing documentation heading

A qualified developer unfamiliar with the project shall be able to
navigate directly to the modification without searching or inferring the
intended location.

Repository locations should identify:

- file
- heading
- subsection
- insertion point
- neighboring heading

The objective is to eliminate ambiguity during repository updates.

### Documentation Structure Standard

The ResumeForge Engineering Methodology governs both engineering execution and
the architecture of engineering documentation.

Engineering documentation shall:

- maintain a consistent heading hierarchy;
- provide deterministic navigation;
- provide stable implementation anchor locations;
- minimize duplicate authoritative concepts;
- preserve predictable section ordering;
- support repository-first engineering.

The following repository artifacts are governed by this standard:

- docs/development_workflow.md
- docs/history.md
- CHECKPOINT.md

Each governed document shall define and preserve a stable organizational
structure.

When documentation organization materially impacts engineering execution,
documentation refactoring shall be completed before additional methodology
expansion.

Documentation architecture shall be periodically reviewed as part of the
ResumeForge Engineering Methodology continuous improvement process.

### Engineering Governance Documents

The following repository artifacts collectively govern ResumeForge engineering
execution.

1. docs/development_workflow.md
2. docs/history.md
3. CHECKPOINT.md

Each document has a distinct engineering responsibility.

docs/development_workflow.md

    Defines engineering methodology.

docs/history.md

    Records permanent engineering evolution.

CHECKPOINT.md

    Records current engineering session state and repository recovery
    information.

These artifacts shall evolve together.

Engineering changes affecting one governance document shall evaluate whether
corresponding updates are required within the remaining governance documents.

Collectively these documents constitute the ResumeForge Engineering Governance
System.

### Self-contained

The artifact does not rely upon undocumented assumptions or previous conversations.

### Traceable

Every implementation can be traced back to an approved planning decision.

### Pattern Consistent

Existing implementation patterns are identified and followed unless Review explicitly approves a deviation.

### Incremental

Engineering implementation should extend existing repository artifacts whenever
possible.

Existing implementation should be modified rather than recreated unless the
story explicitly authorizes replacement.

### Reproducible

Independent reviewers should produce equivalent implementations.

### Verifiable

Evidence exists to demonstrate that the implementation satisfies the approved requirements.

## Engineering Contract

ResumeForge follows strict Test-Driven Development (TDD).

Each workflow phase must produce a verifiable engineering artifact before the
next phase may begin.

Story Planning produces the complete Story Planning Package.

The Story Planning Package is the engineering specification for the entire
story.

Story Planning shall establish the baseline against which every subsequent
workflow phase is verified.

### Reference Classification

When reviewing project documentation, terminology, tests, or implementation
references, each relevant reference shall be classified as:

**Active**
Current story, current workflow, current implementation, or current project
state.

**Historical**
Evidence intentionally retained to describe a completed story or prior
project state.

**Pattern Authority**
A prior implementation or documented pattern intentionally referenced as the
approved consistency model for the current work.

**Stale**
A reference that describes superseded active behavior and is not intentionally
retained as Historical or Pattern Authority.

Only Active references are required to describe the current story or workflow.
Historical and Pattern Authority references shall be preserved unless the
current story explicitly requires their revision.

### Pattern Authority

Pattern Authority identifies the existing implementation pattern that shall be
followed for the current story.

Review shall identify the Pattern Authority before implementation begins.

Implement shall follow the approved Pattern Authority unless Review explicitly
approves a deviation.

Verify shall confirm that implementation conforms to the approved Pattern
Authority.

### Source Authority

Source Authority consists of:

- Current WIP repository.
- Production implementation.
- Existing test suite.
- Repository documentation.
- Repository conventions.

All implementation work shall conform to this Source Authority.

## Source Authority

When a ResumeForge WIP artifact is supplied for an engineering phase,
that artifact becomes the authoritative engineering source for the
duration of that phase.

Review, Implement, and Verify responses shall be based upon the current
WIP artifact unless the user explicitly authorizes another source.

Previous revisions, earlier conversations, or historical implementations
shall not supersede the current WIP artifact.

### Source Authority Verification

Review, Implement, and Verify responses shall identify the primary
Source Authority examined.

When implementation guidance depends upon specific project artifacts,
responses shall include sufficient source references (file names,
sections, or code landmarks) to demonstrate that the guidance was
derived from the current Source Authority.

Claims of reviewing the current WIP shall not be made unless the current
WIP artifact has actually been inspected.

## Repository State Audit

### Purpose

The Repository State Audit establishes a verified understanding of the repository immediately before Story Planning begins.

Where Engineering Session Startup Validation confirms that engineering work may begin, the Repository State Audit documents the current repository state from which engineering decisions will be made.

The Repository State Audit becomes the authoritative repository baseline for the current engineering session.

### Objectives

The Repository State Audit shall:

- Establish the current repository baseline.
- Identify repository changes since the previous engineering session.
- Verify repository documentation consistency.
- Verify repository implementation status.
- Identify incomplete engineering work.
- Identify repository anomalies requiring engineering attention.
- Record engineering observations used during Story Planning.

### Repository Review

Review the current repository at a high level.

Examples include:

- Repository structure.
- Documentation organization.
- Story implementation status.
- Engineering artifacts.
- Repository checkpoints.
- Recent repository changes.

The purpose of this review is to ensure that Story Planning is based upon the repository's actual state rather than assumptions carried forward from previous sessions.

### Repository Baseline

Record the repository baseline for the current engineering session.

The baseline should summarize:

- Current repository status.
- Documentation status.
- Active engineering story.
- Repository observations.
- Outstanding engineering work.

This baseline becomes the engineering reference used throughout the remainder of the story.

### Engineering Findings

Record any Engineering Findings discovered during the Repository State Audit.

Engineering Findings may include:

- Documentation inconsistencies.
- Workflow improvements.
- Repository organization improvements.
- Validation improvements.
- Engineering methodology improvements.

Engineering Findings requiring repository modifications shall be incorporated into Story Planning before implementation begins.

### Acceptance Criteria

The Repository State Audit is complete when:

- The repository has been reviewed.
- The repository baseline has been established.
- Repository observations have been recorded.
- Engineering Findings have been documented.
- Repository readiness has been confirmed for Story Planning.

## Deliverable Contracts

### Engineering Deliverable Matrix

### Development Deliverable Matrix

## Repository Patch Unit Manifest

### Repository Patch Manifest

#### Purpose

The Repository Patch Manifest is the authoritative engineering register for every Repository Patch Unit (RPU) defined for the current engineering story.

The Repository Patch Manifest is the authoritative source for:

- Repository Patch Unit identifiers
- Repository Patch Unit titles
- implementation order
- implementation status
- engineering disposition
- implementation dependencies

The Repository Patch Manifest shall always reflect the current engineering baseline.

Historical conversations, engineering memory, and inferred implementation plans shall never supersede the Repository Patch Manifest.

---

#### Repository Patch Manifest Requirements

Each Repository Patch Unit shall contain:

| Field | Description |
|--------|-------------|
| Identifier | Canonical Repository Patch Unit identifier |
| Title | Canonical Repository Patch Unit title |
| Status | Pending, In Progress, Complete, Retired, Merged, Split |
| Classification | Proceed, Revise, Merge, Split, Complete, Retire |
| Dependencies | Required predecessor Repository Patch Units |
| Notes | Engineering remarks |

---

#### Repository Authority

Whenever Review or Implement phases require Repository Patch information, Avery shall recover the Repository Patch Manifest from the repository.

Repository Patch Units shall never be:

- reconstructed;
- inferred;
- renamed;
- abbreviated;
- recreated from memory.

The repository is the authoritative source.

---

#### Repository Manifest Lifecycle

The Repository Patch Manifest shall be updated whenever:

- a Repository Patch Unit is completed;
- a Repository Patch Unit is retired;
- Repository Patch Units are merged;
- Repository Patch Units are split;
- Remaining Work Validation changes the engineering plan.

The Repository Patch Manifest shall always represent the current engineering plan.

### Repository Anchor Package

### Workflow Continuation Contract

### Repository Correction Package

### Repository Patch Lifecycle

### Engineering Standards

### Documentation Standards

### Validation Standards

### Workflow Standards

### Standards Precedence Model

### Engineering Terminology Standard

### Engineering Design Principles

#### Purpose

Engineering Design Principles establish the architectural philosophy that governs the evolution of the ResumeForge Engineering Methodology (REM).

While Engineering Standards define **what** shall be followed, Engineering Design Principles define **why** the methodology is designed as it is and the principles that shall guide future engineering decisions.

Engineering Design Principles provide the long-term architectural direction for the REM.

#### Objectives

Engineering Design Principles shall:

- Promote long-term maintainability.
- Encourage architectural consistency.
- Minimize engineering complexity.
- Eliminate unnecessary duplication.
- Preserve deterministic engineering behavior.
- Guide future methodology evolution.

#### Core Design Principles

##### Single Responsibility

Each engineering concept shall have one primary responsibility.

Repository sections shall represent one architectural concern and shall avoid combining unrelated concepts.

##### Single Source of Truth

Engineering concepts shall be defined exactly once.

Workflow documentation shall reference authoritative definitions rather than duplicate them.

##### Separation of Concerns

Governance, execution, validation, documentation, and implementation shall remain independent architectural domains.

Each domain shall evolve independently while remaining integrated through defined contracts.

##### Deterministic Engineering

Engineering outcomes shall not depend upon interpretation.

Every workflow, repository modification, and validation activity shall produce predictable, repeatable results.

##### Explicit Over Implicit

Engineering intent shall be explicitly documented.

Repository organization, workflow progression, and engineering expectations shall never rely upon inferred behavior.

##### Progressive Refinement

Higher-level guidance shall establish architectural intent.

Lower-level workflow documentation shall progressively refine implementation details without redefining higher-level guidance.

##### Repository-First Design

Repository modifications shall always be designed around repository integrity before implementation convenience.

Repository organization shall take precedence over workflow shortcuts.

##### Continuous Improvement

Engineering Findings produced during Engineering Stories shall be evaluated for incorporation into the REM.

Accepted findings shall improve existing standards whenever possible before introducing new methodology concepts.

#### Architectural Principles

The ResumeForge Engineering Methodology shall strive to achieve:

- High cohesion.
- Low coupling.
- Minimal duplication.
- Maximum traceability.
- Predictable workflow execution.
- Clear architectural boundaries.

#### Engineering Decision Framework

When multiple engineering solutions are possible, preference shall be given to the solution that:

1. Preserves repository integrity.
2. Reduces methodology complexity.
3. Eliminates duplication.
4. Improves maintainability.
5. Increases engineering determinism.
6. Enhances traceability.

#### Engineering Requirement

All future Engineering (E.x) and Development (G.x) stories shall be evaluated against these Engineering Design Principles.

Engineering Stories shall strengthen adherence to these principles rather than introduce unnecessary architectural complexity.

#### Purpose

The Engineering Terminology Standard establishes the authoritative vocabulary used throughout the ResumeForge Engineering Methodology (REM).

It ensures that every engineering artifact, workflow, repository update, and engineering communication uses a consistent set of defined terms.

Engineering terminology shall be defined once and referenced throughout the methodology.

#### Objectives

The Engineering Terminology Standard shall:

- Establish a common engineering vocabulary.
- Eliminate terminology drift.
- Improve engineering communication.
- Reduce ambiguity.
- Support deterministic engineering execution.
- Promote long-term maintainability.

#### Terminology Principles

Engineering terminology shall adhere to the following principles:

- One authoritative definition per term.
- One meaning per term.
- Terms shall not be redefined by workflow-specific guidance.
- Workflow documentation shall reference defined terminology.
- New terminology shall be introduced only through approved Engineering Stories.

#### Core Engineering Terms

##### Engineering Story

A methodology story whose primary objective is to improve the ResumeForge Engineering Methodology itself.

Engineering Stories use the **E.x** numbering convention.

##### Development Story

A methodology story whose primary objective is to implement repository functionality.

Development Stories use the **G.x** numbering convention.

##### Repository Patch Unit (RPU)

A single, self-contained repository modification performed during Repository Patch Specifications (GREEN).

Each Repository Patch Unit performs exactly one logical repository change.

##### Repository Update Package (RUP)

The complete repository-ready modification generated for a Repository Patch Unit.

A Repository Update Package contains all information necessary to apply the repository modification.

##### Update Implementation Package (UIP)

The implementation artifact delivered during an Implement phase.

The UIP is repository-ready and requires no additional engineering analysis before application.

##### Deliverable Contract

The authoritative definition of the expected outputs for a workflow phase.

Each workflow phase shall satisfy its Deliverable Contract before progression.

##### Entry Contract

The engineering activities required before implementation begins.

The Entry Contract consists of:

- Applied Repository Review
- Repository Baseline Confirmation
- Repository Authorization

##### Exit Contract

The engineering activities required before workflow progression.

The Exit Contract is fulfilled by the Workflow Continuation Contract.

##### Canonical Application Anchor

The single authoritative instruction defining where a repository modification shall be applied.

Each Repository Patch Unit shall define exactly one Canonical Application Anchor.

##### Applied Repository Review

A review of the repository after previously approved modifications have been applied.

The purpose of the review is to establish the inherited engineering baseline.

##### Repository Baseline

The validated repository structure inherited by the current Repository Patch Unit.

All implementation shall begin from the confirmed Repository Baseline.

##### Repository Authorization

Formal engineering approval allowing repository implementation to proceed.

##### Repository Correction Package

The engineering recovery mechanism used when the inherited repository state fails validation.

##### Repository Patch Lifecycle

The authoritative execution model governing all Repository Patch Units.

#### Terminology Governance

All engineering documentation shall use the terminology defined in this standard.

Existing terms shall not be redefined.

Workflow-specific terminology shall supplement—but never replace—the Engineering Terminology Standard.

#### Engineering Requirement

Every Engineering (E.x) and Development (G.x) story shall use the terminology defined by the Engineering Terminology Standard.

Engineering responses shall remain consistent with these definitions throughout the ResumeForge Engineering Methodology.

#### Purpose

The Standards Precedence Model establishes the authoritative order used to resolve conflicts, overlaps, or ambiguity between ResumeForge Engineering Methodology (REM) standards.

This model ensures that all engineering decisions are governed by a single deterministic precedence hierarchy.

#### Objectives

The Standards Precedence Model shall:

- Eliminate conflicting guidance.
- Provide deterministic engineering decision-making.
- Define authoritative governance precedence.
- Prevent duplication of engineering rules.
- Promote long-term maintainability.
- Establish a single conflict-resolution mechanism.

#### Standards Hierarchy

The ResumeForge Engineering Methodology shall apply standards in the following order of precedence:

1. Engineering Standards
2. Documentation Standards
3. Validation Standards
4. Workflow Standards
5. Story-Specific Guidance

Each lower level supplements—but shall never contradict—a higher level.

#### Responsibilities

##### Engineering Standards

Define overarching engineering governance.

Responsible for:

- Engineering principles.
- Repository governance.
- Methodology governance.
- Standards governance.

##### Documentation Standards

Define documentation behavior.

Responsible for:

- Repository organization.
- Section architecture.
- Documentation formatting.
- Documentation maintenance.

##### Validation Standards

Define engineering verification.

Responsible for:

- Repository validation.
- Workflow validation.
- Story validation.
- Engineering approval.

##### Workflow Standards

Define workflow execution.

Responsible for:

- Workflow progression.
- Deliverable Contracts.
- Entry and Exit Contracts.
- Repository execution.

##### Story-Specific Guidance

Defines implementation details unique to an individual Engineering or Development story.

Story guidance may specialize higher-level standards but shall never supersede them.

#### Conflict Resolution

When multiple standards appear applicable:

1. Evaluate the highest applicable standard.
2. Apply higher-level governance first.
3. Apply lower-level guidance only when consistent with higher-level standards.
4. Escalate unresolved conflicts through an Engineering Story.

Conflicting lower-level guidance shall be considered non-authoritative.

#### Standard Inheritance

Lower-level standards inherit behavior from higher-level standards.

Inheritance shall be cumulative.

A lower-level standard may extend—but shall not redefine or invalidate—the behavior established by a higher-level standard.

#### Engineering Requirement

Every Engineering (E.x) and Development (G.x) story shall comply with the Standards Precedence Model.

Engineering decisions shall always be traceable to the highest applicable governing standard.

When uncertainty exists, engineers shall consult the Standards Precedence Model before introducing new workflow guidance.

#### Purpose

Workflow Standards establish the authoritative rules governing the execution, progression, and completion of engineering workflows within the ResumeForge Engineering Methodology (REM).

These standards define how Engineering (E.x) and Development (G.x) stories progress through each workflow phase and ensure all engineering activities are deterministic, repeatable, and traceable.

Workflow documentation shall reference these standards rather than redefining workflow behavior.

#### Objectives

Workflow Standards shall:

- Establish deterministic workflow execution.
- Standardize workflow progression.
- Define workflow entry and exit criteria.
- Govern engineering deliverables.
- Eliminate workflow ambiguity.
- Promote repeatable engineering execution.

#### Workflow Standard Categories

##### Workflow Execution Standards

Govern execution of engineering workflows.

Examples include:

- Story Planning
- Repository Test Specifications (RED)
- Repository Patch Specifications (GREEN)
- Story Signoff

##### Deliverable Standards

Govern workflow outputs.

Examples include:

- Deliverable Contracts
- Engineering Deliverable Matrix
- Development Deliverable Matrix
- Repository Update Packages

##### Workflow Transition Standards

Govern movement between workflow phases.

Examples include:

- Entry Contract (Pre-Implementation Validation)
- Exit Contract (Workflow Continuation Contract)
- Repository Authorization
- Repository Readiness Gates

##### Workflow Recovery Standards

Govern interruption and recovery.

Examples include:

- Repository Correction Package
- Repository Revalidation
- Engineering Findings
- Repository Authorization Recovery

##### Workflow Governance Standards

Govern engineering behavior throughout execution.

Examples include:

- One logical objective per workflow step.
- Repository-first implementation.
- Evidence-based engineering decisions.
- Repository-ready deliverables.
- Complete implementation packages.

#### Workflow Principles

Every workflow shall follow these principles:

- One authoritative workflow path.
- One logical objective per workflow step.
- Deterministic progression.
- Validation before progression.
- Repository-first engineering.
- Explicit workflow transitions.
- Complete engineering traceability.

#### Workflow Progression

Every Engineering and Development story shall progress through the following lifecycle:

1. Story Planning
2. Repository Test Specifications (RED)
3. Repository Patch Specifications (GREEN)
4. Story Signoff

Each phase shall satisfy its Deliverable Contract before progression is authorized.

No workflow phase shall begin until the preceding phase has successfully completed.

#### Workflow Deliverables

Each workflow phase shall produce repository-ready deliverables appropriate to that phase.

Review phases shall produce engineering analysis and implementation planning.

Implement phases shall produce complete repository-ready implementation artifacts.

Verify phases shall confirm engineering correctness and readiness for progression.

#### Engineering Requirement

All Engineering (E.x) and Development (G.x) stories shall conform to the Workflow Standards.

Workflow-specific guidance shall supplement these standards but shall not conflict with or redefine them.

Where workflow guidance conflicts with Engineering, Documentation, or Validation Standards, the established standards precedence hierarchy shall apply.

#### Purpose

Validation Standards establish the authoritative rules governing verification activities performed throughout the ResumeForge Engineering Methodology.

These standards define how engineering work is validated, how repository integrity is confirmed, and how workflow completion is objectively determined.

All validation performed during Engineering (E.x) and Development (G.x) stories shall conform to these standards.

#### Objectives

Validation Standards shall:

- Ensure engineering correctness.
- Verify repository integrity.
- Confirm documentation quality.
- Establish deterministic completion criteria.
- Provide objective engineering approval.
- Support repeatable engineering execution.

#### Validation Standard Categories

##### Repository Validation Standards

Govern validation of repository modifications.

Examples include:

- Applied Repository Review.
- Repository Baseline Confirmation.
- Repository Authorization.
- Repository Correction Package.

##### Workflow Validation Standards

Govern workflow completion.

Examples include:

- Deliverable Contract verification.
- Workflow phase completion.
- Workflow Continuation Contract validation.
- Story completion validation.

##### Documentation Validation Standards

Govern engineering documentation quality.

Examples include:

- Repository Copy/Paste Test.
- Heading hierarchy verification.
- Canonical Application Anchor validation.
- Resulting Hierarchy verification.
- Cross-reference validation.

##### Engineering Validation Standards

Govern engineering artifacts.

Examples include:

- Engineering Traceability.
- Engineering Findings.
- Engineering Decision Records.
- Evidence Chain validation.
- Deliverable Matrix compliance.

##### Story Validation Standards

Govern Engineering and Development story completion.

Examples include:

- Story Planning validation.
- RED validation.
- GREEN validation.
- Story Signoff validation.

#### Validation Principles

Validation shall always be:

- Deterministic.
- Repeatable.
- Evidence-based.
- Repository-first.
- Independent of implementation assumptions.

Engineering approval shall always be supported by objective validation evidence.

#### Validation Lifecycle

Validation occurs throughout repository implementation:

1. Entry Validation (Pre-Implementation Validation)
2. Implementation Validation (Post-Application Validation)
3. Completion Validation (RPU Readiness Gate)
4. Workflow Validation (Workflow Continuation Contract)
5. Story Validation (Story Signoff)

Each validation stage establishes the baseline for the next stage.

#### Engineering Requirement

Every workflow response shall satisfy the applicable Validation Standards before progression to the next workflow activity.

Workflow completion shall never be declared without successful validation.

Where multiple validation mechanisms apply, all applicable validations shall succeed before engineering approval is granted.

#### Purpose

Documentation Standards establish the authoritative rules governing the structure, organization, formatting, and maintenance of ResumeForge engineering documentation.

These standards ensure that all methodology documentation is consistent, deterministic, maintainable, and easy to navigate.

Workflow sections shall reference these standards rather than redefining documentation conventions.

#### Objectives

Documentation Standards shall:

- Establish a consistent document architecture.
- Promote deterministic document organization.
- Eliminate documentation ambiguity.
- Improve long-term maintainability.
- Standardize engineering communication.
- Reduce documentation duplication.

#### Documentation Standard Categories

##### Document Structure Standards

Govern the organization of engineering documentation.

Examples include:

- Heading hierarchy.
- Parent/child section relationships.
- Section ordering.
- Major section sequencing.

##### Repository Update Standards

Govern repository modifications.

Examples include:

- Canonical Application Anchors.
- Single authoritative insertion point.
- Resulting Hierarchy.
- Repository-ready Markdown.
- Repository Patch Units.

##### Engineering Communication Standards

Govern engineering responses.

Examples include:

- Engineering Findings.
- Engineering Rationale.
- Engineering Observations.
- Validation Packages.
- Workflow Continuation Contracts.

##### Traceability Standards

Govern engineering traceability.

Examples include:

- Engineering Traceability tables.
- Engineering Decision Records.
- Repository Update Packages.
- Evidence Chains.
- Deliverable Matrices.

##### Validation Standards

Govern documentation verification.

Examples include:

- Repository Copy/Paste Tests.
- Post-Application Validation.
- Repository Readiness Gates.
- Repository Baseline Confirmation.

#### Documentation Organization Principles

ResumeForge documentation shall adhere to the following principles:

- One authoritative definition per concept.
- References instead of duplication.
- Deterministic section placement.
- Consistent heading hierarchy.
- Explicit architectural justification.
- Repository-first organization.

#### Documentation Maintenance

Documentation Standards shall evolve only through approved Engineering Stories.

When an Engineering Finding affects documentation practices, the corresponding Documentation Standard shall be updated instead of duplicating guidance elsewhere.

Workflow documentation shall inherit documentation behavior from these standards.

#### Engineering Requirement

All ResumeForge engineering documentation shall conform to the Documentation Standards.

Where documentation guidance conflicts with workflow-specific instructions, the precedence hierarchy defined by the Engineering Standards shall apply.

#### Purpose

Engineering Standards establish the authoritative rules governing the creation, validation, maintenance, and evolution of the ResumeForge Engineering Methodology.

Rather than repeating common engineering requirements throughout workflow documentation, the ResumeForge Engineering Methodology shall reference these Engineering Standards as the single source of truth.

#### Objectives

Engineering Standards shall:

- Promote consistency throughout the methodology.
- Reduce duplication across workflow documentation.
- Improve maintainability.
- Increase engineering traceability.
- Establish deterministic engineering behavior.
- Define repository engineering best practices.

#### Engineering Standard Categories

The ResumeForge Engineering Methodology recognizes the following Engineering Standards:

##### Repository Standards

Govern repository organization and repository modifications.

Examples include:

- Repository Patch Lifecycle
- Repository Anchor Package
- Repository Patch Unit Manifest

##### Workflow Standards

Govern workflow execution.

Examples include:

- Workflow Continuation Contract
- Deliverable Contracts
- Deliverable Matrices

##### Validation Standards

Govern engineering validation.

Examples include:

- Pre-Implementation Validation (PIV)
- Repository Baseline Confirmation
- Repository Readiness Gates
- Validation Packages

##### Documentation Standards

Govern methodology documentation.

Examples include:

- Canonical Application Anchors
- Resulting Hierarchies
- Architectural Placement Justification
- Engineering Traceability

##### Story Standards

Govern Engineering (E.x) and Development (G.x) stories.

Examples include:

- Story Planning
- Repository Test Specifications
- Repository Patch Specifications
- Story Signoff

#### Standard Hierarchy

Engineering Standards are hierarchical.

Lower-level workflow guidance shall reference Engineering Standards rather than redefining them.

Engineering Standards shall remain the authoritative source.

#### Standard Evolution

Engineering Standards may be introduced or modified only through approved Engineering Stories.

Engineering Findings accepted during an Engineering Story shall be incorporated into the applicable Engineering Standard rather than duplicated elsewhere in the methodology.

#### Engineering Requirement

All ResumeForge Engineering Methodology documentation shall conform to the Engineering Standards defined herein.

Conflicting workflow guidance shall be resolved in favor of the applicable Engineering Standard.

#### Purpose

The Repository Patch Lifecycle defines the complete engineering lifecycle followed by every Repository Patch Unit (RPU).

It establishes the authoritative execution model governing repository modification, validation, recovery, and workflow progression.

Every Repository Patch Unit shall follow this lifecycle without exception.

#### Lifecycle Overview

The Repository Patch Lifecycle consists of three primary phases:

1. Pre-Implementation Validation (Entry Contract)
2. Repository Patch Unit Execution
3. Workflow Continuation (Exit Contract)

If repository validation fails, execution transitions into the Repository Correction Package before implementation may resume.

#### Phase I — Pre-Implementation Validation (Entry Contract)

The Entry Contract establishes the engineering baseline before repository modification begins.

This phase shall perform:

- Applied Repository Review
- Applied Repository Validation
- Repository Baseline Confirmation
- Repository Authorization

The Entry Contract shall conclude with one of the following outcomes:

- Repository Authorized
- Repository Correction Required

No repository modification shall begin until Repository Authorization has been granted.

#### Phase II — Repository Patch Unit Execution

Repository Patch Unit Execution performs one deterministic repository modification.

Every Repository Patch Unit shall contain:

- Repository Target
- Primary Section
- Update Type
- Canonical Application Anchor
- Repository-Ready Markdown
- Resulting Hierarchy
- Post-Application Validation
- Architectural Placement Justification
- Cross-Reference Impact
- Engineering Traceability
- Validation Package
- RPU Readiness Gate
- RPU Status

Only one logical repository modification shall be performed per Repository Patch Unit.

#### Repository Recovery Path

If the Entry Contract fails, implementation shall immediately transition into the Repository Correction Package.

Recovery shall:

- Document repository findings.
- Define required corrections.
- Restore repository integrity.
- Repeat Pre-Implementation Validation.

Implementation shall not continue until Repository Authorization has been restored.

#### Phase III — Workflow Continuation (Exit Contract)

The Exit Contract formally concludes the Repository Patch Unit.

Every Exit Contract shall contain:

- Current Step Status
- Repository Status
- Next Workflow Step
- Next Repository Patch Unit (or equivalent activity)
- Exact Next Command

The Exit Contract establishes the engineering baseline inherited by the next Repository Patch Unit.

#### Lifecycle Diagram

```text
                Repository Patch Lifecycle

        ┌─────────────────────────────────────┐
        │ Phase I                             │
        │ Pre-Implementation Validation       │
        │ (Entry Contract)                    │
        └─────────────────────────────────────┘
                      │
                      ▼
        Repository Authorized?
             │                 │
            YES               NO
             │                 │
             ▼                 ▼
┌─────────────────────┐   ┌──────────────────────┐
│ Phase II            │   │ Repository           │
│ Repository Patch    │   │ Correction Package   │
│ Unit Execution      │   └──────────────────────┘
└─────────────────────┘             │
             │                      │
             └──────────────┬───────┘
                            ▼
              Repeat Entry Contract
                            │
                            ▼
        ┌─────────────────────────────────────┐
        │ Phase III                           │
        │ Workflow Continuation               │
        │ (Exit Contract)                     │
        └─────────────────────────────────────┘
                            │
                            ▼
           Next Repository Patch Unit
```

#### Engineering Requirements

Every Repository Patch Unit shall comply with the Repository Patch Lifecycle.

Deviation from this lifecycle shall constitute an incomplete Repository Patch Unit.

The Repository Patch Lifecycle is the authoritative execution model governing all Repository Patch Specifications (GREEN).

#### Purpose

The Repository Correction Package defines the standard procedure followed when a Repository Patch Unit cannot proceed because the inherited repository state fails validation during Pre-Implementation Validation (PIV).

The Repository Correction Package ensures repository integrity is restored before additional repository modifications are introduced.

#### Trigger Conditions

A Repository Correction Package shall be generated whenever:

- Applied Repository Review identifies repository inconsistencies.
- Repository Baseline Confirmation fails.
- Canonical Application Anchor cannot be resolved.
- Repository hierarchy differs from the expected Resulting Hierarchy.
- Post-Application Validation from the previous Repository Patch Unit fails.
- Repository modifications have been applied incorrectly.

No subsequent Repository Patch Unit shall begin until all identified issues have been corrected and revalidated.

#### Repository Correction Package Components

Every Repository Correction Package shall contain:

- Repository Review Findings.
- Validation Failure Summary.
- Repository Impact Assessment.
- Required Repository Corrections.
- Repository Revalidation Procedure.
- Repository Readiness Criteria.

These components provide a complete engineering recovery path.

#### Repository Revalidation

After corrections have been applied:

1. Perform a new Applied Repository Review.
2. Repeat Applied Repository Validation.
3. Reconfirm the Repository Baseline.
4. Reauthorize repository implementation.

Only after successful revalidation may implementation resume.

#### Engineering Requirement

The Repository Correction Package is the authoritative recovery mechanism for Repository Patch Specifications (GREEN).

Repository implementation shall remain suspended until the Repository Correction Package has been successfully completed and repository authorization has been restored.

#### Purpose

The Workflow Continuation Contract formally closes the current engineering workflow step and provides the deterministic transition to the next workflow step.

Every Engineering (E.x) and Development (G.x) workflow response shall conclude with a Workflow Continuation Contract.

The Workflow Continuation Contract eliminates workflow ambiguity by explicitly identifying the next engineering action.

#### Objectives

The Workflow Continuation Contract shall:

- Declare completion status of the current workflow step.
- Record the current repository state.
- Identify the next workflow step.
- Identify the next Repository Patch Unit or implementation activity.
- Provide the exact command required to continue the workflow.

#### Workflow Continuation Components

Every Workflow Continuation Contract shall contain:

- Current Step Status.
- Repository Status.
- Next Workflow Step.
- Next Repository Patch Unit or equivalent implementation activity.
- Exact Next Command.

These components collectively provide a deterministic workflow handoff.

#### Engineering Requirements

The Exact Next Command shall:

- Be complete.
- Be copy-and-paste ready.
- Match the current engineering story.
- Identify the correct workflow phase.
- Identify the correct implementation section.
- Reference the current ResumeForge-WIP.zip repository.

If the engineering workflow is complete, the Workflow Continuation Contract shall instead identify the next workflow phase (for example, Story Signoff) or explicitly state that the story has reached completion.

#### Workflow Responsibility

The Workflow Continuation Contract is the authoritative workflow transition mechanism.

Engineers shall use the Exact Next Command as the sole entry point into the next engineering activity.

Workflow progression shall not rely upon operator memory or interpretation.

#### Engineering Requirement

Every engineering workflow response shall terminate with a Workflow Continuation Contract.

Responses shall not conclude without either:

- Providing the Exact Next Command; or
- Declaring successful completion of the current story.

#### Purpose

The Repository Anchor Package defines the standard used to locate, apply, and validate repository modifications.

Every Repository Patch Unit shall include a Repository Anchor Package to ensure repository updates are deterministic, reproducible, and independently verifiable.

The Repository Anchor Package separates repository modification from repository validation.

#### Repository Anchor Components

Every Repository Anchor Package shall contain:

- Repository Target
- Primary Section
- Update Type
- Canonical Application Anchor
- Resulting Hierarchy
- Post-Application Validation
- Architectural Placement Justification

These components collectively define where a repository modification belongs and how its successful application shall be verified.

#### Canonical Application Anchor

The Canonical Application Anchor is the single authoritative instruction describing where a repository modification shall be applied.

A Repository Patch Unit shall define exactly one Canonical Application Anchor.

Insertion ranges shall not be used.

Examples include:

- Immediately before an existing heading.
- Immediately after an existing subsection.
- Replace an existing named section.

The Canonical Application Anchor shall always reference the highest available structural element within the repository.

#### Resulting Hierarchy

Resulting Hierarchy illustrates the repository structure expected after the modification has been applied.

Its purpose is to communicate the intended architectural outcome rather than provide implementation instructions.

#### Post-Application Validation

Post-Application Validation verifies that the repository modification has been applied successfully.

Validation shall confirm:

- Correct repository hierarchy.
- Correct heading relationships.
- Correct placement of the repository modification.
- Preservation of surrounding repository structure.

Validation shall not introduce new repository modifications.

#### Architectural Placement Justification

Every Repository Patch Unit shall explain why the modification belongs at its specified location.

Architectural placement shall be justified using repository organization, workflow sequence, engineering dependencies, or documentation architecture.

#### Engineering Requirement

Repository modifications shall be governed by the Repository Anchor Package.

No Repository Patch Unit shall be considered complete until the Repository Anchor Package has been fully satisfied and validated.

#### Purpose

The Repository Patch Unit (RPU) Manifest defines the complete set of Repository Patch Units required to implement a Repository Patch Specifications (GREEN) phase.

The manifest serves as the engineering implementation roadmap by identifying every Repository Patch Unit, its implementation sequence, and its completion status.

A Repository Patch Specifications (GREEN) implementation shall begin with creation of the Repository Patch Unit Manifest before implementation of the first Repository Patch Unit.

#### Objectives

The Repository Patch Unit Manifest shall:

- Enumerate every Repository Patch Unit required for the story.
- Define the implementation order.
- Establish implementation dependencies.
- Track Repository Patch Unit completion.
- Provide implementation progress visibility.
- Serve as the authoritative implementation plan for the GREEN phase.

#### Repository Patch Unit Entry

Each Repository Patch Unit entry shall contain:

- Repository Patch Unit identifier.
- Repository Patch Unit title.
- Repository target.
- Implementation purpose.
- Dependency information.
- Current implementation status.

#### Manifest Maintenance

The Repository Patch Unit Manifest shall be updated throughout implementation.

Repository Patch Units shall transition through the following states:

- Planned
- In Progress
- Complete
- Verified

The manifest shall always reflect the current implementation status of the repository.

#### Engineering Requirement

The Repository Patch Unit Manifest is the authoritative implementation tracker for Repository Patch Specifications (GREEN).

All Repository Patch Units shall originate from the manifest.

Repository Patch Units not defined within the manifest shall not be implemented unless the manifest is formally updated through Story Planning or an approved Engineering Finding.

#### Purpose

The Development Deliverable Matrix defines the required deliverables for each workflow command used during Development (G.x) stories.

The matrix establishes the authoritative completion contract for feature development by defining the minimum repository-ready artifacts required before each workflow step may be considered complete.

#### Matrix

| Workflow Command | Required Deliverables |
|------------------|-----------------------|
| Initiate: Story Planning | Story Identification, Capability Recommendation, Story Naming Options, Engineering Decision Record |
| Review: Story Planning | Functional Analysis, Repository Assessment, Documentation Audit, Story Scope Validation, Engineering Findings |
| Implement: Story Planning | Complete Story Planning Package, Documentation Update Package (DUP), Story Deliverable Matrix, Engineering Traceability |
| Verify: Story Planning | Story Planning Validation, Documentation Validation, Repository Readiness Confirmation |
| Review: Implementation Package (RED) | Production Code Analysis, Test Strategy, RED Test Mapping, Repository Test Analysis |
| Implement: Implementation Package (RED) | Repository Test Suite, Expected Failure Documentation, Repository Update Manifest, Engineering Traceability |
| Verify: Implementation Package (RED) | Expected Failure Validation, RED Completion Confirmation, Repository Readiness |
| Review: Implementation Package (GREEN) | Repository Patch Analysis, Repository Patch Manifest, GREEN Implementation Strategy |
| Implement: Implementation Package (GREEN) | Pre-Implementation Validation (PIV), Repository Patch Unit(s), Repository-Ready Markdown, Workflow Continuation Contract |
| Verify: Implementation Package (GREEN) | Repository Validation, Functional Validation, Repository Readiness Confirmation |
| Review: Story Signoff | Repository Audit, Documentation Audit, Feature Completion Review, Engineering Findings |
| Implement: Story Signoff | Story Completion Package, Repository Synchronization Package, Documentation Synchronization, Engineering Summary |
| Verify: Story Signoff | Final Repository Validation, Story Acceptance Confirmation, Story Closure Authorization |

#### Development Requirements

Development workflow responses shall satisfy the deliverables defined within this matrix.

Completion of a workflow step shall not be declared until every required deliverable for that workflow command has been produced.

The Development Deliverable Matrix is the authoritative contract governing Development (G.x) stories.

Engineering (E.x) stories are governed independently by the Engineering Deliverable Matrix.

#### Purpose

The Engineering Deliverable Matrix defines the expected deliverables for each workflow command used during Engineering (E.x) stories.

The matrix establishes the minimum engineering artifacts that shall be produced for every workflow phase and serves as the engineering completion contract for methodology development.

#### Matrix

| Workflow Command | Required Deliverables |
|------------------|-----------------------|
| Initiate: Story Planning | Story Identification, Engineering Decision Record, Story Naming Options, Initial Story Recommendation |
| Review: Story Planning | Engineering Analysis, Repository Assessment, Documentation Audit, Engineering Findings, Story Planning Recommendations |
| Implement: Story Planning | Complete Story Planning Package, Documentation Update Package, Repository Update Manifest, Engineering Traceability |
| Verify: Story Planning | Story Planning Validation, Repository Validation, Engineering Approval |
| Review: Repository Test Specifications (RED) | Repository Test Analysis, Test Strategy, Expected Repository Failures |
| Implement: Repository Test Specifications (RED) | Repository Test Specifications, Repository Test Suite, Expected Failure Documentation |
| Verify: Repository Test Specifications (RED) | Repository Test Validation, Expected Failure Confirmation |
| Review: Repository Patch Specifications (GREEN) | Repository Patch Analysis, Repository Patch Manifest, Repository Strategy |
| Implement: Repository Patch Specifications (GREEN) | Pre-Implementation Validation, Repository Patch Unit(s), Workflow Continuation Contract |
| Verify: Repository Patch Specifications (GREEN) | Repository Validation, Repository Readiness Confirmation, Engineering Approval |
| Review: Story Signoff | Repository Audit, Documentation Audit, Engineering Review |
| Implement: Story Signoff | Story Completion Package, Repository Synchronization Package, Engineering Summary |
| Verify: Story Signoff | Final Repository Validation, Engineering Approval, Story Closure |

#### Engineering Requirement

Every workflow command shall satisfy the deliverables defined within this matrix.

Workflow completion shall not be declared until all required deliverables have been produced.

The Engineering Deliverable Matrix is authoritative for Engineering (E.x) stories.

Development (G.x) stories shall define an independent Development Deliverable Matrix.

### Purpose

Deliverable Contracts define the required outputs for each Engineering Methodology workflow command.

A Deliverable Contract specifies the minimum repository-ready artifacts that shall be produced before a workflow step may be considered complete.

Every Engineering (E.x) and Development (G.x) workflow command shall satisfy its corresponding Deliverable Contract.

### Principles

Deliverable Contracts ensure that:

- Workflow expectations are explicit.
- Required engineering artifacts are consistently produced.
- Workflow completion is objectively verifiable.
- Engineering sessions remain reproducible.
- Repository-ready deliverables are generated for every implementation step.

### Contract Structure

Each Deliverable Contract shall define:

- Required engineering artifacts.
- Required validation activities.
- Required repository-ready outputs.
- Completion criteria.
- Workflow transition requirements.

### Engineering Story Deliverables

Engineering stories produce methodology and repository documentation.

Typical deliverables include:

- Engineering Findings.
- Repository Patch Specifications.
- Repository Patch Units.
- Repository-ready documentation.
- Engineering workflow improvements.

### Development Story Deliverables

Development stories produce software implementation artifacts.

Typical deliverables include:

- Story Planning Package.
- Repository Test Specifications (RED).
- Repository Patch Specifications (GREEN).
- Story Signoff Package.
- Repository synchronization updates.

### Completion Rule

A workflow step is complete only when:

- All required Deliverable Contract artifacts have been produced.
- Required validation has passed.
- Repository-ready outputs have been generated where applicable.
- The Workflow Continuation Contract has been provided.

Failure to satisfy the Deliverable Contract shall prevent progression to the next workflow step.

## Story Planning

### Engineering Charter

Engineering stories shall begin with an Engineering Charter.

The Engineering Charter establishes the engineering problem being solved,
defines the desired outcome, identifies the scope of the work, and
documents the engineering constraints that govern implementation.

The Engineering Charter shall be completed before Story Planning is
considered complete.

Minimum contents:

• Current
• Needed
• Objective
• Definition of Success
• Scope
• Constraints

### Planning Philosophy

Story Planning produces engineering artifacts rather than engineering
ideas.

Every implementation expected during later phases shall be planned during
Story Planning.

Review refines the design.

Implement executes the approved plan.

Verify confirms the implementation matches the approved plan.

Planning should eliminate ambiguity rather than defer it.

### Pre-Phase Readiness Checklist

Before beginning any Review, Implement, or Verify phase, confirm:

□ Current ResumeForge-WIP is available (when referenced).
□ Source Authority has been established.
□ Required external connections (GitHub, repository access, etc.) have
been verified when applicable.
□ The engineering phase is using the current project state rather than
historical context.

If any prerequisite cannot be confirmed, the phase shall stop and report
the blocking condition before engineering work begins.

### Story Planning Lifecycle

Story Planning consists of three distinct activities:

1. Review
2. Implement
3. Verify

Review establishes the engineering agreement for the story.

Implement updates the Story Planning artifacts so they accurately reflect the
approved engineering agreement.

Verify confirms that the completed Story Planning artifacts accurately reflect
the approved engineering agreement and are ready for Story Planning Signoff.

Story Planning Signoff authorizes entry into:

Review: Implementation Package (RED)

Once Story Planning has been approved, all remaining workflow phases shall
validate conformance to the approved Story Planning Package rather than
redefining story requirements.

Following Story Planning Signoff, every remaining workflow phase shall validate
conformance to the approved Story Planning Package rather than redefining story
requirements.

It shall contain every piece of information required to complete all remaining
workflow phases without introducing assumptions.

### Planning Deliverables Register

Story Planning shall produce a Deliverables Register.

The Deliverables Register defines every artifact that will be produced
during the story.

Each deliverable shall receive a unique identifier.

Minimum fields:

• Deliverable ID
• Deliverable Name
• Planned Phase
• Description
• Verification Method

### Review Responsibilities

Review: Story Planning establishes the engineering agreement.

The review shall:

• Define story scope.
• Define business purpose.
• Define engineering objectives.
• Identify Pattern Authority.
• Identify Source Authority.
• Identify expected implementation pattern.
• Identify expected RED deliverables.
• Resolve planning questions before documentation is finalized.

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

Engineering stories shall additionally produce:

• Engineering Charter
• Deliverables Register
• Requirements Register
• Acceptance Criteria Matrix

Requirements Register

Every story shall maintain a Requirements Register.
Each requirement shall receive a unique identifier.
Each requirement shall later be traceable to:

• its implementation,
• its verification,
• its acceptance status.

This register becomes the basis for Story Signoff and Release Readiness.

### Verification Responsibilities

Verify: Story Planning confirms that the planning documentation accurately
reflects the approved engineering agreement.

Verification shall confirm:

• Story name
• Story objective
• Business purpose
• Scope
• Acceptance criteria
• Pattern Authority
• Source Authority
• Expected RED deliverables
• Documentation consistency

Verification shall not redefine story requirements unless Review is formally
re-entered.

### Planning Completion Criteria

Story Planning shall not advance until:

✓ Engineering problem is defined.
✓ Story objective is documented.
✓ Scope is defined.
✓ Constraints are documented.
✓ Deliverables Register is complete.
✓ Requirements Register is complete.
✓ Acceptance Criteria Matrix is complete.
✓ Every planned deliverable has a planned verification method.

### Story Planning Signoff

Story Planning Signoff confirms that:

• The engineering agreement has been reached.
• The planning documentation reflects that agreement.
• Pattern Authority has been identified.
• Source Authority has been identified.
• RED implementation may begin.

Completion of Story Planning Signoff authorizes entry into:

Review: Implementation Package (RED)

Test Planning Package

Story Planning shall define the complete testing strategy.

The testing plan shall include:

• new unit tests
• modified unit tests
• persistence tests
• CLI tests
• regression expectations
• expected test count increase

Each planned RED test shall be identified by its expected test function name
whenever practical.

These names become the approved engineering baseline for Review:
Implementation Package (RED).

Each planned test shall identify the existing test family it extends.

### RED Test Plan Verification

Verify: Story Planning shall confirm that the RED Test Plan has been fully
transitioned from the previous story to the current story.

Verification shall confirm:

• Every planned test name reflects the current story.
• Previous story test names have been removed unless retained as historical
  references.
• Planned test names match the approved story terminology.
• Planned tests correspond to the documented acceptance criteria.
• Planned tests follow the identified Pattern Authority.
• Every planned RED test identifies the existing test family it extends.

Story Planning Signoff shall not be approved until the RED Test Plan accurately
represents the current story.

Story Planning shall verify that every planned test follows the established
implementation pattern already present within the corresponding test file.

Before recommending any new test, ChatGPT (Avery) shall identify the
Pattern Authority.

Pattern Authority is the existing ResumeForge implementation that serves as
the canonical engineering reference for the new work.

Story Planning shall identify:

• Pattern Authority file
• Pattern Authority artifact (test, implementation, documentation, etc.)
• Pattern Authority name
• Pattern Authority location
• Story-specific substitutions
• Elements remaining identical

The Pattern Authority shall be explicitly cited in every subsequent workflow
phase until the story is complete.

Recommendations shall be produced by applying Pattern Transformation to the
identified Pattern Authority.

When a Pattern Authority exists, ResumeForge Engineering Methodology
prohibits synthesizing an alternative implementation unless Story Planning
explicitly authorizes a deviation.

For Profile metadata stories, only the approved metadata field substitution
shall differ from the Pattern Authority.

Fixtures, helper functions, save/load sequence, assertion style, and overall
test organization shall remain identical unless Story Planning explicitly
authorizes a deviation.

If no established pattern exists, Story Planning shall explicitly document
the proposed testing approach and explain why a new pattern is required.

Testing shall distinguish between:

• tests expected to fail because implementation is missing
• tests expected to pass because existing architecture already satisfies the
  requirement

Both outcomes shall be documented during Story Planning.

## Pattern-Driven Development

### Pattern Authority

### Pattern Inspection

After identifying the Pattern Authority, ChatGPT (Avery) shall inspect the
current implementation before producing recommendations.

Recommendations shall be derived from the inspected implementation rather than
memory, previous stories, inferred patterns, or analogous implementations.

If the inspected implementation differs from the expected implementation,
the inspected implementation becomes the authoritative engineering reference.

ResumeForge development follows the Existing Pattern First Methodology.

Before proposing any implementation or test, ChatGPT (Avery) shall identify the
current project artifact that serves as the Pattern Authority.

The Pattern Authority shall be an existing implementation already present in the
current ResumeForge-WIP Source Authority.

Recommendations shall be derived from the Pattern Authority rather than being
newly generated.

When extending an existing implementation pattern, ChatGPT shall identify:

• Pattern Authority artifact
• Pattern Authority location
• elements being substituted
• elements remaining identical

For metadata stories, only the new metadata field shall change unless Story
Planning explicitly authorizes additional changes.

If a recommendation differs structurally from the Pattern Authority, ChatGPT
shall explain the reason before presenting the recommendation.

Otherwise, recommendations shall preserve the existing implementation pattern
exactly.

Implementation Package (RED) implements the approved Story Planning Package.

RED shall not redesign, reinterpret, or expand the approved testing strategy.

Before recommending any RED implementation, ChatGPT (Avery) shall identify
the Pattern Authority for every new test.

Each recommendation shall explicitly document:

• Pattern Authority file
• Pattern Authority test name
• Story-specific substitutions
• Elements remaining identical

RED recommendations shall be derived from the Pattern Authority rather than
generated independently.

Only the substitutions approved during Story Planning shall differ.

Later workflow phases shall not determine additional testing requirements
unless Story Planning is formally reopened.

No later workflow phase shall be required to determine missing story
requirements.

### Repository Inspection Requirement

Before producing implementation guidance, engineering shall inspect the
existing repository implementation for:

- constructor signatures
- helper functions
- fixtures
- repository conventions

Implementation shall be based upon verified repository patterns rather than
assumed patterns.

### Pattern Verification

Every RED review shall verify that each proposed test conforms to its
identified Pattern Authority.

Verification shall include:

• identical fixture usage
• identical helper functions
• identical setup sequence
• identical execution sequence
• identical assertion style
• identical naming convention
• identical overall test organization
• identical engineering intent
• identical abstraction level

Only the story-approved substitutions shall differ.

If any additional structural difference exists, ChatGPT (Avery) shall
identify and justify the deviation before recommending the implementation.

If no justification exists, the recommendation shall be considered
non-conforming.

### Pattern Transformation

When extending an existing implementation pattern, ChatGPT (Avery) shall
perform a Pattern Transformation rather than synthesizing a new implementation.

Pattern Transformation consists of:

1. Identify the Pattern Authority.
2. Copy the Pattern Authority without structural modification.
3. Apply only the Story Planning-approved substitutions.
4. Verify that no additional structural changes were introduced.

For Profile metadata stories, the approved substitutions normally consist
only of replacing the existing metadata field with the new metadata field.

All remaining implementation details shall remain identical unless Story
Planning explicitly authorizes otherwise.

Pattern Transformation shall be treated as a controlled engineering activity,
not a redesign activity.

Whenever practical, implementation differences should be explainable as a
direct result of the approved Story Planning substitutions.

### Pattern Authority Evidence

Every review that references a Pattern Authority shall document:

• authority selected
• reason for selection
• substitutions applied
• verification performed
• conclusion

This evidence shall accompany the review recommendations.

### Pattern Conformance Statement

Every recommendation produced from a Pattern Authority shall conclude with a
Pattern Conformance Statement.

The statement shall summarize:

• Pattern Authority used
• approved substitutions
• structural deviations
• conformance result

Example:

Pattern Authority:
test_profile_persists_employment_type()

Approved substitution:
employment_type → work_arrangement

Structural deviations:
None

Result:
Pattern conforms.

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

### Pattern Transformation Verification

Before recommending a transformed implementation, ChatGPT (Avery) shall
perform a line-by-line comparison against the identified Pattern Authority.

Verification shall confirm that every difference is either:

• an approved Story Planning substitution, or
• an explicitly documented engineering deviation.

Undocumented differences shall be considered methodology defects and shall
be corrected before the review is approved.

## Source Authority

### Source Authority Verification

Every workflow phase shall begin by validating the current ResumeForge-WIP
Source Authority.

Source Authority validation shall confirm:

• current ResumeForge-WIP reviewed
• CHECKPOINT.md reviewed
• current workflow phase confirmed
• current story confirmed

Recommendations shall be derived from the current ResumeForge-WIP Source
Authority.

Conversational memory shall never replace inspection of the current
ResumeForge-WIP Source Authority.

If the current ResumeForge-WIP Source Authority cannot support a recommendation,
ChatGPT (Avery) shall explicitly report that verification could not be completed.

### Repository-derived Replacement Rule

All implementation updates shall be derived directly from the current WIP
repository.

Implementation Updates shall never contain:

- Example code.
- Placeholder code.
- Approximate implementations.
- Alternative implementations.
- Repository assumptions.

Every replacement shall match the existing repository implementation pattern.

### Review Evidence Checklist

Every workflow review shall explicitly identify the evidence reviewed before
producing recommendations.

At a minimum, ChatGPT (Avery) shall confirm review of:

• ResumeForge-WIP Source Authority
• CHECKPOINT.md
• current story documentation
• relevant implementation files
• relevant test files
• identified Pattern Authority
• Pattern Inspection
• affected project documentation

If any required artifact was not reviewed, ChatGPT (Avery) shall explicitly state
that limitation before making recommendations.

## Workflow Responsibilities

### Engineering Responsibilities

The following responsibilities define engineering ownership during Story
Planning.

ChatGPT (Avery) is the development lead for the Story Planning phase and is
responsible for producing the complete planning package from the current
ResumeForge-WIP Source Authority.

The developer (Jason) reviews, challenges, approves, and applies the planning
package to the project documentation.

During Story Planning, ChatGPT (Avery) is responsible for leading story
definition.

The Story Planning Package shall include, at a minimum:

• Complete implementation strategy
• Complete RED testing strategy
• Complete GREEN implementation strategy
• Complete documentation update package
• Complete verification strategy

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

### Documentation Responsibilities

Story Planning establishes the documentation authority for the active story.

Every affected project document shall be reviewed before Story Planning may be
approved.

Documentation review shall include every project document that could reasonably
be affected by the approved story.

The review shall conclude only after every affected document has been
explicitly classified as either:

• Update Required
• Reviewed – No Changes Required

ChatGPT (Avery) shall inspect every project document that could reasonably be
affected by the approved story, regardless of whether changes are ultimately
required.

A document shall never be omitted because changes appear unlikely or minor.

If a document requires no modifications, that conclusion shall result from an
explicit review of the current document rather than assumption.

For each document, ChatGPT shall provide:

• Location
• Current
• Suggested
• Reason for Change
• Supporting Pattern Authority (when applicable)

For implementation-related documentation, recommendations shall also identify:

• Existing Implementation Pattern
• Related Implementation Pattern (if applicable)
• Justification for any deviation from established patterns

Location shall identify the exact heading, subsection, command, table,
example, or code block being reviewed so the developer can navigate directly
to the affected content.

General locations such as:

"README"

"Later in the document"

"Documentation examples"

or similar descriptions are not acceptable.

The developer shall be able to navigate directly to the affected location
without searching the document.

Story Planning cannot be approved until every required documentation update
has been reviewed and approved.

### Documentation Review Completion

Documentation review is considered complete only after ChatGPT (Avery) has
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
• recommendations are supported by the current ResumeForge-WIP Source Authority
• all recommendations conform to the identified Pattern Authority

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

These responsibilities define engineering ownership.

The Workflow Phases define the sequence in which those responsibilities are
executed.

## Workflow Phases

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

### Phase 1 – Story Planning

Story Planning defines the complete engineering plan before implementation
begins.

The Story Planning Package establishes the implementation strategy, RED testing
strategy, GREEN implementation strategy, documentation update strategy, and
verification strategy that govern every subsequent workflow phase.

### Phase 2 – Implementation Package (RED)

Implementation Package (RED) produces implemented failing tests.

### RED Definition of Done

Implementation Package (RED) is complete only when:

- Every planned RED test has been implemented.
- Every RED documentation artifact has been updated.
- Test discovery succeeds.
- Test execution succeeds.
- Infrastructure failures have been eliminated.
- Only the intentional behavioral failures introduced by the current story remain.

RED completion is determined by repository evidence rather than implementation discussion.

The RED implementation package shall also confirm that every planned failing test
can be traced directly to an approved Story Planning requirement.

RED Verification confirms the implemented tests fail for the expected reasons.

RED Verification shall distinguish between:

• expected failing tests

• expected passing tests

A newly introduced test that passes immediately is acceptable when it verifies
existing generic functionality already provided by the current architecture.

Verification shall explain why each expected passing test requires no
implementation changes.

### Phase 3 – Implementation Package (GREEN)

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

Before implementation recommendations are produced, ChatGPT (Avery) shall prepare
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

### GREEN Definition of Done

Implementation Package (GREEN) is complete only when:

- The minimum production implementation has been completed.
- Every approved RED test now passes.
- Existing regression tests continue to pass.
- Documentation remains synchronized.
- Repository architecture remains internally consistent.
- No implementation exists without traceability to Story Planning.

GREEN completion is determined by repository evidence rather than engineering discussion.

Implementation should remain the minimum necessary to satisfy the approved RED package.

### Phase 4 – GREEN Verification

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

### Phase 5 – Story Signoff

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

The Workflow Phases define the required execution sequence for every
ResumeForge story.

Each phase specifies its required inputs, engineering responsibilities,
deliverables, verification activities, and exit criteria.

All stories shall progress through these phases sequentially unless the
engineering methodology is formally revised.

### General Workflow Principles

ResumeForge follows an incremental development model.

Implementation guidance shall always begin with the implementation currently
present in the ResumeForge WIP Source Authority before describing the required
modification.

ChatGPT (Avery) shall describe how the existing implementation evolves to satisfy
the approved Story Planning Package.

Recommendations shall reference the current implementation before describing
the required modification.

The existing implementation shall always be identified first.

The required modification shall then be described as an evolution of that
implementation.

ChatGPT (Avery) shall avoid presenting implementation as though the codebase were
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

Whenever possible, stories should remain small enough to complete in a single lifecycle:

Story Planning
Review → Implement → Verify
↓
Implementation Package (RED)
Review → Implement → Verify
↓
Implementation Package (GREEN)
Review → Implement → Verify
↓
Story Signoff
Review → Verify

#### Phase Contract

**Objective**

Approve completion of the current story and establish repository readiness for the next engineering phase.

**Required Inputs**

- Successful Verify
- Current ResumeForge-WIP repository
- Updated CHECKPOINT.md
- Updated history

**Required Deliverables**

- Story Signoff Report
- Evidence Chain Confirmation
- Repository Readiness Assessment
- Lessons Learned
- Final Story Disposition

**Exit Criteria**

Story Signoff concludes only when:

- Verification has passed.
- Required repository artifacts have been updated.
- Lessons Learned have been evaluated.
- Repository is ready for the next story.

### Story Signoff Source Authority Verification

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
□ ChatGPT (Avery) shall first identify the current implementation before proposing changes.
□ Disregard previous repository revisions whenever they conflict with the current archive.

If the archive cannot be opened or reviewed with confidence,
workflow execution shall stop immediately.

ChatGPT (Avery) shall explicitly report that Source Authority could not be
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

Before providing any implementation recommendation, review conclusion,
verification result, or signoff approval, ChatGPT shall first review the
current ResumeForge-WIP Source Authority.

Conversational memory shall never replace inspection of the current
ResumeForge-WIP Source Authority.

If the current Source Authority contradicts previous conversation history,
the Source Authority shall govern.

If verification cannot be performed from the current Source Authority,
ChatGPT (Avery) shall explicitly state that verification could not be completed.

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

Repository Synchronization

Before Story Signoff verification begins, synchronize every engineering
artifact affected by the completed story.

Repository synchronization shall verify:

□ Story implementation complete
□ Story verification complete
□ Repository documentation synchronized
□ CHECKPOINT.md reflects the current workflow state
□ docs/history.md reflects completed engineering work
□ docs/development_workflow.md updated for approved methodology improvements
□ docs/engineering_context.md updated when durable engineering context changed
□ Repository artifacts are internally consistent

Repository synchronization shall be completed before Story Signoff approval.

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
□ Repository Synchronization completed
□ repository ready for commit

Repository Synchronization is the final engineering activity performed before
Story Signoff approval.

Its purpose is to ensure every authoritative engineering artifact accurately
reflects the completed implementation before the repository is committed.

## Standard Story Workflow

Every story progresses through four workflow stages.

The canonical workflow is:

Story Planning
Review → Implement → Verify
↓
Implementation Package (RED)
Review → Implement → Verify
↓
Implementation Package (GREEN)
Review → Implement → Verify
↓
Story Signoff
Review → Verify

This is the canonical workflow definition for ResumeForge Engineering Methodology.
Other methodology sections shall not define an alternate workflow lifecycle.

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

## Standard Implementation Package Format

Every implementation package shall provide sufficient detail for a qualified developer unfamiliar with the current story to complete the implementation without additional clarification.

### Complete Implementation Package

A complete implementation package delivers every repository artifact required
for the current workflow phase.

Implementation should not intentionally defer documentation that belongs to the
current phase unless the deferral is explicitly identified.

### Mandatory Implementation Update Deliverables

Every Implement phase shall produce complete implementation deliverables.

Implementation Updates shall contain only implementation work and shall not
continue the Review phase.

Implementation Updates shall include:

- Exact replacement code.
- Exact replacement test methods.
- Exact insertion locations.
- Exact removal locations (when replacing existing code).
- Required imports.
- Required fixtures.
- Required parser updates.
- Required workflow updates.
- Expected verification results.

Implementation Updates shall not contain:

- Review commentary.
- Design discussion.
- Example implementations.
- Pseudocode.
- "Equivalent" implementations.
- "Adjust as needed" guidance.
- Repository assumptions.

All implementation updates shall be produced directly from the current WIP
repository.

### Engineering Story RED Package Format

Engineering Story RED packages shall include:

1. Engineering Objective
2. Verification Scenarios
3. Planned Evidence
4. Planned Traceability
5. Planned Acceptance Criteria

The RED package shall fully define engineering verification before any
GREEN implementation begins.

### Documentation Implementation Template

Every documentation update shall contain:

- File
- Purpose
- Location (Current)
- Implementation Update
- Expected Result
- Justification (when applicable)

### Code Implementation Template

Every code implementation shall contain:

- File
- Purpose
- Location (Current)
- Pattern Authority
- Location (Current)
- Implementation Update
- Expected Result
- Verification Target

Implementation instructions shall identify precise locations and describe the complete update.

Instructions shall not rely on assumptions that the developer already understands existing patterns.

## Pattern Authority

Pattern Authority identifies the existing implementation or documentation that serves as the approved consistency reference.

Implementation updates shall reference an existing pattern whenever practical.

When no existing pattern exists, the implementation package shall explicitly identify that the implementation establishes a new project pattern.

Pattern deviations require approval during the Review step before implementation.

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

### Engineering Evidence Standards

Engineering evidence provides the objective basis for every Verify step
defined within this methodology.

Engineering evidence establishes objective, verifiable proof that a workflow phase has satisfied its approved requirements.

Engineering evidence shall be:

- Objective
- Reproducible
- Traceable
- Relevant to the current phase
- Sufficient to support phase approval

Engineering evidence may include, but is not limited to:

- Targeted unit test execution
- Targeted integration test execution
- Full regression test execution
- CLI verification
- Persistence verification
- Documentation review
- Code review against the approved implementation package
- Git status
- Commit history
- Version tags
- Regression summaries

Collected engineering evidence shall objectively demonstrate all of the following:

- the approved implementation was completed;
- the implementation satisfies the approved Review;
- no unintended regressions have been introduced; and
- the phase is ready for signoff.

Unless explicitly documented otherwise, every subsequent Phase Evidence Chain defined within this methodology inherits these Engineering Evidence Standards.

These standards define the minimum engineering evidence required for
phase verification.

Individual workflow phases may require additional evidence specific to that phase; however, they shall not reduce, replace, or contradict these minimum requirements.

---

The following sections apply the Engineering Evidence Standards defined above to each workflow phase.

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

#### Story Transition Verification

Verify that all story-specific planning documentation has transitioned from the
previous story to the current story.

Review previous story references and classify each occurrence as one of the
following:

• Historical reference
• Pattern Authority
• Active story content

Historical references and Pattern Authority references shall remain unchanged.

Active story content shall be updated to reflect the current story before
Story Planning Signoff.

Verification shall include, at a minimum:

• Story identifier
• Story title
• Story objective
• Acceptance criteria
• Definition of Ready
• Documentation update references
• Current phase
• Next phase

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
• Implementation Update

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

RED Completion Checklist

Before RED Review may be approved, verify:

✓ Every planned RED test has an identified Pattern Authority.
✓ Every RED recommendation documents its Pattern Authority.
✓ Pattern Transformation has been performed.
✓ No unauthorized structural deviations exist.
✓ Production files remain unchanged.
✓ Expected RED failures are documented.
✓ No unrelated regressions have been introduced.
✓ Pattern Conformance Statement completed.

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

### Engineering Story RED Deliverables

Engineering stories define engineering verification artifacts rather than
production feature tests.

At a minimum, an Engineering Story RED package shall define:

• Engineering verification scenarios
• Methodology acceptance criteria
• Documentation verification requirements
• Repository verification requirements
• Traceability verification requirements

Engineering Story RED deliverables shall also identify:

• the governing methodology section,
• the planned GREEN implementation that will satisfy the verification artifact,
• the Repository Closeout evidence that will certify completion.

Engineering stories shall maintain complete traceability from planning through
Repository Closeout.

These artifacts intentionally fail until the corresponding methodology has
been implemented.

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

ChatGPT (Avery) shall verify:

For Engineering Stories, RED Completion additionally confirms:

• every planned engineering verification artifact has been implemented,
• every planned methodology verification has been documented,
• every planned Repository Closeout artifact has been prepared for GREEN.

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

### RED Completion Criteria

Implementation Package (RED) is complete only when all identified deficiencies
have been corrected.

Completion requires:

- All failing tests corrected.
- All obsolete tests corrected.
- All missing tests created.
- Parser coverage complete.
- CLI coverage complete.
- Workflow coverage complete.
- Service coverage complete.
- Persistence coverage complete.
- Model coverage complete.

Only then may the story advance to Verify: Implementation Package (RED).

### RED Verification Evidence

Engineering Story RED Verification shall additionally report:

• Engineering verification artifacts produced
• Deliverables Register coverage
• Requirements Register coverage
• Repository Closeout coverage
• Outstanding engineering verification gaps

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

### Test Suite Completeness Audit

Review shall classify every affected test as:

- Passing
- Failing
- Missing
- Obsolete

Review shall also identify missing coverage including:

- Parser
- CLI
- Workflow
- Persistence
- Service
- Model

### Engineering Coverage Verification

Engineering stories shall verify that every planned engineering deliverable
is represented by at least one RED verification artifact.

Coverage shall include:

• Engineering Charter
• Requirements Register
• Deliverables Register
• Acceptance Criteria
• Repository Closeout
• Story Completion Report

RED Coverage Verification shall also confirm that every Repository Closeout
deliverable introduced during Story Planning is represented by a planned
engineering verification artifact.

Repository Closeout artifacts shall not first appear during GREEN or Story
Signoff.

No planned engineering deliverable may bypass RED verification.

### CLI Parser Coverage Checklist

Every CLI story shall verify parser coverage for each new command-line option.

Review shall confirm:

- create parser
- edit parser
- parser argument registration
- Namespace population
- workflow dispatch
- service invocation
- CLI output

Parser coverage shall be completed before RED Signoff.

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

### Engineering Traceability Verification

Every engineering requirement shall be traceable to:

• a planned deliverable,

• a RED verification artifact,

• a GREEN implementation,

• a Story Signoff verification,

• Repository Closeout certification.

Traceability shall remain continuous.

Every engineering deliverable introduced during Story Planning shall appear
without interruption throughout RED, GREEN, Story Signoff, and Repository
Closeout.

Broken traceability constitutes an engineering defect.

Missing traceability constitutes a RED failure.

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

For Engineering Stories, RED Signoff additionally certifies that:

• all planned engineering verification artifacts exist,
• traceability remains complete,
• GREEN implementation can proceed without redefining engineering objectives,
• Repository Closeout requirements have been fully planned.

Implementation recommendations should explain how each failing test is expected to transition to passing.

Recommendations should remain traceable to the RED failures.

RED approval shall also confirm that every planned RED test identified during
Story Planning has been implemented.

No approved Story Planning test shall remain unimplemented before GREEN begins.

## Phase 3 – Implementation Package (GREEN)

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

ChatGPT (Avery) shall verify:

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

ChatGPT (Avery) shall explain why no implementation changes were necessary.

### Required GREEN Deliverables

Every GREEN review shall begin with a Project Audit Summary.

The implementation package shall contain:

1. Existing Reference

   Show the verified current implementation.

2. Implementation Update

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

### GREEN Entry Criteria

GREEN begins only after RED has been completed.

Specifically:

- RED tests have been delivered.
- RED tests have been executed.
- Expected failures have been confirmed.
- ChatGPT (Avery) has reviewed the RED failures.
- The implementation is traceable to those failures.

GREEN Entry Criteria shall also verify that the approved Story Planning Package
contains sufficient implementation guidance.

If implementation reveals missing requirements, conflicting requirements, or
insufficient engineering guidance, Story Planning shall be reopened before
GREEN implementation continues.

### GREEN Implementation Package

When GREEN begins, ChatGPT (Avery) shall provide a complete implementation package.

The package shall include:

#### Required Contents

1. Existing Reference

   Verified current implementation.

2. Implementation Update

   Complete replacement or insertion code.

3. Exact Location

   File name and insertion location.

4. Explanation

   Why each modification satisfies one or more RED tests.

Recommendations should be complete enough to paste directly into the
project.

GREEN reviews should not require the developer to infer missing
implementation.

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

Before approving any workflow phase, ChatGPT (Avery) shall confirm that all
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

### Review Evidence Checklist

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
□ Artifact Inventory completed
□ Cross-Artifact Consistency Audit completed
□ Stale Reference Audit completed
□ Evidence Matrix completed
□ Every finding classified
□ Zero unresolved or unclassified findings remain

If any item cannot be confirmed, the workflow phase shall remain incomplete.

The Review Quality Gate shall also require completion of the Engineering
Methodology Audit Gate before approval.

A review shall not be approved solely because the primary story artifact is
correct. Related authoritative artifacts shall be checked for contradictory
active definitions and stale references.

### Review Separation

Workflow reviews shall distinguish between:

• Observed Findings
• Verified conditions identified during review.

### Recommendation Standards

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
• Implementation Update

Documentation Verification shall produce findings for every required document.

Each document shall report:

• Review Status
• Findings
• Required Updates
• Verification Result

#### Documentation Findings

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

Engineering Methodology Review should evaluate lessons learned from the current
story before Story Signoff completes.

Durable process improvements should be incorporated into the engineering
methodology while implementation details remain fresh.

Methodology evolution is considered a normal engineering deliverable rather than
an exceptional activity.

### Methodology Validation

Engineering Methodology Review shall verify:

• methodology improvements identified
• methodology debt identified
• documentation updated
• future workflow impact documented

Methodology improvements shall be incorporated before Story Signoff whenever
practical.

If improvements are deferred, document the rationale.

### Methodology Review Evidence Chain

Engineering Methodology Review shall use the same evidence discipline required
by implementation workflow phases.

Each methodology finding shall record:

- Observed Methodology Behavior
- Evidence
- Root Cause
- Methodology Improvement
- Expected Prevention
- Verification Method
- Disposition

The Evidence shall identify the current ResumeForge-WIP artifact(s) supporting
the finding. Methodology conclusions shall not rely on prior conversations or
remembered project behavior.

Methodology Review shall also complete the Engineering Methodology Audit Gate,
including the Artifact Inventory, Cross-Artifact Consistency Audit, Stale
Reference Audit, Evidence Matrix, and Finding Classification.

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

### Phase Completion Criteria

Every workflow phase shall define objective completion criteria.

Verification confirms repository deliverables.

Completion of discussion alone shall never satisfy a workflow phase.

Every required repository artifact shall be synchronized before the workflow
advances to the next phase.

Completion shall always be evidence-based rather than conversation-based.

Verification confirms implementation.

Signoff confirms repository readiness.

### Story Signoff Deliverable Validation

Story Signoff shall validate that every planned deliverable has been completed.

Validation includes:

- Story Planning documentation.
- RED implementation package.
- RED verification.
- GREEN implementation package.
- GREEN verification.
- Methodology updates.
- History updates.
- CHECKPOINT.md synchronization.

Story Signoff shall identify any planned deliverable that was intentionally
deferred.

Deferred work shall be documented before Repository Closeout.

No story shall enter Repository Closeout with undocumented implementation debt.

### Documentation Verification

Documentation is a required Story Signoff deliverable.

Story Signoff shall determine whether documentation updates are required for the completed story.

Documentation verification shall include, when applicable:

- CHECKPOINT.md
- docs/history.md
- README.md
- docs/development_workflow.md
- Story documentation
- User-facing documentation
- Developer-facing documentation
- Any repository documentation affected by the completed story

Story Signoff shall explicitly record one of the following outcomes:

- Documentation updated.
- Documentation not required.
- Documentation deferred (with justification).

Documentation status shall never be implied.

### Story Signoff Checklist

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
□ Documentation requirements reviewed.
□ Required documentation updated.
□ Documentation exceptions recorded.
□ Documentation verification completed.

## Repository Closeout

Repository Closeout is the final engineering phase of every ResumeForge story.

Story Signoff certifies that the engineering work is complete.

Repository Closeout certifies that the completed engineering work has been
properly recorded, documented, released, and archived.

Repository Closeout verifies repository integrity rather than implementation.

Repository Closeout shall not introduce engineering changes.

Only release activities may occur during this phase.

### Commit: Repository Closeout

Purpose

Execute the Repository Closeout Commands produced during Verify: Repository
Closeout and confirm that repository closure completed successfully.

#### Commit Deliverables

Commit: Repository Closeout shall include:

- Commit Verification
- Repository State Audit
- Push Verification
- Tag Verification
- Working Tree Verification
- Story Completion Confirmation

The Commit response shall confirm the actual repository state after command
execution.

Repository closure is not complete until Commit: Repository Closeout has been
successfully verified.

### Repository Closeout State Model

Repository Closeout shall progress through the following engineering states:

1. Repository Ready for Closeout
2. Repository Closeout Commands Generated
3. Repository Commands Executed
4. Repository Closed
5. Story Archived
6. Engineering Session Complete
7. Ready for Next Story

Each state shall be confirmed before progressing to the next state.

Repository Closeout is complete only after the Repository Closed state has been
verified.

### Repository Closeout Gates

Repository Closeout shall certify completion using engineering gates rather
than engineering judgment.

The following gates shall PASS before Repository Closeout is approved:

• Requirements Complete
• Engineering Complete
• Verification Complete
• Documentation Complete
• Repository Complete

Failure of any gate returns the workflow to the engineering phase responsible
for correcting the deficiency.

Repository Closeout certifies completion. It does not perform engineering
work.

### Repository Verification

Repository verification shall confirm, at a minimum:

✓ Full regression suite executed successfully
✓ Working tree is clean
✓ Commit created
✓ Commit pushed to origin
✓ Story tag created
✓ Story tag pushed
✓ Local and remote repositories synchronized

Repository verification confirms repository integrity.

Repository verification alone does not certify story completion.

### Release Evidence

Repository Closeout shall produce standardized release evidence.

Minimum release evidence shall include:

• Regression summary
• Repository verification
• Commit identifier
• Story tag
• Documentation verification
• Story completion status

Release evidence becomes part of the permanent engineering record.

### Story Completion Report

Repository Closeout concludes by producing a Story Completion Report.

The report shall summarize:

• Story identifier
• Story objective
• Requirements status
• Regression results
• Documentation status
• Repository verification
• Commit identifier
• Story tag
• Final completion status

The Story Completion Report provides a concise engineering summary of the
completed story.

### Documentation Closeout Verification

Repository Closeout shall verify that all documentation identified during Story Signoff has been completed.

Verification shall confirm:

- Story documentation is complete.
- Repository history is current.
- CHECKPOINT.md is synchronized.
- Repository documentation accurately reflects the completed implementation.

Outstanding documentation shall prevent Repository Closeout unless formally deferred during Story Signoff.

### Repository Closeout Philosophy

Engineering completion and repository completion are separate engineering
milestones.

Story Signoff certifies that the engineering implementation is complete.

Repository Closeout certifies that the completed implementation has been
properly documented, synchronized, committed, tagged, and archived.

A clean repository does not prove a completed story.

A completed story requires both successful Story Signoff and successful
Repository Closeout.

### Story Closure

A story is considered closed only after:

• Story Signoff has been approved.
• The repository has been committed and pushed.
• Version tags have been created and pushed (when applicable).
• The working tree is clean.
• The next story may begin with Review: Story Planning.

Only then may the next story begin with Story Planning.

### Story Summary

Story Summary shall include:

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

Documentation synchronization shall be verified as a completion gate rather than assumed from implementation completion.

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
Review → Implement → Verify
↓
Implementation Package (RED)
Review → Implement → Verify
↓
Implementation Package (GREEN)
Review → Implement → Verify
↓
Story Signoff
Review → Verify
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

## Engineering Artifact Authority

Engineering artifacts have distinct authoritative responsibilities. Each
engineering concern shall have exactly one authoritative artifact.

The purpose of this section is to prevent duplicated responsibility,
conflicting project state, and uncertainty regarding where engineering
information shall be maintained.

### Artifact Authority Matrix

| Artifact | Authoritative Responsibility | Mutable After Approval |
|-----------|------------------------------|------------------------|
| Story Planning Package | Approved engineering planning baseline | No |
| CHECKPOINT.md | Current workflow state | Yes |
| docs/phases.md | Workflow lifecycle reference | Rarely |
| docs/development_workflow.md | Engineering methodology | Yes |
| docs/testing.md | Testing methodology | Yes |
| docs/history.md | Historical engineering record | Append only |
| docs/engineering_context.md | Durable engineering context | Yes |

### Artifact Lifecycle Rules

Every engineering artifact has a defined lifecycle.

#### Story Planning Package

- Created during Story Planning.
- Modified only during Story Planning.
- Frozen immediately following Story Planning Signoff.
- Represents the approved engineering planning baseline.

#### CHECKPOINT.md

- Updated throughout every workflow phase.
- Represents the current workflow state.
- Shall remain synchronized with repository progress.

#### docs/history.md

- Append-only.
- Records completed engineering work.

#### docs/engineering_context.md

- Evolves as the engineering methodology evolves.
- Preserves durable engineering context.
- Shall not redefine engineering workflow methodology.

### Single Authority Principle

Every engineering concern shall have one authoritative artifact.

Engineering artifacts shall not duplicate authoritative ownership of the same
project information.

Current workflow state is maintained exclusively in `CHECKPOINT.md`.

Story Planning Packages preserve the approved planning baseline and shall not
be used to track current workflow state.

`docs/development_workflow.md` remains the authoritative engineering
methodology.

`docs/engineering_context.md` provides durable engineering context and
repository bootstrap guidance but shall not supersede the engineering
methodology.

### Methodology Single Authority Rule

Every major ResumeForge Engineering Methodology concept shall have one
authoritative definition.

Examples include, but are not limited to:

- Source Authority
- Pattern Authority
- ResumeForge Engineering Methodology Execution Model
- Story Planning
- Phase Contracts
- Engineering Evidence

The authoritative definition shall exist in exactly one location.

Other sections may reference the authoritative definition but shall not
duplicate or redefine the concept.

When methodology growth introduces duplicate concepts, the methodology shall
be refactored before additional duplicate definitions are introduced.

## Engineering Methodology Audit Gate

The Project Audit Checklist establishes the minimum review inventory. The
Engineering Methodology Audit Gate establishes the minimum proof that the
inventory was actually evaluated for completeness and consistency.

Every Planning, RED, GREEN, Story Signoff, and Engineering Methodology Review
shall complete the following sequence before the review may be approved:

Documentation verification shall be performed whenever a phase modifies repository documentation or project process documentation.

1. Artifact Inventory
   - Identify every artifact required by the current phase.
   - Identify every artifact referenced by the approved Story Planning Package.
   - Identify related implementation, test, and documentation artifacts.
   - Record any unavailable or intentionally excluded artifact.

2. Content Audit
   - Review the required artifacts against the current phase requirements.
   - Verify current story identifiers, feature terminology, acceptance criteria,
     tests, expected regression counts, scope, and phase state where applicable.

3. Cross-Artifact Consistency Audit
   - Compare corresponding requirements and state across the reviewed artifacts.
   - Confirm that active definitions agree across documentation, tests,
     implementation evidence, and project-state artifacts.
   - Contradictory active statements shall be recorded as findings even when
     each statement is individually plausible.

4. Stale Reference Audit
   - Search for the current story identifier and feature terminology.
   - Search for the immediately preceding story identifier and feature
     terminology when they are relevant to the current pattern.
   - Search for superseded terminology and prior lifecycle definitions.
   - Classify each match as Active, Historical, Pattern Authority, or Stale.
   - Historical and Pattern Authority references shall not be treated as stale
     solely because they name a previous story.

5. Evidence Matrix
   - Map each phase requirement to its primary evidence source.
   - Mark each requirement PASS, FAIL, or NOT APPLICABLE.
   - A narrative review shall not substitute for an omitted evidence mapping.

6. Artifact Authority Audit

   - Verify every engineering concern has exactly one authoritative artifact.
   - Verify current workflow state is maintained exclusively in
     `CHECKPOINT.md`.
   - Verify Story Planning Packages remain approved planning baselines and are
     not used as workflow status trackers.
   - Verify no active engineering state is duplicated across multiple
     repository artifacts.

7. Finding Classification
   Every finding shall be classified as exactly one of:
   - Resolved
   - Intentionally Deferred
   - Superseded
   - Unresolved

   An Unresolved or Unclassified finding prevents phase approval.

8. Gate Result
   The review may advance only when:
   - the required artifact inventory is complete;
   - the cross-artifact consistency audit is complete;
   - the stale reference audit is complete;
   - every applicable requirement has evidence;
   - every finding has a classification; and
   - zero Unresolved or Unclassified findings remain.

The Engineering Methodology Audit Gate supplements the Project Audit Checklist.
It does not replace phase-specific evidence requirements.

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
Implementation Update
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

### Phase State Synchronization

A phase transition is not complete until the authoritative project-state
artifact reflects the approved transition.

After Verify approval:

1. The approved verification result establishes the phase outcome.
2. The project-state documentation shall be updated to reflect the new
   current phase and next step.
3. The next workflow phase shall not be treated as active until that state
   synchronization is complete.

Conversational approval and repository/project-state approval shall not be
treated as interchangeable evidence.

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

### Implement Means Deliver

Once a workflow phase enters Implement, the response shall primarily consist of
repository-ready deliverables.

Previously completed review work shall not be repeated unless new repository
evidence invalidates earlier conclusions.

Implementation responses should maximize repository progress rather than repeat
analysis.

## Guiding Principle

> Build the smallest possible change that satisfies the current story, preserves the verified architecture, maintains backward compatibility, keeps documentation synchronized, and leaves the project in a releasable state.

## AI Collaboration Guidelines

To minimize development cycle time:

- ChatGPT (Avery) shall complete the Project Audit Checklist before making any recommendations.
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

ChatGPT (Avery) shall verify:

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
- Signoff verifies implementation, documentation, regression evidence, methodology obligations, and story completion.
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
- ChatGPT (Avery) shall never infer that a previous phase has been completed.
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

If verification cannot be completed, ChatGPT (Avery) shall explicitly identify:

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

### Repository Anchor Validation

Every repository anchor referenced within an Implementation Package shall be
validated against the current repository immediately before the engineering
response is published.

Validation shall confirm:

- Repository artifact exists.
- Primary heading exists exactly as referenced.
- Secondary heading exists exactly as referenced.
- Heading level matches the repository.
- Anchor location uniquely identifies the modification.
- Referenced preceding anchor exists.
- Referenced following anchor exists.

Engineers shall not approximate repository structure.

Examples of prohibited behavior include:

- Incorrect heading levels.
- Referencing headings from memory.
- Semantic references such as "current story entry."
- Assuming repository organization.

If repository validation fails, the engineer shall stop implementation package
generation, reconcile the implementation package with the repository, and
repeat Repository Anchor Validation before publication.

## Workflow Integrity

The workflow itself is considered part of the project's architecture.

Maintaining strict phase boundaries is as important as maintaining code quality.

Each phase should produce a complete, reviewable deliverable before advancing
to the next phase.

Phase progression is developer-controlled.

ChatGPT (Avery) shall never infer that the next phase should begin.

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
Complete Cross-Artifact Consistency Audit
    ↓
Complete Stale Reference Audit
    ↓
Complete Evidence Matrix
    ↓
Classify findings
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
☐ Engineering Methodology Audit Gate completed
☐ Zero unresolved or unclassified findings remain

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
review, ChatGPT (Avery) shall identify:

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