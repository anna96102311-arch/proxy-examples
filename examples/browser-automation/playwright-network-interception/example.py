import os

from dotenv import load_dotenv
from playwright.sync_api import Browser, Playwright, Route, sync_playwright


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


def create_route_handler(
    header_name: str,
    header_value: str,
):
    """Create a route handler that adds a custom header."""

    def handle_route(route: Route) -> None:
        request = route.request

        print(
            "Intercepted request:\n"
            f"{request.method} {request.url}\n"
        )

        headers = {
            **request.headers,
            header_name: header_value,
        }

        print(
            "Added header:\n"
            f"{header_name}: {header_value}\n"
        )

        route.continue_(
            headers=headers,
        )

    return handle_route


def monitor_request(request) -> None:
    """Log outgoing browser requests."""
    print(
        ">> "
        f"{request.method} "
        f"{request.url}"
    )


def monitor_response(response) -> None:
    """Log received browser responses."""
    print(
        "<< "
        f"{response.status} "
        f"{response.url}"
    )


def run_network_interception(
    playwright: Playwright,
    browser: Browser,
) -> None:
    """Run the Playwright network interception example."""
    target_url = os.getenv(
        "TARGET_URL",
        "https://httpbin.org/headers",
    )

    header_name = os.getenv(
        "CUSTOM_HEADER_NAME",
        "X-Rapidproxy-Example",
    )

    header_value = os.getenv(
        "CUSTOM_HEADER_VALUE",
        "playwright-network-interception",
    )

    context = browser.new_context()

    try:
        page = context.new_page()

        page.on(
            "request",
            monitor_request,
        )

        page.on(
            "response",
            monitor_response,
        )

        page.route(
            "**/headers",
            create_route_handler(
                header_name,
                header_value,
            ),
        )

        print(
            f"Opening page:\n{target_url}\n"
        )

        response = page.goto(
            target_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        if response is None:
            raise RuntimeError(
                "No response was returned for "
                "the target page."
            )

        print(
            f"\nResponse status:\n"
            f"{response.status}\n"
        )

        if not response.ok:
            raise RuntimeError(
                f"Target request failed with "
                f"HTTP status {response.status}."
            )

        response_data = response.json()

        received_headers = {
            key.lower(): str(value)
            for key, value in response_data[
                "headers"
            ].items()
        }

        expected_header = header_name.lower()

        actual_value = received_headers.get(
            expected_header
        )

        if actual_value != header_value:
            raise RuntimeError(
                "Modified header was not verified.\n"
                f"Expected: {header_value}\n"
                f"Received: {actual_value}"
            )

        print(
            "Modified header verified successfully."
        )

    finally:
        context.close()


def main() -> None:
    """Run the Playwright network interception example."""
    load_dotenv()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            proxy=build_proxy(),
        )

        try:
            run_network_interception(
                playwright,
                browser,
            )

        finally:
            browser.close()


if __name__ == "__main__":
    main()