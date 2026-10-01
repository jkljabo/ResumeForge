Development Workflow

Typical Story Lifecycle

1. Story Planning
2. RED
3. GREEN
4. Full Regression
5. Story Signoff

Development assumes the workflow defined in docs/development_workflow.md has been followed.

All code changes should complete Planning, RED, GREEN, and Story Signoff before merge.

Run tests

python -m pytest

Build package

python -m build --no-isolation

Install wheel

pip install dist/*.whl

Run CLI

resumeforge --help