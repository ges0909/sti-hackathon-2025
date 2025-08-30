# NINA API

## API Client Generation

```bash
openapi-python-client generate --path nina/openapi.yaml --output-path nina-api-client --meta uv --config nina/openapi-python-client-config.yaml
```

or

```bash
openapi-python-client generate --url https://nina.api.bund.dev/openapi.yaml --output-path nina-api-client --meta uv --config nina/openapi-python-client-config.yaml
```

## Gemini CLI

Integrate MCP server in Gemini with `$HOME/.gemini/settings.json`.

```json
{
  "mcpServers": {
    "NINA API Demo": {
      "command": "uv",
      "args": [
        "run",
        "src/main.py"
      ],
      "cwd": "$HOME/PycharmProjects/sti-hackathon-2025/nina",
      "timeout": 30000,
      "trust": true
    }
  }
}
