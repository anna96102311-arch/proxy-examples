import requests

proxies = {
    "http": "http://USERNAME:PASSWORD@HOST:PORT",
    "https": "http://USERNAME:PASSWORD@HOST:PORT",
}

response = requests.get(
    "https://ipinfo.io/json",
    proxies=proxies,
    timeout=30,
)

print(response.json())