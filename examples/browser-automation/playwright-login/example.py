import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


def main() -> None:
    load_dotenv()

    proxy = {
        "server": (
            f"http://{os.getenv('RAPIDPROXY_HOST')}:"
            f"{os.getenv('RAPIDPROXY_PORT')}"
        ),
        "username": os.getenv("RAPIDPROXY_USERNAME"),
        "password": os.getenv("RAPIDPROXY_PASSWORD"),
    }

    login_url = os.getenv(
        "LOGIN_URL",
        "https://the-internet.herokuapp.com/login",
    )
    login_username = os.getenv("LOGIN_USERNAME", "tomsmith")
    login_password = os.getenv(
        "LOGIN_PASSWORD",
        "SuperSecretPassword!",
    )

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            proxy=proxy,
        )
        context = browser.new_context()

        try:
            page = context.new_page()
            page.goto(
                login_url,
                wait_until="domcontentloaded",
                timeout=60000,
            )

            page.get_by_label("Username").fill(login_username)
            page.get_by_label("Password").fill(login_password)
            page.get_by_role("button", name="Login").click()

            page.wait_for_url("**/secure", timeout=30000)

            print("Login successful.")
        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    main()