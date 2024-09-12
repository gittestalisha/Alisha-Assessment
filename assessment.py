import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0  # CPU usage in percentage
MEMORY_THRESHOLD = 80.0  # Memory usage in percentage
DISK_THRESHOLD = 80.0  # Disk usage in percentage
PROCESS_COUNT_THRESHOLD = 200  # Number of running processes

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High Memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        alert(f"High Disk usage detected: {disk_usage.percent}%")
    return disk_usage.percent

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        alert(f"High number of running processes detected: {process_count}")
    return process_count

def alert(message):
    print(message)
    logging.info(message)

def main():
    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        process_count = check_running_processes()

        # Log the current system health status
        logging.info(f"CPU usage: {cpu_usage}%, Memory usage: {memory_usage}%, Disk usage: {disk_usage}%, Running processes: {process_count}")

        # Sleep for a while before checking again
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()
