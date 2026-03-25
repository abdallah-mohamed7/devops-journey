import os
import sys
db_host = os.environ.get("DB_HOST", "localhost")
db_port = os.environ.get("DB_PORT", "5432")
env = os.environ.get("APP_ENV", "development")
db_pass = os.environ.get("DB_PASSWORD", "")
if db_pass == "":
    print("ERROR: DB_PASSWORD not set")
    sys.exit(1)
print(f"Connecting to {db_host}:{db_port} in {env} mode")
