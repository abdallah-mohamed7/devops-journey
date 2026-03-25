import requests
import json
import sys
from datetime import datetime
import logging
import argparse


logging.basicConfig(level=logging.ERROR, filename='monitor.log')
logging.getLogger("urllib3").setLevel(logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument("--env", required=True)
parser.add_argument("--timeout", type=int, default=5)
args = parser.parse_args()

env = args.env 

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
    except Exception as e:

        status = "ERROR"
        logging.error(f"Unexpected error for {name}: {e}")

    logging.info(f"{status}: {name} — {url}")
    results.append({"server": name, "url": url, "status": status})

report = {
    "environment": env,
    "timestamp": str(datetime.now()),
    "results": results
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=2)

logging.info(f"Report saved to report.json")

