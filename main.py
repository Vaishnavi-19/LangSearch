import os
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent 
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI  
from tavily import TavilyClient

tavily_api_key=os.getenv("TRAVILY_API_KEY")
tavily = TavilyClient(api_key=tavily_api_key)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
 raise RuntimeError("OPENAI_API_KEY is missing. Add it to .env or system environment variables.")
@tool
def search(query: str) -> str:
    """Searches the web for the given query and returns the results."""
    print(f"Searching for: {query}")
    return tavily.search(query=query, num_results=5)

llm = ChatOpenAI(temperature=0, model="gpt-4-0613", api_key=api_key)
tools = [search]
agent = create_agent(model=llm, tools=tools)
def main():
    print("Hello from langsearch!")
    result = agent.invoke({"messages":HumanMessage(content="List five job openings for service virtualization engineer.")})
    print(f"Agent result: {result}")


if __name__ == "__main__":
    main()
