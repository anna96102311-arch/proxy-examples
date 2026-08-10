import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import Browser, sync_playwright


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise ValueError(
            f"Missing required environment variable: {name}"
        )

    return value


def build_proxy() -> dict[str, str]:
    return {
        "server": (
            f"http://"
            f"{get_required_env('RAPIDPROXY_HOST')}:"
            f"{get_required_env('RAPIDPROXY_PORT')}"
        ),
        "username": get_required_env(
            "RAPIDPROXY_USERNAME"
        ),
        "password": get_required_env(
            "RAPIDPROXY_PASSWORD"
        ),
    }


def generate_pdf(browser: Browser) -> None:
    target_url = os.getenv(
        "TARGET_URL",
        "https://example.com",
    )

    output_path = Path(
        os.getenv(
            "OUTPUT_PATH",
            "output/page.pdf",
        )
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    context = browser.new_context()

    try:
        page = context.new_page()

        print(
            f"Opening page: {target_url}"
        )

        page.goto(
            target_url,
            wait_until="networkidle",
            timeout=60000,
        )

        print("Generating PDF...")

        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
        )

        print(
            f"PDF saved successfully: {output_path}"
        )

    finally:
        context.close()


def main() -> None:
    load_dotenv()

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=True,
            proxy=build_proxy(),
        )

        try:
            generate_pdf(browser)

        finally:
            browser.close()


if __name__ == "__main__":
    main()