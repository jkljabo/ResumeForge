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

## Engineering Session Bootstrap

Engineering Session Bootstrap is the mandatory initialization procedure
performed once at the beginning of every ResumeForge Engineering Story.

Its purpose is to establish a verified engineering baseline before Story
Planning and repository implementation begin.

Engineering Session Bootstrap shall:

- establish Engineering Communication Status;
- verify repository synchronization;
- verify the active ResumeForge-WIP repository state;
- synchronize the active Engineering Backlog;
- confirm Engineering Roadmap status;
- establish Story execution context;
- confirm repository readiness for implementation.

Engineering Session Bootstrap initializes engineering execution.

It establishes the engineering baseline for the remainder of the Story and is
not repeated during Repository Patch execution.

## Engineering Communication Status

Engineering Communication Status provides a standardized engineering status
report throughout the execution of every ResumeForge Engineering Story.

Its purpose is to establish a consistent understanding of the current engineering
state before planning, implementation, verification, or repository updates.

Engineering Communication Status reports, as applicable:

- Story identification.
- Current engineering phase.
- Active execution context.
- Repository synchronization status.
- ResumeForge-WIP repository status.
- Engineering Roadmap status.
- Engineering Backlog status.
- Repository continuity status.
- Engineering readiness.

Engineering Communication Status shall appear at the beginning of each
engineering response where it contributes to engineering execution or repository
traceability.

The reported information shall accurately reflect the current engineering state
at the time the response is produced.

## Engineering Roadmap

The Engineering Roadmap is the long-term planning artifact governing the
evolution of the ResumeForge Engineering Methodology (REM).

Unlike Engineering Stories, which execute individual engineering improvements,
the Engineering Roadmap provides strategic direction for methodology growth over
multiple development cycles.

The Engineering Roadmap defines:

- major engineering initiatives;
- methodology enhancements;
- engineering architecture improvements;
- engineering technical debt;
- future engineering capabilities;
- engineering priorities and sequencing.

Engineering Stories implement individual roadmap objectives.

Completion of Engineering Stories advances the Engineering Roadmap.

The Engineering Roadmap serves as the engineering counterpart to the
Development Roadmap.

Together, the ResumeForge Engineering Methodology (REM), Engineering Roadmap,
and Development Roadmap establish the complete planning hierarchy for the
ResumeForge project.

Engineering Roadmap entries should be periodically reviewed, reprioritized, and
updated as the methodology matures.

### Development Roadmap

The Development Roadmap governs the functional evolution of the ResumeForge
application.

Where the Engineering Roadmap focuses on the ResumeForge Engineering
Methodology (REM), the Development Roadmap focuses on the product itself.

The Development Roadmap defines:

- functional capabilities;
- product milestones;
- feature sequencing;
- architectural evolution of the application;
- user experience improvements;
- long-term product priorities.

Development Stories implement individual Development Roadmap objectives.

Completion of Development Stories advances the Development Roadmap.

Engineering Stories improve the engineering system used to build the product.

Development Stories improve the product delivered to the user.

Together, the Engineering Roadmap and Development Roadmap provide coordinated
planning for both methodology evolution and product evolution while remaining
independently managed.

Both roadmaps should be reviewed periodically to ensure that engineering
investment continues to support product priorities and that product priorities
remain achievable within the capabilities of the engineering methodology.

### Engineering Backlog Management

The Engineering Backlog is the temporary working collection of approved
engineering improvements identified during execution of an Engineering Story.

Its purpose is to preserve methodology improvements discovered during
engineering work without interrupting the active Story.

Engineering Backlog entries may originate from:

- engineering observations;
- implementation discoveries;
- repository reviews;
- retrospective findings;
- developer-approved methodology improvements.

Each Engineering Backlog entry shall include:

- a unique Engineering Backlog identifier;
- a concise title;
- implementation status;
- target repository artifact;
- implementation category;
- implementation summary.

The assistant is responsible for maintaining the active Engineering Backlog
throughout the Story.

Engineering Backlog responsibilities include:

- recording approved entries;
- maintaining entry status;
- integrating approved entries into Repository Patch Units;
- tracking implementation progress;
- reconciling implemented entries;
- ensuring all remaining entries are resolved before Story Commit.

Engineering Backlog entries remain active until they are:

- implemented and verified;
- intentionally deferred to a future Engineering Story;
- withdrawn by engineering decision.

The Engineering Backlog provides continuity between engineering discovery,
repository implementation, and long-term methodology evolution.

### Story Lifecycle Ownership

The Story owns the engineering lifecycle.

Repository Patch Units (RPUs) do not own lifecycle phases. They are execution
artifacts that exist entirely within the Story Implement phase.

The Story lifecycle consists of:

- Review
- Implement
- Verify
- Commit

These phases are entered and exited only by Story-level commands.

Repository Patch execution is entered through the Story Implement phase and
returns control to the Story lifecycle only after all executable Repository
Patch Units have been completed.

Repository Patch Units shall never transition between Story lifecycle phases.

Instead, Repository Patch Units transition only to the next executable
Repository Patch Unit within the Repository Patch Work Breakdown Structure.

Story lifecycle ownership provides a clear separation between engineering
orchestration and repository implementation.

This separation ensures that:

- Story phases remain stable and predictable.
- Repository Patch execution remains recursive.
- Repository modifications remain isolated to executable leaf nodes.
- Engineering verification occurs at both the Repository Patch and Story
  levels without duplicating lifecycle responsibilities.

The Story is therefore the sole owner of lifecycle progression, while the
Repository Patch execution engine owns traversal of the Repository Patch Work
Breakdown Structure.

### Repository Patch Continuity

Repository Patch Continuity ensures that every executable Repository Patch Unit
begins from a verified repository state established by the previously completed
Repository Patch Unit.

Before implementing a Repository Patch Unit, the engineering process shall
review the immediately preceding executable Repository Patch Unit to confirm:

- the approved repository modifications were completed;
- repository ordering has been preserved;
- repository integrity has not been compromised;
- the implementation scope remained isolated to the approved Repository Patch
  Unit.

Repository continuity verification is performed once at the beginning of each
executable Repository Patch Unit.

Structural Repository Patch Units do not require continuity reviews because they
perform no repository modifications.

Repository continuity establishes confidence that each repository modification
builds upon a verified engineering baseline, preventing implementation drift
throughout Repository Patch execution.

### Repository Patch Navigation

Repository Patch Navigation governs movement through the Repository Patch Work
Breakdown Structure during Story implementation.

Navigation is driven exclusively by the Repository Patch Work Breakdown
Structure and the execution context identified by the active `Section:` command.

Repository Patch Navigation shall:

- identify the current execution context;
- present the appropriate Repository Patch Work Breakdown Matrix;
- indicate completed Repository Patch Units;
- identify the active Repository Patch Unit;
- expose remaining Repository Patch Units within the current branch;
- guide execution to the next executable Repository Patch Unit.

When recursive decomposition occurs, Repository Patch Navigation shall present
the Work Breakdown Matrix for the active branch while preserving visibility into
the parent Story structure.

Navigation is informational.

It does not determine engineering lifecycle progression or repository
modification scope.

Its purpose is to maintain engineering orientation and execution traceability
throughout Repository Patch implementation.

### Execution Context (Section)

The Execution Context identifies the active Repository Patch Unit currently
being executed within the Repository Patch Work Breakdown Structure.

Execution Context is communicated through the `Section:` command parameter.

The `Section:` parameter is the authoritative execution context for Repository
Patch implementation.

Execution Context shall:

- identify the current executable Repository Patch Unit;
- establish the implementation scope for the current engineering response;
- determine the Repository Patch Work Breakdown Matrix presented to the
  engineer;
- define the Repository Location Specification associated with the current
  implementation;
- determine the next executable Repository Patch Unit.

The Execution Context does not determine Story lifecycle progression.

Story lifecycle transitions are controlled exclusively by Story-level commands.

Execution Context changes only during Repository Patch execution and advances
one executable Repository Patch Unit at a time.

Every executable Repository Patch response shall conclude by issuing the next
`Section:` command until all executable Repository Patch Units have been
completed, at which point execution returns to the Story lifecycle through the
appropriate Story Verify command.

### Repository Patch Response Structure

Every executable Repository Patch Unit shall produce a standardized engineering
response.

The Repository Patch Response Structure provides a consistent engineering
experience throughout Repository Patch execution and ensures that every
implementation response contains the information required for repository
modification, verification, and navigation.

Unless specifically omitted by engineering design, Repository Patch responses
shall be presented in the following order:

1. Engineering Communication Status
2. Repository Patch Work Breakdown Matrix
3. Repository Continuity Review
4. Repository Location Specification (RLS)
5. Repository Update Package
6. Engineering Backlog Synchronization
7. Repository Verification
8. Repository Patch Result
9. Next Developer Command

Each section has a single responsibility and shall appear no more than once
within a Repository Patch response.

Repository Patch responses shall:

- remain focused on the current executable Repository Patch Unit;
- limit repository modifications to the approved implementation scope;
- preserve repository continuity;
- conclude with the next executable developer command.

This standardized response structure provides consistency, traceability, and
predictability throughout Repository Patch execution while allowing individual
Repository Update Packages to remain independent of one another.

### Next Developer Command

Every executable Repository Patch Unit shall conclude by issuing a Next
Developer Command.

The Next Developer Command advances execution through the Repository Patch Work
Breakdown Structure and provides the engineer with the exact command required
to continue execution.

The Next Developer Command shall:

- be the final artifact produced by every executable Repository Patch Unit;
- be immediately executable without modification;
- contain no explanatory text;
- contain no blank lines;
- use the canonical command format;
- identify the next execution context.

