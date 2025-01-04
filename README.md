# Financial Agentic AI System

This repository demonstrates a Financial Agentic AI system with specialized agents that autonomously gather information and perform tasks using various tools. It includes an agent for web search, a financial analysis agent, and a multi-agent system that combines both.

## Overview

The system consists of three main components:

1. **Web Search Agent**: Searches the web for information using the DuckDuckGo tool.
2. **Finance AI Agent**: Retrieves financial data using Yahoo Finance API, including stock prices, analyst recommendations, company fundamentals, and news.
3. **Multi-Agent System**: Combines the web search and finance agents to gather and summarize information from multiple domains.

## Features

- **Web Search**: Utilizes DuckDuckGo to gather search results from the web.
- **Financial Data**: Fetches stock prices, analyst recommendations, company fundamentals, news, and technical indicators using Yahoo Finance tools.
- **Agent Coordination**: Integrates the web search and finance agents to generate summaries and answers based on multi-domain data.
- **Markdown Support**: All results are formatted in markdown for easy display.
- **Tool Calls Logging**: Each agent's tool calls are logged for transparency.
- **Environment Variable Support**: API keys are loaded from a `.env` file for secure management of sensitive data.

## Requirements

Before running the system, ensure that you have the following installed:

- Python 3.12
- pip install -r requirements.txt 
