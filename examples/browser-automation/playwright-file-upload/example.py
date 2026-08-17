import os
from pathlib import Path
from tempfile import TemporaryDirectory

from dotenv import load_dotenv
from playwright.sync_api import Browser, expect, sync_playwright


def get_required_env(name: str) -> str:
    """Get a required environment variable."""
    value = os.getenv(name)

    if not value:
        raise ValueError(
            f"Missing required environment variable: {name}"
        )

    return value


def build_proxy() -> dict[str, str]:
    """Build Playwright proxy configuration."""
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


def create_test_file(directory: Path) -> Path:
    """Create a temporary file for the upload example."""
    file_path = directory / "rapidproxy-upload-test.txt"

    file_path.write_text(
        "This is a temporary file created "
        "for the Rapidproxy Playwright upload example.",
        encoding="utf-8",
    )

    return file_path


def upload_file(browser: Browser) -> None:
    """Upload a temporary file using Playwright."""
    upload_url = os.getenv(
        "UPLOAD_URL",
        "https://the-internet.herokuapp.com/upload",
    )

    context = browser.new_context()

    try:
        page = context.new_page()

        print(
            f"Opening upload page:\n{upload_url}\n"
        )

        page.goto(
            upload_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        with TemporaryDirectory() as temp_directory:
            file_path = create_test_file(
                Path(temp_directory)
            )

            print(
                f"Uploading file:\n"
                f"{file_path.name}\n"
            )

            page.locator(
                "#file-upload"
            ).set_input_files(file_path)

            print("Submitting upload...\n")

            page.locator(
                "#file-submit"
            ).click()

            expect(
                page.locator("h3")
            ).to_have_text(
                "File Uploaded!"
            )

            expect(
                page.locator("#uploaded-files")
            ).to_have_text(
                file_path.name
            )

            print(
                f"File uploaded successfully:\n"
                f"{file_path.name}"
            )

    finally:
        context.close()


def main() -> None:
    """Run the Playwright file upload example."""
    load_dotenv()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            proxy=build_proxy(),
        )

        try:
            upload_file(browser)

        finally:
            browser.close()


if __name__ == "__main__":
    main()