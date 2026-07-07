import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


def main():
    load_dotenv()

    proxy = {
        "server": f"http://{os.getenv('RAPIDPROXY_HOST')}:{os.getenv('RAPIDPROXY_PORT')}",
        "username": os.getenv("RAPIDPROXY_USERNAME"),
        "password": os.getenv("RAPIDPROXY_PASSWORD"),
    }

    target_url = os.getenv("TARGET_URL", "https://www.python.org/")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            proxy=proxy,
        )

        context = browser.new_context(
    viewport={"width": 1280, "height": 720},
)

        try:
            page = context.new_page()
            page.goto(target_url, wait_until="domcontentloaded", timeout=60000)

            print(f"Page title: {page.title()}")

            page.screenshot(path="screenshot.png", full_page=True)
            print("Screenshot saved to screenshot.png")
        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    main()