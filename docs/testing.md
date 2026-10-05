
## Testing Philosophy

ResumeForge follows strict TDD.

Every story must include:

Planning
RED
GREEN
Regression
Signoff

## Testing Strategy

Testing is organized into:

• Unit Tests
• Integration Tests
• CLI Tests
• Full Regression Tests

python -m pytest

## Unit Tests

## Integration Tests

## CLI Tests

## Regression Tests

Standard regression command

python -m pytest

Expected result

All tests pass before Story Signoff.

## Current Regression Count

471 tests

Update this value whenever new regression tests are merged.

## Current Planned RED Tests

Story

G.2.5.26 – Profile Target Role

tests/test_profile.py

• Profile defaults target_role to None
• Profile stores target_role

tests/test_profile_persistence.py

• Profile persists target_role

tests/test_cli.py

• profile edit updates target_role

Status

Planned

Implementation begins during Implementation Package (RED).

## Expected Result

All tests pass

Expected GREEN Results

tests/test_profile.py

22 passed

tests/test_profile_persistence.py

13 passed

tests/test_cli.py

106 passed

Full Regression

471 passed