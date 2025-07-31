from prometheus_client import start_http_server, Gauge
import psutil
import time

memory_usage = Gauge('memory_usage_percent', 'Memory usage in percent')

def collect_memory_usage():
    while True:
        mem = psutil.virtual_memory().percent
        memory_usage.set(mem)
        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8001)
    collect_memory_usage()