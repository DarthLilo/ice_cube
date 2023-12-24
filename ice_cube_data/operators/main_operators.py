import json
import bpy
import os
import shutil
from bpy.props import EnumProperty
from bpy_extras.io_utils import ImportHelper
import datetime
import random
import zipfile
import distutils
from mathutils import Vector, Quaternion, Matrix, Euler
import math

#Custom Functions
from ice_cube import root_folder, dlc_id,dlc_type,dlc_author,bl_info,valid_dlcs,settings_file

from ice_cube_data.utils.general_func import BlenderVersConvert, IC_FKIK_Switch, bakeIceCube, badToTheBone, convertStringNumbers, setRestPose, resetRestPose, getLanguageTranslation
from ice_cube_data.utils.file_manage import getFiles, open_json
from ice_cube_data.utils.ui_tools import CustomErrorBox
from ice_cube_data.utils.web_tools import CustomLink, ICDownloadImage
from ice_cube_data.utils.selectors import isRigSelected, mat_holder_func, eye_mesh
from ice_cube_data.operators import web

from . import os_management

#Operator Functions
from .append import append_preset_func, append_default_rig, append_emotion_line_func
from .parenting import parent_left_arm, parent_right_arm, parent_right_leg, parent_left_leg, parent_body_func, parent_head_func
from .os_management import open_user_packs, install_update_func, create_backup_func, refresh_backups_func, load_backup_func, delete_backup_func, export_settings_data, import_settings_data, reset_all_settings_func, IC_download_dlc, reset_all_ui_func, compressDirectory
from .web import check_for_updates_func, refresh_dlc_func, IC_refresh_dlc


#Custom Libraries
from ice_cube_data.properties import properties

import ice_cube

#reload

#file variables
rig_pack_list = []
rig_pack_names = []
rig_id = "ice_cube"
cur_blender_version = convertStringNumbers(list(bpy.app.version))

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
        easter_eggs = bpy.context.preferences.addons["ice_cube"].preferences.easter_eggs

        if easter_eggs:
            ran = random.randint(1,50)
            if ran == 1:
                badToTheBone()
        return{'FINISHED'}

class append_defaultrig(bpy.types.Operator): #Appends the default version of the rig
    """Appends the default rig into your scene"""
    bl_idname = "append.defaultrig"
    bl_label = "Ice Cube "+getLanguageTranslation("ice_cube.ops.append_default_rig")
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        append_default_rig(self, context)
        easter_eggs = bpy.context.preferences.addons["ice_cube"].preferences.easter_eggs

        if easter_eggs:
            ran = random.randint(1,50)
            if ran == 1:
                badToTheBone()
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
    
class rigpage(bpy.types.Operator):
    """Opens a link to the Ice Cube page"""
    bl_idname = "rigpage.link"
    bl_label = getLanguageTranslation("ice_cube.ops.ice_cube_carrd")
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        CustomLink("https://ice-cube-rig.carrd.co/")
        
        return {'FINISHED'}

class discord_link(bpy.types.Operator):
    """Opens a link to my Discord server"""
    bl_idname = "discordserver.link"
    bl_label = getLanguageTranslation("ice_cube.ops.discord_server")
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
    
        CustomLink("https://www.dropbox.com/scl/fi/wkjptijpqxlqkifss5ejj/template_asset_pack.zip?rlkey=l3qhq0wetdgfimeq8jhcx0jtr&dl=1")
        
        return {'FINISHED'}

class download_template_2(bpy.types.Operator):
    """Downloads a rig template pack from my discord server"""
    bl_idname = "template2.download"
    bl_label = "Download Rig Pack Template"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
    
        CustomLink("https://www.dropbox.com/scl/fi/xw1r9cqsu6vrtldvnrlao/template_rig_pack.zip?rlkey=32omitbebqv7ybzxfema20303&dl=1")
        
        return {'FINISHED'}

class open_wiki(bpy.types.Operator):
    """Opens the Ice Cube wiki"""
    bl_idname = "wiki.open"
    bl_label = getLanguageTranslation("ice_cube.ops.open_wiki")
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        CustomLink("https://darthlilo.gitbook.io/ice-cube/")
        
        return{'FINISHED'}

class open_custom_presets(bpy.types.Operator):
    """Opens the DLC folder"""
    bl_idname = "custom_presets.open"
    bl_label = getLanguageTranslation("ice_cube.ops.dlc_folder")
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        open_user_packs(self, context)
        return{'FINISHED'}

