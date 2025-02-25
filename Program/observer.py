from watchdog.observers import Observer
from downloads_handler import DownloadsHandler
import time
def start_observe(downloads_folder):
    observer = Observer() #create observer instance
    downloads_handler = DownloadsHandler() #create handler instance
    observer.schedule(event_handler=downloads_handler,path=downloads_folder,recursive=False) #setup observer settings
    observer.start()

    try:
        while True:
            time.sleep(10) #for keeping program open.
    except KeyboardInterrupt:
        observer.stop() #if ctrl+c stop the observer
    observer.join() #wait until the thread terminates