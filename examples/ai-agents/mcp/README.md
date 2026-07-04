# MCP Tool with Residential Proxy

A minimal MCP-style tool example demonstrating how external API calls can be routed through Rapidproxy residential proxies.

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

- No dependency on unstable MCP SDK APIs
- Uses stable HTTP layer
- Fully compatible with any MCP evolution
- Easy to extend for real MCP servers later

---

## Related Docs

- https://modelcontextprotocol.io/
- https://docs.rapidproxy.io/