The canonical command format is:

Story: <Story Identifier>
<Story Lifecycle Command>
Section: <Next Repository Patch Unit>
ResumeForge-WIP.zip

When Repository Patch execution reaches the final executable Repository Patch
Unit, the Next Developer Command shall transition execution back to the Story
lifecycle by issuing the appropriate Story Verify command rather than another
Section command.

The Next Developer Command is the exclusive mechanism used to advance execution
through Repository Patch implementation and to return control to the Story
lifecycle.

No alternative navigation mechanism shall be used.

### Recursive Decomposition

Repository Patch execution follows a recursive decomposition model.

Repository Patch Units may represent either:

- structural engineering organization; or
- executable repository implementation.

When a Repository Patch Unit contains child Repository Patch Units, it is
considered a structural node within the Repository Patch Work Breakdown
Structure.

Structural Repository Patch Units shall:

- review the previous executable Repository Patch Unit;
- verify repository continuity;
- determine whether the current node is executable;
- descend to the first executable child Repository Patch Unit.

Structural Repository Patch Units shall not:

- generate Repository Update Packages;
- modify repository content;
- alter Story lifecycle progression.

Recursive decomposition continues until an executable leaf Repository Patch
Unit is reached.

After completion of a leaf Repository Patch Unit, execution returns to the
parent Repository Patch Work Breakdown Structure to determine the next
executable Repository Patch Unit.

Recursive decomposition continues until every executable Repository Patch Unit
within the Repository Patch Work Breakdown Structure has been completed, after
which control returns to the Story lifecycle.

### Cohesion Rule

Every Repository Patch Unit shall exhibit strong functional cohesion.

A Repository Patch Unit is cohesive when all repository modifications performed
within that unit contribute to a single engineering objective.

Repository Patch Units shall:

- implement one engineering responsibility;
- produce one logical repository outcome;
- remain independently understandable;
- minimize dependencies on unrelated Repository Patch Units;
- support independent verification.

When a Repository Patch Unit grows beyond a single cohesive responsibility, it
shall be recursively decomposed into child Repository Patch Units.

Recursive decomposition shall continue until each executable Repository Patch
Unit represents one cohesive engineering objective.

Cohesion improves:

- repository readability;
- engineering traceability;
- implementation maintainability;
- verification accuracy;
- long-term methodology evolution.

The Cohesion Rule governs the organization of the Repository Patch Work
Breakdown Structure and complements the Recursive Decomposition and Leaf Node
rules.

### Leaf Node Rule

A Repository Patch Unit is executable only when it is a leaf node within the
Repository Patch Work Breakdown Structure.

A leaf node is a Repository Patch Unit that contains no child Repository Patch
Units.

Only executable leaf Repository Patch Units shall:

- generate Repository Update Packages;
- modify repository artifacts;
- produce Repository Location Specifications;
- update Engineering Backlog implementation status;
- conclude with the next executable Repository Patch command.

Structural Repository Patch Units shall never perform repository
implementation.

Instead, structural Repository Patch Units recursively descend to the first
executable child Repository Patch Unit.

Execution returns to the parent Repository Patch Unit after completion of each
leaf node until all executable Repository Patch Units have been completed.

The Leaf Node Rule establishes a single implementation boundary throughout the
Repository Patch Work Breakdown Structure, ensuring that every repository
modification is isolated to one cohesive engineering responsibility.

Together, Recursive Decomposition, the Cohesion Rule, and the Leaf Node Rule
form the governing principles of the Repository Patch Work Breakdown
Structure.

### Engineering Philosophy

The ResumeForge Engineering Methodology is founded on the principle that
engineering processes should evolve through disciplined application rather than
ad hoc refinement.

Engineering improvements are expected to emerge through execution, observation,
verification, and continuous refinement.

The methodology is guided by the following principles:

- engineer once and reuse everywhere;
- extend proven patterns before introducing new ones;
- prefer evolutionary improvement over reinvention;
- preserve repository continuity at every implementation step;
- maintain clear ownership boundaries throughout the engineering lifecycle;
- decompose complexity into cohesive engineering responsibilities;
- implement only at executable leaf nodes;
- verify every repository modification before building upon it;
- document engineering decisions where they become repeatable methodology.

The Engineering Methodology shall favor consistency over novelty.

When multiple engineering solutions are possible, preference should be given to
the solution that best aligns with established methodology unless a measurable
engineering benefit justifies change.

Engineering discoveries shall be captured through the Engineering Backlog and
incorporated into the official methodology through future Engineering Stories.

The Engineering Methodology is intended to be self-improving.

Each completed Engineering Story should strengthen the methodology for all
future Stories by reducing ambiguity, increasing repeatability, and improving
engineering efficiency.

The objective of the ResumeForge Engineering Methodology is not merely to
produce software, but to continuously improve the engineering system that
produces the software.

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

### Engineering Continuity

Engineering Continuity is the architectural foundation of the ResumeForge Engineering Methodology (REM).

The ResumeForge Engineering Methodology is founded on the principle that every engineering session should leave the repository in a more understandable, more maintainable, more reproducible, more executable, and more valuable state than it was at the beginning of the session.

Engineering Continuity defines **why** the engineering lifecycle exists, while the Workflow Lifecycle defines **how** engineering progresses.

Engineering Continuity is achieved by:

- preserving engineering intent;
- synchronizing repository state;
- converting engineering discoveries into durable repository knowledge;
- reducing future engineering startup effort;
- continuously improving the engineering methodology.

Every lifecycle phase contributes to Engineering Continuity through its own responsibilities, collectively ensuring that engineering knowledge becomes progressively more complete, more consistent, and easier to execute over time.

### Repository Closeout Purpose

Repository Closeout is the lifecycle phase responsible for Engineering Continuity.

Its purpose is to transform completed engineering work into durable repository knowledge while preparing the repository for efficient continuation regardless of engineer, ChatGPT session, elapsed time, or project growth.

Repository Closeout is not the end of a Story.

Repository Closeout is the engineering bridge to the next Story.

### Repository Closeout Objectives

Repository Closeout shall:

1. Synchronize Repository State.
2. Capture Engineering Knowledge.
3. Capture Engineering Discoveries.
4. Improve the ResumeForge Engineering Methodology.
5. Synchronize Engineering and Development Roadmaps.
6. Reconcile the Engineering Backlog.
7. Preserve Engineering Context.
8. Optimize Future Engineering Session Startup.

The success of Repository Closeout is measured by the ability of a new engineering session to resume productive work with minimal reconstruction effort.

### Repository Closeout Execution Model

Repository Closeout executes as a structured engineering workflow that converts engineering discoveries into durable repository improvements.

Repository Closeout progresses through a sequence of engineering activities, with each activity producing the evidence required by the next.

The execution flow is:

1. Assess the current repository state.
2. Validate repository objectives.
3. Identify repository improvements.
4. Produce deterministic Repository Patch Units.
5. Verify engineering evidence, completion standards, and transition standards.
6. Prepare the repository for Commit by confirming Engineering Continuity and Repository Readiness.

The execution principles that follow define how each activity is performed. Together they provide a deterministic, auditable, and repeatable Repository Closeout process.

### Engineering Backlog Consolidation

Engineering stories frequently identify methodology improvements that are intentionally deferred to a future REM consolidation effort.

Repository Closeout is responsible for ensuring that these discoveries are preserved in an Engineering Backlog until they are formally evaluated and incorporated into the ResumeForge Engineering Methodology.

Every Engineering Backlog entry shall:

- identify the engineering problem discovered;
- describe the proposed methodology improvement;
- record the engineering rationale;
- identify the originating story;
- remain traceable until formally implemented, superseded, or rejected.

Engineering Backlog Consolidation transforms individual lessons learned into managed engineering work, ensuring that methodology improvements remain visible, actionable, and recoverable across future engineering sessions.

The Engineering Backlog is reviewed during Repository Closeout to verify that newly discovered methodology improvements have been captured before the story transitions to Commit.

### Engineering Roadmap Synchronization

The Engineering Roadmap defines the planned evolution of the ResumeForge Engineering Methodology.

While the Engineering Backlog preserves newly discovered improvements, the Engineering Roadmap establishes their implementation priority, sequencing, and long-term integration strategy.

Engineering Roadmap Synchronization ensures that approved methodology improvements progress through a deliberate engineering planning process rather than being incorporated opportunistically.

Engineering Roadmap Synchronization is responsible for:

- aligning Engineering Backlog entries with long-term engineering objectives;
- identifying implementation dependencies between methodology improvements;
- prioritizing future engineering work;
- maintaining a coherent evolution strategy for the ResumeForge Engineering Methodology;
- ensuring that approved improvements remain visible until implementation is complete.

Repository Closeout verifies that newly approved methodology improvements have been synchronized with the Engineering Roadmap before the repository transitions to Commit.

### Repository Status Documentation

Repository Closeout is responsible for ensuring that the repository accurately reflects its engineering state before transitioning to Commit.

Repository Status Documentation provides future engineering sessions with sufficient information to understand the repository's current condition without reconstructing prior engineering activity.

Repository Status Documentation verifies that repository status information is current, consistent, and traceable across repository artifacts.

Repository Status Documentation is responsible for confirming:

- repository documentation reflects the implemented engineering work;
- repository history accurately records completed engineering activities;
- repository checkpoints accurately represent the current repository state;
- engineering evidence remains traceable to the originating story;
- repository artifacts remain internally consistent.

The successful completion of Repository Status Documentation confirms that future engineering sessions can begin from the documented repository state rather than rebuilding context from repository history.

### Repository Closeout Verification

