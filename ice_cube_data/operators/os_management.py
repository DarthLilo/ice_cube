import os
import subprocess
import bpy
from sys import platform
import json
from urllib import request
import zipfile
import shutil
import distutils.dir_util
import datetime
import pathlib

from ice_cube import root_folder, latest_dlc, github_url

from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.file_manage import ClearDirectory, getFiles, open_json
from ice_cube_data.utils.general_func import GetListIndex, getIndexCustom

properties_to_export = ["r_arm_ik","l_arm_ik","r_leg_ik","l_leg_ik","ankle_r","ankle_l","stretch_leg_r","stretch_leg_l","stretch_arm_r","stretch_arm_l","fingers_r","fingers_l","wrist_lock_r","wrist_lock_l","eyelashes","wireframe","jaw","round_jaw","bevelmouth","teeth_cartoon","antilag","teeth_bool","tongue","facerig",
    "leg_deform","body_deforms","dynamichair","eyebrowdeform","togglepupil","togglegradient","togglesparkle1","togglesparkle2","toggleemission","toggle_1","toggle_2","squaremouth","mouthrotate","toggle_3","toggle_4","breastswitch","line_mouth","baked_rig","global_head_rotation","squish_arm_r","squish_arm_l","squish_leg_r",
    "squish_leg_l","squish_body","squish_head","breastshape","jaw_strength","bevelmouthstrength","leg_taper_strength","hip","upperbodywidth","lowerbodywidth","bulge_arm_r","bulge_arm_l","bulge_leg_r","bulge_leg_l","eyebrowheight","eyebrowtaper1","eyebrowtaper2","leg_taper_strength2","armtaper","bodybulge","eyedepth","mouthdepth",
    "innermouthdepth","breastsize","breastweight","bodytopround","breath","armtype_enum","bendstyle","arm_ik_parent_r","arm_ik_parent_l"]

backup_dates = {}

def open_user_packs(self, context):
    #addon location
    #opens a popup if you're using windows
    if platform == "win32":
        asset_directory_win = root_folder+"\\ice_cube_data\\internal_files\\user_packs"
        subprocess.Popen(fr'explorer "{asset_directory_win}"')
    #opens a popup if you're using mac os
    elif platform == "darwin":
        asset_directory_mac = root_folder+"/ice_cube_data/internal_files/user_packs/"
        subprocess.call(["open", "-R", asset_directory_mac])
    #opens a popup if you're using linux
    elif platform == "linux" or platform == "linux2":
        asset_directory_linux = root_folder+"/ice_cube_data/internal_files/user_packs/"
        subprocess.Popen(['xdg-open', asset_directory_linux])
    else:
        CustomErrorBox(message="Please contact \"DarthLilo#4103\" on discord for help.", title="Unknown Operating System", icon='ERROR')

    return{'FINISHED'}

def install_update_func(self, context):
    #sets up variables
    install_loc = root_folder+""
    downloads_folder = root_folder+"/downloads"
    backups_folders = root_folder+"/backups"
    can_backup = False
    #checks if the downloads folder exists, if not, create one.
    if os.path.exists(downloads_folder):
        print("Path Found")
    else:
        os.mkdir(downloads_folder)
        print("Created Downloads Folder")

    download_folder = os.path.normpath(downloads_folder)
    backups_folders = os.path.normpath(backups_folders)

    #checking if there's an up to date backup
    backups_list = {}
    for file in getFiles(backups_folders):
        creation_date = pathlib.Path(f"{backups_folders}/{file}").stat().st_mtime
        creation_date = "".join(str(datetime.datetime.fromtimestamp(creation_date)).split(" ")[0].split("-"))
        backups_list[file] = creation_date
    
    cur_time = "".join(str(datetime.datetime.now()).split(" ")[0].split("-"))
    
    for entry in backups_list:
        if backups_list[entry] == cur_time:
            can_backup = True
            break
    
    if can_backup == False:
        CustomErrorBox("Please create an up-to-date backup before updating!","No updated backup found!","ERROR")
        return{'FINISHED'}
    

    #clear folder
    ClearDirectory(download_folder)

    download_file_loc = str(download_folder+"/latest_release.zip")

    github_repo = json.loads(request.urlopen(github_url).read().decode())
    github_zip = github_repo['zipball_url']

    #download the zip
    try:
        request.urlretrieve(github_zip, download_file_loc)
        print("File Downloaded!")
    except Exception as e:
        CustomErrorBox(str(e), "Error while downloading update.", icon="CANCEL")
        print("Error while downloading file.")
    #unzips the file
    try:
        print(f"Unzipping File")
        with zipfile.ZipFile(download_file_loc, 'r') as zip_ref:
            zip_ref.extractall(download_folder)
        print("Successfully Unzipped File!")
        #removes the zip
        os.remove(download_file_loc)
        #if there's an old Ice Cube, remove it
        try:
            shutil.rmtree(download_folder+"/Ice Cube")
        except:
            pass
        print("Cleaned Folder")
    except Exception as e:
        CustomErrorBox(str(e), "Error unpacking update file.", icon="CANCEL")
        print("Unknown Error")
    #Rename the downloaded file to Ice Cube
    for file in getFiles(download_folder):
        filepath = str(f"{download_folder}/{file}")
        renamed_file = str(f"{download_folder}/Ice Cube")
        os.rename(filepath, renamed_file)
    
    #Install the downloaded addon
    try:
        distutils.dir_util.copy_tree(download_folder+"/Ice Cube", install_loc)
        print("Finished Install!")
        CustomErrorBox("Finished installing update! Restart Blender before continuing!","Updated Finished",'INFO')
    except Exception as e:
        print("Error Completing Install.")
        CustomErrorBox(str(e),"Error installing update file.",'ERROR')

    return{'FINISHED'}

