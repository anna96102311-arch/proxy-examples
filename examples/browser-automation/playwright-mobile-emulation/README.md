# Playwright Mobile Emulation with Residential Proxies

Learn how to emulate an iPhone with Playwright while routing browser traffic through Rapidproxy residential proxies.

---

## What You'll Learn

In this example, you'll learn how to:

- Launch WebKit with Rapidproxy proxy configuration
- Emulate an iPhone 13 device with Playwright
- Use a predefined Playwright device profile
- Navigate to a target webpage
- Verify the emulated viewport, user agent, and touch capability

---

## When Should You Use This Example?

Use this example when you need to:

- Test responsive web pages
- Automate mobile browser workflows
- Validate mobile-specific layouts
- Test websites under different device configurations
- Build browser automation workflows for mobile scenarios

Common use cases include:

- Responsive website testing
- Mobile web automation
- Mobile UI validation
- Cross-device testing
- Browser-based data collection

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

Install WebKit:

```bash
playwright install webkit
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

TARGET_URL=https://playwright.dev/
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
https://playwright.dev/

Mobile device:
iPhone 13

Viewport:
390x664

Touch support:
True

User agent:
Mozilla/5.0 ...

Mobile emulation verified successfully.
```

The exact User-Agent string may vary with the Playwright device definition.

---

## How It Works

The script follows this workflow:

1. Load Rapidproxy credentials from `.env`
2. Launch WebKit with the proxy configuration
3. Load the predefined `iPhone 13` device profile
4. Create a browser context with the device configuration
5. Open the target webpage
6. Read the emulated viewport, User-Agent, and touch capability
7. Verify the mobile environment

Workflow:

```text
Environment Configuration
          |
          ↓
Rapidproxy Proxy Connection
          |
          ↓
Launch WebKit
          |
          ↓
Load iPhone 13 Device Profile
          |
          ↓
Create Mobile Browser Context
          |
          ↓
Open Target Website
          |
          ↓
Verify Mobile Environment
```

---

## Emulating a Mobile Device

Playwright provides predefined device configurations through `playwright.devices`.

Example:

```python
iphone_13 = playwright.devices["iPhone 13"]

context = browser.new_context(
    **iphone_13,
)
```

A device profile can configure properties such as:

- User-Agent
- Viewport
- Screen size
- Device scale factor
- Touch capability
- Mobile behavior

For an iPhone device profile, Playwright's documentation demonstrates using the profile with WebKit.

See the official documentation:

https://playwright.dev/python/docs/emulation

---

## Verifying Mobile Emulation

You can inspect the browser environment with JavaScript:

```python
viewport = page.evaluate(
    "() => ({"
    "width: window.innerWidth,"
    "height: window.innerHeight"
    "})"
)

user_agent = page.evaluate(
    "() => navigator.userAgent"
)

touch_points = page.evaluate(
    "() => navigator.maxTouchPoints"
)
```

This helps verify that the browser context is running with the expected device configuration.

---

## Device Profiles

Playwright provides a registry of predefined device parameters.

For example:

```python
playwright.devices["iPhone 13"]
```

You can use predefined device profiles instead of manually configuring viewport, User-Agent, device scale factor, and touch settings.

This makes device emulation easier to maintain when Playwright updates its device definitions.

---

## Custom Viewport

If you do not need a complete device profile, you can configure a custom viewport:

```python
context = browser.new_context(
    viewport={
        "width": 390,
        "height": 844,
    },
)
```

For complete device emulation, a predefined device profile is usually more convenient because it configures multiple device characteristics together.

---

## Best Practices

- Use Playwright's predefined device profiles when possible.
- Use WebKit for iPhone/Safari-oriented emulation.
- Keep proxy credentials in environment variables.
- Do not commit `.env` files.
- Verify the emulated environment instead of assuming the device configuration was applied.
- Use a consistent device profile when comparing test results.
- Test responsive behavior at multiple viewport sizes when required.
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

### WebKit is missing

Install the Playwright browser:

```bash
playwright install webkit
```

---

### Device profile not found

Make sure the device name matches a device available in your installed Playwright version.

The example uses:

```python
playwright.devices["iPhone 13"]
```

You can inspect available devices with:

```python
print(playwright.devices.keys())
```

---

### Mobile viewport is not what you expected

Check that the device configuration is passed to the browser context:

```python
context = browser.new_context(
    **iphone_13,
)
```

Do not replace the device configuration with only a viewport if you need the complete mobile emulation behavior.

---

## Related Documentation

- Rapidproxy Documentation:

https://docs.rapidproxy.io/

- Playwright Emulation:

https://playwright.dev/python/docs/emulation

- Playwright Browser Context:

https://playwright.dev/python/docs/api/class-browser

- Playwright Devices:

https://playwright.dev/python/docs/api/class-playwright#playwright-devices