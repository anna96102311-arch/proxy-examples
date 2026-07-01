# Playwright Proxy Example

Learn how to configure Rapidproxy with Playwright to browse websites through residential proxies.

---

## What You'll Learn

In this example you'll learn how to:

- Configure a proxy in Playwright
- Authenticate with username and password
- Verify your proxy IP
- Build a reusable browser instance

---

## Prerequisites

Before you begin, make sure you have:

- Node.js 20+
- A Rapidproxy account
- Proxy credentials

---

## Installation

Install dependencies:

```bash
npm install
```

---

## Configure Proxy

Replace the following placeholders with your own Rapidproxy credentials.

```text
HOST
PORT
USERNAME
PASSWORD
```

---

## Run the Example

```bash
node example.js
```

---

## Expected Result

If everything is configured correctly, you'll receive a JSON response similar to:

```json
{
  "ip": "xxx.xxx.xxx.xxx",
  "country": "...",
  "city": "..."
}
```

---

## Related Documentation

https://docs.rapidproxy.io/