Repository Closeout concludes with a formal verification that all Repository Closeout responsibilities have been completed before transitioning to the Commit lifecycle.

Repository Closeout Verification confirms that the repository has been left in a coherent, maintainable, and recoverable state for future engineering sessions.

Repository Closeout Verification shall confirm that:

- Engineering Continuity has been preserved;
- Repository documentation accurately reflects approved engineering work;
- Engineering Backlog entries have been captured where required;
- Engineering Roadmap synchronization has been completed for approved methodology improvements;
- Repository status documentation accurately represents the repository state;
- Repository artifacts remain internally consistent;
- all Repository Update Packages have reached Repository-Ready Certification.

Repository Closeout transitions to Commit only after every Repository Closeout verification objective has been satisfied.

Successful Repository Closeout Verification certifies that the repository is prepared for both repository commit activities and future engineering session bootstrap.

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

## Engineering Lifecycle Governance

### Purpose

Engineering Lifecycle Governance establishes the architectural governance model for the ResumeForge Engineering Methodology (REM). It defines how engineering stories progress, how engineering work is organized, how implementation baselines evolve, and how repository modifications are governed. The objective is to provide deterministic engineering outcomes while minimizing unnecessary engineering cycles.

### Guiding Principle

The ResumeForge Engineering Methodology shall optimize for deterministic engineering outcomes with the fewest practical engineering cycles while preserving repository integrity, traceability, implementation quality, and engineering consistency.

### Layered REM Architecture

The REM is organized into three architectural layers.

#### Engineering Story Lifecycle

The Engineering Story Lifecycle defines the progression of an engineering story.

Current lifecycle:

1. Engineering Session Startup
2. Story Planning
3. Repository Implementation
4. Repository Closeout
5. Repository Commit
6. Story Complete

The lifecycle defines **where** a story is within its progression.

#### Development Story Lifecycle

The Development Story Lifecycle defines the authoritative execution model for all ResumeForge Development Stories.

Development Stories implement functional capabilities within the ResumeForge application while adhering to the engineering standards established by the Engineering Story Lifecycle.

##### Purpose

The Development Story Lifecycle ensures that application features are developed using a consistent, test-driven, evidence-based process that maintains repository quality and traceability.

##### Objectives

The Development Story Lifecycle shall:

- Deliver one cohesive functional capability per story.
- Maintain complete requirements traceability.
- Produce repository-ready implementation artifacts.
- Validate functionality through RED/GREEN verification.
- Preserve repository integrity throughout implementation.

##### Lifecycle

Development Stories progress through the following lifecycle phases.

| Phase | Primary Deliverable |
|--------|---------------------|
| Initiate | Engineering Decision Record |
| Review | Story Planning / Review Artifact |
| Implement | Package Artifact or Section Artifact |
| Verify | Verification Artifact |
| Commit | Repository Baseline |

Progression between lifecycle phases is permitted only after successful completion of the current phase.

##### Relationship to Engineering Stories

Engineering Stories improve the ResumeForge Engineering Methodology.

Development Stories apply that methodology to implement ResumeForge functionality.

Development Stories shall conform to the standards, quality gates, and execution principles established by the Engineering Story Lifecycle.

##### Lifecycle Principles

Development Stories inherit the following engineering principles:

- Single Functional Capability
- One Command, One Deliverable
- Package Before Sections
- Repository-Ready Implementation
- Evidence-Based Engineering
- Controlled Replanning

Where Development Story requirements conflict with implementation convenience, the Engineering Story Lifecycle governs.

##### Lifecycle Completion

A Development Story is complete when:

- all planned functionality has been implemented;
- all acceptance criteria have been satisfied;
- repository verification has completed successfully;
- repository documentation has been updated;
- repository history has been recorded;
- the repository baseline has been committed and tagged.

Completion establishes the new functional baseline for ResumeForge.

#### Active Engineering State

The Active Engineering State defines the minimum execution context that shall be maintained throughout every Engineering Story and Development Story lifecycle.

Its purpose is to preserve deterministic execution, provide an authoritative view of the current engineering activity, and establish an explicit re-entry point whenever execution is interrupted.

##### Purpose

The Active Engineering State provides a single source of truth describing where a story is within its lifecycle and what action is authorized next.

It enables engineering work to pause and resume without ambiguity.

##### Required State

The Active Engineering State shall identify:

- Active Story
- Story Classification
- Current Lifecycle
- Current Phase
- Current Step
- Current Section (when applicable)
- Current Status
- Previous Completed Step
- Next Authorized Step
- Repository Communication Status

##### State Management

The Active Engineering State shall be established at the beginning of every lifecycle response.

The state shall be updated only upon successful completion of the active lifecycle command.

Engineering discussions occurring outside the lifecycle shall preserve the current state and shall not advance the lifecycle.

##### Lifecycle Re-entry

Whenever execution temporarily departs from the lifecycle for engineering discussion, methodology refinement, or clarification, the Active Engineering State shall remain unchanged.

The response shall conclude with a **Lifecycle Re-entry** section containing:

- Current Story
- Current Phase
- Current Active Step
- Ready to Re-enter status
- Copy/paste-ready next valid command

This establishes the authoritative checkpoint for resuming execution.

##### Engineering Principles

The Active Engineering State shall ensure:

- deterministic lifecycle execution;
- explicit command authorization;
- one command produces one deliverable;
- interruption without loss of execution context;
- complete lifecycle traceability.

##### Lifecycle Responsibility

Maintaining the Active Engineering State is the responsibility of every lifecycle response.

Each response shall accurately reflect the repository's current execution state before authorizing the next lifecycle command.

#### Lifecycle Phase Contract

The Lifecycle Phase Contract defines the common execution contract shared by every phase of every ResumeForge lifecycle.

Its purpose is to ensure that each lifecycle phase has a clearly defined responsibility, produces one authoritative deliverable, satisfies explicit completion criteria, and authorizes the next valid phase without ambiguity.

##### Purpose

The Lifecycle Phase Contract standardizes lifecycle execution by establishing a consistent structure for every phase regardless of lifecycle type.

This contract applies equally to Engineering Stories and Development Stories.

##### Phase Responsibilities

Every lifecycle phase shall perform one primary responsibility.

| Phase | Primary Responsibility | Primary Deliverable |
|--------|------------------------|---------------------|
| Initiate | Select and authorize the next engineering capability | Engineering Decision Record |
| Review | Analyze, evaluate, and define the work to be performed | Review Artifact |
| Implement | Produce installation-ready implementation artifacts | Package Artifact or Section Artifact |
| Verify | Validate that implementation satisfies approved requirements | Verification Artifact |
| Commit | Establish the verified repository baseline | Repository Baseline |

A lifecycle phase shall not perform the responsibilities assigned to another phase.

##### One Command, One Deliverable

Every lifecycle command shall produce exactly one authoritative deliverable.

Commands shall not implicitly perform subordinate commands.

When subordinate implementation units exist, the parent command authorizes those units but does not execute them.

##### Package and Section Execution

When a lifecycle phase requires multiple implementation units, execution shall occur in two levels:

1. Package
2. Section

The package defines:

- implementation scope;
- execution order;
- dependencies;
- implementation units.

Each section performs exactly one implementation unit defined by the package.

##### Phase Completion Criteria

A lifecycle phase is complete only when:

- its primary responsibility has been fulfilled;
- its authoritative deliverable has been produced;
- required quality gates have been satisfied;
- the Active Engineering State has been updated;
- the next lifecycle command has been explicitly authorized.

##### Phase Boundaries

Each lifecycle phase shall remain within its defined responsibility.

Review phases shall not implement repository changes.

Implement phases shall not perform verification.

Verify phases shall not introduce new implementation.

Commit phases shall not reopen completed implementation work except through controlled replanning.

##### Controlled Lifecycle Advancement

Progression through the lifecycle shall occur only through explicit developer commands.

Lifecycle advancement shall never be implied by completion of a previous response.

Each completed response authorizes the next valid lifecycle command while preserving complete execution traceability.

#### Lifecycle Transition Model

The Lifecycle Transition Model defines the authoritative rules governing movement between lifecycle phases.

Its purpose is to ensure that lifecycle progression is deterministic, explicitly authorized, evidence-based, and completely traceable.

##### Purpose

The Lifecycle Transition Model establishes the legal execution paths through every ResumeForge Engineering Story and Development Story.

A lifecycle transition occurs only after the current phase has successfully completed its defined responsibilities and all required quality gates have been satisfied.

##### Standard Lifecycle Flow

Every ResumeForge story shall progress through the following lifecycle.

```text
Initiate
    ↓
Review
    ↓
Implement
    ↓
Verify
    ↓
Commit
```

A transition to the next phase shall occur only through an explicit developer command.

##### Transition Requirements

Before a lifecycle transition is authorized, the following conditions shall be satisfied:

- the current phase has completed successfully;
- the authoritative deliverable has been produced;
- all applicable quality gates have passed;
- the Active Engineering State has been updated;
- the next valid lifecycle command has been identified.

If any condition is not satisfied, the lifecycle shall remain in its current phase.

##### Controlled Re-entry

Engineering discussions, retrospectives, methodology refinement, and design exploration may temporarily interrupt lifecycle execution.

These discussions do not advance the lifecycle.

At the conclusion of every out-of-band engineering discussion, the response shall include a **Lifecycle Re-entry** section that identifies:

- Current Story
- Current Phase
- Current Active Step
- Ready to Re-enter status
- Copy/paste-ready next valid command

This establishes the authoritative checkpoint for resuming execution.

##### Controlled Replanning

When review, verification, or implementation identifies a planning deficiency, execution shall return to the earliest affected lifecycle phase.

