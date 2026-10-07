
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

G.2.5.28 – Profile Employment Type

tests/test_profile.py

• Profile defaults employment_type to None
• Profile stores employment_type

tests/test_profile_persistence.py

• Profile persists employment_type

tests/test_cli.py

• profile edit updates employment_type

Status

Completed

RED Outcome

Existing regression remained green.

New employment_type tests produced the expected RED failures.

No unexpected regressions were introduced.

Existing regression remains green.

New employment_type tests fail for the expected reasons.

No unexpected regressions occur.

## Expected Result

All tests pass

Verified during GREEN Verification.

483 passing regression tests confirm successful implementation.

## Actual GREEN Results

tests/test_profile.py

28 passed

tests/test_profile_persistence.py

16 passed

tests/test_cli.py

109 passed

Full Regression

483 passed