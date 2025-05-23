import autogen  # type: ignore
from tools.web_content_extractor import get_text_from_url
from config import LLM_CONFIG

web_content_tool_schema = {
    "type": "function",
    "function": {
        "name": "get_text_from_url",
        "description": "Fetches all human-readable text content from a given web URL.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL of the webpage to extract text from."
                }
            },
            "required": ["url"],
        },
    },
}

def create_web_scraping_agent() -> autogen.ConversableAgent:
    current_llm_config = LLM_CONFIG.copy()
    current_llm_config["tools"] = [web_content_tool_schema]
    
    agent = autogen.ConversableAgent(
        name="Generic Web Information Agent",
        system_message="You are an AI assistant that answers questions based on the content of a webpage. "
                       "The user will provide a URL and a question or task related to that URL. "
                       "Your first step is to use the 'get_text_from_url' tool to fetch the text content of the page. "
                       "IMPORTANT: After receiving the text from the tool, first check if the text seems relevant to the user\'s query or if it looks like a cookie consent page, an error message, a login page, or other irrelevant content. "
                       "If the text seems irrelevant (e.g., it talks about cookies, asks to sign in, or is a generic error), inform the user that you couldn\'t access the main content and why (e.g., 'The page returned a cookie consent form.'). Do NOT attempt to answer the user\'s question based on irrelevant text. "
                       "If the text seems relevant, then proceed to analyze it to answer the user\'s question or perform the requested task. "
                       "For example, if the user asks: 'What are the main headlines on [URL]?', first call get_text_from_url(url='[URL]'). If the text is relevant, read it, identify the main headlines, and then respond with something like 'The main headlines are: ...'. "
                       "If the user asks: 'Summarize this article: [URL]', first get the text. If relevant, then summarize it and respond with 'Here is the summary: ...'. "
                       "If the user asks: 'What is the price of META on [URL_to_google_finance]?', first get the text. If relevant, then find the price in the text and respond with 'The price of META is X.'. "
                       "Present your findings clearly. ",
        llm_config=current_llm_config,
    )
    agent.register_for_llm(name="get_text_from_url", description="Fetch text content from a URL.")(get_text_from_url)
    return agent

def create_user_proxy_agent() -> autogen.UserProxyAgent:
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg.get("content", "").upper(),
        code_execution_config=False,
        llm_config=False,
    )
    user_proxy.register_for_execution(name="get_text_from_url")(get_text_from_url)
    return user_proxy

def main():
    web_scraping_agent = create_web_scraping_agent()
    user_proxy = create_user_proxy_agent()
    
    while True:
        task_description = input("Please enter your task and the URL or type 'quit' to exit: ")
        if task_description.strip().lower() == 'quit':
            break
        
        if not task_description.strip():
            print("No input received, please try again.")
            continue

        user_proxy.initiate_chat(
            recipient=web_scraping_agent,
            message=task_description,
            max_turns=2  # Stop after one response. Removes the need for the agent to reply with TERMINATE.
        )
        
        user_proxy.reset()
        web_scraping_agent.reset()

if __name__ == "__main__":
    main() 