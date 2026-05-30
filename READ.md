# MCP Research Assistant Server

## Overview

This project implements a Model Context Protocol (MCP) Server that acts as an AI-powered research assistant. The server integrates Groq LLMs to provide text summarization, question answering, and live technology news retrieval through MCP tools.

## Features

### 1. Text Summarization

Summarizes large blocks of text into five concise bullet points using Groq's Llama models.

### 2. Question Answering

Answers general knowledge and research-related questions through Groq AI.

### 3. Live News Search

Retrieves current technology and AI-related news headlines and generates a concise news briefing.

## Tools Available

| Tool           | Description                              |
| -------------- | ---------------------------------------- |
| summarize_text | Summarize text into 5 key bullet points  |
| ask_groq       | Answer general knowledge questions       |
| search_web     | Fetch and summarize current tech/AI news |

## Technologies Used

* Python
* MCP (Model Context Protocol)
* Groq API
* Llama 3.3 70B Versatile
* Llama 3.1 8B Instant
* AsyncIO
* Requests
* Google Colab

## Architecture

User Query → MCP Client → MCP Server → Groq Models / Web Search → Response

The MCP client dynamically discovers available tools from the MCP server and invokes the appropriate tool based on the user's query.

## Installation

```bash
pip install mcp groq httpx duckduckgo-search nest_asyncio
```

Set your Groq API key:

```bash
export GROQ_API_KEY="your_api_key"
```

## Running the Project

Start the MCP server:

```bash
python mcp_server.py
```

Run the MCP client:

```bash
python mcp_client.py
```

## Example Queries

```text
What are the latest AI news today?
```

```text
Summarize what transformers are in machine learning.
```

```text
What is the difference between RAM and ROM?
```

## Learning Outcomes

* Implemented an MCP-compliant server.
* Created custom MCP tools.
* Integrated Groq LLM APIs.
* Built an AI research assistant workflow.
* Implemented tool discovery and execution through MCP.
* Developed asynchronous client-server communication.

