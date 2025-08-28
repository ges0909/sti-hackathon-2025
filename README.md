# 🏆 Valantic STI Hackathon 2025

This project demonstrates the use of a `FastMCP` server with _lifespan_
management to interact with a user database.

## Get the project

```bash
git clone git@github.com:ges0909/sti-hackathon-2025.git
```

## Install `uv`

> _An extremely fast Python package and project manager, written in Rust_.

```bash
winget install astral-sh.uv
```

Other installation options.

```http
https://github.com/astral-sh/uv?tab=readme-ov-file#installation
```

Restart terminal and check installation.

```bash
uv --version 
uv self update
```

## Manage dependencies

| Command                         | Description                          |
|---------------------------------|--------------------------------------|
| `uv sync`                       | Install dependencies                 |
| `uv sync --extra dev`           | Install including `dev` dependencies |
| `uv add fastmcp`                | Add new dependency                   |
| `uv remove mcp`                 | Remove dependency                    |
| `uv sync --upgrade`             | Upgrade dependencies                 |
| `uv sync --upgrade --extra dev` | Upgrade including `dev` dependencies |

## `.env` file (optional)

```properties
DATABASE_URL=sqlite+aiosqlite:///./data/people.db
LOG_LEVEL=INFO
INITIAL_USERS_COUNT=10
```

## Run MCP server

```bash
uv run people/src/main.py
```

## Run tests

```bash
uv run pytest people
```

## Formatting

```bash
uvx ruff format
```

## Linting

```bash
ruff check --select ALL .
ruff check --select F,E,W,B .
ruff check --select F,E,W,B src # Only important rules
```

## Gemini CLI

Install [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation).

Test installation by running the `gemini` command.

Add the following snippet to `$HOME/.gemini/settings.json`.

```json
{
  "mcpServers": {
    "STI valantic Hackathon MCP Demo": {
      "command": "uv",
      "args": [
        "run",
        "src/main.py"
      ],
      "cwd": "$HOME/PycharmProjects/sti-hackathon-2025/people",
      "timeout": 30000,
      "trust": true
    }
  }
}
```

| Command  | Description                   |
|----------|-------------------------------|
| `/about` | Show information about Gemini |
| `/mcp`   | Show connected MCP servers    |
| `/quit`  | Quit _Gemini_                 |
