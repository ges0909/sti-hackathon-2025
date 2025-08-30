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
      "cwd": "$HOME/PycharmProjects/sti-hackathon-2025/employee",
      "timeout": 30000,
      "trust": true
    }
  }
}
