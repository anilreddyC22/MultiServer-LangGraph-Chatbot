from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.memory import ConversationBufferMemory

from client.multi_client import mcp_client
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

system_prompt = """
You are a helpful assistant. 
Always use the registered tools when they are relevant.
Do NOT answer directly if a tool exists for the user request.
For example:
- If the query asks about "courses of student <id>", always call get_courses_by_student_id.
"""

# Gather all tools from MCP servers
tools = mcp_client.get_all_tools()

print("Loaded tools:", [t.name for t in tools])

# Function to create persistent memory per session
def get_memory(session_id: str = "default_session"):
    history = SQLChatMessageHistory(
        connection="sqlite:///chat_memory.db",  # correct arg in 0.4.x
        session_id=session_id
    )
    return ConversationBufferMemory(
        return_messages=True,
        chat_memory=history
    )

# Checkpointer (saves memory snapshots automatically)
checkpointer = MemorySaver()

#  Create agent with memory persistence
agent_with_memory = create_react_agent(llm, tools, checkpointer=checkpointer)


