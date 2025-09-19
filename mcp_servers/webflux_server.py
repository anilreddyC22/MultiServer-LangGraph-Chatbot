from mcp.server.fastmcp import FastMCP
from tools.webflux_api_product import webflux_tools

app = FastMCP("webflux")

# Register tools
for tool in webflux_tools:
    app.tool(tool)