Replanning replaces incremental correction whenever the approved implementation strategy is no longer valid.

All completed work that remains valid shall be preserved.

##### Illegal Transitions

The following transitions are prohibited:

- skipping lifecycle phases;
- implicitly advancing to another phase;
- executing multiple lifecycle commands within a single command response;
- reopening completed phases without controlled replanning;
- performing repository modifications outside an Implement phase;
- introducing new implementation during Verify.

##### Lifecycle Completion

A story reaches lifecycle completion when:

- Commit has successfully completed;
- the repository baseline has been established;
- repository history has been updated;
- checkpoint information has been recorded;
- the repository has been verified clean.

Completion establishes the new authoritative repository baseline and concludes the lifecycle.

#### Engineering Phases

Engineering work is organized into Engineering Phases.

Current phases:

- Story Planning
- Repository Patch Specifications
- Repository Closeout
- Repository Commit

Engineering Phases define **what engineering work** is being performed.

#### Engineering Execution Cycle

Every Engineering Phase follows the same execution model:

- Review
- Implement
- Verify

The Engineering Execution Cycle defines **how engineering work** is performed.

### Architectural Relationships

```text
Engineering Story
        │
        ▼
Engineering Story Lifecycle
        │
        ▼
Engineering Phase
        │
        ▼
Engineering Execution Cycle
```

### Governance Principles

The REM shall adhere to the following principles:

- Engineering Story Lifecycle governs story progression.
- Engineering Phases govern engineering work.
- Engineering Execution Cycle governs engineering execution.
- Engineering Decision Records govern methodology changes.
- Repository modifications shall be deterministic.
- Repository-ready updates shall reference verified repository structure.
- Repository-ready updates shall identify the correct implementation operation.
- Only one approved Implementation Baseline may exist at any time.

### Repository Patch Continuity Verification

Beginning with RPU-02, every Repository Patch Unit implementation shall begin by verifying the successful application of the immediately preceding Repository Patch Unit.

Repository Patch Continuity Verification confirms:

- previous RPU successfully applied,
- repository continuity maintained,
- repository ready for current implementation.

RPU-01 is exempt.

### Repository Structure Verification

Repository Structure Verification shall verify:

- target document,
- verified repository anchor,
- anchor hierarchy,
- implementation operation (Insert, Replace, Append, or Delete),
- repository readiness.

Repository-ready updates shall never be generated from assumed repository structure.

### Re-entry Governance

Engineering phase re-entry shall be classified before repeating a phase.

#### Corrective Re-entry

Corrective Re-entry repairs incomplete or failed engineering work.

#### Evolutionary Re-entry

Evolutionary Re-entry incorporates approved methodology improvements that do not materially change scope, dependencies, or sequencing.

### Engineering Freeze Governance

Material methodology changes affecting the approved Implementation Baseline shall initiate an Engineering Freeze.

During an Engineering Freeze:

- RPU implementation pauses.
- The active baseline is frozen.
- The Nested REM Update Process is completed.
- A Baseline Revision or Baseline Replacement decision is made before implementation resumes.

### Engineering Phase Transition Governance

Every engineering response shall conclude with:

- Evidence Chain
- Completion Verification
- Engineering Phase Status
- Authoritative Next Command

The Next Command constitutes the formal transition between engineering phases.

## Engineering Decision Record Governance

### Purpose

Engineering Decision Records (EDRs) provide the authoritative record of architectural and methodology decisions made during the evolution of the ResumeForge Engineering Methodology (REM). They preserve the rationale behind engineering decisions, support future maintenance, and provide traceability between engineering discussions and repository implementation.

### Governance Principles

Engineering Decision Records shall be used whenever an engineering decision:

- changes the REM architecture,
- introduces or modifies governance,
- changes repository implementation strategy,
- affects engineering workflow,
- establishes new terminology,
- changes engineering quality requirements.

Routine implementation details that do not affect methodology or architecture do not require an Engineering Decision Record.

### Engineering Decision Record Structure

Every Engineering Decision Record shall contain:

- Decision
- Context
- Analysis
- Recommendation
- Repository Impact
- Evidence
- Verification

This structure provides consistent documentation and supports future engineering review.

### Decision Authority

Approved Engineering Decision Records become part of the current Implementation Baseline.

Implementation guidance derived from approved Engineering Decision Records shall be reflected in:

- Story Planning,
- Repository Patch Specifications,
- Engineering Quality Gates,
- Repository implementation.

Superseded Engineering Decision Records shall remain part of the engineering history to preserve architectural traceability.

### Relationship to Engineering Freeze Governance

When a methodology change triggers an Engineering Freeze, the resulting methodology update shall be documented by one or more Engineering Decision Records before implementation resumes.

The approved Engineering Decision Record(s) become the authoritative basis for either:

- Implementation Baseline Revision, or
- Implementation Baseline Replacement.

### Traceability

Engineering Decision Records shall maintain traceability between:

- Engineering discussions,
- Engineering recommendations,
- Repository-ready updates,
- Final repository implementation.

This traceability ensures that future engineering work can understand not only *what* changed, but *why* it changed.

## Repository Governance

### Purpose

Repository Governance establishes the standards that ensure all modifications to the ResumeForge repository are deterministic, traceable, verifiable, and maintainable. It defines how repository updates are planned, validated, implemented, and documented throughout the ResumeForge Engineering Methodology (REM).

### Governance Principles

Repository modifications shall adhere to the following principles:

- All repository updates shall be based on verified repository structure.
- Every repository modification shall be deterministic and reproducible.
- Repository-ready updates shall identify the implementation operation before implementation.
- Only one approved Implementation Baseline may exist at any time.
- Repository history shall preserve engineering traceability.

### Repository Modification Operations

Repository modifications shall explicitly identify one of the following operations:

- Insert Before
- Insert After
- Replace Section
- Append
- Delete (future capability)

The required operation shall be determined through Repository Structure Verification and shall never be assumed.

### Repository Integrity

Repository integrity shall be preserved by ensuring:

- existing engineering work is not unintentionally overwritten,
- section hierarchy remains consistent,
- verified anchors are used for all repository-ready updates,
- implementation boundaries are explicitly identified.

### Repository Traceability

Every repository modification shall maintain traceability between:

- Engineering Decision Records,
- Repository Patch Units,
- repository-ready updates,
- implemented repository changes.

This traceability provides an auditable engineering history and supports future maintenance and methodology evolution.

### Relationship to Repository Patch Units

Repository Patch Units are the authorized mechanism for modifying repository documentation within the REM.

Each Repository Patch Unit shall:

- verify repository continuity (when applicable),
- verify repository structure,
- identify the implementation operation,
- produce a repository-ready update,
- include an Evidence Chain,
- conclude with Engineering Phase Status and the Authoritative Next Command.

This governance ensures consistent repository evolution throughout every engineering story.

## Repository Structure Verification

### Purpose

Repository Structure Verification establishes the mandatory validation process that shall be completed before generating every Repository Patch Unit. Its purpose is to ensure that repository-ready updates are based on the actual repository state rather than assumptions, preventing incorrect insertions, duplicate sections, and invalid implementation operations.

### Verification Objectives

Repository Structure Verification shall verify:

- Target document.
- Verified repository anchor.
- Anchor hierarchy.
- Section existence.
- Implementation operation.
- Repository readiness.

Implementation shall not proceed until all verification objectives have been satisfied.

### Repository Verification Process

Repository Structure Verification shall be performed in the following order:

1. Review the current repository.
2. Verify the target document.
3. Verify the requested section or anchor.
4. Determine whether the requested section already exists.
5. Select the appropriate implementation operation.
6. Verify the implementation boundary.
7. Confirm repository readiness.

### Implementation Operations

The implementation operation shall always be explicitly identified.

Supported operations include:

- Insert Before
- Insert After
- Replace Section
- Append
- Delete (future capability)

The operation shall be determined from the verified repository state and shall never be assumed.

### Repository Anchor Governance

Verified repository anchors shall:

- uniquely identify the implementation location,
- remain stable throughout implementation,
- preserve document hierarchy,
- support deterministic repository updates.

If the requested anchor is not found, Repository Structure Verification shall identify the nearest valid implementation point and document the rationale before implementation continues.

### Repository Structure Changes

Repository Structure Verification shall determine whether the repository state requires:

- insertion of a new section,
- replacement of an existing section,
- extension of an existing section,
- postponement of implementation due to repository inconsistency.

Repository changes shall never be inferred from previous engineering sessions.

### Relationship to Repository Patch Continuity Verification

Repository Patch Continuity Verification confirms that previous engineering work remains intact.

Repository Structure Verification determines how the current engineering work shall be applied.

These verification activities are complementary and shall always be performed in this order:

1. Repository Patch Continuity Verification (when applicable).
2. Repository Structure Verification.
3. Repository implementation.

## Engineering Quality Gates

### Purpose

Engineering Quality Gates establish the mandatory verification criteria that must be satisfied before an engineering phase is considered complete. Their purpose is to ensure consistent engineering quality, deterministic repository evolution, and implementation readiness throughout the ResumeForge Engineering Methodology (REM).

### Quality Gate Sequence

Every Repository Patch Unit shall satisfy the following quality gates in order:

1. Repository Patch Continuity Verification (RPU-02 and later).
2. Repository Structure Verification.
3. Repository-ready implementation.
4. Evidence Chain completion.
5. Completion Verification.
6. Engineering Phase Status.
7. Authoritative Next Command.

Implementation shall not advance until each applicable quality gate has passed.

### Repository Patch Continuity Gate

Beginning with RPU-02, verify:

