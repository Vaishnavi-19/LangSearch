# LangSearch

Simple LangChain agent that uses Tavily web search as a tool.

## Prerequisites

- Python 3.10+
- A virtual environment (recommended)
- OpenAI API key
- Tavily API key

## Install

If you use `uv`:

```powershell
uv add langchain langchain-openai tavily-python python-dotenv
```

If you use `pip`:

```powershell
python -m pip install langchain langchain-openai tavily-python python-dotenv
```

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
TRAVILY_API_KEY=your_tavily_api_key
```

Important: this project currently reads `TRAVILY_API_KEY` (with an `R`) from `main.py`.

## Tavily Import

Use this import in Python:

```python
from tavily import TavilyClient
```

## Run

```powershell
python main.py
```

## Troubleshooting

- `ModuleNotFoundError: No module named 'tavily'`
	- Install the package: `uv add tavily-python` (or `pip install tavily-python`).

- `openai.OpenAIError: The api_key client option must be set`
	- Ensure `OPENAI_API_KEY` is set in `.env`.

- Tavily auth or key issues
	- Ensure `TRAVILY_API_KEY` is set in `.env` and not empty.

- If using Windows terminal and vars still do not load
	- Restart the terminal after editing `.env`.