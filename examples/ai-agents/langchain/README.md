# Use LangChain with Residential Proxies

Learn how to use LangChain with the OpenAI integration while routing requests through Rapidproxy residential proxies.

---

## What You'll Learn

In this example you'll learn how to:

- Configure LangChain with OpenAI
- Route OpenAI API requests through Rapidproxy residential proxies.
- Store credentials securely with `.env`

---

## When Should You Use This Example?

Use this example if you:

- Build AI applications with LangChain.
- Need to access OpenAI APIs through a residential proxy.
- Want a clean and maintainable proxy configuration.

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

## Configure Environment

1. Copy the example environment file.

```bash
cp .env.example .env
```

2. Configure your credentials.

```env
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
OPENAI_MODEL=gpt-4.1-mini

HTTP_PROXY=http://USERNAME:PASSWORD@HOST:PORT
HTTPS_PROXY=http://USERNAME:PASSWORD@HOST:PORT
```

> **Note:** Replace `OPENAI_MODEL` with any model supported by your OpenAI account.

---

## Run the Example

```bash
python example.py
```

---

## Expected Result

The script prints the model response returned through LangChain.

---

## Related Documentation

- Official Documentation: https://docs.rapidproxy.io/
- Rapidproxy Website: https://www.rapidproxy.io/