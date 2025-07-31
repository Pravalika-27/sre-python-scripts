import requests

url = "https://example.com"
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print("✅ Website is UP")
    else:
        print("⚠️ Website returned:", response.status_code)
except requests.exceptions.RequestException:
    print("❌ Website is DOWN")