class append_emotion_line(bpy.types.Operator):
    """Appends an emotion line to the rig"""
    bl_idname = "append.emotion"
    bl_label = getLanguageTranslation("ice_cube.ops.append_emotion_line")
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        append_emotion_line_func(self, context)
        return{'FINISHED'}

class check_for_updates(bpy.types.Operator):
    """Checks the Ice Cube GitHub for updates"""
    bl_idname = "ice_cube_check.updates"
    bl_label = "Check for updates"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ice_cube.update_available = check_for_updates_func()
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
    bl_label = "Create Backup"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        create_backup_func(self, context)
        return{'FINISHED'}

class load_backup(bpy.types.Operator):
    """Loads the selected backup from your backups folder"""
    bl_idname = "load.backup"
    bl_label = "Load Selected Backup"
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

class refresh_backups(bpy.types.Operator):
    """Refreshes the backups list"""
    bl_idname = "refresh.backup"
    bl_label = "Refresh Backup"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        refresh_backups_func(self, context)
        return{'FINISHED'}

class refresh_dlc(bpy.types.Operator):
    """Checks the Ice Cube GitHub for new DLC"""
    bl_idname = "refresh.dlc"
    bl_label = "Delete Backup"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        refresh_dlc_func(self, context)
        downloads_path = f"{root_folder}/ice_cube_data/ui/advanced/downloads.py"
        exec(open(downloads_path).read())
        
        return{'FINISHED'}
    
class grab_dlc(bpy.types.Operator):
    """Checks the Ice Cube GitHub for new DLC"""
    bl_idname = "refresh_grab.dlc"
    bl_label = "Grabs the latest DLC"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        IC_refresh_dlc(self, context)
        
        return{'FINISHED'}

