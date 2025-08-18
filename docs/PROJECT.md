# Project

## How to build

The command indicates `uv`, each of your four packages in the "Editable" mode in one, central `.venv` in the root
directory to install and also the [DEV] dependencies for quickstart and MCP server take into account.

```powershell
uv pip install -e ./apps/quickstart[dev] -e ./apps/mix-server[dev] -e ./dev-tools -e ./libs/utils
```

## How to format

```powershell
uv run ruff format
```

## How to deploy

```powershell
uv pip compile apps/quickstart/pyproject.toml -o apps/quickstart/requirements.lock
uv pip sync apps/quickstart/requirements.lock
```
