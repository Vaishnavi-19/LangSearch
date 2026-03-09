from typing import List
import os

from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()



class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )


openai_api_key = os.getenv("OPENAI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY") or os.getenv("TRAVILY_API_KEY")

if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")

if not tavily_api_key:
    raise RuntimeError(
        "TAVILY_API_KEY is missing. Add it to your .env file (or use TRAVILY_API_KEY)."
    )

llm = ChatOpenAI(model="gpt-5", api_key=openai_api_key)
tools = [TavilySearch(tavily_api_key=tavily_api_key)]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Search for 3 job postings for an AI engineer using LangChain in the Bay Area on LinkedIn and list their details.",
                }
            ]
        }
    )
    print(result)


if __name__ == "__main__":
    main()