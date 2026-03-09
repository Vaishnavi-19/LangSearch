import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY") or os.getenv("TRAVILY_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")

if not tavily_api_key:
    raise RuntimeError(
        "TAVILY_API_KEY is missing. Add it to your .env file (or use TRAVILY_API_KEY)."
    )

llm = ChatOpenAI(temperature=0, model="gpt-4-0613", api_key=openai_api_key)
tools = [TavilySearch(tavily_api_key=tavily_api_key)]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langsearch!")
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "List five job openings for service virtualization engineer.",
                }
            ]
        }
    )
    print(f"Agent result: {result}")


if __name__ == "__main__":
    main()
