from urllib import request
import bpy
import json

from ice_cube import root_folder, github_url,latest_dlc ,dlc_id,dlc_type,dlc_author,dlc_date,dlc_enum_data, bl_info

from ice_cube_data.utils.general_func import IsVersionUpdated, getIndexCustom
from ice_cube_data.utils.ui_tools import CustomErrorBox



def check_for_updates_func(self, context):

        #gets the current version of the addon
        current_version = bl_info['version']

        #Attempts to get the latest version and description of the addon from github, if not, returns NONE
        try:
            repo = json.loads(request.urlopen(github_url).read().decode())
            github_latest_vers = repo['tag_name']
            github_changes = repo['body']
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
        elif version == False:
            has_update = True
            CustomErrorBox(f"Changes:\n{github_changes}", title=f"There is an update available! Version: {github_latest_vers}", icon='IMPORT')
        elif version == "broken":
            has_update = False
            CustomErrorBox("Unable to connect to GitHub API, check your internet connection!",title="Connection Error", icon='CANCEL')
        else:
            CustomErrorBox("Unknown Error, contact \"DarthLilo#4103\" on Discord.", title="Unknown Error", icon='ERROR')
        

        return has_update




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