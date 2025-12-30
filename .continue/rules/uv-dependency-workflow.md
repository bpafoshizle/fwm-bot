---
description: Explain the correct workflow for adding a new Python dependency using uv.
alwaysApply: true
---

To add a new dependency, first manually add it to the `dependencies` list in `pyproject.toml`. Update the uv.lock file by running `uv sync`. Then, update the pip-style requirements file (used by the github actions CI file) by running `uv pip compile pyproject.toml -o requirements.txt`.