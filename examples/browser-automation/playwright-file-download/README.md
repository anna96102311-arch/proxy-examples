# Playwright File Download with Residential Proxies

Learn how to download files with Playwright while routing browser traffic through Rapidproxy residential proxies.

---

## What You'll Learn

In this example, you'll learn how to:

- Launch Chromium with Rapidproxy proxy configuration
- Navigate to a download page
- Capture browser download events
- Save downloaded files locally
- Verify downloaded files

---

## When Should You Use This Example?

Use this example when you need to:

- Automate file downloads from websites
- Export reports automatically
- Download resources during scraping workflows
- Test browser-based download flows
- Build automated browser workflows

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

DOWNLOAD_URL=https://demo.playwright.dev/api/class-download
DOWNLOAD_PATH=downloads
```

---

## Run

Execute:

```bash
python example.py
```

---

## Expected Output

Example output:

```text
Opening download page:
https://demo.playwright.dev/api/class-download

Download started.

File saved successfully:
downloads/example-file.zip
```

---

## How It Works

The script follows this workflow:

1. Load Rapidproxy configuration from `.env`
2. Launch Chromium with proxy authentication
3. Open the download page
4. Wait for the browser download event
5. Click the download link
6. Save the downloaded file
7. Verify the file exists

---

## Core Download Logic

Playwright provides a built-in download listener:

```python
with page.expect_download() as download_info:
    page.get_by_role(
        "link",
        name="Download file",
    ).click()

download = download_info.value

download.save_as(
    "downloads/file.zip"
)
```

This allows Playwright to handle browser download behavior directly.

---

## Best Practices

- Always wait for the download event before clicking download buttons.
- Use stable selectors for download actions.
- Store downloaded files outside the source directory.
- Add download folders to `.gitignore`.
- Keep proxy credentials in environment variables.
- Respect website terms and download permissions.

---

## Troubleshooting

### Proxy authentication failed

Check:

```env
RAPIDPROXY_HOST=
RAPIDPROXY_PORT=
RAPIDPROXY_USERNAME=
RAPIDPROXY_PASSWORD=
```

---

### Download did not start

Possible causes:

- The page changed its download element.
- The download requires authentication.
- The target URL is unavailable.

Update the locator in `example.py`.

---

### Chromium is missing

Run:

```bash
playwright install chromium
```

---

### File was not saved

Check:

- The download directory exists.
- The process has write permission.
- The download event completed successfully.

---

## Related Documentation

- Rapidproxy Documentation:
https://docs.rapidproxy.io/

- Playwright Downloads:
https://playwright.dev/python/docs/downloads

- Playwright Browser Context:
https://playwright.dev/python/docs/browser-contexts