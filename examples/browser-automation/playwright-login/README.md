# Playwright Login with Residential Proxies

Learn how to automate a login flow with Playwright while routing browser traffic through Rapidproxy residential proxies.

---

## What You'll Learn

In this example you'll learn how to:

- Load proxy and login settings from `.env`
- Launch Chromium through Rapidproxy
- Fill a login form with Playwright locators
- Submit the form and wait for navigation
- Verify that the login succeeded

---

## When Should You Use This Example?

Use this example if you:

- Test login workflows with Playwright.
- Need browser traffic to use a residential proxy.
- Want a reusable starting point for authenticated browser automation.
- Need a safe public practice page for login testing.

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.11+
- A Rapidproxy account
- Rapidproxy proxy credentials

---

## Installation

Install the dependencies and Chromium browser:

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

2. Open `.env` and replace the Rapidproxy placeholders with your own credentials.

```env
RAPIDPROXY_HOST=HOST
RAPIDPROXY_PORT=PORT
RAPIDPROXY_USERNAME=USERNAME
RAPIDPROXY_PASSWORD=PASSWORD

LOGIN_URL=https://the-internet.herokuapp.com/login
LOGIN_USERNAME=tomsmith
LOGIN_PASSWORD=SuperSecretPassword!
```

The login credentials above belong to the public practice website and are not real account credentials.

---

## Run the Example

```bash
python example.py
```

---

## Expected Output

If the login succeeds, the script prints:

```text
Login successful.
```

The browser reaches the secure area of the public practice website.

---

## Best Practices

- Store proxy and login credentials in `.env`.
- Use Playwright locators instead of brittle CSS selectors when possible.
- Wait for the expected URL after submitting a login form.
- Use public practice websites for demonstration code.
- Do not commit authenticated browser state or real credentials.

---

## Troubleshooting

### Proxy authentication failed

Check the Rapidproxy host, port, username, and password in `.env`.

### Login did not complete

Confirm that `LOGIN_URL`, `LOGIN_USERNAME`, and `LOGIN_PASSWORD` match the values in `.env.example`.

### Chromium is missing

Run:

```bash
playwright install chromium
```

---

## Related Documentation

- Rapidproxy Documentation: https://docs.rapidproxy.io/
- Rapidproxy Website: https://www.rapidproxy.io/
- Playwright Authentication Guide: https://playwright.dev/python/docs/auth