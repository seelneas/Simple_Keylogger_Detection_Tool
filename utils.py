import os
import datetime

LOG_FILE = "detection_log.txt"

def log_detection(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    print(entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
