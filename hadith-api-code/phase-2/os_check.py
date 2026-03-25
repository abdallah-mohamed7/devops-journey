import os

paths = [
    "/home/abdallahm7/devops-journey",
    "/home/abdallahm7/devops-journey/phase-2",
    "/etc/hosts",
    "/fake/path"
]

for path in paths:
    if os.path.exists(path):
        print(f"EXISTS: {path}")
        if os.path.isfile(path):
         print(f"  is file: {path}")
        else:
            print(f"  is dir: {path}")
    else:
        print(f"MISSING: {path}")
