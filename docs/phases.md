Phase A
Foundation

Completed

-----------------

Phase B

Resume Model

Completed

-----------------

...

Phase G

Profiles

G.1.1 ✓
G.1.2 ✓
...
G.1.6 ✓

Phase G

Profile Management

Phase G — Profile Management

✓ G.1.1
✓ G.1.2
✓ G.1.3
✓ G.1.4
✓ G.1.5
✓ G.1.6
✓ G.1.7 Profile Listing
✓ G.1.8 Profile Removal
✓ G.1.9 Profile Editing

Phase G.2 — Profile Domain & Persistence Cleanup

✓ Story: G.2.1 – Configuration Model
✓ Story: G.2.2 – Configuration Repository
✓ Story: G.2.3 – Configuration Service
✓ Story: G.2.4 – Configuration Workflow
✓ Story: G.2.5.2 – Workflow Routing
✓ Story: G.2.5.3 – Display Configuration
✓ Story: G.2.5.4 – Update Configuration
✓ Story: G.2.5.5 – Validate Configuration
✓ Story: G.2.5.6 – Configuration Reset
✓ Story: G.2.5.7 – Configuration Help
✓ Story: G.2.5.8 – Configuration List
✓ Story: G.2.5.9 – Default Profile Enhancements
✓ Story: G.2.5.10 – Configuration Aliases
✓ Story: G.2.5.11 – Profile Import
✓ Story: G.2.5.12 – Profile Export
✓ Story: G.2.5.13 – Profile Clone
✓ Story: G.2.5.14 – Profile Rename
✓ Story: G.2.5.15 – Profile Set Default
✓ Story: G.2.5.16 – Profile List Details
✓ Story: G.2.5.17 – Profile Color Theme
✓ Story: G.2.5.18 – Profile Description
✓ Story: G.2.5.19 – Profile Tags
✓ Story: G.2.5.20 – Profile Notes
✓ Story: G.2.5.21 – Profile Category
✓ Story: G.2.5.22 – Profile Visibility
✓ Story: G.2.5.23 – Profile Owner
✓ Story: G.2.5.24 – Profile Organization
✓ Story: G.2.5.25 – Profile Purpose

→ Story: G.2.5.26 – Profile Target Role
Status

Story Planning (Verified)

Purpose

Introduce a Target Role metadata field that identifies the intended employment role associated with a Profile.

Objectives

• Add target_role to Profile
• Default to None
• Persist target_role
• Restore target_role
• Support CLI editing
• Maintain backward compatibility

Engineering Pattern

This story intentionally follows the implementation pattern established by:

• G.2.5.24 – Profile Organization
• G.2.5.25 – Profile Purpose

Implementation Pattern

Profile Target Role intentionally follows the architecture established by the previous metadata stories.

Implementation order:

1. Profile model
2. Persistence
3. CLI
4. Documentation
5. Regression verification

This story introduces no architectural changes. It extends the existing Profile metadata model using the established implementation pattern.

Target Role is another Profile metadata property and therefore follows the same implementation architecture:

• Profile model
• Serialization
• Persistence
• CLI
• Documentation
• Regression testing

Acceptance Criteria

✓ Constructor accepts target_role
✓ Defaults to None
✓ Saves target_role
✓ Loads target_role
✓ CLI updates target_role
✓ Regression remains green

Phase H

Export Improvements

⬜ PDF
⬜ DOCX themes
⬜ HTML

Phase I

Plugin System

Phase J

AI Enhancements

Development Lifecycle

Every story follows:

Planning
↓

RED
↓

GREEN
↓

Story Signoff