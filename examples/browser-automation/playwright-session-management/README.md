# Playwright Session Management with Residential Proxies

Learn how to save and reuse an authenticated Playwright session while routing browser traffic through Rapidproxy residential proxies.

---

## What You'll Learn

In this example you'll learn how to:

- Launch Playwright through Rapidproxy
- Log in to a public practice website
- Save cookies and local storage with `storage_state()`
- Reuse the saved session in a new browser context
- Avoid logging in again for every browser task

---

## When Should You Use This Example?

Use this example if you:

- Run repeated authenticated browser workflows.
- Want to reduce unnecessary login requests.
- Need to reuse cookies and local storage between Playwright contexts.
- Want to keep proxy and login configuration outside the source code.

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

LOGIN_URL=https://the-internet.herokuapp.com/login
SECURE_URL=https://the-internet.herokuapp.com/secure
LOGIN_USERNAME=tomsmith
LOGIN_PASSWORD=SuperSecretPassword!
```

The login credentials belong to the public practice website and are not real account credentials.

---

## Run the Example

```bash
python example.py
```

The first run logs in and creates:

```text
playwright/.auth/state.json
```

Later runs reuse this authenticated state when it is available.

---

## Expected Output

On the first run:

```text
No saved session found. Logging in...
Authentication state saved.
Session reuse verified successfully.
```

On later runs:

```text
Saved session found.
Session reuse verified successfully.
```

---

## How It Works

The script follows this process:

1. Launch Chromium with Rapidproxy
2. Check whether a saved authentication state exists
3. Log in when no saved state is available
4. Save cookies and local storage to `state.json`
5. Create a new browser context with the saved state
6. Open the authenticated page and verify the session

---

## Best Practices

- Never commit authenticated state files.
- Treat storage state files like passwords or API keys.
- Reuse authentication state only for the same application and account.
- Regenerate the state when the session expires.
- Use separate state files for separate accounts.
- Keep proxy and login credentials in `.env`.

---

## Troubleshooting

### The saved session has expired

Delete the following file and run the script again:

```text
playwright/.auth/state.json
```

### Login failed

Confirm that the login URL, username, and password match `.env.example`.

### Proxy authentication failed

Check the Rapidproxy host, port, username, and password in `.env`.

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