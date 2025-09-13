# Employee Database

Integrate MCP server in Gemini with `$HOME/.gemini/settings.json`.

```json
{
  "mcpServers": {
    "Employee Database Demo": {
      "command": "uv",
      "args": [
        "run",
        "src/main.py"
      ],
      "cwd": "$HOME/PycharmProjects/trip-planner-mcp-server/servers/employee",
      "timeout": 30000,
      "trust": true
    }
  }
}
