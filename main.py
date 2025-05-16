from utils import ensure_directory, log_detection
from file_watcher import watch_folder
from process_monitor import scan_processes
import threading
import time

WATCH_DIR = "suspicious_logs"

def monitor_processes():
    while True:
        flagged = scan_processes()
        if flagged:
            log_detection("Suspicious Processes Detected:")
            for pid, name, cmd in flagged:
                log_detection(f" - PID: {pid}, Name: {name}, Command: {cmd}")
        time.sleep(5)

if __name__ == "__main__":
    ensure_directory(WATCH_DIR)
    
    t1 = threading.Thread(target=watch_folder, args=(WATCH_DIR,))
    t2 = threading.Thread(target=monitor_processes)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
