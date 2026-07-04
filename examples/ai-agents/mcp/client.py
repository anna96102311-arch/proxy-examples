from server import fetch_ip_info


def main():
    print("MCP Client Calling Tool...\n")

    result = fetch_ip_info()

    print("=== CLIENT RECEIVED ===")
    print(result)


if __name__ == "__main__":
    main()