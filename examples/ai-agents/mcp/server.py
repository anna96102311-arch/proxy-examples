import os
from urllib.parse import quote

import httpx
from dotenv import load_dotenv


def build_proxy_url() -> str:
    """
    Build the Rapidproxy proxy URL from environment variables.
    """
    host = os.getenv("RAPIDPROXY_HOST")
    port = os.getenv("RAPIDPROXY_PORT")
    username = os.getenv("RAPIDPROXY_USERNAME")
    password = os.getenv("RAPIDPROXY_PASSWORD")

    missing_variables = [
        name
        for name, value in {
            "RAPIDPROXY_HOST": host,
            "RAPIDPROXY_PORT": port,
            "RAPIDPROXY_USERNAME": username,
            "RAPIDPROXY_PASSWORD": password,
        }.items()
        if not value
    ]

    if missing_variables:
        raise ValueError(
            "Missing required environment variables: "
            + ", ".join(missing_variables)
        )

    encoded_username = quote(username, safe="")
    encoded_password = quote(password, safe="")

    return (
        f"http://{encoded_username}:{encoded_password}"
        f"@{host}:{port}"
    )


def fetch_ip_info() -> dict:
    """
    Fetch IP information through Rapidproxy.

    This function demonstrates the proxy-enabled request layer
    used by an MCP-style integration pattern.
    """
    proxy_url = build_proxy_url()

    with httpx.Client(
        proxy=proxy_url,
        timeout=30,
    ) as client:
        response = client.get("https://ipinfo.io/json")
        response.raise_for_status()
        return response.json()


def main() -> None:
    load_dotenv()

    print("MCP-style proxy tool started.\n")

    result = fetch_ip_info()

    print("=== TOOL OUTPUT ===")
    print(result)


if __name__ == "__main__":
    main()