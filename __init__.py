bl_info ={
    "name": "Ice Cube",
    "author": "DarhtLilo",
    "version": (1, 4, 8),
    "blender": (3, 4, 0),
    "location": "View3D > Tool",
    "description": "The official python panel for Ice Cube!",
    "tracker_url": "https://discord.gg/3G44QQM",
    "category": "Lilo's Rigs",
}

import bpy
import importlib
import sys
import os
import json
import datetime
import time

#File Variables
root_folder = os.path.dirname(os.path.abspath(__file__))
settings_file = f"{root_folder}\\ice_cube_data\\settings.json"
github_url = "https://api.github.com/repos/DarthLilo/ice_cube/releases/latest"
latest_dlc = "https://raw.githubusercontent.com/DarthLilo/ice_cube/master/ice_cube_data/dlc_list.json"
dlc_id = []
dlc_type = []
dlc_author = []
dlc_date = []
dlc_enum_data = []
valid_dlcs = {}
update_available = False
get_time = datetime.datetime.now()
cur_date = f"{get_time.year}-{get_time.month}-{get_time.day}"
has_checked_for_updates = False

#Folder Creation
required_dirsmain = ["backups","downloads","cache"]

for dir in required_dirsmain:
    dir_path = os.path.normpath(f"{root_folder}/{dir}")
    if os.path.exists(dir_path):
        print(f"Found path {dir_path}")
    else:
        os.mkdir(dir_path)
        print(f"Made directory {dir_path}")


required_dirs = ["skins","user_packs", "user_packs/rigs", "user_packs/inventory"]
for dir in required_dirs:
    dir_path = os.path.normpath(f"{root_folder}/ice_cube_data/internal_files/{dir}")
    if os.path.exists(dir_path):
        print(f"Found path {dir_path}")
    else:
        os.mkdir(dir_path)
        print(f"Made directory {dir_path}")


#Path Appending
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



#Import Files
from . import main
from . import ice_cube_data
from ice_cube_data.operators.os_management import generate_settings_json

#Launch Code

## Generating the settings.json file if it isn't there
if not os.path.exists(settings_file):
    generate_settings_json()


#Reload
importlib.reload(main)
importlib.reload(ice_cube_data)


def register():
    main.register()
    ice_cube_data.register()

def unregister():
    main.unregister()
    ice_cube_data.unregister()
