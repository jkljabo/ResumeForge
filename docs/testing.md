
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

475 tests

Update this value whenever new regression tests are merged.

## Story Test Coverage

Story

G.2.5.27 – Profile Experience Level

tests/test_profile.py

• Profile defaults experience_level to None
• Profile stores experience_level

tests/test_profile_persistence.py

• Profile persists experience_level

tests/test_cli.py

• profile edit updates experience_level

Status

Completed

Implementation completed following the approved RED and GREEN workflow.

## Expected Result

All tests pass

## Actual GREEN Results

tests/test_profile.py

26 passed

tests/test_profile_persistence.py

15 passed

tests/test_cli.py

108 passed

Full Regression

475 passed