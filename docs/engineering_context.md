# ResumeForge Engineering Context

## Purpose

This document preserves durable engineering context for ResumeForge.

Its purpose is to enable engineering work to continue consistently across
multiple ChatGPT conversations without depending on prior conversation history.

This document supplements the engineering methodology by recording project
context that changes infrequently while avoiding duplication of engineering
workflow rules.

Current workflow state is maintained in `CHECKPOINT.md`.

Engineering methodology is maintained in
`docs/development_workflow.md`.

## Source Authority

Engineering decisions shall always be derived from the highest available Source
Authority.

The order of authority is:

1. Repository source code.
2. Repository engineering documentation.
3. Current story planning artifacts.
4. CHECKPOINT.md.
5. Verified implementation evidence.
6. Conversation guidance that does not conflict with repository artifacts.

If conflicting information is discovered, the higher Source Authority shall
prevail.

Repository artifacts always supersede remembered conversation context.

## Engineering Principles

ResumeForge engineering follows these principles:

- One authoritative artifact for every engineering concern.
- Evidence-based verification.
- Deterministic implementation guidance.
- Incremental engineering improvements.
- Traceability from requirements through repository closeout.
- Repository artifacts take precedence over conversation history.
- Workflow authority remains in `docs/development_workflow.md`.
- Durable engineering context belongs in this document.

## Repository Navigation

The primary engineering documents are:

| Artifact | Purpose |
|----------|---------|
| `docs/development_workflow.md` | Engineering methodology |
| `docs/testing.md` | Testing methodology |
| `docs/phases.md` | Workflow model |
| `docs/history.md` | Historical engineering record |
| `CHECKPOINT.md` | Current workflow state |
| Story Planning Package | Approved planning baseline |
| `docs/engineering_context.md` | Durable engineering context |

Each artifact has one authoritative responsibility as defined by the
Engineering Artifact Authority section of the engineering methodology.

## Active Story Recovery

ResumeForge engineering sessions shall recover project state from repository
artifacts rather than previous conversation history.

The recovery procedure is:

1. Establish the current Source Authority.
2. Review `CHECKPOINT.md` to identify the active story and workflow phase.
3. Review the applicable Story Planning package for the active story.
4. Review `docs/history.md` for recently completed work.
5. Review `docs/development_workflow.md` for governing methodology.
6. Review `docs/testing.md` when verification activities are involved.
7. Continue from the current repository state.

If repository artifacts conflict with remembered conversation history, the
repository artifacts take precedence.

## Conversation Bootstrap Procedure

Every new engineering conversation shall begin by establishing repository
context before implementation work begins.

Bootstrap sequence:

1. Perform the Environment State Audit.
2. Establish the current Source Authority.
3. Verify repository readiness.
4. Verify engineering documentation readiness.
5. Verify Story Continuity.
6. Verify conditional engineering integrations when available.
7. Identify the active story.
8. Identify the active workflow phase.
9. Review unresolved findings.
10. Review approved engineering decisions.
11. Identify the requested workflow action.
12. Begin the requested engineering phase.

### Engineering Execution Principles

Every engineering phase shall begin by:

- Refreshing Source Authority.
- Reviewing the governing engineering methodology.
- Reconciling the repository state.
- Identifying affected engineering artifacts.
- Producing outputs from repository evidence.

Conversation history may provide context but shall not supersede repository
artifacts.

## Decision Preservation

Engineering decisions that affect future stories shall be preserved within the
repository rather than relying on conversation memory.

Decision preservation follows these principles:

- Record durable methodology changes in
  `docs/development_workflow.md`.
- Record completed engineering work in `docs/history.md`.
- Record current workflow state in `CHECKPOINT.md`.
- Record durable engineering context in this document.
- Record engineering session lifecycle changes in
  `docs/development_workflow.md`.
- Record Environment State Audit enhancements in the engineering methodology
  rather than conversation history.

No engineering decision shall rely exclusively on previous conversation
history.

## Engineering Boundaries

This document provides durable engineering context.

It does not:

- define engineering workflow,
- redefine testing methodology,
- replace Story Planning Packages,
- replace `CHECKPOINT.md`,
- replace repository history.

Engineering workflow authority remains with
`docs/development_workflow.md`.

Testing authority remains with `docs/testing.md`.

Current workflow state remains in `CHECKPOINT.md`.

## Repository Closeout Expectations

Repository Closeout confirms that a completed story leaves the repository in a
consistent, reproducible state.

Repository Closeout shall verify:

- all approved requirements have been implemented;
- required verification activities have passed;
- engineering documentation is synchronized;
- repository status is clean;
- required history has been recorded;
- project context accurately reflects the completed work.

Repository Closeout provides the final engineering verification before a story
is considered complete.

Repository Synchronization is performed during Story Signoff to ensure every
authoritative engineering artifact accurately represents the completed
implementation prior to repository commit and closeout.