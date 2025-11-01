# Editable Git Install with uv

---
description: Instructions for installing a Python package in editable mode from
  a Git repository using uv pip.
alwaysApply: true
---

To install an editable Python package from a Git repository using uv:

1.  make libs directory at workspace root if it doesn't exist
   `mkdir libs && cd libs`

2.  Clone the repository to a local directory:
   `git clone <repository_url>`

3.  Navigate into the cloned repository's directory:
   `cd <repository_directory>`

4.  Install the package in editable mode using uv:
   `uv pip install -e .`