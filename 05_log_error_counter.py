error_count = 0

with open("app.log") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1

print(f"Total ERROR lines in log: {error_count}")