- the previous Repository Patch Unit has been successfully applied,
- repository continuity has been preserved,
- the repository is ready for the current implementation.

### Repository Structure Gate

Verify:

- target document,
- verified repository anchor,
- section existence,
- implementation operation,
- implementation boundary,
- repository readiness.

### Implementation Baseline Stability Gate

Before generating repository-ready updates, verify:

- no active Engineering Freeze exists,
- the current Implementation Baseline is approved,
- no unresolved Nested REM Update Process is in progress.

If any of these conditions fail, implementation shall stop until the methodology has been stabilized.

### Evidence Gate

Every Repository Patch Unit shall include an Evidence Chain consisting of:

- Evidence
- Analysis
- Recommendation
- Verification

### Completion Gate

Every Repository Patch Unit shall conclude with:

- RPU Completion Verification,
- Engineering Phase Status,
- Authoritative Next Command.

A Repository Patch Unit is not complete until all required quality gates have passed.

## Engineering Execution Governance

### Purpose

Engineering Execution Governance defines the standard execution model used throughout the ResumeForge Engineering Methodology (REM). It establishes a consistent, repeatable process for performing engineering work while ensuring repository integrity, implementation quality, and engineering traceability.

### Engineering Execution Cycle

Every Engineering Phase shall be executed using the following sequence:

1. Review
2. Implement
3. Verify

This execution cycle applies uniformly to all engineering phases unless an approved Engineering Decision Record explicitly defines an exception.

### Review

The Review activity establishes the engineering baseline before implementation.

Review shall:

- inspect the current repository state,
- evaluate the active Implementation Baseline,
- identify repository impacts,
- determine required Repository Patch Units,
- identify blockers,
- determine whether an Engineering Freeze is required.

Review activities shall not modify the repository.

### Implement

The Implement activity produces repository-ready engineering artifacts.

Implement shall:

- perform Repository Patch Continuity Verification (when applicable),
- perform Repository Structure Verification,
- identify the implementation operation,
- generate repository-ready updates,
- preserve engineering traceability.

Implementation shall follow the approved Implementation Baseline.

### Verify

The Verify activity confirms that implementation has been successfully completed.

Verification shall confirm:

- repository modifications were correctly applied,
- repository continuity has been preserved,
- implementation objectives have been satisfied,
- engineering quality gates have passed,
- the repository is ready for the next engineering activity.

### Engineering Execution Principles

Engineering execution shall adhere to the following principles:

- Execute one Engineering Phase at a time.
- Maintain a single approved Implementation Baseline.
- Perform required verification before implementation.
- Preserve repository integrity.
- Record engineering evidence.
- Produce deterministic engineering outcomes.

### Relationship to Engineering Quality Gates

Engineering Execution Governance defines **how** engineering work is performed.

Engineering Quality Gates define **when** engineering work is considered complete.

Together they provide the operational framework for consistent execution throughout the REM.

## Repository Patch Unit Governance

### Purpose

Repository Patch Unit (RPU) Governance defines the standard for planning, generating, reviewing, implementing, and verifying repository modifications within the ResumeForge Engineering Methodology (REM). Each Repository Patch Unit represents a single, repository-ready unit of engineering work.

### Repository Patch Unit Principles

Every Repository Patch Unit shall:

- represent one logical repository modification,
- be independently reviewable,
- be independently implementable,
- be independently verifiable,
- preserve repository integrity,
- maintain engineering traceability.

Repository Patch Units shall be ordered to minimize implementation risk and support deterministic repository evolution.

### Standard Repository Patch Unit Workflow

Beginning with RPU-02, every Repository Patch Unit implementation shall execute the following sequence:

1. Repository Patch Continuity Verification
2. Repository Structure Verification
3. Repository Patch Unit Metadata
4. Repository-ready Update
5. Evidence Chain
6. Repository Patch Unit Completion Verification
7. Engineering Phase Status
8. Authoritative Next Command

RPU-01 begins with Repository Structure Verification because no previous Repository Patch Unit exists.

### Repository Patch Unit Completion Verification

A Repository Patch Unit shall not be considered complete until all of the following have been confirmed:

- Repository Patch Continuity Verification completed (when applicable).
- Repository Structure Verification completed.
- Repository-ready update produced.
- Evidence Chain completed.
- Engineering Phase Status recorded.
- Authoritative Next Command issued.

### Repository Patch Unit Independence

Each Repository Patch Unit shall be self-contained and shall not rely on unpublished engineering work.

Repository Patch Units shall reference only:

- verified repository state,
- approved Implementation Baseline,
- completed Repository Patch Units.

### Relationship to Engineering Quality Gates

Repository Patch Units implement engineering work.

Engineering Quality Gates determine whether each Repository Patch Unit satisfies the required engineering standards before implementation proceeds.

### Governance Objective

Repository Patch Unit Governance ensures that repository modifications remain deterministic, traceable, reproducible, and maintainable throughout the engineering lifecycle.

## Continuous Improvement Governance

### Purpose

Continuous Improvement Governance defines how the ResumeForge Engineering Methodology (REM) evolves while preserving engineering stability, implementation quality, and repository integrity. It establishes a controlled process for incorporating lessons learned without disrupting active engineering work.

### Guiding Principle

The REM shall continuously improve through disciplined, evidence-based engineering. Improvements shall enhance determinism, reduce unnecessary engineering cycles, and maintain a single authoritative Implementation Baseline.

### Improvement Classification

Methodology improvements shall be classified before implementation.

#### Minor Improvement

A Minor Improvement:

- clarifies existing guidance,
- improves documentation,
- refines terminology,
- does not materially change architecture, scope, sequencing, or implementation strategy.

Minor Improvements may be incorporated through **Evolutionary Re-entry**.

#### Material Improvement

A Material Improvement:

- changes governance,
- changes engineering workflow,
- changes the Implementation Baseline,
- affects Repository Patch Specifications,
- changes engineering lifecycle behavior.

Material Improvements shall initiate **Engineering Freeze Governance**.

### Engineering Freeze

When a Material Improvement is identified:

1. Freeze the active Implementation Baseline.
2. Suspend Repository Patch Unit generation.
3. Initiate the Nested REM Update Process.
4. Complete and approve the methodology update.
5. Determine whether the result requires:
   - **Implementation Baseline Revision**, or
   - **Implementation Baseline Replacement**.
6. Resume the parent engineering story using the approved baseline.

### Nested REM Update Process

The Nested REM Update Process shall:

- isolate methodology work from story implementation,
- complete its own engineering lifecycle,
- preserve engineering traceability,
- return control to the parent story only after methodology approval.

Upon completion, the parent Review phase shall regenerate or revise the Repository Patch Specification package as required by the approved methodology.

### Evolutionary Re-entry

Evolutionary Re-entry may be used only for approved Minor Improvements that do not materially affect:

- story scope,
- dependencies,
- sequencing,
- repository implementation strategy,
- approved Implementation Baseline.

### Continuous Improvement Backlog

Approved methodology improvements that are not blockers shall be recorded for future engineering stories rather than introduced during active implementation.

This preserves Implementation Baseline stability while ensuring valuable improvements are not lost.

### Governance Objective

Continuous Improvement Governance ensures that the REM evolves in a controlled, traceable, and deterministic manner while maintaining engineering throughput and repository integrity.

## Engineering Documentation Governance

### Purpose

Engineering Documentation Governance establishes the standards for creating, maintaining, and evolving engineering documentation within the ResumeForge Engineering Methodology (REM). Its purpose is to ensure that engineering documentation remains authoritative, consistent, deterministic, and maintainable throughout the engineering lifecycle.

### Documentation Principles

Engineering documentation shall:

- maintain a single authoritative source for each engineering concept,
- preserve engineering traceability,
- use consistent terminology throughout the repository,
- remain deterministic and reproducible,
- distinguish governance from implementation guidance,
- evolve through approved engineering processes.

Documentation shall not duplicate authoritative content without explicit justification.

### Documentation Hierarchy

Engineering documentation shall be organized according to the following hierarchy:

1. Engineering Governance
2. Engineering Process
3. Engineering Standards
4. Engineering Procedures
5. Engineering Examples

Each level shall reference higher-level guidance rather than redefine it.

### Documentation Update Governance

Every documentation update shall identify:

- target document,
- verified repository anchor,
- implementation operation,
- implementation boundary,
- affected engineering concepts.

Documentation updates shall always be based on the verified repository state.

### Documentation Consistency

When modifying documentation, engineering work shall:

- preserve heading hierarchy,
- maintain terminology consistency,
- avoid duplicate authoritative sections,
- update cross-references where required,
- preserve repository readability.

### Documentation Evolution

Engineering documentation shall evolve through the governance mechanisms defined by the REM.

Minor documentation improvements may be incorporated through Evolutionary Re-entry.

Material documentation changes that alter engineering governance, implementation baselines, or methodology architecture shall follow Engineering Freeze Governance and the Nested REM Update Process.

### Documentation Traceability

Engineering documentation shall maintain traceability between:

- Engineering Decision Records,
- Story Planning,
- Repository Patch Specifications,
- implemented repository changes,
- engineering history.

This traceability ensures that future engineering work can understand the purpose, rationale, and evolution of repository documentation.

### Governance Objective

Engineering Documentation Governance ensures that the ResumeForge repository remains a coherent engineering knowledge base whose documentation evolves with the same rigor applied to repository implementation.

## Engineering Session Governance

### Purpose

Engineering Session Governance establishes the standard operating model for every ResumeForge engineering session. Its purpose is to ensure that engineering work begins from a verified repository state, proceeds from an approved Implementation Baseline, and concludes with a deterministic transition to the next engineering activity.

### Engineering Session Lifecycle

