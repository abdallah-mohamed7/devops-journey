import requests
import json
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python3 monitor.py <environment>")
    sys.exit(1)

env = sys.argv[1]

urls = {
    "google": "https://google.com",
    "github": "https://github.com"
}

results = []

for name, url in urls.items():
    try:
        response = requests.get(url, timeout=5)
        status = "UP" if response.status_code == 200 else "WARNING"
    except requests.exceptions.ConnectionError:
        status = "DOWN"
    except requests.exceptions.Timeout:
        status = "TIMEOUT"

    results.append({"server": name, "url": url, "status": status})
    print(f"{status}: {name} — {url}")
report = {
    "environment": env,
    "timestamp": str(datetime.now()),
    "results": results
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=2)

print(f"Report saved to report.json")


     