def create_backup_func(self, context):
    #sets up variables
    obj = context.object
    virtual_ice_cube = root_folder+""
    virtual_ice_cube = os.path.normpath(virtual_ice_cube)
    backups_folder = root_folder+"/backups"

    files = []
    files_nopath = []
    folders = []
    folders_nopath = []

    backup_name = obj.backup_name

    #check for a folder in the backups folder with the name entered, if none, create it.
    if obj.get("backup_name"):
        if obj.get("backup_name") == "":
            backups_folder = os.path.dirname(backups_folder)+"/backups/main"
            if os.path.exists(backups_folder) is False:
                os.mkdir(backups_folder)
        else:
            backups_folder = os.path.dirname(backups_folder)+"/backups/"+backup_name
            if os.path.exists(backups_folder) is False:
                os.mkdir(backups_folder)
    else:
        backups_folder = os.path.dirname(backups_folder)+"/backups/main"
        if os.path.exists(backups_folder):
            pass
        else:
            os.mkdir(backups_folder)
    
    #list of files to backup
    files_to_backup = ["__init__.py","main.py"]
    for file in files_to_backup:
        file_w_path = os.path.normpath(f"{root_folder}/{file}")
        files.append(file_w_path)
        files_nopath.append(file)
    

    #list of folders to backup
    folders_to_backup = ["ice_cube_data"]
    for folder in folders_to_backup:
        folder_w_path = os.path.normpath(f"{root_folder}/{folder}")
        folders.append(folder_w_path)
        folders_nopath.append(folder)




    print(files_nopath)
    print(folders_nopath)

    print(files)
    print(folders)

    #Actual Backing Up
    try:
        for file in files_nopath:
            file_nopy = file.split(".")[0]
            shutil.copy(f"{virtual_ice_cube}/{file}", f"{backups_folder}/{files_nopath[GetListIndex(file_nopy, files_nopath)]}")

        for folder in folders_nopath:
            try:
                os.mkdir(f"{backups_folder}/{folders_nopath[GetListIndex(folder, folders_nopath)]}")
            except:
                pass
            
        for folder in folders_nopath:
            distutils.dir_util.copy_tree(f"{virtual_ice_cube}/{folder}", f"{backups_folder}/{folder}")
        if obj.get("backup_name"):
            if obj.get("backup_name") == "":
                backup_name = "main"
            else:
                pass
        else:
            backup_name = "main"
        CustomErrorBox(f"Created Backup: [{backup_name}]", "Created Backup", 'INFO')
    except:
        CustomErrorBox(f"An Error Has Occured: [{backup_name}]", "Unknown Error", 'ERROR')
    
    refresh_backups_func(self,context)

    return{'FINISHED'}