Every engineering session shall follow the same lifecycle:

1. Engineering Session Startup
2. Engineering Activity Execution
3. Engineering Session Closeout

Each session shall begin by establishing repository state and shall conclude by documenting engineering status and the next authoritative engineering command.

### Engineering Session Startup

Engineering Session Startup shall establish the engineering baseline before any implementation begins.

Startup activities shall include:

- Repository State Audit.
- Repository connectivity verification.
- Engineering environment verification.
- Review of the current engineering story.
- Review of the active engineering phase.
- Verification of the approved Implementation Baseline.
- Identification of blockers requiring Engineering Freeze Governance.
- Confirmation of the next engineering objective.

No repository modifications shall occur during Engineering Session Startup.

### Engineering Activity Execution

Engineering work shall be performed in accordance with:

- the approved Engineering Story,
- the current Engineering Phase,
- the Engineering Execution Cycle,
- the approved Implementation Baseline.

Repository modifications shall only be performed through approved Repository Patch Units.

### Engineering Session Closeout

Every engineering session shall conclude by documenting:

- work completed,
- repository status,
- Engineering Phase Status,
- outstanding blockers,
- Evolutionary Re-entry items (if any),
- authoritative Next Command.

The Engineering Session Closeout establishes the transition point for the next engineering session.

### Session Continuity

Engineering sessions shall maintain continuity by:

- verifying repository continuity before implementation,
- preserving the approved Implementation Baseline,
- recording Engineering Decision Records for methodology changes,
- maintaining traceability between engineering sessions.

Engineering work shall never resume from assumptions about repository state.

### Governance Objective

Engineering Session Governance provides a repeatable operational framework that allows engineering work to pause and resume across sessions without sacrificing determinism, repository integrity, or engineering traceability.

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

### Phase Exit Gate (PEG)

Every Story Planning transition shall conclude with a Phase Exit Gate.

The Phase Exit Gate determines whether the next lifecycle phase is
authorized to begin.

A lifecycle phase is not considered complete until its Phase Exit Gate has
been evaluated.

The purpose of the Phase Exit Gate is to prevent engineering from entering
a lifecycle phase that cannot execute deterministically.

---


### Canonical Execution Contract

Every executable lifecycle phase shall inherit a Canonical Execution
Contract.

The Canonical Execution Contract defines the minimum engineering
specification required before execution of that lifecycle phase may begin.

The contract is owned by the parent lifecycle phase.

Child lifecycle phases inherit the contract and specialize only the
behavior unique to their responsibilities.

Execution responsibilities shall never be redefined by child lifecycle
phases.

---

#### Canonical Contract Components

Every executable lifecycle phase shall define, at minimum:

- Purpose
- Inputs
- Outputs
- Repository Operations
- Verification Requirements
- Completion Criteria
- Ownership Transfer

These components constitute the minimum executable engineering contract.

Lifecycle phases may extend this contract but shall not omit any required
component.

---

#### Parent / Child Lifecycle Responsibilities

Parent lifecycle phases define engineering architecture.

Child lifecycle phases inherit that architecture and provide only the
specialization necessary to fulfill their assigned responsibilities.

Engineering architecture shall exist in one authoritative location.

---

#### Contract Inheritance

Child lifecycle phases shall reference inherited engineering contracts
rather than duplicate them.

Where additional responsibilities are required, they shall be documented
as explicit extensions to the inherited contract.

This preserves architectural consistency while minimizing repository
duplication.

---

#### Deterministic Execution

A Canonical Execution Contract shall enable independent engineers to
execute a lifecycle phase without interpreting engineering intent.

Execution behavior shall originate from the approved engineering
specification rather than engineering discussion.

If execution requires interpretation, the contract is incomplete and the
lifecycle shall not transition through the Phase Exit Gate.

### Engineering Readiness Assessment (ERA)

The Phase Exit Gate is evaluated by performing an Engineering Readiness
Assessment (ERA).

The ERA validates that the proposed next lifecycle phase is ready to
execute without engineering interpretation.

The ERA shall evaluate, at minimum:

• Ownership Readiness
• Specification Readiness
• Repository Readiness
• Execution Readiness
• Lifecycle Readiness

The ERA produces one of two outcomes:

PASS
    Transition Authorized

FAIL
    Transition Denied

If the ERA fails, the lifecycle shall not advance.

---

### Lifecycle Escalation

When the Engineering Readiness Assessment determines that unresolved work
belongs to another lifecycle phase:

1. Suspend the current lifecycle phase.
2. Record the engineering reason for suspension.
3. Return ownership to the authoritative lifecycle phase.
4. Resolve the engineering deficiency.
5. Verify the updated engineering specification.
6. Resume the suspended lifecycle phase.

Lifecycle Escalation is an engineering control mechanism.

It is not a restart of the story.

---

### Phase Responsibility Integrity

Each lifecycle phase owns a distinct engineering responsibility.

Review
    Produces complete engineering specifications.

Implement
    Executes approved engineering specifications.

Verify
    Confirms implemented work matches the approved engineering
    specification.

A lifecycle phase shall not assume the responsibilities of another phase.

---

### Implementation Readiness

Implement shall begin only after the Engineering Readiness Assessment has
authorized lifecycle transition.

Implement shall never:

• complete engineering design;
• infer repository architecture;
• interpret incomplete engineering specifications;
• compensate for planning deficiencies.

Implementation executes approved engineering specifications.

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

### RED Evidence Integrity

The RED phase establishes the engineering evidence required before implementation begins. Its purpose is to ensure that implementation is driven by engineering analysis rather than assumptions, producing an implementation package that fully defines the work to be completed during the GREEN phase.

#### Required Engineering Evidence

Before the RED phase may be considered complete, the implementation package shall include:

- Functional requirements affected by the proposed change.
- Analysis of the impacted production code.
- Analysis of existing implementation patterns within the repository.
- Analysis of existing testing patterns applicable to the proposed change.
- Planned production code modifications.
- Planned additions or modifications to automated tests.
- Expected failing test cases demonstrating the required behavior.
- Traceability between requirements, implementation, and testing.
- Identification of unresolved engineering questions or blockers.

#### RED Completion Criteria

The RED phase is complete only when:

- All required engineering evidence has been documented.
- Existing implementation patterns have been analyzed.
- Existing testing patterns have been analyzed.
- Expected failing tests have been identified.
- The implementation package provides sufficient engineering guidance to perform GREEN implementation without requiring additional engineering analysis.
- Outstanding engineering questions have been resolved or explicitly documented as blockers.

Completion of the RED phase authorizes progression to the GREEN phase. It does not authorize production code modification until GREEN implementation begins.

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

### Repository Patch Execution Planning

Repository Patch implementation begins with execution planning rather than repository modification. The purpose of execution planning is to determine the complete implementation strategy required to satisfy the approved engineering story before any Repository Patch Units (RPUs) are executed.

#### Repository Patch Execution Matrix (RPEM)

The Repository Patch Execution Matrix (RPEM) is the authoritative execution plan for the Repository Patch phase.

The RPEM shall:

- Identify every Repository Patch Unit (RPU) required to complete the story.
- Define the execution order of each RPU.
- Identify any RPUs that require subdivision into child sections (`RPU-0x.x`).
- Establish the parent-child relationships between RPUs and their subdivisions.
- Remain fixed for the duration of the story unless the approved story scope changes.

Execution planning is performed exactly once for each engineering story.

#### Implementation Decision

The initial **Implement: Repository Patch Specifications (GREEN)** command shall determine whether the approved engineering story requires:

- a single Repository Patch Unit, or
- multiple Repository Patch Units.

If multiple RPUs are required, the implementation shall generate the complete Repository Patch Execution Matrix before any repository modifications are produced.

Repository updates begin only after the Repository Patch Execution Matrix has been established.

#### Execution Authority

Once approved, the Repository Patch Execution Matrix becomes the authoritative execution plan for the Repository Patch phase.

Subsequent implementation commands shall execute the approved matrix sequentially without re-planning the story unless the approved story scope changes.

### Sequential Repository Patch Execution

After the Repository Patch Execution Matrix (RPEM) has been established, implementation proceeds by executing one Repository Patch Unit (RPU) at a time in the approved sequence.

#### Sequential Execution

Each implementation command shall perform the following activities in order:

1. Review the previously completed Repository Patch Unit (or subdivision).
2. Verify that the previous implementation was correctly incorporated into the repository.
3. Correct the previous implementation if necessary.
4. Generate exactly one new repository-ready implementation deliverable.
5. Identify the next implementation command.
6. End execution.

No implementation command shall generate more than one Repository Patch Unit or subdivision.

#### Continuity Validation

Repository Patch execution is continuous.

Each implementation command begins by validating the immediately preceding implementation before producing additional repository modifications.

If the previous implementation is incomplete or incorrect:

- Execution shall stop.
- The previous implementation shall be corrected.
- No subsequent Repository Patch Unit shall be generated until continuity has been restored.

#### Execution Progression

Execution shall follow the approved Repository Patch Execution Matrix without skipping approved Repository Patch Units.

Implementation shall not return to Repository Patch review until every Repository Patch Unit and approved subdivision defined by the execution matrix has been completed.

### Recursive Execution and Completion Governance

Repository Patch execution is hierarchical. Repository Patch Units (RPUs) may be implemented as either a single repository update or as a parent RPU containing one or more subordinate implementation sections (`RPU-0x.x`).

#### Recursive Execution

When the approved Repository Patch Execution Matrix identifies an RPU requiring subdivision:

