from fastapi import FastAPI, Query
from graph.agent_graph import agent_with_memory
from schemas.chat import QueryRequest, QueryResponse

import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_DEBUG"] = "true"

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ChatBot API is running with MCP + SQLite persistent memory!"}

@app.post("/chat", response_model=QueryResponse)
def chat(request: QueryRequest, session_id: str = Query("default_session")):
    """
    Each user/session gets its own memory stored in SQLite.
    Pass ?session_id=user123 in your API call to separate histories.
    """
    user_input = request.query
    if user_input.lower() in ["exit", "quit"]:
        return QueryResponse(answer="Exiting the chat. Goodbye!")

    response = agent_with_memory.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config={"configurable": {"thread_id": session_id}}
    )

    answer = response["messages"][-1].content
    return QueryResponse(answer=answer)
