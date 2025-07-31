from prometheus_client import start_http_server, Gauge
import psutil
import time

cpu_usage = Gauge('cpu_usage_percent', 'CPU usage in percent')

def collect_cpu_usage():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        cpu_usage.set(cpu)
        time.sleep(5)

if __name__ == "__main__":
    start_http_server(8000)
    collect_cpu_usage()