- The parent RPU establishes the subdivision plan.
- No repository update is generated by the parent RPU beyond the approved subdivision matrix.
- Each subordinate section (`RPU-0x.x`) is implemented sequentially.
- Each subordinate implementation begins by validating the immediately preceding completed implementation.
- After the final subordinate section has been completed, execution returns to the parent execution sequence.

This recursive execution model allows complex engineering changes to be implemented incrementally while maintaining continuous engineering validation.

#### Completion Governance

Execution continues until every Repository Patch Unit and every approved subdivision defined by the Repository Patch Execution Matrix has been completed.

A parent Repository Patch Unit shall not be considered complete until all of its subordinate implementation sections have been successfully implemented.

The Repository Patch phase shall not transition to the next engineering workflow phase until:

- Every Repository Patch Unit has been implemented.
- Every approved subdivision has been completed.
- Repository continuity has been verified throughout execution.
- All repository updates have been successfully incorporated into the repository.

Completion of the Repository Patch Execution Matrix authorizes progression to the subsequent workflow phase.

### Repository Location Integrity

Repository Update Packages shall identify a single, deterministic repository location for every repository modification.

#### Repository Location Specification (RLS)

Every Repository Update Package shall include a Repository Location Specification consisting of:

- Target repository document.
- Verified Primary Anchor.
- Verified Secondary Anchor.
- Explicit insertion rule.
- Repository verification summary.

The Repository Location Specification becomes part of the engineering evidence supporting the repository modification.

#### Anchor Verification

Primary and Secondary Anchors shall be copied verbatim from the current repository.

Anchors shall:

- Match the repository heading exactly.
- Preserve the repository heading level.
- Be verified against the current repository state.
- Never be inferred or reconstructed from memory.

#### Location Determination

The insertion rule shall uniquely identify where the repository update is to be applied.

Acceptable insertion rules include:

- Immediately before a verified heading.
- Immediately after a verified heading.
- Append as the final subsection within a verified parent section.

Positional instructions that require interpretation are prohibited.

#### Repository Location Continuity

When a parent Repository Patch Unit establishes a verified Repository Location Specification, child Repository Patch Units may inherit that location.

Each child implementation shall verify that the inherited Repository Location Specification remains valid before generating repository updates.

If repository structure changes invalidate the inherited location, execution shall stop until a new Repository Location Specification has been established.

### Methodology Continuity Law

The ResumeForge Engineering Methodology (REM) shall evolve incrementally while preserving established engineering practices that have been validated through implementation experience.

#### Purpose

Methodology improvements shall extend or refine existing engineering processes rather than replacing them unnecessarily. The objective is to preserve engineering consistency across development stories while allowing the methodology to mature through practical application.

#### Continuity Principles

When introducing methodology changes:

- Existing approved methodology shall remain authoritative unless explicitly superseded.
- New engineering guidance shall integrate with existing workflow rather than duplicate or conflict with established practices.
- Methodology enhancements shall preserve compatibility with prior engineering stories whenever practical.
- Engineering terminology shall remain consistent throughout the repository.

#### Methodology Evolution

Engineering observations, lessons learned, and validated workflow improvements identified during implementation shall be accumulated throughout the engineering story.

These improvements shall be incorporated into the official ResumeForge Engineering Methodology during the designated methodology update phase rather than immediately modifying the baseline methodology during active implementation.

#### Regression Prevention

Methodology changes shall not introduce unnecessary workflow cycles, duplicate engineering responsibilities, or invalidate previously approved engineering practices without documented engineering justification.

Any methodology change that supersedes an existing process shall explicitly identify:

- The process being superseded.
- The engineering rationale.
- The replacement process.
- The expected engineering benefit.

This continuity model ensures that the ResumeForge Engineering Methodology evolves as a coherent engineering system rather than a collection of isolated process changes.

### Story Execution Planning Law

Repository Patch implementation shall separate execution planning from execution. The complete execution strategy for an engineering story shall be established before repository modifications begin.

#### Execution Planning

Execution planning is performed exactly once during the initial **Implement: Repository Patch Specifications (GREEN)** command.

Execution planning shall:

- Analyze the approved engineering story as a whole.
- Determine the complete set of Repository Patch Units (RPUs) required to satisfy the story.
- Identify any RPUs requiring subdivision into implementation sections (`RPU-0x.x`).
- Establish the execution order for all RPUs and subdivisions.
- Produce the Repository Patch Execution Matrix (RPEM).

No repository modifications shall be generated during execution planning.

#### Repository Patch Execution Matrix

The Repository Patch Execution Matrix (RPEM) is the authoritative implementation plan for the Repository Patch phase.

Once established, the RPEM shall:

- Define the complete execution tree for the engineering story.
- Remain fixed throughout execution unless the approved story scope changes.
- Serve as the authoritative sequence for all subsequent Repository Patch implementations.

#### Execution Model

Implementation shall execute the Repository Patch Execution Matrix sequentially.

Each implementation command shall:

1. Validate the immediately preceding implementation.
2. Generate exactly one approved Repository Patch Unit or subdivision.
3. Identify the next implementation command.
4. End execution.

When an RPU contains subordinate implementation sections, execution shall complete every subordinate section before returning to the parent execution sequence.

#### Story Completion

Execution planning is complete when the Repository Patch Execution Matrix has been established.

Repository Patch implementation is complete only after every Repository Patch Unit and every approved subdivision defined by the Repository Patch Execution Matrix has been successfully implemented.

### Repository Patch Numbering and Execution Hierarchy

Repository Patch implementation shall use a hierarchical numbering model that accurately represents the engineering execution structure for the approved Repository Patch Execution Matrix (RPEM).

#### Repository Patch Unit Numbering

Each top-level Repository Patch Unit shall use the format:

- `RPU-01`
- `RPU-02`
- `RPU-03`

Each Repository Patch Unit represents one logical engineering capability within the Repository Patch phase.

#### Subdivision Numbering

When a Repository Patch Unit cannot reasonably be completed within a single implementation response, it shall be subdivided.

Subdivisions shall use the format:

- `RPU-03.1`
- `RPU-03.2`
- `RPU-03.3`

Subdivisions remain part of their parent Repository Patch Unit and shall not be treated as independent RPUs.

#### Execution Hierarchy

Repository Patch implementation follows a hierarchical execution model.

A parent Repository Patch Unit may either:

- Produce a repository update directly, or
- Establish a subdivision plan for subordinate implementation sections.

When subordinate sections exist:

- Parent execution pauses.
- Child sections execute sequentially.
- Upon completion of the final child section, execution returns to the parent sequence defined by the Repository Patch Execution Matrix.

This recursive execution model preserves engineering continuity while supporting complex methodology updates.

#### Numbering Integrity

Repository Patch numbering shall remain stable throughout implementation.

Repository Patch Units and subdivisions shall not be renumbered after execution planning unless the approved engineering story scope changes and the Repository Patch Execution Matrix is formally regenerated.

Stable numbering ensures:

- deterministic execution,
- reproducible engineering history,
- consistent implementation references,
- accurate methodology traceability.

### GREEN Phase Completion Governance

Completion of the GREEN Repository Patch phase is governed by successful execution of the approved Repository Patch Execution Matrix (RPEM). Completion is determined by execution of the approved engineering work, not by completion of individual Repository Patch Units in isolation.

#### Completion Requirements

The GREEN Repository Patch phase shall not be considered complete until:

- Every Repository Patch Unit (RPU) defined by the approved Repository Patch Execution Matrix has been implemented.
- Every approved child implementation section (`RPU-0x.x`) has been completed.
- Repository continuity has been maintained throughout execution.
- All required repository modifications have been incorporated into the repository.
- No approved Repository Patch work remains outstanding.

#### GREEN Phase Completeness Review

After the final Repository Patch Unit has been implemented, a GREEN Phase Completeness Review shall be performed.

The review shall verify:

- The approved Repository Patch Execution Matrix has been fully traversed.
- Every execution node has been completed.
- Parent Repository Patch Units containing child implementation sections are complete.
- The repository reflects every approved repository modification.
- Repository execution history remains internally consistent.

#### Workflow Progression

The engineering workflow shall not transition to the next lifecycle phase until the GREEN Phase Completeness Review has successfully completed.

The GREEN Phase Completeness Review is the sole authorization for exiting the Repository Patch implementation loop and resuming the standard ResumeForge Engineering Methodology workflow.

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

### GREEN Evidence Integrity

The GREEN phase transforms the approved RED engineering analysis into repository-ready implementation. Every implementation activity shall be directly traceable to the engineering evidence established during the RED phase.

#### Required Implementation Evidence

Before the GREEN phase may be considered complete, the implementation package shall include:

- Production code implementing the approved design.
- Automated tests validating the implemented behavior.
- Resolution of all expected failing tests identified during RED.
- Documentation updates required by the implemented change.
- Verification that implementation follows established repository patterns.
- Verification that testing follows established repository testing patterns.
- Traceability between RED engineering evidence, implementation, and automated tests.

#### GREEN Completion Criteria

The GREEN phase is complete only when:

- All planned production code modifications have been implemented.
- All planned automated tests have been implemented.
- Previously expected failing tests now pass.
- Existing automated test suites continue to pass unless an approved exception exists.
- Documentation required by the implementation has been completed.
- Every implemented change is traceable to engineering evidence established during the RED phase.

Completion of the GREEN phase authorizes progression to the next engineering workflow phase in accordance with the ResumeForge Engineering Methodology.

## Engineering Story Lifecycle

### Purpose

The Engineering Story Lifecycle defines the authoritative execution model for all ResumeForge Engineering Stories.

Engineering Stories evolve the ResumeForge Engineering Methodology itself. Their purpose is to improve engineering practices while maintaining deterministic execution, complete traceability, and repository integrity.

