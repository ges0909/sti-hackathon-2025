import asyncio

from fastmcp import Client


async def main():
    # Replace with your MCP server URL
    server_url = "http://localhost:8000/mcp"

    # Initialize the client
    client = Client(server_url)

    async with client:
        # List all available resources
        resources = await client.list_resources()

        print(f"Found {len(resources)} resources:\n")
        for resource in resources:
            print(f"🔗 URI: {resource.uri}")
            print(f"📛 Name: {resource.name}")
            print(f"📝 Description: {resource.description}")
            print(f"📦 MIME Type: {resource.mimeType}")

            # Optional: Access FastMCP-specific metadata
            fastmcp_meta = resource.meta.get("_fastmcp", {}) if resource.meta else {}
            tags = fastmcp_meta.get("tags", [])
            print(f"🏷️ Tags: {tags}\n")

        # You can also list resource templates (dynamic endpoints)
        templates = await client.list_resource_templates()
        print(f"\nFound {len(templates)} resource templates:\n")
        for template in templates:
            print(f"🧪 Template URI: {template.uriTemplate}")
            print(f"📛 Name: {template.name}")
            print(f"📝 Description: {template.description}\n")

        # List all available tools
        tools = await client.list_tools()
        print(f"Found {len(tools)} tools:\n")
        for tool in tools:
            print(f"🔧 Name: {tool.name}")
            print(f"📝 Description: {tool.description}")
            print(f"📋 Input Schema: {tool.inputSchema}\n")

        # List all available prompts
        prompts = await client.list_prompts()
        print(f"Found {len(prompts)} prompts:\n")
        for prompt in prompts:
            print(f"💬 Name: {prompt.name}")
            print(f"📝 Description: {prompt.description}")
            if hasattr(prompt, "arguments"):
                print(f"📋 Arguments: {prompt.arguments}")
            print()


if __name__ == "__main__":
    asyncio.run(main())
