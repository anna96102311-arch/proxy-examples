import asyncio
import os

from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatBrowserUse
from browser_use.browser import ProxySettings


async def main():
    load_dotenv()

    proxy = ProxySettings(
        server=f"http://{os.getenv('RAPIDPROXY_HOST')}:{os.getenv('RAPIDPROXY_PORT')}",
        username=os.getenv("RAPIDPROXY_USERNAME"),
        password=os.getenv("RAPIDPROXY_PASSWORD"),
    )

    browser = Browser(
        headless=False,
        proxy=proxy,
    )

    agent = Agent(
        task="Open https://ipinfo.io/json and tell me the IP address shown on the page.",
        browser=browser,
        llm=ChatBrowserUse(),
    )

    try:
        history = await agent.run()
        print(history.final_result())
    finally:
        await browser.stop()


if __name__ == "__main__":
    asyncio.run(main())