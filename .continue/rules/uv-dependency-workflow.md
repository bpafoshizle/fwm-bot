# uv Dependency Workflow

---

description: Explain the correct workflow for adding a new Python dependency using uv.
alwaysApply: true

---

To add a new dependency, first manually add it to the `dependencies` list in `pyproject.toml`. Then, update the lock file by running `uv pip compile pyproject.toml -o requirements.txt`. Finally, install the updated dependencies into your environment with `uv sync -r requirements.txt`.