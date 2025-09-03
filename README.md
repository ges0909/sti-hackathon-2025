# 🏆 STI Hackathon

Demonstrates a `FastMCP` server with _lifespan_ management to interact with a user database.

## Get the project

```bash
git clone git@github.com:ges0909/sti-hackathon-2025.git
```

## Install 'uv'

> _An extremely fast Python package and project manager, written in Rust_.

```bash
winget install astral-sh.uv
```

For other installation options see [Installation](https://github.com/astral-sh/uv?tab=readme-ov-file#installation).

Restart terminal and check installation.

```bash
uv --version 
uv self update
```

## Manage dependencies

| Command                            | Description                                    |
|------------------------------------|------------------------------------------------|
| `uv init nina`                     | Initialize new project in folder 'nina'        |
| `uv sync`                          | Install dependencies                           |
| `uv sync --all-packages`           | Install all dependencies including workspaces  |
| `uv add fastmcp`                   | Add new dependency                             |
| `uv remove mcp`                    | Remove dependency                              |
| `uv add --group dev ruff`          |                                                |
| `uv remove --group dev ruff`       |                                                |
| `uv sync --upgrade`                | Upgrade dependencies                           |
| `uv sync --upgrade --all-packages` | Upgrade  all dependencies including workspaces |

## `.env` file (optional)

```properties
DATABASE_URL=sqlite+aiosqlite:///./data/employee.db
LOG_LEVEL=INFO
INITIAL_USERS_COUNT=10
```

## MCP server

| Command                                 | Description                           |
|-----------------------------------------|---------------------------------------|
| `uv run servers/employee/src/main.py`   | Run your custom MCP server            |
| `uv run pytest`                         | Run unit tests                        |
| `uvx ruff format`                       | Format sources                        |
| `ruff check`                            | Check sources                         |
| `ruff check --fix`                      | Check and fix sources                 |
| `mcp dev servers/employee/src/main.py ` | Run MCP Inspector to debug MCP server |

## Open WebUI

### How to install

```bash
uv venv --python 3.11 --seed open-webui
cd open-webui
source ./Scripts/activate
pip install open-webui
```

### How to run

```bash
source ./Scripts/activate
open-webui serve
```

Navigate to [http://localhost:8080](http://localhost:8080).

## Gemini CLI

Install [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation).

Test installation by running the `gemini` command.

| Command        | Description                |
|----------------|----------------------------|
| `/about`       | Show about Gemini CLI      |
| `/mcp`         | Show connected MCP servers |
| `/mcp refresh` | Restart MCP servers        |
| `/quit`        | Exit Gemini                |
