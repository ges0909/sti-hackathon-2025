# 🏆 Valantic STI Hackathon 2025

## ⚙️ Managing Pythons with `uv`

Install [uv](https://github.com/astral-sh/uv) and restart terminal.

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check installation

```powershell
uv --version
```

| `uv` Command                | Description                        | 
|-----------------------------|------------------------------------|
| `uv init mcp-server`        | create new project                 |
| `uv init mcp-library --lib` |                                    |
| `uv venv`                   | create virtual environment         |
| `uv run python --version`   | check installed python version     |
| `uv tree`                   |                                    |
| `uv add --dev ruff`         | add package                        |
| `uv remove --dev ruff`      | remove package                     |
| `uv add --dev ruff`         | lint project files                 |
| `uv run ruff format`        | format project files               |
| `uv lock`                   | create/update '.lock' file         |
| `uv sync`                   | sync virtual env with '.lock' file |
| `uv run main.py`            | execute python script              |
| `uv python install ...`     | manage python installations        |
| `uv python use ...`         |                                    |

## Project

```
uv pip install -e ./apps/quickstart[dev] -e ./apps/mcp-server[dev] -e ./dev-tools -e ./libs/utils
```

The command indicates `uv`, each of your four packages in the "Editable" mode in one, central `.venv` in the root
directory to install and also the [DEV] dependencies for quickstart and MCP server take into account.