class download_dlc(bpy.types.Operator):
    """Downloads the selected DLC from GitHub"""
    bl_idname = "download_selected.dlc"
    bl_label = "Download DLC"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        IC_download_dlc(self, context, valid_dlcs)
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
        if obj.get("ipaneltab6") == 0: #ASSETS
            CustomErrorBox("Generation for assets from the Ice Cube UI has been disabled, please use the new Scene UI found in the toolbar under \'Tool\'")

        if obj.get("ipaneltab6") == 1:
            #CHECKING FOR VARS

            if not bpy.data.is_saved:
                CustomErrorBox("Please save the file first!",'Save Error','ERROR')
                return{'FINISHED'}
            
            if obj.asset_pack_name == "":
                CustomErrorBox("Please enter a name for the pack!",'Invalid Name','ERROR')
                return{'FINISHED'}
            
            if obj.export_to_icpreset == True and obj.export_icpreset_file == "":
                CustomErrorBox("Choose a valid export folder!",'Invalid export folder','ERROR')
                return{'FINISHED'}

            if obj.entry_name_asset != "" and obj.asset_author != "" and obj.asset_version != "":
                
                if os.path.exists(obj.target_thumbnail_generate) is False and obj.generate_thumbnail is False:
                    CustomErrorBox("Invalid Thumbnail Path!",'Invalid Thumbnail','ERROR')
                    return{'FINISHED'}
                
                rig = isRigSelected(context)
                ice_cube_col = rig.users_collection
                ice_cube_col[0].name = obj.entry_name_asset

                #folder generation
                rigs = f"{root_folder}/ice_cube_data/internal_files/user_packs/rigs"

                if not obj.export_to_icpreset:
                    
                    target_save_path = f"{rigs}/{obj.asset_pack_name}"

                    list_of_dirs_to_gen = ["","rigs","thumbnails",f"rigs/{obj.entry_name_asset}"]

                    for folder in list_of_dirs_to_gen:
                        if os.path.exists(f"{target_save_path}/{folder}") is False:
                            os.mkdir(f"{target_save_path}/{folder}")
                    
                    
                else:
                    temp_gen_folder = f"{rigs}/temp_generation"
                    if not os.path.exists(temp_gen_folder):
                        os.mkdir(temp_gen_folder) #Making temp generation folder
                    target_save_path = temp_gen_folder

                    list_of_dirs_to_gen = ["","rigs","thumbnails",f"rigs/{obj.entry_name_asset}"]

                    for folder in list_of_dirs_to_gen:
                        if os.path.exists(f"{target_save_path}/{folder}") is False:
                            os.mkdir(f"{target_save_path}/{folder}")

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
                	"base_rig_vers": BlenderVersConvert(bl_info['version']),
                    "author": obj.asset_author,
                    "rig_version": obj.asset_version,
                	"has_baked": f"{obj.generate_baked}"
                }
                current_time = datetime.datetime.now()
                formatted_time = current_time.strftime("%m-%d-%Y")

                metadata_json = {
                    "creation_date": formatted_time,
                    "type": "single_rig"
                }


                converted_settings_json = json.dumps(settings_json_data,indent=4)
                with open(f"{target_save_path}/settings.json", "w") as json_file:
                    json_file.write(converted_settings_json)
                
                if obj.export_to_icpreset:
                    converted_metadata_json = json.dumps(metadata_json,indent=4)
                    with open(f"{target_save_path}/metadata.json", "w") as json_file:
                        json_file.write(converted_metadata_json)

                converted_info_json = json.dumps(info_json_data,indent=4)
                with open(f"{target_save_path}/rigs/{obj.entry_name_asset}/info.json", "w") as json_file:
                    json_file.write(converted_info_json)
                
                #packing textures
                bpy.ops.file.pack_all()


                #saving a copy of the file
                if bpy.data.is_saved is True:
                    filepath = f"{target_save_path}/rigs/{obj.entry_name_asset}/{obj.entry_name_asset}_NORMAL.blend"
                    bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)

                #thumbnail management
                if obj.target_thumbnail_generate != "" and str(obj.target_thumbnail_generate).__contains__(".png"): #Copy Thumbnail
                    shutil.copyfile(obj.target_thumbnail_generate,f"{target_save_path}/thumbnails/{obj.entry_name_asset}.png")
                
                if obj.generate_baked == True:
                    bakeIceCube(self,context,True)
                    if bpy.data.is_saved is True:
                        filepath = f"{target_save_path}/rigs/{obj.entry_name_asset}/{obj.entry_name_asset}_BAKED.blend"
                        bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)
                
                #generating thumbnail
                if obj.generate_thumbnail is True:
                

                    

                    #setting save loc
                    sce = bpy.context.scene.name
                    org_save_loc = bpy.data.scenes[sce].render.filepath
                    bpy.data.scenes[sce].render.filepath = f"{target_save_path}/thumbnails/{obj.entry_name_asset}.png"

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
                    
                    #setting solid mode
                    old_shading = bpy.context.space_data.shading.type
                    old_render_type = bpy.context.space_data.shading.color_type
                    old_lighting_type = bpy.context.space_data.shading.light
                    bpy.context.space_data.shading.type = 'SOLID'

                    #setting solid mode render to textured
                    bpy.context.space_data.shading.color_type = 'TEXTURE'

                    #setting solid mode to flat
                    bpy.context.space_data.shading.light = 'FLAT'



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
                    
                    bpy.context.space_data.shading.type = old_shading
                    bpy.context.space_data.shading.color_type = old_render_type
                    bpy.context.space_data.shading.light = old_lighting_type
            
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
                CustomErrorBox("Please select a valid thumbnail!","Invalid Path",'ERROR')
                return{'FINISHED'}
            
            if obj.export_to_icpreset:
                print("RAH")
                rigs = f"{root_folder}/ice_cube_data/internal_files/user_packs/rigs"
                temp_gen_folder = f"{rigs}/temp_generation"
                compressDirectory(temp_gen_folder,f"{bpy.path.abspath(obj.export_icpreset_file)}/{obj.asset_pack_name}.icpreset")
                shutil.rmtree(temp_gen_folder)

        return{'FINISHED'}

class import_icpreset_file(bpy.types.Operator,ImportHelper):
    """Generates an asset pack"""
    bl_idname = "import.icpreset_file"
    bl_label = "Import icpreset"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = ".icpreset"

    filter_glob: bpy.props.StringProperty(
        default="*.icpreset",
        options={'HIDDEN'},
        maxlen=255
    )

    def execute(self, context):
        try:
            selected_preset = self.filepath

            filename = os.path.basename(selected_preset)
            clean_filename = os.path.splitext(filename)[0]

            downloads = f"{root_folder}/downloads"
            extracted_path = f"{downloads}/{clean_filename}"
            try:
                shutil.rmtree(extracted_path)
            except:
                pass
            os.mkdir(extracted_path)

            with zipfile.ZipFile(selected_preset, 'r') as zip_ref:
                zip_ref.extractall(extracted_path)

            dlc_folder = root_folder+"/ice_cube_data/internal_files/user_packs/rigs/"

            try:
                #install the new DLC
                distutils.dir_util.copy_tree(extracted_path, f"{dlc_folder}/{clean_filename}")
                print("Finished Install!")
                CustomErrorBox("Finished installing DLC!","Updated Finished",'INFO')
            except:
                print("Error Completing Install.")
                CustomErrorBox("Error Completing Install.","Updated Cancelled",'ERROR')
        except:
            pass

        return {'FINISHED'}



