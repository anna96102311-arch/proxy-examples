# Use OpenAI SDK with Residential Proxies

Learn how to configure the OpenAI Python SDK with Rapidproxy residential proxies.

---

## What You'll Learn

In this example you'll learn how to:

- Configure the OpenAI Python SDK with a proxy
- Load API keys and proxy credentials from `.env`
- Route OpenAI SDK traffic through Rapidproxy

---

## When Should You Use This Example?

Use this example if you:

- Need to call OpenAI APIs through a proxy.
- Want to keep API keys and proxy credentials out of source code.
- Build AI applications that require controlled network routing.

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.11+
- An OpenAI API key
- A Rapidproxy account
- Rapidproxy proxy credentials

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

2. Open `.env` and replace the placeholders with your own credentials.

```env
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
OPENAI_MODEL=gpt-4.1-mini

RAPIDPROXY_HOST=HOST
RAPIDPROXY_PORT=PORT
RAPIDPROXY_USERNAME=USERNAME
RAPIDPROXY_PASSWORD=PASSWORD
```

> **Note:** `OPENAI_MODEL` can be replaced with any model supported by your OpenAI account.

---

## Run the Example

Make sure your `.env` file has been configured before running the example.

```bash
python example.py
```

---

## Expected Result

If everything is configured correctly, the script will print a response from the OpenAI API.

---

## Related Documentation

- Official Documentation: https://docs.rapidproxy.io/
- Rapidproxy Website: https://www.rapidproxy.io/