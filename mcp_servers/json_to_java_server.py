from mcp.server.fastmcp import FastMCP
from tools.json_to_java import json_to_java_tools

app = FastMCP("json-to-java")

# Register tools
for tool in json_to_java_tools:
    app.tool(tool)