class generate_asset_pack_global(bpy.types.Operator):
    """Generates an asset pack"""
    bl_idname = "generate.asest_pack_global"
    bl_label = "Generate Asset Pack"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        obj = context.object
        scene = context.scene

        pack_name = scene.asset_pack_name
        entry_name = scene.entry_name_asset
        asset_author = scene.asset_author
        asset_version = scene.asset_version
        customizable = scene.asset_customizable
        if customizable:
            has_entries = scene.has_entries
            armor_trims = scene.supports_armor_trims
            leggings_half = scene.leggings_half
            material_type = scene.materialType
        else:
            armor_trims = False
            leggings_half = False
            material_type = 'default'
        thumbnail_path = scene.target_thumbnail_generate

        if bpy.data.is_saved is False:
            CustomErrorBox("Please save first!","ERROR: File not saved!",'ERROR')
            return {'CANCELLED'}

            #CHECKING FOR VARS
        if pack_name != "" and entry_name != "" and asset_author != "" and asset_version != "" and os.path.exists(thumbnail_path) is True:
            #folder generation
            inventory = f"{root_folder}/ice_cube_data/internal_files/user_packs/inventory"

            asset_pack_path = f"{inventory}/{pack_name}"

            list_of_dirs_to_gen = ["","assets","thumbnails",f"assets/{entry_name}"]

            for folder in list_of_dirs_to_gen:
                if os.path.exists(f"{asset_pack_path}/{folder}") is False:
                    os.mkdir(f"{asset_pack_path}/{folder}")

            #settings json generation
            settings_json_data = {
                "pack_name": pack_name,
                "author": asset_author,
                "version": asset_version,
            	"default": entry_name
            }

            #info json generation
            if customizable:
                if has_entries:
                    valid_collections = []
                    for collection in bpy.data.collections:
                        valid_collections.append(collection.name)

                    for collection in bpy.data.collections:
                        for child in collection.children_recursive:
                            try:
                                valid_collections.remove(child.name)
                            except:
                                pass
                    

                    info_json_data = {
                        "asset_name": entry_name,
                        "asset_id": entry_name,
                        "author": asset_author,
                        "asset_version": asset_version,
                        "customizable": customizable,
                        "asset_settings": {
                            "entries" : valid_collections,
                            "supports_armor_trims" : armor_trims,
                            "leggings_half" : leggings_half,
                            "materialType" : material_type
                        }
                    }
                else:
                    info_json_data = {
                        "asset_name": entry_name,
                        "asset_id": entry_name,
                        "author": asset_author,
                        "asset_version": asset_version,
                        "customizable": customizable,
                        "asset_settings": {
                            "supports_armor_trims" : armor_trims,
                            "leggings_half" : leggings_half,
                            "materialType" : material_type
                        }
                    }
            else:
                info_json_data = {
                    "asset_name": entry_name,
                    "asset_id": entry_name,
                    "author": asset_author,
                    "asset_version": asset_version,
                    "customizable": customizable
                }

            converted_settings_json = json.dumps(settings_json_data,indent=4)
            with open(f"{asset_pack_path}/settings.json", "w") as json_file:
                json_file.write(converted_settings_json)

            converted_info_json = json.dumps(info_json_data,indent=4)
            with open(f"{asset_pack_path}/assets/{entry_name}/info.json", "w") as json_file:
                json_file.write(converted_info_json)


            #saving a copy of the file
            if bpy.data.is_saved is True and pack_name != "" and entry_name != "":
                filepath = f"{inventory}/{pack_name}/assets/{entry_name}/{entry_name}.blend"
                bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)

            #thumbnail management
            if thumbnail_path != "" and str(thumbnail_path).__contains__(".png"): #Copy Thumbnail
                shutil.copyfile(thumbnail_path,f"{inventory}/{pack_name}/thumbnails/{entry_name}.png")

        elif pack_name == "":
            CustomErrorBox("Please enter a name for the pack!",'Invalid Name','ERROR')
            return{'FINISHED'}
        elif entry_name == "":
            CustomErrorBox("Please enter an asset name!","Invalid Name",'ERROR')
            return{'FINISHED'}
        elif asset_author == "":
            CustomErrorBox("Please enter an author!","Invalid Author",'ERROR')
            return{'FINISHED'}
        elif asset_version == "":
            CustomErrorBox("Please enter a valid version!","Invalid Version",'ERROR')
            return{'FINISHED'}
        elif os.path.exists(thumbnail_path) is False:
            CustomErrorBox("Please select a valid thumbnail!","Invalid Path",'ERROR')
            return{'FINISHED'}

        return{'FINISHED'}

