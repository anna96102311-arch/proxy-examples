# Playwright Proxy Best Practice

Use Playwright with Rapidproxy residential proxies for realistic browser automation workflows.

---

## What You'll Learn

In this example you'll learn how to:

- Load Rapidproxy credentials from `.env`
- Launch Playwright with proxy authentication
- Create a reusable browser context
- Configure browser context
- Open a public web page through proxy
- Save a screenshot as proof of execution

---

## When Should You Use This Example?

Use this example if you:

- Build browser automation workflows with Playwright.
- Need residential proxy routing for browser traffic.
- Want a practical Playwright setup that is easier to extend.
- Need a screenshot-based verification workflow.

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.11+
- Playwright
- A Rapidproxy account
- Rapidproxy proxy credentials

---

## Installation

```bash
pip install -r requirements.txt
playwright install chromium
```

---

## Configure Environment

1. Copy the example environment file.

```bash
cp .env.example .env
```

2. Open `.env` and replace the placeholders with your own Rapidproxy credentials.

```env
RAPIDPROXY_HOST=HOST
RAPIDPROXY_PORT=PORT
RAPIDPROXY_USERNAME=USERNAME
RAPIDPROXY_PASSWORD=PASSWORD
TARGET_URL=https://www.python.org/
```

---

## Run the Example

```bash
python example.py
```

---

## Expected Output

The script will:

- Open the target website through Rapidproxy
- Print the page title
- Save a screenshot as `screenshot.png`

---

## Related Documentation

- Official Documentation: https://docs.rapidproxy.io/
- Rapidproxy Website: https://www.rapidproxy.io/