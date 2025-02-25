import os
# computer downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

#destination folder for categoriesed files
dest_folder = os.path.expanduser("~/Downloads/SortedDownloads")

#categories
category_archives_folder = os.path.join(dest_folder,"Arşivler")
category_pictures_folder = os.path.join(dest_folder,"Resimler")
category_executables_folder = os.path.join(dest_folder,"Executables")

#make folder for every category
def make_category_folders():
    os.makedirs(category_archives_folder,exist_ok=True)
    os.makedirs(category_pictures_folder,exist_ok=True)
    os.makedirs(category_executables_folder,exist_ok=True)