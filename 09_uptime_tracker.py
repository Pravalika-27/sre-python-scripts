import time
import requests

url = "https://example.com"
while True:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(f"{time.ctime()} - UP")
        else:
            print(f"{time.ctime()} - DOWN ({r.status_code})")
    except:
        print(f"{time.ctime()} - DOWN (Exception)")
    time.sleep(60)