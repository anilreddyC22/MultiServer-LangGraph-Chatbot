# MultiServer-LangGraph-Chatbot

## Overview

**MultiServer-LangGraph-Chatbot** is an advanced AI chatbot platform built with FastAPI, LangChain, and LangGraph. It connects to multiple backend microservices (Java Spring Boot, WebFlux, and JSON-to-Java) and exposes their data and actions through natural language queries. The chatbot supports persistent conversation memory, multi-domain queries, and is easily extensible for new domains and endpoints.

---

## Features

- **Multi-Backend Integration:** Connects to several Java Spring Boot and WebFlux microservices, as well as a JSON-to-Java API.
- **LangChain & LangGraph Powered:** Uses modern LLM orchestration for tool-calling, contextualization, and memory.
- **Persistent Memory:** Remembers conversations per user/session using SQLite.
- **Tool-Based Endpoints:** Each backend endpoint is exposed as a tool callable by the LLM.
- **FastAPI Interface:** RESTful API for easy integration and testing.
- **Extensible:** Add new tools and services with minimal code changes.

---

## Requirements

- Python 3.10+
- Java (for backend microservices)
- [OpenAI API Key](https://platform.openai.com/)
- The following Python packages (see `requirements.txt`):
  - langchain
  - langgraph
  - openai
  - tiktoken
  - pydantic
  - fastapi
  - uvicorn

---

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/MultiServer-LangGraph-Chatbot.git
    cd MultiServer-LangGraph-Chatbot
    ```

2. **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your `.env` file:**
    ```
    OPENAI_API_KEY=sk-...
    ```

4. **Start your Java backend services** (ensure endpoints like `/students`, `/courses`, etc. are running).

5. **Run the FastAPI server:**
    ```sh
    uvicorn main:app --reload
    ```

6. **Test the chatbot:**
    - Visit `http://localhost:8000/docs` for Swagger UI.
    - Use the `/chat` endpoint with queries like:
      - `Get courses for student 1`
      - `Enroll student 2 in course 3`
      - `List professors with multiple courses`
      - `Show products below price 100`

---

## What We Have Done

- Designed a modular chatbot system that connects to multiple backend APIs.
- Implemented tool wrappers for each backend endpoint.
- Integrated LangChain and LangGraph for advanced LLM orchestration and memory.
- Provided persistent, per-session conversation history.
- Built a clean FastAPI interface for easy access and testing.

---

## Outcome

- **Unified Access:** Users can query multiple backend systems through a single chatbot interface.
- **Contextual Conversations:** The chatbot remembers previous interactions for a more natural experience.
- **Rapid Extensibility:** New endpoints and domains can be added as tools with minimal effort.
- **Production-Ready API:** Easily deployable and integrable with other systems.

---

## Why Is This Useful?

- **Bridges Data Silos:** Aggregates information from multiple microservices into one conversational interface.
- **Boosts Productivity:** Users (students, admins, customers) get instant answers without navigating multiple apps.
- **Modernizes Legacy Systems:** Adds an AI-powered layer to existing backend APIs.
- **Educational & Business Use:** Perfect for universities, e-commerce, or any organization with distributed data/services.

---

## License

MIT

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss changes.

---