class r_arm_ik_to_fk(bpy.types.Operator):
    """Translates the Right Arm from IK to FK"""
    bl_idname = "fk_arm_r.snapping"
    bl_label = "Right Arm IK Snap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        IC_FKIK_Switch(context,"IK_TO_FK","ARM_R")
        return{'FINISHED'}

class l_arm_ik_to_fk(bpy.types.Operator):
    """Translates the Left Arm from IK to FK"""
    bl_idname = "fk_arm_l.snapping"
    bl_label = "Left Arm IK Snap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        IC_FKIK_Switch(context,"IK_TO_FK","ARM_L")
        return{'FINISHED'}

class r_arm_fk_to_ik(bpy.types.Operator):
    """Translates the Right Arm from FK to IK"""
    bl_idname = "ik_arm_r.snapping"
    bl_label = "Right Arm IK Snap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        IC_FKIK_Switch(context,"FK_TO_IK","ARM_R")
        return{'FINISHED'}

class l_arm_fk_to_ik(bpy.types.Operator):
    """Translates the Left Arm from FK to IK"""
    bl_idname = "ik_arm_l.snapping"
    bl_label = "Left Arm IK Snap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        IC_FKIK_Switch(context,"FK_TO_IK","ARM_L")
        return{'FINISHED'}

class r_leg_ik_to_fk(bpy.types.Operator):
    """Translates the Right Leg from IK to FK"""
    bl_idname = "fk_leg_r.snapping"
    bl_label = "Right Leg IK Snap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        IC_FKIK_Switch(context,"IK_TO_FK","LEG_R")
        return{'FINISHED'}

class l_leg_ik_to_fk(bpy.types.Operator):
    """Translates the Left Leg from IK to FK"""
    bl_idname = "fk_leg_l.snapping"
    bl_label = "Left Leg IK Snap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        IC_FKIK_Switch(context,"IK_TO_FK","LEG_L")

        return{'FINISHED'}

class r_leg_fk_to_ik(bpy.types.Operator):
    """Translates the Right Leg from FK to IK"""
    bl_idname = "ik_leg_r.snapping"
    bl_label = "Right Leg IK Snap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        IC_FKIK_Switch(context,"FK_TO_IK","LEG_R")
        return{'FINISHED'}

class l_leg_fk_to_ik(bpy.types.Operator):
    """Translates the Left Leg from FK to IK"""
    bl_idname = "ik_leg_l.snapping"
    bl_label = "Left Leg IK Snap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):
        IC_FKIK_Switch(context,"FK_TO_IK","LEG_L")
        return{'FINISHED'}

class IC_DevMode_ResetRig(bpy.types.Operator):
    """COMPLETELY RESETS ICE CUBE TO DEFAULT SETTINGS!"""
    bl_idname = "reset_to_default.icecube"
    bl_label = "Ice Cube Reset"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        obj = context.object
        rig = isRigSelected(context)

        if obj.get("confirm_ice_cube_reset"):

            reset_all_settings_func(self,context) #Resets Settings
            obj.ic_dlc_i.clear() #Resets DLC
            obj.confirm_ice_cube_reset = False

            for bone in rig.pose.bones:
                bone.location = (0,0,0)
                bone.rotation_quaternion = [1,0,0,0]
                bone.scale = (1,1,1)
        else:
            CustomErrorBox("Please confirm the reset with the button to the side!",'UNCONFIRMED RESET','ERROR')

        return{'FINISHED'}

class IC_DevMode_ResetUI(bpy.types.Operator):
    """Resets the Ice Cube UI only"""
    bl_idname = "reset_ui.icecube"
    bl_label = "Ice Cube UI Reset"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        reset_all_ui_func(self,context) #Resets Settings
        return{'FINISHED'}
    
