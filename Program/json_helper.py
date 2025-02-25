import json
import os
json_file_path = "your/path"

def load_data_from_json():
    if(os.path.exists(json_file_path)):
        with open(json_file_path,"r",encoding="utf-8") as file:
            return json.load(file)
    return {}