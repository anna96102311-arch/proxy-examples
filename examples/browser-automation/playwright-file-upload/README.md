# Playwright File Upload with Residential Proxies

Learn how to upload files with Playwright while routing browser traffic through Rapidproxy residential proxies.

---

## What You'll Learn

In this example, you'll learn how to:

- Launch Chromium with Rapidproxy proxy configuration
- Navigate to a file upload page
- Create a temporary local file for testing
- Upload a file with Playwright
- Verify that the file was uploaded successfully

---

## When Should You Use This Example?

Use this example when you need to:

- Automate file upload workflows
- Submit documents through web forms
- Upload files during browser automation
- Build automated data collection workflows
- Test file upload functionality

Common use cases include:

- Document submission
- Image uploads
- Data import workflows
- Automated form submission
- Browser-based automation

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

UPLOAD_URL=https://the-internet.herokuapp.com/upload
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
Opening upload page:
https://the-internet.herokuapp.com/upload

Uploading file:
rapidproxy-upload-test.txt

Submitting upload...

File uploaded successfully:
rapidproxy-upload-test.txt
```

The test file is created temporarily during execution and automatically removed after the upload workflow finishes.

---

## How It Works

The script follows this workflow:

1. Load Rapidproxy credentials from `.env`
2. Launch Chromium with proxy authentication
3. Open the file upload page
4. Create a temporary test file
5. Select the file with Playwright
6. Submit the upload form
7. Verify the uploaded filename
8. Automatically remove the temporary file

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
Open Upload Page
          |
          ↓
Create Temporary File
          |
          ↓
set_input_files()
          |
          ↓
Submit Upload
          |
          ↓
Verify Result
          |
          ↓
Remove Temporary File
```

---

## Uploading Files with Playwright

Playwright provides the `locator.set_input_files()` API for file uploads.

Example:

```python
page.locator(
    "#file-upload"
).set_input_files(
    file_path
)
```

The method sets files directly on an `<input type="file">` element without requiring manual interaction with the operating system file picker.

For dynamically created file inputs, Playwright also supports `page.expect_file_chooser()`.

Official documentation:

https://playwright.dev/python/docs/input

---

## Why Use `set_input_files()`?

Using `set_input_files()` is usually simpler than manually opening a file chooser.

For example:

```python
page.locator(
    "#file-upload"
).set_input_files(
    file_path
)
```

For pages where the file input is created dynamically:

```python
with page.expect_file_chooser() as fc_info:
    page.get_by_text("Choose File").click()

file_chooser = fc_info.value
file_chooser.set_files(file_path)
```

Choose the approach that matches the page implementation.

---

## Best Practices

- Keep proxy credentials in environment variables.
- Do not commit `.env` files.
- Use stable locators for file input elements.
- Create temporary test files when an example does not require permanent test assets.
- Remove temporary files after the workflow finishes.
- Verify the upload result instead of assuming the upload succeeded.
- Respect website terms and file upload permissions.

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

### File upload failed

Check:

- The upload page is accessible.
- The proxy credentials are correct.
- The file input selector has not changed.
- The local process has permission to create temporary files.

The current example uses:

```text
#file-upload
```

for the file input on the public test page.

---

### Upload page is unavailable

The example uses a public testing page rather than a production website. If the testing service becomes unavailable or changes its HTML structure, update `UPLOAD_URL` and the corresponding locators in `example.py`.

---

## Related Documentation

- Rapidproxy Documentation:

https://docs.rapidproxy.io/

- Playwright Python Actions:

https://playwright.dev/python/docs/input

- Playwright Python Locator API:

https://playwright.dev/python/docs/api/class-locator

- Playwright File Upload:

https://playwright.dev/python/docs/input#upload-files