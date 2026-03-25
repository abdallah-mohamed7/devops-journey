import subprocess

commands = ["uptime", "df -h", "free -m","ls ~/devops-journey"]

for cmd in commands:
    print(f"\n--- Running: {cmd} ---")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(f"Exit code: {result.returncode}")
