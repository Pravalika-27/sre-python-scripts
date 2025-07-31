import os

hostname = "google.com"
response = os.system(f"ping -c 1 {hostname}")  # use `-n` for Windows

if response == 0:
    print(f"{hostname} is reachable ✅")
else:
    print(f"{hostname} is not reachable ❌")