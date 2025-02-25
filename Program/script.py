import os
import folders
from observer import start_observe

DOWNLOADS_FOLDER = folders.downloads_folder  #downloads folder

folders.make_category_folders() #create category folders if not exists

if __name__ == "__main__":
    print(f"📂 {DOWNLOADS_FOLDER} klasörü değişiklikleri izleniyor...")
    start_observe(DOWNLOADS_FOLDER)
