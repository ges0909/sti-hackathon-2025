# MCP Server API Documentation

## Overview

This MCP (Model Context Protocol) server provides tools for managing users in a SQLite database.

## Tools

### 1. Find all users

**Name:** `Find all users`
**Description:** Get all users from database.
**Parameters:** None
**Returns:** `list[UserDto]`

```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "age": 30
  }
]
```

### 2. Find user by name

**Name:** `Find user by name`
**Description:** Get a user by last name.
**Parameters:**

- `name` (string): Last name to search for

**Returns:** `UserDto | None`

```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "age": 30
}
```

### 3. Add a user

**Name:** `Add a user`
**Description:** Add a user with name, email and age to the database.
**Parameters:**

- `first_name` (string): First name (1-255 chars)
- `last_name` (string): Last name (1-255 chars)
- `email` (string): Valid email address
- `age` (integer): Age between 0-150

**Returns:** `None`
**Errors:** `ValueError` if email already exists

### 4. Delete user by last name

**Name:** `Delete user by last name`
**Description:** Delete a user by last name from the database.
**Parameters:**

- `last_name` (string): Last name of user to delete

**Returns:** `string` - Confirmation message

```json
"User 'Doe' deleted"
```

### 5. Delete all users

**Name:** `Delete all users`
**Description:** Deletes all users from the database.
**Parameters:** None
**Returns:** `string` - Count of deleted users

```json
"10 users deleted"
```

### 6. Get database stats

**Name:** `Get database stats`
**Description:** Get current database statistics.
**Parameters:** None
**Returns:** `string` - Database statistics

```json
"Total users: 5\nDatabase: SQLite\nStatus: Active"
```

## Resources

### user://database/stats

**Description:** Static resource providing user database statistics.
**Returns:** `string`

```
Total users: Dynamic
Database: SQLite
Status: Active
```

## Prompts

### analyze-user

**Description:** Prompt template for analyzing a specific user.
**Parameters:**

- `name` (string): Name of user to analyze

**Returns:** Analysis prompt template

## Data Models

### UserBase

```json
{
  "first_name": "string (1-255 chars)",
  "last_name": "string (1-255 chars)",
  "email": "valid email address",
  "age": "integer 0-150 or null"
}
```

### UserDto

Extends UserBase with:

```json
{
  "id": "integer (auto-generated)"
}
```

## Error Handling

- **ValidationError**: Invalid input data (email format, age range, etc.)
- **ValueError**: Business logic errors (duplicate email)
- **Database errors**: Automatically rolled back with error propagation
