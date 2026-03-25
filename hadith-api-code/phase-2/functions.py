def check_server(name, status):
    if status == "down":
        print(f"ALERT: {name} is down!")
    elif status == "maintenance" :
        print(f"ALERT: {name} is warning")
    else :
        print(f"ok: {name} is running")

servers = {
    "web-01": "up",
    "web-02": "down",
    "db-01": "up",
    "db-02": "maintenance"
}

for name, status in servers.items():
    check_server(name, status)
