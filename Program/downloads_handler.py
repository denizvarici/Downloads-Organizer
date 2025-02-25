import os
import time
import shutil
from watchdog.events import FileSystemEventHandler
import folders
import json_helper


def move_file_according_to_extension(file_path,file_name,file_extension):
    try:
        if file_extension in [".tmp",".crdownload"]:
            return
        categories = json_helper.load_data_from_json()
        target_folder = ""
        if categories:
            for category,extension in categories.items():
                if file_extension in extension:
                    target_folder = os.path.join(folders.dest_folder,category)
                    break
        else:
            print("Hiçbir kategori bulunamadı.")
        if target_folder == "":
            print(f"{file_name} öğesine ait bir kategori bulunamadı")
        else:
            shutil.move(file_path,os.path.join(target_folder,file_name))
            print(f"{file_name} -> {target_folder} klasörüne taşındı.")
            target_folder = ""
    except:
        pass
    
    

# downloads folder handler by watchdog
class DownloadsHandler(FileSystemEventHandler):
    # when new file created this event will be executed
    def on_created(self, event):
        if event.is_directory: # if new directory created pass
            return
        # else : show new file created message
        print(f"Yeni bir dosya eklendi : {event.src_path}")

        #take added file informations
        file_path = event.src_path
        file_name = os.path.basename(file_path)
        file_extension = os.path.splitext(file_name)[1].lower()
        
        time.sleep(1)

        move_file_according_to_extension(file_path,file_name,file_extension)
    def on_modified(self, event):
        if event.is_directory: # if new directory created pass
            return
        file_path = event.src_path
        file_name = os.path.basename(file_path)
        file_extension = os.path.splitext(file_name)[1].lower()

        time.sleep(1)
        move_file_according_to_extension(file_path,file_name,file_extension)