def refresh_backups_func(self, context):

    obj = context.object
    virtual_ice_cube = root_folder+""
    virtual_ice_cube = os.path.normpath(virtual_ice_cube)
    backups_folder = root_folder+"/backups"
    backup_folder_scan = os.listdir(backups_folder)

    #test = obj.ic_backups_i.add()

    obj.ic_backups_i.clear()

    for backup in backup_folder_scan:
        try:
            add_backup = obj.ic_backups_i.add()
            add_backup.name = backup
            creation_date = pathlib.Path(f"{backups_folder}/{backup}").stat().st_mtime
            creation_date = str(datetime.datetime.fromtimestamp(creation_date)).split(" ")[0]
            backup_dates[backup] = creation_date
        except:
            pass


def load_backup_func(self, context):
    #set up the variables
    obj = context.object
    backup_storage = obj.ic_backups_i
    backup_index = obj.ic_backups_active_index
    backup_list = []
    virtual_ice_cube = root_folder+""
    for i in backup_storage:
        backup_list.append(i.name)
    selected_backup = backup_list[backup_index]
    backup_loc = root_folder+"/backups/"+selected_backup
    
    #loading backup folder

    if os.path.exists(backup_loc):
        print(selected_backup)
        distutils.dir_util.copy_tree(backup_loc, virtual_ice_cube)
        CustomErrorBox(f"Loaded Backup: [{selected_backup}], restart Blender for changes!", "Loaded Backup", 'INFO')
    else:
        CustomErrorBox("INVALID BACKUP","Selection Error",'ERROR')


    return{'FINISHED'}

def delete_backup_func(self, context):
        #set up variables
        obj = context.object
        virtual_ice_cube = root_folder+""
        virtual_ice_cube = os.path.normpath(virtual_ice_cube)
        backups_folder = root_folder+"/backups"
        backup_storage = obj.ic_backups_i
        backup_index = obj.ic_backups_active_index
        backup_list = []
        for i in backup_storage:
            backup_list.append(i.name)
        try:
            selected_backup = backup_list[backup_index]
        except:
            CustomErrorBox("No backup found!","Invalid Backup",'ERROR')
            return{'FINISHED'}

        #check if you've entered a name, if not, give a prompt, if so, delete the entered name if a backup exists for it
        backup_to_remove = os.path.dirname(backups_folder)+"/backups/"+selected_backup
        if os.path.exists(backup_to_remove) and backup_to_remove != backups_folder and backup_to_remove != backups_folder+"/":
            shutil.rmtree(backup_to_remove)
            CustomErrorBox(f"Deleted Backup: [{selected_backup}]", "Deleted Backup", 'INFO')
        else:
            CustomErrorBox("No backup found!","Invalid Backup",'ERROR')

        refresh_backups_func(self,context)

        return{'FINISHED'}


def IC_download_dlc(self, context, valid_dlcs):
    obj = context.object

    dlc_storage = obj.ic_dlc_i
    dlc_index = obj.ic_dlc_active_index
    dlc_data_list = []
    try:
        for i in dlc_storage:
            dlc_data_list.append(str(i.name).split("|")[3])
        selected_dlc = dlc_data_list[dlc_index]
        cur_dlc_data = valid_dlcs[selected_dlc]

        dlc_type = cur_dlc_data['dlc_type']
        dlc_id_name = cur_dlc_data['dlc_id']
        dlc_download = cur_dlc_data['download_link']


        downloads_folder = root_folder+"/downloads"
        dlc_folder = root_folder+"/ice_cube_data/internal_files/user_packs/"+dlc_type+"/"+dlc_id_name

        #checks if a folder for the selected dlc exists, if not, create one.
        if os.path.exists(dlc_folder):
            print("Path Found")
        else:
            os.mkdir(dlc_folder)
            print(f"Created {dlc_id_name} Folder")
        download_folder = os.path.normpath(downloads_folder)
        #clear folder
        ClearDirectory(download_folder)

        download_file_loc = str(download_folder+"/dlc.zip")

        #download the zip
        try:
            request.urlretrieve(dlc_download, download_file_loc)
            print("File Downloaded!")
        except:
            CustomErrorBox("An unknown error has occured, canceled download.","Downloading Error","ERROR")
        #unzips the file
        try:
            print(f"Unzipping File")
            try:
                shutil.rmtree(download_folder+"/"+dlc_id_name)
            except:
                pass
            with zipfile.ZipFile(download_file_loc, 'r') as zip_ref:
                zip_ref.extractall(download_folder)
            print("Successfully Unzipped File!")
            #remove the zip file when done
            os.remove(download_file_loc)
            print("Cleaned Folder")
        except:
            print("Unknown Error")

        try:
            #install the new DLC
            distutils.dir_util.copy_tree(download_folder+"/"+dlc_id_name, dlc_folder)
            print("Finished Install!")
            CustomErrorBox("Finished installing DLC!","Updated Finished",'INFO')
        except:
            print("Error Completing Install.")
            CustomErrorBox("Error Completing Install.","Updated Cancelled",'ERROR')
    except:
            CustomErrorBox("Invalid DLC","Selection Error",'ERROR')
    
    return{'FINISHED'}



