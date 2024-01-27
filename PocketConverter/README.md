# PocketConverter

This script converts Pocket export to a Firefox compatible JSON file.

## Usage

Install dependencies

    poetry update

Run JupyterLab

    poetry ./convert.py [Pocket export filepath]

or

    poetry shell
    poetry ./convert.py [Pocket export filepath]

## Package Management

This project is using [poetry](https://python-poetry.org/) Python package and dependency manager.

- Init interactively `poetry init`
- Add package `poetry add package-name`
- Remove package `poetry remove package-name`
- Install dependencies `poetry install`
- Update dependencies `poetry update`
- Show available packages `poetry show`
- Run a command in the virtualenv `poetry run command`
- Open virtualenv `poetry shell`
