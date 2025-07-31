import shutil

total, used, free = shutil.disk_usage("/")
used_percent = (used / total) * 100
print(f"Disk used: {used_percent:.2f}%")

if used_percent > 80:
    print("⚠️ Warning: High disk usage!")