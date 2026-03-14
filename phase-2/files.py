servers = ["web-01", "web-02", "db-01","db-02"]

with open("servers.txt","w") as f:
    for server in servers:
        f.write(server + "\n")

print("File written.")

with open("servers.txt", "r") as f:
    for line in f:
        print(f"Found: {line.strip()}")


with open("down.txt", "w") as f:
    for server in servers :
      if "db" in server :
        print(f"Found: {server}")

