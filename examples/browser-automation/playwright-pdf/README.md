# Playwright PDF Generation with Residential Proxies

Learn how to generate PDF files from web pages with Playwright while routing browser traffic through Rapidproxy residential proxies.

---

## What You'll Learn

In this example, you'll learn how to:

- Launch Chromium with Rapidproxy proxy configuration
- Open a target webpage through a residential proxy
- Generate PDF files using Playwright
- Save generated documents locally
- Build automated webpage archiving workflows

---

## When Should You Use This Example?

Use this example when you need to:

- Generate automated website reports
- Archive webpage content
- Export online documents as PDF
- Create webpage snapshots for monitoring
- Build browser-based reporting workflows

Common use cases include:

- SEO monitoring
- Website change tracking
- Automated reports
- Data collection workflows
- Content archiving

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

TARGET_URL=https://www.wikipedia.org
OUTPUT_PATH=output/page.pdf
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
https://www.wikipedia.org

Generating PDF...

PDF saved successfully:
output/page.pdf
```

The generated PDF file will be saved according to the configured `OUTPUT_PATH`.

Example:

```text
output/
└── page.pdf
```

---

## How It Works

The script follows this workflow:

1. Load Rapidproxy credentials from `.env`
2. Launch Chromium with proxy authentication
3. Create a browser context
4. Navigate to the target webpage
5. Wait for the page to finish loading
6. Generate a PDF file
7. Save the file locally

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
Open Target Website
          |
          ↓
Generate PDF
          |
          ↓
Save File
```

---

## PDF Generation

Playwright provides built-in PDF generation through Chromium.

> Note: Playwright PDF generation is supported only with Chromium browsers running in headless mode.

Example:

```python
page.pdf(
    path="output/page.pdf",
    format="A4",
    print_background=True,
)
```

Parameters:

| Parameter | Description |
|---|---|
| `path` | Output PDF file path |
| `format` | Paper format such as A4 |
| `print_background` | Include background graphics |

---

## Best Practices

- Use Chromium when generating PDFs.
- Run PDF generation in headless mode.
- Wait for the page to finish loading before creating PDFs.
- Use consistent page formats for automated reports.
- Store generated files outside the source directory.
- Keep proxy credentials in environment variables.
- Avoid generating PDFs from websites without authorization.
- Use descriptive filenames for scheduled tasks.

---

## Troubleshooting

### Proxy authentication failed

Check that your `.env` configuration is correct:

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

### PDF generation failed

Check:

- The target URL is accessible.
- The page loads successfully.
- The output directory has write permissions.
- Chromium is installed correctly.
- The browser is running in headless mode.

---

### Navigation timeout

If the website loads slowly:

- Check proxy connectivity.
- Verify the target URL.
- Increase the timeout value in `example.py`.

Example:

```python
page.goto(
    target_url,
    timeout=120000,
)
```

---

## Related Documentation

- Rapidproxy Documentation:

https://docs.rapidproxy.io/

- Playwright PDF API:

https://playwright.dev/python/docs/api/class-page#page-pdf

- Playwright Browser Context:

https://playwright.dev/python/docs/browser-contexts