from mcp.server.fastmcp import FastMCP
from tools.student_tool import student_tools
from tools.course import course_tools
from tools.professor import professor_tools

app = FastMCP("student-course-professor")

# Register tools
for tool in student_tools + course_tools + professor_tools:
    app.tool(tool)