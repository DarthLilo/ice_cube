import importlib
import sys
import os
import datetime
import bpy


bl_info ={
    "name": "Ice Cube",
    "author": "DarthLilo",
    "version": (1, 5, 4),
    "blender": (3, 4, 0),
    "location": "View3D > Tool",
    "description": "The official python panel for Ice Cube!",
    "tracker_url": "https://discord.gg/3G44QQM",
    "category": "Lilo's Rigs",
}


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
cur_asset_id = ["ice_cube"]
#Folder Creation
required_dirsmain = ["backups","downloads","cache"]

for dir in required_dirsmain:
    dir_path = os.path.normpath(f"{root_folder}/{dir}")
    if os.path.exists(dir_path):
        pass
    else:
        os.mkdir(dir_path)


required_dirs = ["skins","user_packs", "user_packs/rigs", "user_packs/inventory"]
for dir in required_dirs:
    dir_path = os.path.normpath(f"{root_folder}/ice_cube_data/internal_files/{dir}")
    if os.path.exists(dir_path):
        pass
    else:
        os.mkdir(dir_path)


#Path Appending
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



#Import Files



if "ice_cube_data" in locals():
    importlib.reload(ice_cube_data)
else:
    from . import ice_cube_data

if "main" in locals():
    importlib.reload(main)
else:
    from . import main



from ice_cube_data.operators.os_management import generate_settings_json


class iceCubeAddonPreferneces(bpy.types.AddonPreferences):
    bl_idname = __name__

    easter_eggs: bpy.props.BoolProperty(
        name="easter_eggs",
        default=False
    )

    debug_logging: bpy.props.BoolProperty(
        name="debug_logging",
        description='CURRENTLY DOES NOTHING',
        default=False
    )

    automatically_check_for_updates: bpy.props.BoolProperty(
        name="auto_updates",
        default=True
    )

    def draw(self,context):
        layout = self.layout
        row = layout.row()
        row.prop(self,'automatically_check_for_updates',text='Automatically Check For Updates',icon='URL')
        row.prop(self,'debug_logging',text='Debug Logging',icon='INFO')
        row.prop(self,'easter_eggs',text='',icon='BONE_DATA',expand=True)
        

#Launch Code

## Generating the settings.json file if it isn't there
if not os.path.exists(settings_file):
    generate_settings_json()


classes = [
    iceCubeAddonPreferneces
           ]

def register():
    main.register()
    ice_cube_data.register()
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    main.unregister()
    ice_cube_data.unregister()
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__=="__main__":
    register()
