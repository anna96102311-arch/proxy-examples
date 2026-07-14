# MCP Integration Pattern with Residential Proxy

A minimal integration example demonstrating how an MCP-style tool can route external API requests through Rapidproxy residential proxies.

This example focuses on the integration pattern rather than implementing a complete MCP server.

---

## What You'll Learn

In this example you'll learn how to:

- Structure a simple MCP-style tool integration
- Send external API requests through Rapidproxy
- Keep proxy credentials outside the source code
- Separate the tool layer from the client layer
- Handle proxy and HTTP request errors

---

## When Should You Use This Example?

Use this example if you:

- Build tools that need external API access
- Want to understand where proxy routing belongs in an MCP-style architecture
- Need a minimal proxy-enabled HTTP request pattern
- Prefer a simple example that can be extended later

---

## Architecture

```text
Client
  ↓
MCP-style Tool (Proxy-enabled HTTP request)
  ↓
HTTP Request (httpx)
  ↓
Rapidproxy
  ↓
External API
```

---

## Project Structure

```text
mcp
├── README.md
├── server.py
├── client.py
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.11+
- A Rapidproxy account
- Rapidproxy proxy credentials

---

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Configure Proxy

Copy the example environment file:

```bash
cp .env.example .env
```

Update `.env` with your Rapidproxy credentials:

```env
RAPIDPROXY_HOST=HOST
RAPIDPROXY_PORT=PORT
RAPIDPROXY_USERNAME=USERNAME
RAPIDPROXY_PASSWORD=PASSWORD
```

Do not commit your completed `.env` file to GitHub.

---

## Run

Run the tool directly:

```bash
python server.py
```

Or run the client example:

```bash
python client.py
```

The client imports and calls the proxy-enabled tool function from `server.py`. It does not connect to a standalone MCP server process.

---

## Expected Output

The script prints public IP information returned through the Rapidproxy connection.

Example:

```text
=== TOOL OUTPUT ===
{
  "ip": "xxx.xxx.xxx.xxx",
  "city": "...",
  "region": "...",
  "country": "..."
}
```

When running `client.py`, the output begins with:

```text
=== CLIENT RECEIVED ===
```

---

## How It Works

The proxy URL is built from the Rapidproxy environment variables.

The `fetch_ip_info()` function then:

1. Creates an HTTPX client with the Rapidproxy proxy configuration
2. Requests `https://ipinfo.io/json`
3. Checks the HTTP response status
4. Returns the JSON response to the caller

The client example imports this function and demonstrates how another application layer can reuse the proxy-enabled tool.

---

## Why This Design?

This example intentionally focuses on the integration pattern instead of implementing a complete MCP server.

Benefits of this approach:

- Easy to understand
- Uses stable Python networking libraries
- Clearly shows where proxy routing belongs in a tool architecture
- Keeps proxy configuration separate from application logic
- Can be extended into a full MCP implementation later

---

## Best Practices

- Store proxy credentials in `.env`
- Keep `.env` excluded from Git
- Validate required environment variables before sending requests
- Encode proxy usernames and passwords before building a proxy URL
- Call `raise_for_status()` before processing an HTTP response
- Keep the networking layer reusable and separate from client logic

---

## Troubleshooting

### Missing environment variables

Make sure `.env` contains all four Rapidproxy variables:

```text
RAPIDPROXY_HOST
RAPIDPROXY_PORT
RAPIDPROXY_USERNAME
RAPIDPROXY_PASSWORD
```

### Proxy authentication failed

Check that the Rapidproxy username and password are correct.

### Connection timeout

Verify the proxy host, port, and your local network connection.

### HTTP request failed

Confirm that the target URL is available and that the proxy connection is working.

---

## Related Documentation

- Rapidproxy Documentation: https://docs.rapidproxy.io/
- Rapidproxy Website: https://www.rapidproxy.io/
- Model Context Protocol: https://modelcontextprotocol.io/
- HTTPX Proxy Documentation: https://www.python-httpx.org/advanced/proxies/