class IC_Jump_To_Panel_RigStyle(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.rigstyle"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'style')
        setattr(context.object, "style_menu_switcher", 'rig')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}

class IC_Jump_To_Panel_MeshStyle(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.meshstyle"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'style')
        setattr(context.object, "style_menu_switcher", 'mesh')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}
    
class IC_Jump_To_Panel_Controls(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.controls"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'controls')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}
    
class IC_Jump_To_Panel_Skins(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.skins"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'materials')
        setattr(context.object, "material_menu_switcher", 'skin')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}

class IC_Jump_To_Panel_Eyes(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.eyes"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'materials')
        setattr(context.object, "material_menu_switcher", 'eyes')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}

class IC_Jump_To_Panel_Misc(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.misc"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'materials')
        setattr(context.object, "material_menu_switcher", 'misc')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}

class IC_Jump_To_Panel_DLC(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.dlc"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'advanced')
        setattr(context.object, "advanced_menu_switcher", 'dlc')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}

class IC_Jump_To_Panel_Parenting(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.parenting"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'advanced')
        setattr(context.object, "advanced_menu_switcher", 'parenting')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}

class IC_Jump_To_Panel_System(bpy.types.Operator):
    """Jumps to a specific panel"""
    bl_idname = "jump_to_panel.system"
    bl_label = "Jump To Panel"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setattr(context.object, "main_panel_switcher", 'advanced')
        setattr(context.object, "advanced_menu_switcher", 'system')
        setattr(context.object, "ice_cube_search_filter", '')
        return{'FINISHED'}

class ic_parent_all(bpy.types.Operator):
    """Parents all meshes to Ice Cube relating to their respective collections"""
    bl_idname = "parent.allcollections"
    bl_label = "Update Parenting"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        rig = isRigSelected(context)
        ice_cube_col = rig.users_collection
        col_children = ice_cube_col[0].children

        vaild_collections = {}

        collection_objects = {}

        for child1 in col_children:
            for child2 in child1.children:
                for key in ["Head","Body","Right Arm","Left Arm","Right Leg","Left Leg"]:
                    if str(child2).__contains__(key):
                        vaild_collections[key] = child2
        
        for entry in vaild_collections:
            temp_col_obj = []
            for thing in vaild_collections[entry].objects:
                temp_col_obj.append(thing)
            collection_objects[entry] = temp_col_obj
        
        for headchild in collection_objects['Head']:
            parent_head_func(self,context,headchild)
        
        for bodychild in collection_objects['Body']:
            parent_body_func(self,context,bodychild)
        
        for rarmchild in collection_objects['Right Arm']:
            parent_right_arm(self,context,rarmchild)
        
        for larmchild in collection_objects['Left Arm']:
            parent_left_arm(self,context,larmchild)
        
        for rlegchild in collection_objects['Right Leg']:
            parent_right_leg(self,context,rlegchild)
        
        for llegchild in collection_objects['Left Leg']:
            parent_left_leg(self,context,llegchild)
            

        return{'FINISHED'}

class ic_bake_rig(bpy.types.Operator):
    """EXTREMELY DESTRUCTIVE, PROCEED WITH CAUTION"""
    bl_idname = "ice_cube.bake_rig"
    bl_label = "Ice Cube Bake Rig"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        bakeIceCube(self,context)

        return{'FINISHED'}

class ic_update_bonelayer(bpy.types.Operator):
    """Updates the bonelayer system to 4.0+"""
    bl_idname = "updateic.bonelayer"
    bl_label = "Update Ice Cube Bonelayers"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        rig = isRigSelected(context)
        
        if cur_blender_version >= 400:
            rig = isRigSelected(context)
            collections = rig.data.collections
    
            layer_update_dict = {
            "Layer 1" : "Main Bones",
            "Layer 2" : "Right Arm IK",
            "Layer 3" : "Left Arm IK",
            "Layer 4" : "Right Leg IK",
            "Layer 5" : "Left Leg IK",
            "Layer 6" : "Right Fingers",
            "Layer 7" : "Dynamic Hair",
            "Layer 8" : "Body Tweak",
            "Layer 9" : "Right Arm Tweak",
            "Layer 10" : "Left Arm Tweak",
            "Layer 11" : "Twist",
            "Layer 12" : "Custom Default",
            "Layer 16" : "Emotion Bones",
            "Layer 17" : "Face Tweak",
            "Layer 18" : "Right Arm FK",
            "Layer 19" : "Left Arm FK",
            "Layer 20" : "Right Leg FK",
            "Layer 21" : "Left Leg FK",
            "Layer 22" : "Left Fingers",
            "Layer 23" : "Extra",
            "Layer 24" : "Face Panel Bones",
            "Layer 25" : "Right Leg Tweak",
            "Layer 26" : "Left Leg Tweak",
            "Layer 27" : "Footroll",
            "Layer 28" : "Cartoon Mouth",
            "Layer 31" : "Body Internal",
            "Layer 32" : "Main Internal",
            "Main" : "DELETE",
            "Right" : "DELETE",
            "Left" : "DELETE",
            "Accessory" : "DELETE",
            "Misc" : "DELETE",
            "Face Panel" : "DELETE",
        }
    
            if "Layer 16" not in collections:
                collections.new("Layer 16")
            
            if "Layer 12" not in collections:
                collections.new("Layer 12")
    
            for collection in collections:
                try:
                    collection["layer"]
                except:
                    if collection.name in layer_update_dict:
                        if layer_update_dict[collection.name] == "DELETE":
                            collections.remove(collection)
                        else:
                            collection["layer"] = layer_update_dict[collection.name]
                            collection.name = layer_update_dict[collection.name]
        
        rig.data["UpdatedTo4.0"] = 1

        return{'FINISHED'}

class ic_set_rest_pose(bpy.types.Operator):
    """Sets the rest pose to be the current pose of the rig"""
    bl_idname = "ice_cube.setrestpose"
    bl_label = "Set Rest Pose Ice Cube"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        setRestPose(context)

        return{'FINISHED'}

class ic_reset_rest_pose(bpy.types.Operator):
    """Resets the rest pose to be the base rest pose of the rig"""
    bl_idname = "ice_cube.resetrestpose"
    bl_label = "Reset Rest Pose Ice Cube"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        
        resetRestPose(context)

        return{'FINISHED'}

class ic_update_rest_pose(bpy.types.Operator):
    """Updates the rest pose to be the current pose of the rig"""
    bl_idname = "ice_cube.updaterestpose"
    bl_label = "Update Rest Pose Ice Cube"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        resetRestPose(context)
        setRestPose(context)
        
        return{'FINISHED'}

class update_default_rig(bpy.types.Operator):
    """Updates the default rig to your current file"""
    bl_idname = "ice_cube.updatedefaultrig"
    bl_label = "Update Default File"
    bl_options = {'REGISTER', 'UNDO'}

    default_name : bpy.props.StringProperty(name="Default Name?:", default="")

    def execute(self,context):
        name = self.default_name
        rigs_folder = f"{root_folder}/ice_cube_data/internal_files/rigs"

        if not bpy.data.is_saved:
            CustomErrorBox("Please save the file first!",'Save Error','ERROR')
            return{'FINISHED'}
        
        if name.__contains__("Ice Cube"):
            CustomErrorBox("Name cannot contain \"Ice Cube\"!",'Name Error','ERROR')
            return{'FINISHED'}
        
        rig = isRigSelected(context)
        ice_cube_col = rig.users_collection
        ice_cube_col[0].name = name

        settings_data = open_json(settings_file)

        settings_data["default_import_file"] = name

        if cur_blender_version >= 400:
            filepath = f"{rigs_folder}/{name} 4.0+.blend"
        else:
            filepath = f"{rigs_folder}/{name}.blend"
        bpy.ops.file.pack_all()
        bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)

        converted_settings_data = json.dumps(settings_data, indent=4)
        with open(settings_file, "w") as json_file:
            json_file.write(converted_settings_data)
        



        return{'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class reset_default_rig(bpy.types.Operator):
    """Resets the default rig back to the vanilla Ice Cube file"""
    bl_idname = "ice_cube.resetdefaultrig"
    bl_label = "Update Default File"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self,context):

        settings_data = open_json(settings_file)

        settings_data["default_import_file"] = "Ice Cube"

        converted_settings_data = json.dumps(settings_data, indent=4)
        with open(settings_file, "w") as json_file:
            json_file.write(converted_settings_data)
        



        return{'FINISHED'}

