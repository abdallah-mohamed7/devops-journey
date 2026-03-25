import argparse

parser = argparse.ArgumentParser(description="Server monitor")
parser.add_argument("--env", required=True, help="Environment name")
parser.add_argument("--timeout", type=int, default=5, help="Request timeout")
parser.add_argument("--verbose", action="store_true", help="flag status")
args = parser.parse_args()

print(f"Environment: {args.env}")
print(f"Timeout: {args.timeout}")
print(f"flag: {args.verbose}")
