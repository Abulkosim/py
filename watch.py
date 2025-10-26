#!/usr/bin/env python3
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def __init__(self, target):
        self.target = target
        
    def on_modified(self, event):
        if event.src_path.endswith(self.target):
            result = subprocess.run(['python3', self.target], 
                                  text=True)
            
def main():
    target = 'refresher.py'
    
    handler = Handler(target)
    observer = Observer()
    observer.schedule(handler, '.', recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
