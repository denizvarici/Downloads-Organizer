import os
import time
import shutil
from watchdog.events import FileSystemEventHandler
import folders


def move_file_according_to_extension(file_path,file_name,file_extension):
    if file_extension in [".zip",".rar"]:
        target_folder = folders.category_archives_folder
    elif file_extension in [".exe",".msi"]:
        target_folder = folders.category_executables_folder
    elif file_extension in ['.jpg', '.png', '.gif']:
        target_folder = folders.category_pictures_folder
    else:
        print(f"Yeni dosya : {file_name} için taşınabilecek kategori bulunamadı.")
        return
    shutil.move(file_path,os.path.join(target_folder,file_name))
    print(f"{file_name} -> {target_folder} klasörüne taşındı.")
    

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

