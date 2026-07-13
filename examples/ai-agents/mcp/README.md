# # MCP Integration Pattern with Residential Proxy

A minimal integration example demonstrating how an MCP-style tool can route external API requests through Rapidproxy residential proxies.

This project focuses on the integration pattern rather than implementing a complete MCP server.

---

## What You'll Learn

- MCP tool concept (simplified)
- How tools access external APIs
- How to route requests through a proxy
- How MCP-style architecture works

---

## When Should You Use This Example?

Use this example if you:

- Build MCP-based tools
- Need external API access in tools
- Want proxy-enabled tool execution
- Prefer minimal and stable architecture

---

## Architecture

```
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

## Installation

```bash
pip install -r requirements.txt
```

---

## Configure Proxy

```bash
cp .env.example .env
```

Fill in:

```env
HTTP_PROXY=http://USERNAME:PASSWORD@HOST:PORT
HTTPS_PROXY=http://USERNAME:PASSWORD@HOST:PORT
```

---

## Run

```bash
python server.py
python client.py
```

---

## Expected Output

IP information returned via proxy-enabled request.

---

## Why This Design?

This example intentionally focuses on the integration pattern instead of implementing a complete MCP server.

Benefits of this approach:

- Easy to understand
- Uses stable Python networking libraries
- Demonstrates where proxy routing belongs in an MCP-style architecture
- Easy to extend into a full MCP implementation later

---

## Related Docs

- https://modelcontextprotocol.io/
- https://docs.rapidproxy.io/