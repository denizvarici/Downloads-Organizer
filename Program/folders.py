import os
import json
import json_helper
# computer downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

#destination folder for categoriesed files
dest_folder = os.path.expanduser("~/Downloads/İndirilenler Düzenleyicisi")



#make folder for every category
def make_category_folders():
    os.makedirs(dest_folder,exist_ok=True)
    categories = json_helper.load_data_from_json()
    if categories:
        for category in categories:
            os.makedirs(os.path.join(dest_folder,category),exist_ok=True)
    else:
        print("Herhangi bir kategori bulunamadı. downloadsettings.json dosyasını kontrol edin !")

    