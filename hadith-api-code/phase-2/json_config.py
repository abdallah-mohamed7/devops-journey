import json

config = {
    "environment": "production",
    "app": "hadith-api",
    "version": "1.0",
    "servers": ["web-01", "web-02"],
    "database": {
        "host": "db-01",
        "port": 5432,
        
    }
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

print("Config written.")

with open("config.json", "r") as f:
    loaded = json.load(f)

print(f"App: {loaded['app']}")
print(f"DB host: {loaded['database']['host']}")
servers=loaded['servers']
for server in servers:
     print(f"server is : {server }")
