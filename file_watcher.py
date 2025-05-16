from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils import log_detection
import time

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        log_detection(f"File modified: {event.src_path}")

def watch_folder(folder_path):
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    log_detection(f"Watching folder: {folder_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
