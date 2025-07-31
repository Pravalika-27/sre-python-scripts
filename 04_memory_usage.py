import psutil

mem = psutil.virtual_memory()
print(f"Memory Usage: {mem.percent}%")

if mem.percent > 85:
    print("⚠️ Memory usage is high")