class IC_DEVONLY_UpdateInternalRig(bpy.types.Operator):
    """DO NOT RUN UNLESS YOU KNOW WHAT YOU'RE DOING"""
    bl_idname = "ice_cube_dev.updateinternalrig"
    bl_label = "IC Update Internal Rig DEV ONLY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        if cur_blender_version >= 400:
            filepath = f"{root_folder}/ice_cube_data/internal_files/rigs/Ice Cube 4.0+.blend"
            bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)
            blend1 = f"{root_folder}/ice_cube_data/internal_files/rigs/Ice Cube 4.0+.blend1"

            if os.path.exists(blend1):
                os.remove(blend1)
        else:
            filepath = f"{root_folder}/ice_cube_data/internal_files/rigs/Ice Cube.blend"
            bpy.ops.wm.save_as_mainfile(filepath=filepath,copy=True)
            blend1 = f"{root_folder}/ice_cube_data/internal_files/rigs/Ice Cube.blend1"

            if os.path.exists(blend1):
                os.remove(blend1)

        return {'FINISHED'}



class IC_DevMode_TestOperator(bpy.types.Operator):
    """DO NOT RUN UNLESS YOU KNOW WHAT YOU'RE DOING"""
    bl_idname = "ice_cube_dev.testoperator"
    bl_label = "Ice Cube Test Operator DEV ONLY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        print(getLanguageTranslation("ice_cube.experimentations.test"))

        return{'FINISHED'}



