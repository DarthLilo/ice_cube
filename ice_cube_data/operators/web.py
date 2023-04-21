from urllib import request
import bpy
import json

from ice_cube import root_folder, github_url,latest_dlc ,dlc_id,dlc_type,dlc_author,dlc_date,dlc_enum_data, bl_info, settings_file, cur_date,valid_dlcs

from ice_cube_data.utils.general_func import IsVersionUpdated, getIndexCustom
from ice_cube_data.utils.file_manage import open_json, ClearDirectoryOfFiles
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.web_tools import ICDownloadImage

import ice_cube



def check_for_updates_func():

        #gets the current version of the addon
        current_version = bl_info['version']

        #Attempts to get the latest version and description of the addon from github, if not, returns NONE
        try:
            repo = json.loads(request.urlopen(github_url).read().decode())
            github_latest_vers = repo['tag_name']
        except:
            github_latest_vers = "NONE"
        
        #Checks the current version of the rig, if none found returns "broken"
        try:
            version = IsVersionUpdated(current_version)
        except:
            version = "broken"

        #Prints the correct message based on the version
        if version == True:
            has_update = False
            CustomErrorBox(f"You're running the latest version of Ice Cube. Version: {current_version}", title="Running Latest Version", icon='CHECKMARK')
            
            with open(settings_file, "r") as jsonFile:
                data = json.load(jsonFile)
            
            data["last_check_date"] = cur_date

            with open(settings_file, "w") as jsonFile:
                json.dump(data, jsonFile,indent=4)

        elif version == False:
            has_update = True
            CustomErrorBox(f"View changelog on Github!", title=f"There is an update available! Version: {github_latest_vers}", icon='IMPORT')
        elif version == "broken":
            has_update = False
            CustomErrorBox("Unable to connect to GitHub, check your internet connection!",title="Connection Error", icon='CANCEL')
        else:
            CustomErrorBox("Unknown Error, contact \"DarthLilo#4103\" on Discord.", title="Unknown Error", icon='ERROR')

        return has_update

def check_for_updates_auto():

    settings_json = open_json(settings_file)
    last_check_date = settings_json['last_check_date']
    
    ice_cube.has_checked_for_updates = True

    if cur_date != last_check_date:
        check_for_updates_func()
        print("Checked For Updates!")
    else:
        print("Waiting 24HR")
        
    

    return{'FINISHED'}

def refresh_dlc_func(self, context):
        #checks github for the latest DLCs
        github_repo = json.loads(request.urlopen(latest_dlc).read().decode())
        dlc_id.clear()
        dlc_type.clear()
        dlc_author.clear()
        dlc_date.clear()
        dlc_enum_data.clear()
        for dlc in github_repo:
            dlc_number = getIndexCustom(str(dlc), github_repo)
            dlc_id.append(github_repo[dlc_number]['dlc_id'])
            dlc_type.append(github_repo[dlc_number]['dlc_type'])
            dlc_author.append(github_repo[dlc_number]['author'])
            dlc_date.append(github_repo[dlc_number]['dlc_date'])
            dlc_enum_data.append(tuple(github_repo[dlc_number]['dlc_enum_data']))

        return{'FINISHED'}

def IC_refresh_dlc(self, context):
    obj = context.object
    cache_folder = root_folder+"/cache/"
    cache_folder2 = root_folder+"/cache"
    github_repo = json.loads(request.urlopen(latest_dlc).read().decode())
    add_dlc_data = obj.ic_dlc_i.clear()

    ClearDirectoryOfFiles(cache_folder2)

    for dlc in github_repo:
        dlc_number = getIndexCustom(str(dlc), github_repo)
        print(dlc_number)
        github_dlc_id = github_repo[dlc_number]['dlc_id']
        github_dlc_label = github_repo[dlc_number]['dlc_name']
        dlc_info_type = github_repo[dlc_number]['dlc_type']
        dlc_upload_date = github_repo[dlc_number]['dlc_date']
        dlc_thumbnail = github_repo[dlc_number]['thumbnail']
        if dlc_info_type == "rigs":
            name_extension_dlc = 'OUTLINER_OB_ARMATURE'
        elif dlc_info_type == "inventory":
            name_extension_dlc = 'OUTLINER_COLLECTION'
        add_dlc_data = obj.ic_dlc_i.add()
        add_dlc_data.name = f"{github_dlc_label}|{name_extension_dlc}|{dlc_upload_date}|{github_dlc_id}"

        ICDownloadImage(dlc_thumbnail,cache_folder,github_dlc_id)

        valid_dlcs[github_dlc_id] = dlc
    


classes = [
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()