import sys

if len(sys.argv) < 3:
    print("Usage: python3 args.py <server> <environment>")
    sys.exit(0)

server = sys.argv[1]
env = sys.argv[2]

if env != "production" and  env != "staging" :
  print(f"ERROR: invalid environment")    
else: 
 print(f"Deploying to {server} in {env} environment")
