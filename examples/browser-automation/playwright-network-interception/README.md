# Playwright Network Interception with Residential Proxies

Learn how to intercept and modify browser network requests with Playwright while routing traffic through Rapidproxy residential proxies.

---

## What You'll Learn

In this example, you'll learn how to:

- Launch Chromium with Rapidproxy proxy configuration
- Monitor browser requests and responses
- Intercept a network request with Playwright
- Modify request headers before sending the request
- Inspect the response returned by the target service
- Verify that the modified header reached the server

---

## When Should You Use This Example?

Use this example when you need to:

- Inspect browser network traffic
- Add or modify request headers
- Monitor HTTP responses
- Debug browser automation workflows
- Control requests made by a webpage
- Build more advanced browser automation workflows

Common use cases include:

- Request monitoring
- Custom request headers
- Browser automation debugging
- Network testing
- Web scraping workflows
- API request inspection

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.11+
- A Rapidproxy account
- Rapidproxy proxy credentials

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Chromium:

```bash
playwright install chromium
```

---

## Configure Environment

Copy `.env.example` to `.env` using your preferred file manager or command line.

### macOS / Linux

```bash
cp .env.example .env
```

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

Update `.env` with your Rapidproxy credentials:

```env
RAPIDPROXY_HOST=HOST
RAPIDPROXY_PORT=PORT
RAPIDPROXY_USERNAME=USERNAME
RAPIDPROXY_PASSWORD=PASSWORD

TARGET_URL=https://httpbin.org/headers
CUSTOM_HEADER_NAME=X-Rapidproxy-Example
CUSTOM_HEADER_VALUE=playwright-network-interception
```

---

## Run

Execute the example:

```bash
python example.py
```

---

## Expected Output

Example terminal output:

```text
Opening page:
https://httpbin.org/headers

>> GET https://httpbin.org/headers

Intercepted request:
GET https://httpbin.org/headers

Added header:
X-Rapidproxy-Example: playwright-network-interception

<< 200 https://httpbin.org/headers

Response status:
200

Modified header verified successfully.
```

The exact request sequence may vary depending on the target page and browser version.

---

## How It Works

The script follows this workflow:

1. Load Rapidproxy credentials from `.env`
2. Launch Chromium with the proxy configuration
3. Create a browser context
4. Register a network route handler
5. Open the target URL
6. Intercept the request before it reaches the server
7. Add a custom HTTP header
8. Continue the request
9. Receive the server response
10. Verify that the modified header was returned by the test service

Workflow:

```text
Environment Configuration
          |
          ↓
Rapidproxy Proxy Connection
          |
          ↓
Launch Chromium
          |
          ↓
Register Route Handler
          |
          ↓
Open Target URL
          |
          ↓
Intercept Request
          |
          ↓
Modify Request Header
          |
          ↓
Continue Request
          |
          ↓
Receive Response
          |
          ↓
Verify Modified Header
```

---

## Monitor Requests and Responses

Playwright can listen for browser network events with `page.on()`.

For example:

```python
page.on(
    "request",
    lambda request: print(
        ">>",
        request.method,
        request.url,
    ),
)

page.on(
    "response",
    lambda response: print(
        "<<",
        response.status,
        response.url,
    ),
)
```

The `request` event is emitted when a request is issued, while the `response` event is emitted when the response status and headers are received. :contentReference[oaicite:2]{index=2}

---

## Intercept a Request

Use `page.route()` to intercept matching requests:

```python
def handle_route(route):
    headers = {
        **route.request.headers,
        "X-Rapidproxy-Example": "playwright-network-interception",
    }

    route.continue_(
        headers=headers,
    )


page.route(
    "**/headers",
    handle_route,
)
```

The route handler runs before the matching request is sent to the network.

Playwright's `route.continue_()` supports overriding request headers, URL, method, and post data. :contentReference[oaicite:3]{index=3}

---

## Why Modify Headers?

