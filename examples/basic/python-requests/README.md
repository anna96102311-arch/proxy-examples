# Python Requests Example

This example demonstrates how to use Rapidproxy with the Python `requests` library.

## Requirements

- Python 3.9+
- requests

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Replace the placeholder values with your Rapidproxy credentials:

```python
http://USERNAME:PASSWORD@HOST:PORT
```

Then run:

```bash
python example.py
```

## Expected Output

If the proxy is configured correctly, you'll receive a response similar to:

```json
{
  "ip": "xxx.xxx.xxx.xxx",
  "country": "...",
  "city": "..."
}
```

## Learn More

https://docs.rapidproxy.io/