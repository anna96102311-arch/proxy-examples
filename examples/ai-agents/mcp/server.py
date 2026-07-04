import os
import httpx
from dotenv import load_dotenv

load_dotenv()


def fetch_ip_info():
    """
    MCP Tool Simulation:
    Fetch external API through proxy
    """

    proxy = os.getenv("HTTP_PROXY")

    with httpx.Client(proxies=proxy, timeout=30) as client:
        response = client.get("https://ipinfo.io/json")
        return response.json()


def main():
    print("MCP Tool Server Started (Proxy Enabled)\n")

    result = fetch_ip_info()

    print("=== MCP TOOL OUTPUT ===")
    print(result)


if __name__ == "__main__":
    main()