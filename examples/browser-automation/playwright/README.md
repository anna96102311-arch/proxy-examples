# Playwright Proxy Authentication Example

Use Rapidproxy with Playwright to authenticate residential proxies and verify your proxy connection in minutes.

---

## What You'll Learn

Use this example if you:

- Need to use Playwright with a residential proxy.
- Want to verify that proxy authentication is working correctly.
- Need a simple Playwright proxy configuration for your project.

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

## Why ipinfo.io?

This example uses `https://ipinfo.io/json` to verify that your proxy is working correctly.

If the returned IP address is different from your local public IP, your proxy has been configured successfully.

---

## Troubleshooting

### Authentication failed

Check that your proxy username and password are correct.

### Connection timeout

Verify your proxy host, port, and local network connectivity.

### Wrong IP address

Ensure that Playwright is using the configured proxy instead of your local network.

---

## Related Documentation

- Official Documentation: https://docs.rapidproxy.io/
- Rapidproxy Website: https://www.rapidproxy.io/