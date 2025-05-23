# Web Scraping Agent

## Setup

Install the Python dependencies.

```bash
pip install -r requirements.txt
```
If you run into issues with the dependency installation in regards to the git cloning, then run this instead:
```bash
$env:GIT_CLONE_PROTECTION_ACTIVE="false"; pip install -r requirements.txt
```

## Run the agent

```bash
python -m agent.web_scraping_agent
```

## Requirements

- Python 3.10+
- autogen
- mistralai
- ollama
- fix-busted-json
- beautifulsoup4
- request-html
- lxml[html_clean]

## Note
You need to include your own config.py file in the root directory that looks like the following:
```python
LLM_CONFIG = {
    "config_list": [
        {
            "model": "open-mistral-nemo",
            "api_key": "YOUR_API_KEY",
            "api_type": "mistral",
            "api_rate_limit": 0.25,
            "repeat_penalty": 1.1,
            "temperature": 0.0,
            "seed": 42,
            "stream": False,
            "native_tool_calls": False,
            "cache_seed": None,
        }
    ]
}
```