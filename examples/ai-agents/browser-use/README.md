# Use Browser Use with Residential Proxies

Learn how to configure Browser Use with Rapidproxy residential proxies to securely automate browser tasks.

---

## What You'll Learn

In this example you'll learn how to:

- Configure Browser Use with Rapidproxy
- Authenticate residential proxies
- Verify your proxy configuration
- Launch browser automation through a proxy

---

## When Should You Use This Example?

Use this example if you:

- Build AI browser agents.
- Need residential IPs for browser automation.
- Want Browser Use traffic to go through Rapidproxy.

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.11+
- Browser Use
- A Rapidproxy account
- Rapidproxy proxy credentials
- Browser Use API Key

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Configure Proxy

1. Copy the example environment file.

```bash
cp .env.example .env
```

2. Open `.env` and replace the placeholders with your Rapidproxy credentials.

```env
RAPIDPROXY_HOST=HOST
RAPIDPROXY_PORT=PORT
RAPIDPROXY_USERNAME=USERNAME
RAPIDPROXY_PASSWORD=PASSWORD

BROWSER_USE_API_KEY=YOUR_BROWSER_USE_API_KEY
```

---

## Run the Example

Make sure your `.env` file has been configured before running the example.

```bash
python example.py
```

---

## Expected Result

Browser Use launches successfully through your Rapidproxy residential proxy.

---

## Related Documentation

- Official Documentation: https://docs.rapidproxy.io/
- Rapidproxy Website: https://www.rapidproxy.io/