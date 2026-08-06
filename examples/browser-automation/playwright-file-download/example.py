import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import Browser, expect, sync_playwright


def get_required_env(name: str) -> str:
    """
    Get required environment variable.
    """
    value = os.getenv(name)

    if not value:
        raise ValueError(
            f"Missing required environment variable: {name}"
        )

    return value


def build_proxy() -> dict[str, str]:
    """
    Build Playwright proxy configuration.
    """
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


def download_file(browser: Browser) -> None:
    """
    Download a file using Playwright.
    """
    download_url = os.getenv(
        "DOWNLOAD_URL",
        "https://demo.playwright.dev/api/class-download",
    )

    download_directory = Path(
        os.getenv(
            "DOWNLOAD_PATH",
            "downloads",
        )
    )

    download_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    context = browser.new_context()

    try:
        page = context.new_page()

        print(
            f"Opening download page: {download_url}"
        )

        page.goto(
            download_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        with page.expect_download() as download_info:
            page.get_by_role(
                "link",
                name="Download file",
            ).click(
                timeout=30000
            )

        download = download_info.value

        file_name = download.suggested_filename

        file_path = (
            download_directory / file_name
        )

        download.save_as(file_path)

        if not file_path.exists():
            raise RuntimeError(
                "Downloaded file was not created."
            )

        print("Download started.")
        print(
            f"File saved successfully: {file_path}"
        )

    finally:
        context.close()


def main() -> None:
    """
    Run Playwright file download example.
    """
    load_dotenv()

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=True,
            proxy=build_proxy(),
        )

        try:
            download_file(browser)

        finally:
            browser.close()


if __name__ == "__main__":
    main()