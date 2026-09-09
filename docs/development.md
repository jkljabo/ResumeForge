Development Workflow

Run tests

python -m pytest

Build package

python -m build --no-isolation

Install wheel

pip install dist/*.whl

Run CLI

resumeforge --help