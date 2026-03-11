import requests

urls = [
    "https://google.com",
    "https://github.com",
    "https://fake-server-123.com"
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        r = response.status_code
        if r !=200 :
         print(f"warning: {url}")
        else :
         print(f"UP: {url} — status {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"DOWN: {url} — connection failed")
    except requests.exceptions.Timeout:
        print(f"TIMEOUT: {url}")


