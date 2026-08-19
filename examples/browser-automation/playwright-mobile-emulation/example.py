import os

from dotenv import load_dotenv
from playwright.sync_api import Browser, Playwright, sync_playwright


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


def emulate_mobile_device(
    playwright: Playwright,
    browser: Browser,
) -> None:
    """Run a mobile device emulation example."""
    target_url = os.getenv(
        "TARGET_URL",
        "https://playwright.dev/",
    )

    device = playwright.devices["iPhone 13"]

    context = browser.new_context(
        **device,
    )

    try:
        page = context.new_page()

        print(
            f"Opening page:\n{target_url}\n"
        )

        page.goto(
            target_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        viewport = page.evaluate(
            "() => ({"
            "width: window.innerWidth,"
            "height: window.innerHeight"
            "})"
        )

        user_agent = page.evaluate(
            "() => navigator.userAgent"
        )

        touch_points = page.evaluate(
            "() => navigator.maxTouchPoints"
        )

        print(
            "Mobile device:\n"
            "iPhone 13\n"
        )

        print(
            "Viewport:\n"
            f"{viewport['width']}x"
            f"{viewport['height']}\n"
        )

        print(
            "Touch support:\n"
            f"{touch_points > 0}\n"
        )

        print(
            "User agent:\n"
            f"{user_agent}\n"
        )

        if (
            viewport["width"]
            != device["viewport"]["width"]
        ):
            raise RuntimeError(
                "Mobile viewport does not match "
                "the selected device profile."
            )

        if touch_points <= 0:
            raise RuntimeError(
                "Touch support was not enabled "
                "for the selected device profile."
            )

        print(
            "Mobile emulation verified successfully."
        )

    finally:
        context.close()


def main() -> None:
    """Run the Playwright mobile emulation example."""
    load_dotenv()

    with sync_playwright() as playwright:
        browser = playwright.webkit.launch(
            headless=True,
            proxy=build_proxy(),
        )

        try:
            emulate_mobile_device(
                playwright,
                browser,
            )

        finally:
            browser.close()


if __name__ == "__main__":
    main()