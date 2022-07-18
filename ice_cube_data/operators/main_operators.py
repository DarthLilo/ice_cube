import bpy
import os
import sys
from bpy.props import EnumProperty


#Custom Functions
from ice_cube import root_folder, dlc_id,dlc_type,dlc_author

from ice_cube_data.utils.general_func import GetListIndex, IsVersionUpdated
from ice_cube_data.utils.file_manage import getFiles, ClearDirectory, GetRootFolder
from ice_cube_data.utils.selectors import isRigSelected
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.web_tools import CustomLink

#Operator Functions
from .append import append_preset_func, append_default_rig, append_emotion_line_func
from .parenting import parent_left_arm, parent_right_arm, parent_right_leg, parent_left_leg, parent_body_func, parent_head_func
from .os_management import open_user_packs, install_update_func, create_backup_func, load_backup_func, delete_backup_func, download_dlc_func, export_settings_data, import_settings_data, reset_all_settings_func
from .web import check_for_updates_func, refresh_dlc_func


#Custom Libraries
from ice_cube_data.properties import properties

import ice_cube

#file variables
final_list = []
files_list = []
rig_id = "ice_cube"


internalfiles = os.path.join(root_folder, "ice_cube_data/internal_files/user_packs/rigs")
user_packs = os.path.normpath(internalfiles)
get_test_files = getFiles(user_packs)
count = 0
try:
    for file in get_test_files:
        count += 1
        addition_map = ["rig_", str(count)]
        ID = "".join(addition_map)
        description = "Rig ID Number: " + ID
        test_thing = (ID, file, description)
        final_list.append(test_thing)
        files_list.append(file)
except:
    pass

#Classes
class rig_baked_class(bpy.types.Operator): #A boolean that controls whether to use _NORMAL or _BAKED
    """Changes whether the imported rig is baked or not"""
    bl_idname = "rig.bakedbutton"
    bl_label = "Is the rig baked?"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = context.object

        properties.global_rig_baked = not properties.global_rig_baked
        

        return {'FINISHED'}

class append_preset(bpy.types.Operator):
    """Imports a preset or rig from your library"""
    bl_idname = "append.preset"
    bl_label = "append preset"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        append_preset_func(self, context, files_list, properties.global_rig_baked)
        return{'FINISHED'}


class append_defaultrig(bpy.types.Operator): #Appends the default version of the rig
    """Appends the default rig into your scene"""
    bl_idname = "append.defaultrig"
    bl_label = "Ice Cube [DEFAULT]"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        append_default_rig(self, context)
        return{'FINISHED'}

class parent_leftarm(bpy.types.Operator):
    """Parents anything with the \"_LeftArmChild\" tag to the left arm"""
    bl_idname = "parent.leftarm"
    bl_label = "parent left arm"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_left_arm(self, context)
        return{'FINISHED'}

class parent_rightarm(bpy.types.Operator):
    """Parents anything with the \"_RightArmChild\" tag to the right arm"""
    bl_idname = "parent.rightarm"
    bl_label = "parent right arm"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_right_arm(self, context)
        return{'FINISHED'}

class parent_rightleg(bpy.types.Operator):
    """Parents anything with the \"_RightLegChild\" tag to the right leg"""
    bl_idname = "parent.rightleg"
    bl_label = "parent right leg"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_right_leg(self, context)
        return{'FINISHED'}
    
class parent_leftleg(bpy.types.Operator):
    """Parents anything with the \"_LeftLegChild\" tag to the left leg"""
    bl_idname = "parent.leftleg"
    bl_label = "parent left leg"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_left_leg(self, context)
        return{'FINISHED'}
        
class parent_body(bpy.types.Operator):
    """Parents anything with the \"_BodyChild\" tag to the body"""
    bl_idname = "parent.body"
    bl_label = "parent body"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_body_func(self, context)
        return{'FINISHED'}

class parent_head(bpy.types.Operator):
    """Parents anything with the \"_HeadChild\" tag to the head"""
    bl_idname = "parent.head"
    bl_label = "parent head"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        parent_head_func(self, context)
        return{'FINISHED'}
    
class lilocredits(bpy.types.Operator):
    """Opens a link to my credits page"""
    bl_idname = "lilocredits.link"
    bl_label = "About the Creator"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        CustomLink("https://darthlilo.carrd.co/")
        
        return {'FINISHED'}

class discord_link(bpy.types.Operator):
    """Opens a link to my Discord server"""
    bl_idname = "discordserver.link"
    bl_label = "Join the Discord!"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        CustomLink("https://discord.gg/3G44QQM")
        
        return {'FINISHED'}

class download_template_1(bpy.types.Operator):
    """Downloads an asset template pack from my discord server"""
    bl_idname = "template1.download"
    bl_label = "Download Asset Pack Template"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        CustomLink("https://cdn.discordapp.com/attachments/978737749995683851/978737884897107968/template_asset_pack.zip")
        
        return {'FINISHED'}

class download_template_2(bpy.types.Operator):
    """Downloads a rig template pack from my discord server"""
    bl_idname = "template2.download"
    bl_label = "Download Rig Pack Template"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        CustomLink("https://cdn.discordapp.com/attachments/978737749995683851/978744989691555850/template_rig_pack.zip")
        
        return {'FINISHED'}

