import os
from pathlib import Path
from typing import TypedDict

from dotenv import load_dotenv
from playwright.sync_api import Browser, expect, sync_playwright


class ProxySettings(TypedDict):
    """Playwright proxy configuration."""

    server: str
    username: str
    password: str


def get_required_environment_variable(name: str) -> str:
    """Return a required environment variable or raise an error."""
    value = os.getenv(name)

    if not value:
        raise ValueError(
            f"Missing required environment variable: {name}"
        )

    return value


def build_proxy() -> ProxySettings:
    """Build the Playwright proxy configuration."""
    host = get_required_environment_variable(
        "RAPIDPROXY_HOST"
    )
    port = get_required_environment_variable(
        "RAPIDPROXY_PORT"
    )
    username = get_required_environment_variable(
        "RAPIDPROXY_USERNAME"
    )
    password = get_required_environment_variable(
        "RAPIDPROXY_PASSWORD"
    )

    return {
        "server": f"http://{host}:{port}",
        "username": username,
        "password": password,
    }


def capture_screenshots(browser: Browser) -> None:
    """Capture viewport, full-page, and element screenshots."""
    target_url = os.getenv(
        "TARGET_URL",
        "https://example.com",
    )
    output_directory = Path(
        os.getenv("OUTPUT_DIR", "screenshots")
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    viewport_path = output_directory / "viewport.png"
    full_page_path = output_directory / "full-page.png"
    heading_path = output_directory / "heading.png"

    context = browser.new_context(
        viewport={
            "width": 1440,
            "height": 900,
        }
    )

    try:
        page = context.new_page()

        print(f"Opening {target_url}...")

        page.goto(
            target_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        heading = page.locator(
            "h1, h2, h3, h4, h5, h6"
        ).first
        expect(heading).to_be_visible(timeout=30000)

        page.screenshot(path=viewport_path)
        print(
            f"Saved viewport screenshot: {viewport_path}"
        )

        page.screenshot(
            path=full_page_path,
            full_page=True,
        )
        print(
            f"Saved full-page screenshot: {full_page_path}"
        )

        heading.screenshot(path=heading_path)
        print(
            f"Saved element screenshot: {heading_path}"
        )

        print(
            "Screenshot capture completed successfully."
        )
    finally:
        context.close()


def main() -> None:
    """Run the Playwright screenshot example."""
    load_dotenv()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            proxy=build_proxy(),
        )

        try:
            capture_screenshots(browser)
        finally:
            browser.close()


if __name__ == "__main__":
    main()