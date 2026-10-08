
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

487 passing

Update this value whenever new regression tests are merged.

## Story Test Coverage

Story

G.2.5.28 – Profile Employment Type

tests/test_profile.py

• Profile defaults work_type to None
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

G.2.5.29 – Profile Work Arrangement

tests/test_profile.py

• Profile defaults work_arrangement to None
• Profile stores work_arrangement

tests/test_profile_persistence.py

• Profile persists work_arrangement

tests/test_cli.py

• profile edit updates work_arrangement

Status

Completed

RED Outcome

Existing regression remained green.

New work_arrangement tests produced the expected RED failures.

No unexpected regressions were introduced.

Existing regression remains green.

New work_arrangement tests fail for the expected reasons.

No unexpected regressions occur.

G.2.5.30 – Profile Work Authorization

tests/test_profile.py

• Profile defaults work_authorization to None
• Profile stores work_authorization

tests/test_profile_persistence.py

• Profile persists work_authorization

tests/test_cli.py

• profile edit updates work_authorization

Status

Completed

RED Outcome

Existing regression remained green.

New work_authorization tests produced the expected RED failures.

No unexpected regressions were introduced.

Existing regression remains green.

New work_authorization tests fail for the expected reasons.

No unexpected regressions occur.

## Expected Result

All tests pass

Verified during GREEN Verification.

487 passing regression tests confirm successful implementation.

## Actual GREEN Results

tests/test_profile.py

28 passed

tests/test_profile_persistence.py

16 passed

tests/test_cli.py

109 passed

Full Regression

487 passed