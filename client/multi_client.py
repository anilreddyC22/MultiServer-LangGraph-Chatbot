# client/multi_client.py

class MultiServerMCPClient:
    def __init__(self):
        self.servers = {}

    def add_server(self, name: str, tools_list: list):
        """Attach a server by its tool list."""
        self.servers[name] = tools_list

    def get_all_tools(self):
        """Flatten and return all tools from all servers."""
        all_tools = []
        for tools in self.servers.values():
            all_tools.extend(tools)
        return all_tools


# -----------------------
# Import actual tool lists from MCP servers
# -----------------------
from tools.student_tool import student_tools
from tools.course import course_tools
from tools.professor import professor_tools
from tools.webflux_api_product import webflux_tools
from tools.json_to_java import json_to_java_tools

# Create multi-server client
mcp_client = MultiServerMCPClient()

# Register servers with their tools
mcp_client.add_server("student-course-professor", student_tools + course_tools + professor_tools)
mcp_client.add_server("webflux", webflux_tools)
mcp_client.add_server("json-to-java", json_to_java_tools)


