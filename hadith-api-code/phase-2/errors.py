
with open("status.txt", "w") as f:
          f.write("web-01: up\nweb-02: down\n")


try:
        with open("status.txt", "r") as f:
            print(f.read())
except FileNotFoundError:
         print("ERROR: status.txt not found")
except Exception as e:
    print(f"Unexpected error: {e}")
