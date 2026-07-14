import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import Browser, expect, sync_playwright


AUTH_STATE_PATH = Path("playwright/.auth/state.json")


def build_proxy() -> dict[str, str | None]:
    """Build the Playwright proxy configuration."""
    required_variables = {
        "RAPIDPROXY_HOST": os.getenv("RAPIDPROXY_HOST"),
        "RAPIDPROXY_PORT": os.getenv("RAPIDPROXY_PORT"),
        "RAPIDPROXY_USERNAME": os.getenv("RAPIDPROXY_USERNAME"),
        "RAPIDPROXY_PASSWORD": os.getenv("RAPIDPROXY_PASSWORD"),
    }

    missing_variables = [
        name
        for name, value in required_variables.items()
        if not value
    ]

    if missing_variables:
        raise ValueError(
            "Missing required environment variables: "
            + ", ".join(missing_variables)
        )

    return {
        "server": (
            f"http://{required_variables['RAPIDPROXY_HOST']}:"
            f"{required_variables['RAPIDPROXY_PORT']}"
        ),
        "username": required_variables["RAPIDPROXY_USERNAME"],
        "password": required_variables["RAPIDPROXY_PASSWORD"],
    }


def save_authenticated_state(browser: Browser) -> None:
    """Log in and save the authenticated browser state."""
    login_url = os.getenv(
        "LOGIN_URL",
        "https://the-internet.herokuapp.com/login",
    )
    login_username = os.getenv("LOGIN_USERNAME", "tomsmith")
    login_password = os.getenv(
        "LOGIN_PASSWORD",
        "SuperSecretPassword!",
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

        success_message = page.locator("#flash")
        expect(success_message).to_contain_text(
            "You logged into a secure area!"
        )

        AUTH_STATE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        context.storage_state(path=AUTH_STATE_PATH)

        print("Authentication state saved.")
    finally:
        context.close()


def verify_saved_state(browser: Browser) -> None:
    """Open an authenticated page using the saved browser state."""
    secure_url = os.getenv(
        "SECURE_URL",
        "https://the-internet.herokuapp.com/secure",
    )

    context = browser.new_context(
        storage_state=AUTH_STATE_PATH,
    )

    try:
        page = context.new_page()
        page.goto(
            secure_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        if "/secure" not in page.url:
            raise RuntimeError(
                "The saved session is no longer valid. "
                "Delete the state file and run the example again."
            )

        secure_heading = page.get_by_role(
            "heading",
            name="Secure Area",
        )
        expect(secure_heading).to_be_visible()

        print("Session reuse verified successfully.")
    finally:
        context.close()


def main() -> None:
    """Run the Playwright session management example."""
    load_dotenv()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            proxy=build_proxy(),
        )

        try:
            if AUTH_STATE_PATH.exists():
                print("Saved session found.")
            else:
                print("No saved session found. Logging in...")
                save_authenticated_state(browser)

            verify_saved_state(browser)
        finally:
            browser.close()


if __name__ == "__main__":
    main()