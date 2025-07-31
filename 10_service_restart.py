import os

service = "nginx"

status = os.system(f"systemctl is-active --quiet {service}")

if status != 0:
    print(f"❌ {service} is down. Restarting...")
    os.system(f"sudo systemctl restart {service}")
else:
    print(f"✅ {service} is running")