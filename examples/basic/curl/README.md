# cURL Example

This example demonstrates how to verify that your Rapidproxy proxy is working using cURL.

## Prerequisites

Before running the command, make sure you have:

- Rapidproxy username
- Rapidproxy password
- Proxy endpoint

## Test Command

```bash
curl -x http://USERNAME:PASSWORD@HOST:PORT https://ipinfo.io/json
```

Replace the placeholder values with your own Rapidproxy credentials.

## Expected Result

If the configuration is correct, you'll receive a JSON response similar to:

```json
{
  "ip": "xxx.xxx.xxx.xxx",
  "city": "...",
  "country": "..."
}
```

## Related Documentation

https://docs.rapidproxy.io/