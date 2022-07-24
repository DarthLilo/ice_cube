import json
import bpy
import os
import sys
import shutil
from bpy.props import EnumProperty
from ....ice_cube import print_information


#Custom Functions
from ice_cube import root_folder, dlc_id,dlc_type,dlc_author,bl_info

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
rig_pack_list = []
rig_pack_names = []
RIG_ID = "ice_cube"


internalfiles = os.path.join(root_folder, "ice_cube_data/internal_files/user_packs/rigs")
user_packs = os.path.normpath(internalfiles)

def RefreshRigList():
    items = []
    items = rig_pack_list
    return items
    
bpy.types.Scene.selected_rig_preset = EnumProperty(
        name = "Selected Pack",
        items = [('NONE', 'REFRESH','REFRESH')]
        )

#Classes
class refresh_rigs_list(bpy.types.Operator):
    bl_idname = "refresh.rig_list"
    bl_label = "refresh rig list"
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        #Clearing the old lists
        rig_pack_list.clear()
        rig_pack_names.clear()
        
        #variables
        count = 1

        #Updating the list of installed packs
        for file in getFiles(user_packs):
            description = f"Rig ID: {count}"
            item_descriptor = (file, file, description)
            rig_pack_list.append(item_descriptor)
            rig_pack_names.append(file)
            count += 1
        
        
        #Drawing the custom property
        bpy.types.Scene.selected_rig_preset = EnumProperty(
        name = "Selected Rig",
        items = RefreshRigList()
        )

        try:
            context.scene.selected_rig_preset = rig_pack_names[0]
        except:
            pass

        return{'FINISHED'}


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
        append_preset_func(self, context, properties.global_rig_baked)
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
        if print_information:
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
    """Resets all the rig settings to default!"""
    bl_idname = "reset.settings"
    bl_label = "Update Backups"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        reset_all_settings_func(self,context)
        return{'FINISHED'}

