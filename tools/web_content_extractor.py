import os
os.environ["PYPPETEER_CHROMIUM_REVISION"] = "1181217"
from requests_html import HTMLSession, MaxRetries, TimeoutError as HTMLTimeoutError
from bs4 import BeautifulSoup

def get_text_from_url(url: str) -> str:
    session = HTMLSession()
    try:
        root = session.get(url, timeout=15)
        root.html.render(sleep=2, timeout=20)
        
        soup = BeautifulSoup(root.html.html, 'html.parser')

        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        text = soup.get_text(separator=' ', strip=True)
        
        if not text:
            return "Could not extract any text content from the page after rendering JavaScript."
            
        return text

    except HTMLTimeoutError:
        return f"Error: The request to {url} or its JavaScript rendering timed out."
    except MaxRetries:
        return f"Error: Maximum retries exceeded for {url}. The site may be inaccessible or blocking requests."
    except Exception as e:
        return f"An unexpected error occurred while processing {url}: {e}"
    finally:
        session.close()