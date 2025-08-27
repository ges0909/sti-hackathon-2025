# 🏆 Valantic STI Hackathon 2025

This project demonstrates the use of a `FastMCP` server with _lifespan_
management to interact with a user database.

## Description

The application provides a set of tools to manage users in a database. It uses a
`lifespan` event handler to initialize the database connection and schema on
startup, and to clean up the database on shutdown.

## Features

### Tools

- **Find all users**: Retrieves all users from the database.
- **Find user by name**: Retrieves a specific user by their name.
- **Add a user**: Adds a new user to the database with a name, email, and age.
- **Delete user by name**: Deletes a user from the database by their name.
- **Delete all users**: Deletes all users from the database.

### Resources

- **user://database/stats**: A static resource that provides statistics about
  the user database.

### Prompts

- **analyze-user**: A prompt template for analyzing a specific user.

## Project

### Get the project

```bash
git clone git@github.com:ges0909/sti-hackathon-2025.git
```

### Install `uv`

Install [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation), "
_an extremely fast Python package and project manager, written in Rust_".

```bash
winget install astral-sh.uv
```

Restart terminal and check installation.

```bash
uv --version
```

Update `uv`.

```bash
uv self update
```

### Manage dependencies

| Command                         | Description                    |
| ------------------------------- | ------------------------------ |
| `uv sync`                       | Install dependencies ...       |
| `uv sync --extra dev`           | ... include `dev` dependencies |
| `uv add fastmcp`                | Add new dependency             |
| `uv remove mcp`                 | Remove dependency              |
| `uv sync --upgrade`             | Upgrade dependencies ...       |
| `uv sync --upgrade --extra dev` | ... include `dev` dependencies |
| `uvx ruff format`               | Format codebase                |

### Run MCP server

```bash
cd mcp-server
uv run src/main.py
```

### Run tests

```bash
uv run pytest --verbose
```

## Gemini CLI

Install [Gemini CLI](https://github.com/google-gemini/gemini-cli?tab=readme-ov-file#-installation).

Test installation by trying command `gemini`.

Add following snippet to `$HOME/.gimini/settings.json`.

```json
{
  "mcpServers": {
    "STI valantic Hackathon MCP Demo": {
      "command": "uv",
      "args": ["run", "src/main.py"],
      "cwd": "$HOME/PycharmProjects/sti-hackathon-2025",
      "timeout": 30000,
      "trust": true
    }
  }
}
```

| Command | Description                |
| ------- | -------------------------- |
| `/mcp`  | Show connected MCP servers |
| `/quit` | Quit _Gemini_              |

### Example Prompts

1. > How many user are stored in the user database?
2. > Show me all users in user database with the leading id!
3. > Delete user with id 10!
4. > Add a new user with randomly assigned user data!
5. > Add at least 3 users with randomly assigned user data!
6. > Add a new user Max Mustermann, max.mustermann@mail.de, 20 years old!
7. > Add a new user Maria Mustermann, maria.mustermann@mail.de!
8. > Delete all users!
9. > How many user are stored in the user database?