class generate_asset_pack(bpy.types.Operator):
    """Generates an asset pack"""
    bl_idname = "generate.asest_pack"
    bl_label = "Generate Asset Pack"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        obj = context.object
        scene = context.scene
        if obj.get("ipaneltab6") == 0:
            #CHECKING FOR VARS
            if obj.asset_pack_name != "" and obj.entry_name_asset != "" and obj.asset_author != "" and obj.asset_version != "" and os.path.exists(obj.target_thumbnail_generate) == True:
                #folder generation
                inventory = f"{root_folder}/ice_cube_data/internal_files/user_packs/inventory"

                asset_pack_path = f"{inventory}/{obj.asset_pack_name}"

                list_of_dirs_to_gen = ["","assets","thumbnails",f"assets/{obj.entry_name_asset}"]

                for folder in list_of_dirs_to_gen:
                    if os.path.exists(f"{asset_pack_path}/{folder}") is False:
                        os.mkdir(f"{asset_pack_path}/{folder}")

                #settings json generation
                settings_json_data = {
                    "pack_name": obj.asset_pack_name,
                    "author": obj.asset_author,
                    "version": obj.asset_version,
                	"default": obj.entry_name_asset
                }

                #info json generation
                info_json_data = {
                    "asset_name": obj.entry_name_asset,
                    "author": obj.asset_author,
                    "asset_version": obj.asset_version
                }

                converted_settings_json = json.dumps(settings_json_data,indent=4)
                with open(f"{asset_pack_path}/settings.json", "w") as json_file:
                    json_file.write(converted_settings_json)

                converted_info_json = json.dumps(info_json_data,indent=4)
                with open(f"{asset_pack_path}/assets/{obj.entry_name_asset}/info.json", "w") as json_file:
                    json_file.write(converted_info_json)


                #saving a copy of the file
                if bpy.data.is_saved is True and obj.asset_pack_name != "" and obj.entry_name_asset != "":
                    filepath = f"{inventory}/{obj.asset_pack_name}/assets/{obj.entry_name_asset}/{obj.entry_name_asset}.blend"
                    bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)

                #thumbnail management
                if obj.target_thumbnail_generate != "" and str(obj.target_thumbnail_generate).__contains__(".png"): #Copy Thumbnail
                    shutil.copyfile(obj.target_thumbnail_generate,f"{inventory}/{obj.asset_pack_name}/thumbnails/{obj.entry_name_asset}.png")

            elif obj.asset_pack_name == "":
                CustomErrorBox("Please enter a name for the pack!",'Invalid Name','ERROR')
                return{'FINISHED'}
            elif obj.entry_name_asset == "":
                CustomErrorBox("Please enter an asset name!","Invalid Name",'ERROR')
                return{'FINISHED'}
            elif obj.asset_author == "":
                CustomErrorBox("Please enter an author!","Invalid Author",'ERROR')
                return{'FINISHED'}
            elif obj.asset_version == "":
                CustomErrorBox("Please enter a valid version!","Invalid Version",'ERROR')
                return{'FINISHED'}
            elif os.path.exists(obj.target_thumbnail_generate) is False:
                CustomErrorBox("Please select a valid thumbnail!")
                return{'FINISHED'}

        if obj.get("ipaneltab6") == 1:
            #CHECKING FOR VARS
            if obj.asset_pack_name != "" and obj.entry_name_asset != "" and obj.asset_author != "" and obj.asset_version != "":
                
                if obj.has_baked_version is True and os.path.exists(obj.baked_version_filepath) is False:
                    CustomErrorBox("Please enter a valid thumbnail path!",'Invalid Thumbnail','ERROR')
                    return{'FINISHED'}
                
                if os.path.exists(obj.target_thumbnail_generate) is False and obj.generate_thumbnail is False:
                    CustomErrorBox("Invalid Thumbnail Path!",'Invalid Thumbnail','ERROR')
                    return{'FINISHED'}

                #folder generation
                rigs = f"{root_folder}/ice_cube_data/internal_files/user_packs/rigs"

                rig_pack_path = f"{rigs}/{obj.asset_pack_name}"

                list_of_dirs_to_gen = ["","rigs","thumbnails",f"rigs/{obj.entry_name_asset}"]

                for folder in list_of_dirs_to_gen:
                    if os.path.exists(f"{rig_pack_path}/{folder}") is False:
                        os.mkdir(f"{rig_pack_path}/{folder}")

                #settings json generation
                settings_json_data = {
                    "pack_name": obj.asset_pack_name,
                    "author": obj.asset_author,
                    "version": obj.asset_version,
                	"default": obj.entry_name_asset
                }

                #info json generation
                info_json_data = {
                    "rig_name": obj.entry_name_asset,
                	"base_rig": "Ice Cube",
                	"base_rig_vers": f"{bl_info['version']}",
                    "author": obj.asset_author,
                    "rig_version": obj.asset_version,
                	"has_baked": f"{obj.has_baked_version}"
                }

                converted_settings_json = json.dumps(settings_json_data,indent=4)
                with open(f"{rig_pack_path}/settings.json", "w") as json_file:
                    json_file.write(converted_settings_json)

                converted_info_json = json.dumps(info_json_data,indent=4)
                with open(f"{rig_pack_path}/rigs/{obj.entry_name_asset}/info.json", "w") as json_file:
                    json_file.write(converted_info_json)


                #saving a copy of the file
                if bpy.data.is_saved is True:
                    filepath = f"{rigs}/{obj.asset_pack_name}/rigs/{obj.entry_name_asset}/{obj.entry_name_asset}_NORMAL.blend"
                    bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)
                
                if obj.has_baked_version is True:
                    baked_path = f"{rigs}/{obj.asset_pack_name}/rigs/{obj.entry_name_asset}/{obj.entry_name_asset}_BAKED.blend"
                    shutil.copyfile(obj.baked_version_filepath,baked_path)

                #thumbnail management
                if obj.target_thumbnail_generate != "" and str(obj.target_thumbnail_generate).__contains__(".png"): #Copy Thumbnail
                    shutil.copyfile(obj.target_thumbnail_generate,f"{rigs}/{obj.asset_pack_name}/thumbnails/{obj.entry_name_asset}.png")

                #generating thumbnail
                if obj.generate_thumbnail is True:

                    

                    #setting save loc
                    sce = bpy.context.scene.name
                    org_save_loc = bpy.data.scenes[sce].render.filepath
                    bpy.data.scenes[sce].render.filepath = f"{rig_pack_path}/thumbnails/{obj.entry_name_asset}.png"

                    #generating camera
                    camera_data = bpy.data.cameras.new(name='AutoGenCam')
                    camera_object = bpy.data.objects.new('AutoGenCam', camera_data)
                    bpy.context.scene.collection.objects.link(camera_object)

                    #setting camera data
                    auto_cam = bpy.data.objects["AutoGenCam"]
                    auto_cam.location = (3.53542, -7.55179, 2.08197)
                    auto_cam.rotation_euler = (1.5252,-0.0000,0.4321)
                    bpy.data.cameras["AutoGenCam"].lens = 80

                    #setting resolution
                    for scene_thing in bpy.data.scenes:
                        org_trans_setting = scene_thing.render.film_transparent
                        org_res_x = scene_thing.render.resolution_x
                        org_res_y = scene_thing.render.resolution_y
                        scene_thing.render.resolution_x = 1920
                        scene_thing.render.resolution_y = 1920
                        scene_thing.render.film_transparent = True
                        scene_thing.camera = auto_cam
                    
                    #setting view
                    for area in bpy.context.screen.areas:
                        if area.type == 'VIEW_3D':
                            area.spaces[0].region_3d.view_perspective = 'CAMERA'
                            break

                    #disabling overlays
                    bpy.context.space_data.overlay.show_overlays = False

                    #rendering img
                    bpy.ops.render.opengl(write_still=True)

                    #fixing scene

                    bpy.context.space_data.overlay.show_overlays = True

                    bpy.data.objects.remove(auto_cam)
                    bpy.data.cameras.remove(bpy.data.cameras["AutoGenCam"])

                    bpy.data.scenes[sce].render.filepath = org_save_loc

                    for scene_thing in bpy.data.scenes:
                        scene_thing.render.film_transparent = org_trans_setting
                        scene_thing.render.resolution_x = org_res_x
                        scene_thing.render.resolution_y = org_res_y
            elif obj.asset_pack_name == "":
                CustomErrorBox("Please enter a name for the pack!",'Invalid Name','ERROR')
                return{'FINISHED'}
            elif obj.entry_name_asset == "":
                CustomErrorBox("Please enter an asset name!","Invalid Name",'ERROR')
                return{'FINISHED'}
            elif obj.asset_author == "":
                CustomErrorBox("Please enter an author!","Invalid Author",'ERROR')
                return{'FINISHED'}
            elif obj.asset_version == "":
                CustomErrorBox("Please enter a valid version!","Invalid Version",'ERROR')
                return{'FINISHED'}
            elif os.path.exists(obj.target_thumbnail_generate) is False and obj.generate_thumbnail is False:
                CustomErrorBox("Please select a valid thumbnail!")
                return{'FINISHED'}

        return{'FINISHED'}

classes = [
    refresh_rigs_list,
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
    generate_asset_pack,
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()
