# Playwright Screenshot with Residential Proxies

Learn how to capture viewport, full-page, and element screenshots with Playwright while routing browser traffic through Rapidproxy residential proxies.

---

## What You'll Learn

In this example, you'll learn how to:

- Launch Chromium through Rapidproxy
- Open a configurable target page
- Capture the visible browser viewport
- Capture the complete scrollable page
- Capture a specific page element
- Store screenshots in a dedicated output directory

---

## When Should You Use This Example?

Use this example when you need to:

- Monitor website layouts or localized content
- Capture visual evidence during automated workflows
- Generate screenshots for reports
- Verify how pages appear from different proxy locations
- Capture individual elements without saving the entire page

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.11+
- A Rapidproxy account
- Rapidproxy proxy credentials

---

## Installation

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Install Chromium for Playwright:

```bash
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

TARGET_URL=https://example.com
OUTPUT_DIR=screenshots
```

---

## Run the Example

```bash
python example.py
```

---

## Expected Output

The script creates the following files:

```text
screenshots/
├── viewport.png
├── full-page.png
└── heading.png
```

The terminal output should look similar to:

```text
Opening https://example.com...
Saved viewport screenshot: screenshots/viewport.png
Saved full-page screenshot: screenshots/full-page.png
Saved element screenshot: screenshots/heading.png
Screenshot capture completed successfully.
```

---

## How It Works

The script follows this process:

1. Loads the Rapidproxy configuration from `.env`
2. Launches Chromium with proxy authentication
3. Creates a browser context with a fixed viewport
4. Opens the configured target page
5. Waits for the page heading to become visible
6. Captures the current viewport
7. Captures the complete scrollable page
8. Captures the first visible heading element
9. Saves all images to the configured output directory

---

## Screenshot Types

### Viewport Screenshot

Captures only the part of the page currently visible inside the browser viewport:

```python
page.screenshot(path="screenshots/viewport.png")
```

### Full-Page Screenshot

Captures the entire scrollable page:

```python
page.screenshot(
    path="screenshots/full-page.png",
    full_page=True,
)
```

### Element Screenshot

Captures only a specific element:

```python
heading.screenshot(path="screenshots/heading.png")
```

---

## Best Practices

- Wait for important page elements before capturing screenshots.
- Use a consistent viewport when comparing screenshots.
- Store generated images outside the source-code directory when running large jobs.
- Use descriptive filenames for scheduled monitoring tasks.
- Do not commit generated screenshots unless they are required for documentation.
- Keep proxy credentials in `.env`.
- Capture only websites and content you are authorized to access.

---

## Troubleshooting

### Proxy authentication failed

Confirm that the following values are correct in `.env`:

```env
RAPIDPROXY_HOST=
RAPIDPROXY_PORT=
RAPIDPROXY_USERNAME=
RAPIDPROXY_PASSWORD=
```

### Chromium is not installed

Run:

```bash
playwright install chromium
```

### The target page timed out

Confirm that `TARGET_URL` is valid and accessible through the selected proxy location.

You can also increase the navigation timeout in `example.py`.

### The heading element was not found

This example expects the target page to contain at least one visible heading from `h1` to `h6`.

When using a different website, update the locator in `example.py`:

```python
heading = page.locator("h1, h2, h3, h4, h5, h6").first
```

### Screenshots were not created

Confirm that the process has permission to create the configured output directory.

---

## Related Documentation

- Rapidproxy Documentation: https://docs.rapidproxy.io/
- Rapidproxy Website: https://www.rapidproxy.io/
- Playwright Screenshots Guide: https://playwright.dev/python/docs/screenshots
- Playwright Page API: https://playwright.dev/python/docs/api/class-page
- Playwright Locator API: https://playwright.dev/python/docs/api/class-locator