class open_wiki(bpy.types.Operator):
    """Opens the Ice Cube wiki"""
    bl_idname = "wiki.open"
    bl_label = "Ice Cube Wiki"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        CustomLink("https://darthlilo.gitbook.io/ice-cube/")
        
        return{'FINISHED'}

class open_custom_presets(bpy.types.Operator):
    """Opens the DLC folder"""
    bl_idname = "custom_presets.open"
    bl_label = "Open DLC Folder"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        open_user_packs(self, context)
        return{'FINISHED'}

class append_emotion_line(bpy.types.Operator):
    """Appends an emotion line to the rig"""
    bl_idname = "append.emotion"
    bl_label = "Append Emotion Line"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        append_emotion_line_func(self, context)
        return{'FINISHED'}

class check_for_updates(bpy.types.Operator):
    """Checks the Ice Cube GitHub for updates"""
    bl_idname = "check.updates"
    bl_label = "Check for updates"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ice_cube.update_available = check_for_updates_func(self, context)
        return{'FINISHED'}

class install_update(bpy.types.Operator):
    """Installs the latest version from GitHub"""
    bl_idname = "install.update"
    bl_label = "Install the latest update"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        install_update_func(self, context)
        return{'FINISHED'}

class open_update_page(bpy.types.Operator):
    """Opens the Ice Cube website"""
    bl_idname = "open.update"
    bl_label = "Open Ice Cube Website"
    bl_options = {'REGISTER', 'UNDO'}



    def execute(self, context):
        CustomLink("https://ice-cube-beta.carrd.co/")
        properties.update_available = False
        return{'FINISHED'}

class create_backup(bpy.types.Operator):
    """Creates a backup of the currently installed version"""
    bl_idname = "create.backup"
    bl_label = "Load Backup"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        create_backup_func(self, context)
        return{'FINISHED'}

class load_backup(bpy.types.Operator):
    """Loads the selected backup from your backups folder"""
    bl_idname = "load.backup"
    bl_label = "Append Emotion Line"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        load_backup_func(self, context)
        return{'FINISHED'}
    
class delete_backup(bpy.types.Operator):
    """Deletes the selected backup"""
    bl_idname = "delete.backup"
    bl_label = "Delete Backup"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        delete_backup_func(self, context)
        return{'FINISHED'}



class refresh_dlc(bpy.types.Operator):
    """Checks the Ice Cube GitHub for new DLC"""
    bl_idname = "refresh.dlc"
    bl_label = "Delete Backup"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        refresh_dlc_func(self, context)

        print(f"DLC IDs : {dlc_id}\nDLC TYPE : {dlc_type}\nDLC AUTHOR : {dlc_author}")
        downloads_path = f"{root_folder}/ice_cube_data/ui/advanced/downloads.py"
        exec(open(downloads_path).read())
        
        return{'FINISHED'}

class download_dlc(bpy.types.Operator):
    """Downloads the selected DLC from GitHub"""
    bl_idname = "download.dlc"
    bl_label = "Download DLC"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        download_dlc_func(self, context, dlc_id)
        return{'FINISHED'}


class export_settings_data_class(bpy.types.Operator):
    """Exports the current rig settings"""
    bl_idname = "export.settings"
    bl_label = "Export Settings"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        export_settings_data(self, context)
        return{'FINISHED'}

class import_settings_data_class(bpy.types.Operator):
    """Imports rig settings from the clipboard or a file"""
    bl_idname = "import.settings"
    bl_label = "Export Settings"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        import_settings_data(self, context)
        return{'FINISHED'}

class update_backups_list(bpy.types.Operator):
    """Updates the list of current backups!"""
    bl_idname = "update.backups"
    bl_label = "Update Backups"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        downloads_path = f"{root_folder}/ice_cube_data/ui/advanced/downloads.py"
        exec(open(downloads_path).read())
        return{'FINISHED'}

class reset_all_settings(bpy.types.Operator):
    """Updates the list of current backups!"""
    bl_idname = "reset.settings"
    bl_label = "Update Backups"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        reset_all_settings_func(self,context)
        return{'FINISHED'}


try:
    bpy.types.Scene.selected_asset = EnumProperty(
        name = "Selected Pack",
        default = 'rig_1',
        items = final_list
    )
except:
    bpy.types.Scene.selected_asset = EnumProperty(
        name = "Selected Pack",
        default = 'rig_1',
        items = [('rig_1', "NO PACKS FOUND", 'Please install or create an asset pack!')]
    )


classes = [
    rig_baked_class,
    append_preset,
    append_defaultrig,
    parent_leftarm,
    parent_rightarm,
    parent_rightleg,
    parent_leftleg,
    parent_body,
    parent_head,
    lilocredits,
    discord_link,
    download_template_1,
    download_template_2,
    open_wiki,
    open_custom_presets,
    append_emotion_line,
    check_for_updates,
    install_update,
    open_update_page,
    create_backup,
    load_backup,
    delete_backup,
    refresh_dlc,
    download_dlc,
    export_settings_data_class,
    import_settings_data_class,
    update_backups_list,
    reset_all_settings,
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()