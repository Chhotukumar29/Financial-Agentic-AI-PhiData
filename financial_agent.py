import openai
import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv 

load_dotenv() 
openai.api_key = os.getenv('OPENAI_API_KEY')

# My first web search agent autonomous agent 
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tools_calls = True,
    markdown = True,
    
)


# My second financial autonomous agent 
finance_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, 
                        company_news= True, technical_indicators= True, symbol="AAPL")],
    instructions = ["Use tables to display the data"],
    show_tool_calls=True,
    markdown = True,
    
)


# My third multi ai autonomous agent 
multi_ai_agents = Agent(
    team = [web_search_agent, finance_agent],
    instructions= ['Always include sources', 'Use tables to display the data'],
    show_tool_calls= True,
    markdown = True,
    
)


multi_ai_agents.print_response("Summarize analyst recommendation and share the latest news for Clean Science",stream=True)

