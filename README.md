# 🏆 Valantic STI Hackathon 2025

This project demonstrates the use of a `FastMCP` server with lifespan management
to interact with a user database.

## Description

The application provides a set of tools to manage users in a database. It uses a
`lifespan` event handler to initialize the database connection and schema on
startup, and to clean up the database on shutdown.

## Features

### Tools

* **Find all users**: Retrieves all users from the database.
* **Find user by name**: Retrieves a specific user by their name.
* **Add a user**: Adds a new user to the database with a name, email, and age.
* **Delete user by name**: Deletes a user from the database by their name.
* **Delete all users**: Deletes all users from the database.

### Resources

* **user://database/stats**: A static resource that provides statistics about
  the user database.

### Prompts

* **analyze-user**: A prompt template for analyzing a specific user.

## How to install `uv`?

Install [uv](https://github.com/astral-sh/uv), "_an extremely fast Python
package and project manager, written in
Rust_".

```bash
winget install astral-sh.uv
```

Restart terminal and check installation.

```bash
uv --version
```

## How to build?

Synchronizes your env with _lock_ file only, i.e. without dev dependencies.

```bash
uv sync
```

Install dev dependencies generally by `uv pip install -e .[extra-name]`.

```bash
uv pip install -e .[dev]
```

## How to format?

```bash
uvx ruff format
```

## How to run?

```bash
cd mcp-server
uv run src/main.py
```

## How to run tests?

```bash
```