#This needs to be run in the folder that is being monitored
# Next to dos:
#1: Add logging so i know when something happens
#2: chcek for a specific file type to sort it out
#3: Find if hard drive is connected
#4: If its not connected, put it in temp folders
#5: Run program when connected to move all the files

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
    def on_created(self, event):
        print(f"hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"what the f**k! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"hey buddy, {event.src_path} has been modified")

    def on_moved(self, event):
        print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = MyHandler()
    path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
    my_observer.join()