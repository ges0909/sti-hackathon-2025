# Lifespan Demo

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

## How to Run

1. Install the dependencies from `pyproject.toml`.
2. Run the main application:
   ```bash
   python src/main.py
   ```
   