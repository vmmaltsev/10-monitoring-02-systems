import json
import time
from datetime import datetime
import os

def get_network_connections():
    with open('/proc/net/tcp', 'r') as f:
        return len(f.readlines()) - 1  # Вычитаем одну строку заголовка

def get_cpu_count():
    return os.cpu_count()

def get_swap_size():
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if line.startswith('SwapTotal'):
                return int(line.split()[1])

def collect_metrics():
    timestamp = int(time.time())
    uptime = float(open('/proc/uptime').readline().split()[0])
    load_avg = open('/proc/loadavg').readline().split()[:3]
    memory_total = float(open('/proc/meminfo').readline().split()[1])
    
    network_connections = get_network_connections()
    cpu_count = get_cpu_count()
    swap_size = get_swap_size()

    metrics = {
        "timestamp": timestamp,
        "uptime": uptime,
        "load_avg": load_avg,
        "memory_total_kb": memory_total,
        "network_connections": network_connections,
        "cpu_count": cpu_count,
        "swap_size_kb": swap_size
    }

    log_filename = datetime.now().strftime("/var/log/%Y-%m-%d-awesome-monitoring.log")
    with open(log_filename, "a") as log_file:
        log_file.write(json.dumps(metrics) + "\n")

if __name__ == "__main__":
    collect_metrics()
