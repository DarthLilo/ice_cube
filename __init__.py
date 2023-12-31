import importlib
import sys
import os
import datetime
import bpy
import json


bl_info ={
    "name": "Ice Cube",
    "author": "DarthLilo",
    "version": (1, 6, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Tool",
    "description": "The official python panel for Ice Cube!",
    "tracker_url": "https://discord.gg/3G44QQM",
    "category": "Lilo's Rigs",
}


#File Variables
root_folder = os.path.dirname(os.path.abspath(__file__))
settings_file = f"{root_folder}\\ice_cube_data\\settings.json"
lang_folder = f"{root_folder}\\lang"
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
required_dirsmain = ["backups","downloads","cache","lang"]

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



from ice_cube_data.operators.os_management import generate_settings_json,update_settings_json
from ice_cube_data.utils.file_manage import getFiles, open_json

if not os.path.exists(settings_file):
    generate_settings_json()

languages = []
internal_language_storage = []
authors = open_json(settings_file)['current_language_authors']


for file in getFiles(lang_folder):
    cur_filepath = f"{lang_folder}/{file}"
    
    lang_data = open_json(cur_filepath)

    if lang_data['metadata']:
        languages.append((str(len(languages)),lang_data['metadata']['language_name'],lang_data['metadata']['language_description']))
        internal_language_storage.append(file)


def language_update(self,context):
    selected_language = self.available_languages
    language_file = internal_language_storage[int(selected_language)]
    settings_data = open_json(settings_file)
    global authors
    language_file_data = open_json(f"{root_folder}/lang/{language_file}")
    authors.clear()
    authors = language_file_data['metadata']['authors']
    settings_data['current_language_file'] = language_file
    settings_data['current_language_authors'] = language_file_data['metadata']['authors']

    converted_settings_data = json.dumps(settings_data, indent=4)
    with open(settings_file, "w") as json_file:
        json_file.write(converted_settings_data)



settings_data = open_json(settings_file)



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

    available_languages : bpy.props.EnumProperty(
        name="Available Languages",
        default=0,
        items=languages,
        update=language_update
    )

    def draw(self,context):
        layout = self.layout
        row = layout.row()
        row.prop(self,'automatically_check_for_updates',text='Automatically Check For Updates',icon='URL')
        row.prop(self,'debug_logging',text='Debug Logging',icon='INFO')
        row.prop(self,'easter_eggs',text='',icon='BONE_DATA',expand=True)
        row = layout.row()
        row.prop(self,'available_languages',text='Language',icon='WORLD')
        row = layout.row()
        authors_box = row.box()
        authors_row = authors_box.row(align=True)
        authors_row.label(text="Translators:",icon='BOOKMARKS')
        authors_row = authors_box.row(align=True)
        for author in authors:
            authors_row = authors_box.row(align=True)
            authors_row.label(text=f"       {author}",icon='GREASEPENCIL')

        

#Launch Code

## Generating the settings.json file if it isn't there

def BlenderVersConvertLocal(version, has_v = False):
    new_version = []
    for number in version:
        new_version.append(str(number))

    new_version = ".".join(new_version)

    if has_v is True:
        new_version = f"v{new_version}"




with open(settings_file, "r") as jsonFile:
    settings_data = json.load(jsonFile)
    
    if "settings_version" in settings_data:
        if settings_data["settings_version"] != BlenderVersConvertLocal(bl_info['version'], has_v=False):
            update_settings_json()
    else:
        update_settings_json()


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
