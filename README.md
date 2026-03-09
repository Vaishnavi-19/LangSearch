# LangSearch

Simple LangChain agent that uses Tavily web search via `tavily_search` tool.

## Prerequisites

- Python 3.10+
- A virtual environment (recommended)
- OpenAI API key
- Tavily API key

## Install

If you use `uv`:

```powershell
uv add langchain langchain-openai langchain-tavily python-dotenv
```

If you use `pip`:

```powershell
python -m pip install langchain langchain-openai langchain-tavily python-dotenv
```

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Optional backward compatibility:

```env
TRAVILY_API_KEY=your_tavily_api_key
```

`main.py` accepts either `TAVILY_API_KEY` or `TRAVILY_API_KEY`.

## Tavily Search Tool (`tavily_search`)

This project uses the LangChain Tavily tool:

```python
from langchain_tavily import TavilySearch
tools = [TavilySearch(tavily_api_key=tavily_api_key)]
```

When the model decides to search the web, it calls `tavily_search` automatically through the tool binding.

## Run

```powershell
python main.py
```

## Troubleshooting

- `ModuleNotFoundError: No module named 'langchain_tavily'`
  - Install the package: `uv add langchain-tavily` (or `pip install langchain-tavily`).

- `openai.OpenAIError: The api_key client option must be set`
	- Ensure `OPENAI_API_KEY` is set in `.env`.

- Tavily auth or key issues (`Did not find tavily_api_key`)
	- Ensure `TAVILY_API_KEY` is set in `.env` and not empty.
	- `TRAVILY_API_KEY` also works in this project as fallback.

- If using Windows terminal and vars still do not load
	- Restart the terminal after editing `.env`.