#Backups Classes

#Collection Classes

class ICBackupsListClass(bpy.types.PropertyGroup):
    value: bpy.props.FloatProperty(
        name="value",
        description="value",
        default=1.0,
        min=0.0, max=1,
        soft_min=0.0, soft_max=1.0,
    )

class ICDLC_ListClass(bpy.types.PropertyGroup):
    value: bpy.props.FloatProperty(
        name="value",
        description="value",
        default=1.0,
        min=0.0, max=1,
        soft_min=0.0, soft_max=1.0,
    )

#UI Classes



class IC_BACKUP_UL_list_i(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        
        if self.layout_type in {'DEFAULT', 'COMPACT'}:

            col = layout.column()
            colrow = col.row()
            colrow.label(
                text=item.name,
                icon='FILE_BACKUP',
            )
            colrow.label(
                text=f"Created: [{os_management.backup_dates[item.name]}]",
            )
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)


class IC_DLC_UL_available_list_i(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            split_name = str(item.name).split("|")
            col = layout.column()
            colrow = col.row()
            colrow.label(
                text=split_name[0],
                icon=split_name[1],
            )
            colrow.label(
                text=f"Uploaded: [{split_name[2]}]",
            )

        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)



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
    rigpage,
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
    refresh_backups,
    load_backup,
    delete_backup,
    refresh_dlc,
    grab_dlc,
    download_dlc,
    export_settings_data_class,
    import_settings_data_class,
    update_backups_list,
    reset_all_settings,
    generate_asset_pack,
    import_icpreset_file,
    generate_asset_pack_global,
    r_arm_ik_to_fk,
    l_arm_ik_to_fk,
    r_arm_fk_to_ik,
    l_arm_fk_to_ik,
    r_leg_ik_to_fk,
    l_leg_ik_to_fk,
    r_leg_fk_to_ik,
    l_leg_fk_to_ik,
    IC_DevMode_ResetRig,
    IC_DevMode_ResetUI,
    IC_BACKUP_UL_list_i,
    IC_DLC_UL_available_list_i,
    ICBackupsListClass,
    ICDLC_ListClass,
    IC_Jump_To_Panel_RigStyle,
    IC_Jump_To_Panel_MeshStyle,
    IC_Jump_To_Panel_Controls,
    IC_Jump_To_Panel_Skins,
    IC_Jump_To_Panel_Eyes,
    IC_Jump_To_Panel_Misc,
    IC_Jump_To_Panel_DLC,
    IC_Jump_To_Panel_Parenting,
    IC_Jump_To_Panel_System,
    IC_DevMode_TestOperator,
    ic_parent_all,
    ic_bake_rig,
    ic_update_bonelayer,
    ic_set_rest_pose,
    ic_reset_rest_pose,
    ic_update_rest_pose,
    update_default_rig,
    reset_default_rig,
    IC_DEVONLY_UpdateInternalRig
]

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Object.ic_backups_i = bpy.props.CollectionProperty(type=ICBackupsListClass)
    bpy.types.Object.ic_dlc_i = bpy.props.CollectionProperty(type=ICDLC_ListClass)
    bpy.types.Object.ic_backups_active_index = bpy.props.IntProperty(name="IC Backups List Active Item Index")
    bpy.types.Object.ic_dlc_active_index = bpy.props.IntProperty(name="IC DLC List Active Item Index")
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()