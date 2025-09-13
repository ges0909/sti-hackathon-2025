# NINA API

1. [Automating MCP Server Creation from OpenAPI and FastAPI](https://www.pondhouse-data.com/blog/automating-mcp-server-creation)

## Integration

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
      "cwd": "$HOME/PycharmProjects/trip-planner-mcp-server/servers/nina",
      "timeout": 30000,
      "trust": true
    }
  }
}
