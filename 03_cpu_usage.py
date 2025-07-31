import psutil

cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")

if cpu > 85:
    print("⚠️ High CPU usage detected")