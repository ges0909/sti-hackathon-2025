#    

How to build?

In the project root.

```bash
uv pip install -e ./apps/quickstart[dev] -e ./apps/mcp-server[dev] -e ./dev-tools -e ./libs/utils
```

How to deploy?

```bash
uv pip compile apps/quickstart/pyproject.toml -o apps/quickstart/requirements.lock
uv pip sync apps/quickstart/requirements.lock
```