def export_settings_data(self, context):

    obj = context.object
    wm = bpy.context.window_manager

    
    filepath = obj.export_settings_filepath
    filename = obj.export_settings_name

    if obj.get("prop_clipboard") == True:
        json_name = filename
    else:
        json_name = "default"

    json_data = {
        "name" : json_name,
        "prop_data" : {}
    }

    for prop in properties_to_export:
        try:
            json_data["prop_data"][prop] = getattr(obj, prop)
        except:
            pass
    converted_json_data = json.dumps(json_data,indent=4)

    if obj.get("prop_clipboard") == True:
        wm.clipboard = f"{converted_json_data}"
    elif obj.get("prop_clipboard") == False:
        if filepath == "":
            CustomErrorBox("Please select a valid filepath!","Invalid File Path",'ERROR')
            return{'FINISHED'}
        if filename == "":
            CustomErrorBox("Please enter a valid filename!","Invalid File Name",'ERROR')
            return{'FINISHED'}
        with open(f"{filepath}/{filename}.ice_cube_data", "w") as json_file:
            json_file.write(converted_json_data)

    return{'FINISHED'}

def import_settings_data(self, context):
    obj = context.object
    wm = bpy.context.window_manager
    filepath = obj.import_settings_filepath

    if obj.get("prop_clipboard") == True:
        settings_json_data = ""
        settings_name = ""
        prop_data = ""
        try:
            settings_json_data = json.loads(wm.clipboard)
        except:
            CustomErrorBox("Please export the settings data before attempting an import!","Invalid Clipboard Data!",'ERROR')
            return{'FINISHED'}
        try:
            settings_name = settings_json_data['name']
            prop_data = settings_json_data['prop_data']
        except:
            CustomErrorBox("Please export the settings data before attempting an import!","Invalid Clipboard Data!",'ERROR')
            return{'FINISHED'}
        
        for prop in prop_data:
            try:
                setattr(obj, prop, prop_data[prop])
            except:
                pass
        CustomErrorBox("Successfully loaded settings data from clipboard!\nInteract with the scene to update!","Imported Settings",'INFO')
    
    elif obj.get("prop_clipboard") == False:
        settings_json_data = ""
        settings_name = ""
        prop_data = ""

        try:
            settings_json_data = open_json(filepath)
        except:
            CustomErrorBox("Please select a valid settings file!","Invalid File!",'ERROR')
            return{'FINISHED'}
        
        prop_data = settings_json_data['prop_data']

        for prop in prop_data:
            try:
                setattr(obj, prop, prop_data[prop])
                print(f"{prop} == {prop_data[prop]}")
            except:
                pass
        CustomErrorBox(f"Successfully loaded settings data from file [{settings_json_data['name']}.ice_cube_data]!\nInteract with the scene to update!","Imported Settings",'INFO')
        

    return{'FINISHED'}

def reset_all_settings_func(self, context):
    obj = context.object

    settings_json_data = ""
    settings_name = ""
    prop_data = ""

    settings_json_data = open_json(f"{root_folder}/ice_cube_data/internal_files/default_settings.ice_cube_data")
    
    prop_data = settings_json_data['prop_data']

    for prop in prop_data:
        try:
            setattr(obj, prop, prop_data[prop])
            print(f"{prop} == {prop_data[prop]}")
        except:
            pass
    CustomErrorBox(f"Successfully reset settings data!\nInteract with the scene to update!","Imported Settings",'INFO')
        

    return{'FINISHED'}

def generate_settings_json():

    settings_json_path = f"{root_folder}\\ice_cube_data\\settings.json"

    settings_json_data = {
        "last_check_date" : ""
    }

    converted_settings_data = json.dumps(settings_json_data, indent=4)

    
    with open(settings_json_path, "w") as json_file:
        json_file.write(converted_settings_data)
    

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