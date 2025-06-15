# PocketConverter

This script converts Pocket export to a Firefox compatible JSON file.

## Usage

Install dependencies

    uv lock && uv sync

Run JupyterLab

    uv ./convert.py [Pocket export filepath]

## Package management

We are using [uv](https://docs.astral.sh/uv/getting-started/) Python package and dependency
manager.

- Init interactively `uv init`
- Add package `uv add package-name`
- Remove package `uv remove package-name`
- Create lockfile `uv lock`
- Update dependencies `uv sync`
- Show available packages `uv show`
- Run a command in the virtualenv `uv run command`