### Objectives

The Engineering Story Lifecycle shall:

- Define a deterministic engineering workflow.
- Maintain a single active engineering state throughout execution.
- Produce repository-ready implementation artifacts.
- Preserve complete evidence from planning through repository closeout.
- Ensure every engineering improvement remains fully traceable.

### Lifecycle

Engineering Stories progress through the following lifecycle phases:

| Phase | Primary Deliverable |
|--------|---------------------|
| Initiate | Engineering Decision Record |
| Review | Review Artifact |
| Implement | Package Artifact or Section Artifact |
| Verify | Verification Artifact |
| Commit | Repository Baseline |

Progression to the next phase is authorized only after successful completion of the current phase.

### Engineering Principles

#### Single Architectural Capability

Each Engineering Story shall implement one cohesive architectural capability.

If additional independent capabilities are discovered, the story shall return to Story Planning for controlled replanning.

#### One Command, One Deliverable

Every lifecycle command produces exactly one authoritative deliverable.

A lifecycle command shall never implicitly execute another lifecycle command.

Each completed command authorizes, but does not perform, the next command.

#### Package Before Sections

Whenever an implementation phase contains multiple implementation units, execution shall follow this pattern:

```text
Review
    ↓
Implement (Package)
    ↓
Implement (Section)
    ↓
...
    ↓
Verify
```

The package defines the implementation contract.

Section-level implementation fulfills that contract one unit at a time.

#### Repository-Ready Implementation

Implement phases produce repository-ready installation artifacts requiring no additional interpretation.

#### Evidence-Based Engineering

Every engineering decision shall remain traceable through:

- Story Deliverables
- Repository Test Specifications
- Repository Patch Units
- Verification Evidence
- Commit Evidence

#### Controlled Replanning

When a quality gate identifies a planning deficiency, engineering work shall return to the earliest affected lifecycle phase.

### Lifecycle Completion

An Engineering Story is complete when:

- all lifecycle phases have successfully completed;
- verification has passed;
- repository documentation has been updated;
- repository history has been recorded;
- checkpoint information has been updated;
- the repository baseline has been committed and tagged.

Completion establishes the new authoritative engineering baseline.

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

Repository Closeout is the final engineering lifecycle phase before Commit.

Its purpose is to leave the repository in a more coherent, more maintainable, and more executable state than when the engineering session began.

Repository Closeout transforms engineering discoveries made during the current story into durable repository knowledge that benefits every future engineering session.

Repository Closeout is responsible for:

- reconciling repository architecture;
- consolidating approved engineering methodology improvements;
- preserving engineering continuity;
- synchronizing repository documentation;
- preparing the repository for efficient future session startup.

Repository Closeout concludes only when:

- repository architecture is internally consistent;
- approved methodology improvements have been incorporated or formally queued;
- repository documentation accurately reflects repository behavior;
- engineering continuity has been preserved;
- the repository is ready to transition to Commit.

### Commit: Repository Closeout

**Commit Lifecycle**

Commit is executed as a sequence of Commit Processing Units (CPUs).

Each CPU has:

- one engineering responsibility;
- one or more defined engineering artifacts;
- objective completion criteria;
- explicit ownership transfer to the next CPU.

The Commit lifecycle consists of:

- CPU-00 – Commit Lifecycle Architecture
- CPU-01 – Story Retrospective
- CPU-02 – Repository Synchronization
- CPU-03 – Repository History
- CPU-04 – Repository Checkpoint
- CPU-05 – Commit Package
- CPU-06 – Commit Verification

The existing Commit guidance below represents the implementation details that will be reconciled into this lifecycle during the remaining Commit Processing Units.

#### CPU-00 – Commit Lifecycle Architecture

**Purpose**

Establish the architectural framework for the Commit lifecycle and define the Commit Processing Unit (CPU) execution model.

**Primary Engineering Artifact**

- Commit Lifecycle Architecture

**Completion Criteria**

CPU-00 is complete when:

- the Commit lifecycle has been established;
- Commit Processing Units have been defined;
- execution order has been documented;
- ownership transitions have been established.

**Ownership Transfer**

Upon successful completion of CPU-00, ownership transfers to:

**CPU-01 – Story Retrospective**

#### CPU-01 – Story Retrospective

**Purpose**

Capture the enduring engineering value produced by the completed story.

The Story Retrospective records engineering knowledge that remains valuable
after story completion. It preserves methodology improvements, engineering
decisions, repository improvements, lifecycle observations, and future
engineering opportunities.

The Story Retrospective is an engineering artifact rather than a narrative
history of the implementation session.

---

**Inputs**

- Completed story objectives.
- Repository modifications.
- Verified engineering artifacts.
- Engineering observations accumulated during the lifecycle.
- Approved methodology improvements.

---

**Outputs**

- Completed Story Retrospective.
- Permanent engineering lessons learned.
- Methodology improvements for future REM evolution.
- Clearly identified follow-on engineering opportunities.

---

**Repository Operations**

Review the completed story against its original objectives.

Identify engineering improvements that extend beyond the current story.

Separate:

- story accomplishments;
- repository improvements;
- methodology improvements;
- future engineering opportunities.

Record only durable engineering knowledge suitable for long-term repository
maintenance.

---

**Verification Requirements**

Verify that:

- the retrospective accurately reflects the completed story;
- methodology improvements are clearly distinguished from story-specific work;
- future engineering work is identified separately from completed work;
- the retrospective is understandable without requiring access to the original engineering conversation.

---

**Completion Criteria**

CPU-01 is complete when the Story Retrospective captures the enduring
engineering value of the story and provides sufficient guidance to improve
future engineering work.

---

**Ownership Transfer**

Upon successful verification, ownership transfers to:

`CPU-02 – Repository History`

#### CPU-02 – Repository Synchronization

**Purpose**

Verify that all permanent repository artifacts communicate the same completed engineering state before permanent repository records are finalized.

Repository Synchronization confirms repository consistency; it does not create new engineering work.

**Primary Engineering Artifact**

- Repository Synchronization Verification

**Completion Criteria**

CPU-02 is complete when:

- permanent repository documents have been reviewed for consistency;
- required repository updates have been completed;
- repository documentation reflects a single engineering state;
- synchronization has been verified.

**Ownership Transfer**

Upon successful completion of CPU-02, ownership transfers to:

**CPU-03 – Repository History**

#### CPU-03 – Repository History

**Purpose**

Record the completed engineering work within the repository's permanent historical record.

Repository History ensures that completed stories, engineering decisions, and significant repository improvements are preserved in the appropriate history documentation before repository checkpoints and Git commit activities occur.

**Primary Engineering Artifact**

- Repository History Update

**Completion Criteria**

CPU-03 is complete when:

- required repository history documentation has been updated;
- the completed story has been permanently recorded;
- engineering improvements have been captured in the appropriate historical record;
- history updates have been verified for completeness and accuracy.

**Ownership Transfer**

Upon successful completion of CPU-03, ownership transfers to:

**CPU-04 – Repository Checkpoint**

#### CPU-04 – Repository Checkpoint

**Purpose**

Establish the repository's next engineering baseline following completion of the current story.

Repository Checkpoint captures the repository's current engineering state so the next engineering session begins from a verified and reproducible baseline.

**Primary Engineering Artifact**

- Repository Checkpoint Update

**Completion Criteria**

CPU-04 is complete when:

- repository checkpoint documentation has been updated;
- the next engineering starting point has been recorded;
- repository status reflects the completed engineering work;
- checkpoint information has been verified for accuracy and completeness;
- repository recovery information has been synchronized with the current engineering state;
- repository checkpoint reflects the verified completion of all prior Commit Processing Units;
- repository checkpoint establishes a deterministic engineering baseline for the next engineering session.

**Ownership Transfer**

Upon successful completion of CPU-04, ownership transfers to:

**CPU-05 – Commit Package**

#### CPU-05 – Commit Package

**Purpose**

Assemble and validate the complete engineering deliverable that is ready to become the repository's next permanent commit.

The Commit Package represents the complete set of engineering artifacts produced by the completed story and confirms that the repository is ready to enter final commit verification.

**Primary Engineering Artifact**

- Commit Package

**Completion Criteria**

CPU-05 is complete when:

- all required engineering artifacts have been produced;
- all Repository Patch Specifications have been implemented and verified;
- repository updates have been synchronized across all affected documents;
- repository history and repository checkpoint updates are complete;
- engineering lifecycle ownership transfers have been completed and verified;
- the Commit Package represents a complete, internally consistent repository state;
- the Commit Package has been reviewed for completeness and is ready for final Commit Verification.

**Ownership Transfer**

Upon successful completion of CPU-05, ownership transfers to:

**CPU-06 – Commit Verification**

#### CPU-06 – Commit Verification

**Purpose**

Perform the final verification that the Commit Package is complete, internally consistent, and ready to become the repository's permanent engineering baseline.

Commit Verification confirms that all required engineering activities have been completed before any Git commit, tag creation, or repository publication activities are performed.

**Primary Engineering Artifact**

- Commit Verification Report

**Completion Criteria**

CPU-06 is complete when:

- all previous Commit Processing Units have been successfully completed and verified;
- required engineering artifacts have been verified;
- Repository Context Audits have been completed for all repository modifications;
- repository history, repository checkpoint, and synchronization activities have been confirmed;
- repository identity, structure, terminology, and implementation contracts remain internally consistent;
- repository status is clean and ready for commit;
- the Commit Package has been verified as complete and internally consistent;
- final commit verification has been successfully completed.

**Ownership Transfer**

CPU-06 completes the Commit lifecycle.

Ownership transfers to the Repository Commit execution.

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