Custom headers can be useful when a browser automation workflow needs to:

- Pass application-specific metadata
- Add tracing information
- Identify automated test requests
- Modify request behavior
- Debug requests sent by a browser

For example:

```python
headers = {
    **route.request.headers,
    "X-Rapidproxy-Example": "playwright-network-interception",
}
```

The existing headers are preserved and the custom header is added before the request continues.

---

## Verify the Modified Request

The example uses the `https://httpbin.org/headers` endpoint.

This service returns the headers received by the server, which makes it useful for demonstrating request interception.

The script reads the JSON response:

```python
data = response.json()
```

and checks the returned header:

```python
headers = {
    key.lower(): value
    for key, value in data["headers"].items()
}

assert (
    headers.get("x-rapidproxy-example")
    == "playwright-network-interception"
)
```

Playwright's `Response.json()` API returns the JSON representation of a response body. :contentReference[oaicite:4]{index=4}

---

## `page.route()` vs `page.on("request")`

These APIs serve different purposes.

### `page.on("request")`

Use it when you want to observe requests:

```python
page.on(
    "request",
    lambda request: print(request.url),
)
```

It is useful for:

- Logging
- Debugging
- Monitoring

### `page.route()`

Use it when you need to control a request:

```python
page.route(
    "**/*",
    handle_route,
)
```

It is useful for:

- Modifying request headers
- Blocking requests
- Changing request data
- Mocking or modifying responses

Playwright provides routing APIs specifically for handling and modifying network traffic. :contentReference[oaicite:5]{index=5}

---

## Blocking a Request

Routes can also abort requests.

For example:

```python
def handle_route(route):
    if route.request.resource_type == "image":
        route.abort()
        return

    route.continue_()
```

This can be useful when a workflow does not need certain resources.

Do not add this behavior to the current example unless you specifically want to demonstrate request blocking.

---

## Modifying a Request

The current example modifies request headers:

```python
headers = {
    **route.request.headers,
    "X-Rapidproxy-Example": "playwright-network-interception",
}

route.continue_(
    headers=headers,
)
```

Playwright also supports overriding other request properties through `route.continue_()`. :contentReference[oaicite:6]{index=6}

---

## Best Practices

- Keep proxy credentials in environment variables.
- Do not commit `.env` files.
- Use narrow route patterns when possible.
- Preserve existing request headers when adding custom headers.
- Use `page.on("request")` for monitoring rather than interception when no modification is required.
- Verify the resulting request or response when testing interception logic.
- Avoid modifying security-sensitive headers unless you understand the browser restrictions.
- Respect website terms and automation policies.

---

## Troubleshooting

### Proxy authentication failed

Check your `.env` configuration:

```env
RAPIDPROXY_HOST=
RAPIDPROXY_PORT=
RAPIDPROXY_USERNAME=
RAPIDPROXY_PASSWORD=
```

---

### Chromium is missing

Install the Playwright browser:

```bash
playwright install chromium
```

---

### Modified header was not detected

Check:

```env
CUSTOM_HEADER_NAME=X-Rapidproxy-Example
CUSTOM_HEADER_VALUE=playwright-network-interception
```

Also make sure the route pattern matches the target URL.

The example uses:

```python
page.route(
    "**/headers",
    handle_route,
)
```

---

### Target service is unavailable

The example uses httpbin as a public HTTP request inspection service.

You can change:

```env
TARGET_URL=https://httpbin.org/headers
```

to another compatible endpoint, but the verification logic may need to be updated if the endpoint does not return request headers.

---

## Related Documentation

- Rapidproxy Documentation:

https://docs.rapidproxy.io/

- Playwright Network:

https://playwright.dev/python/docs/network

- Playwright Route API:

https://playwright.dev/python/docs/api/class-route

- Playwright Request API:

https://playwright.dev/python/docs/api/class-request

- Playwright Response API:

https://playwright.dev/python/docs/api/class-response