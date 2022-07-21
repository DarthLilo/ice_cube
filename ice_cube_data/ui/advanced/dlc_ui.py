#Libraries
import bpy
import os
import json

from ice_cube import root_folder, dlc_id,dlc_type,dlc_author,dlc_date
from ice_cube_data.properties import properties
from ice_cube_data.systems import inventory_system

from ice_cube_data.utils.general_func import GetListIndex
from ice_cube_data.utils.file_manage import getFiles

def dlc_menu(self, context, layout, rig_baked):
    scene = context.scene
    obj = context.object
    box = layout.box()
    b = box.row(align=True)
    b.prop(obj, "dlc_menu_switcher", text="")
    wm = context.window_manager

    if obj.get("dlc_menu_switcher") is 0: #APPEND MENU
        b.prop(obj,"ipaneltab6",text="")

        if obj.get("ipaneltab6") is 0:
            thumbnail = bpy.data.window_managers["WinMan"].inventory_preview
            thumbnailnopng = thumbnail.split(".")[0]
            cur_asset = context.scene.get("selected_inv_asset")

            asset_missing_file_dir_set = root_folder+"/ice_cube_data/internal_files/important/missing_settings.json"
            asset_missing_file_dir_inf = root_folder+"/ice_cube_data/internal_files/important/missing_info.json"
            
            if cur_asset != None:
                cur_selected_asset = context.scene.selected_inv_asset
                asset_settings_dir = f"{root_folder}/ice_cube_data/internal_files/user_packs/inventory/{cur_selected_asset}/settings.json"
                asset_info_dir = f"{root_folder}/ice_cube_data/internal_files/user_packs/inventory/{cur_selected_asset}/assets/{thumbnailnopng}/info.json"
            
            else:
                asset_settings_dir = root_folder+"/ice_cube_data/internal_files/important/settings.json"
                asset_info_dir = root_folder+"/ice_cube_data/internal_files/important/info_asset.json"
            
            try:
                with open(asset_settings_dir, 'r') as myfile:
                    asset_data = myfile.read()
            except:
                with open(asset_missing_file_dir_set, 'r') as myfile:
                    asset_data = myfile.read()
            
            try:
                with open(asset_info_dir, 'r') as notmyfile:
                    asset_data_inf = notmyfile.read()
            except:
                with open(asset_missing_file_dir_inf, 'r') as notmyfile:
                    asset_data_inf = notmyfile.read()
            
            asset_packdata = json.loads(asset_data)
            asset_infodata = json.loads(asset_data_inf)


            #json variables
            asset_json_pack_name = str(asset_packdata['pack_name'])
            asset_json_pack_author = str(asset_packdata['author'])
            asset_json_pack_version = str(asset_packdata['version'])
            asset_json_pack_default = str(asset_packdata['default'])

            if str(asset_infodata['asset_name']) == "MISSING FILE":
                bpy.data.window_managers["WinMan"].inventory_preview = str(asset_json_pack_default+".png")
            asset_json_asset_name = str(asset_infodata['asset_name'])
            asset_json_asset_author = str(asset_infodata['author'])
            asset_json_asset_version = str(asset_infodata['asset_version'])

            b = box.row(align=True)
            b.label(text= "Select an asset to append!", icon='BLENDER')
            b = box.row(align=True)
            b.template_icon_view(wm, "inventory_preview")
            b = box.row(align=True)
            b.prop(scene, "selected_inv_asset",text="")
            b.operator("refresh.inv_list",text="",icon='FILE_REFRESH')
            b = box.row(align=True)
            b.operator("append.asset", text = "Append Selected")
            b = box.row(align=True)
            b.operator("custom_presets.open", text = "DLC Folder")
            b.operator("template1.download", text = "Asset Template")

            box = layout.box()
            b = box.row(align=True)
            b.label(text="Asset Pack Info:", icon='INFO')
            try:
                row_labels = {
                               "Pack Name": asset_json_pack_name,
                               "Author": asset_json_pack_author,
                               "Version": asset_json_pack_version
                            }
                for label in row_labels:
                    b = box.row(align = True)
                    b.label(text = f"{label}: {row_labels[label]}")
            except:
                b.label(text = "Select a pack from the list")

            box = layout.box()
            b = box.row(align=True)
            b.label(text="Current Asset Info:", icon='INFO')
            b = box.row(align=True)
            b = box.row(align=True)
            b.label(text="Name: " + asset_json_asset_name)
            b = box.row(align=True)
            b.label(text="Author: " + asset_json_asset_author)
            b = box.row(align=True)
            b.label(text="Version: " + asset_json_asset_version)
        
        if obj.get("ipaneltab6") is 1:
            thumbnail = bpy.data.window_managers["WinMan"].my_previews_presets
            thumbnailnopng = thumbnail.split(".")[0]
            cur_asset = context.scene.get("selected_rig_preset")
            
            missing_file_dir_set = root_folder+"/ice_cube_data/internal_files/important/missing_settings.json"
            missing_file_dir_inf = root_folder+"/ice_cube_data/internal_files/important/missing_info.json"

            if cur_asset != "None":
                cur_selected_asset = context.scene.selected_rig_preset
                settings_directory = f"{root_folder}/ice_cube_data/internal_files/user_packs/rigs/{cur_selected_asset}/settings.json"
                info_directory = f"{root_folder}/ice_cube_data/internal_files/user_packs/rigs/{cur_selected_asset}/rigs/{thumbnailnopng}/info.json"
            
            else:
                settings_directory = root_folder+"/ice_cube_data/internal_files/important/settings.json"
                info_directory = root_folder+"/ice_cube_data/internal_files/important/info_asset.json"
            
            try:
                with open(settings_directory, 'r') as myfile:
                    data = myfile.read()
            except:
                with open(missing_file_dir_set, 'r') as myfile:
                    data = myfile.read()

            try:
                with open(info_directory, 'r') as notmyfile:
                    data_inf = notmyfile.read()
            except:
                with open(missing_file_dir_inf, 'r') as notmyfile:
                    data_inf = notmyfile.read()
            packdata = json.loads(data)
            infodata = json.loads(data_inf)

            #Json Variables
            json_pack_name = str(packdata['pack_name'])
            json_pack_author = str(packdata['author'])
            json_pack_version = str(packdata['version'])
            json_pack_default = str(packdata['default'])

            #if str(infodata['rig_name']) == "MISSING FILE":
            #    bpy.data.window_managers["WinMan"].my_previews_presets = str(json_pack_default+".png")
            json_rig_name = str(infodata['rig_name'])
            json_rig_author = str(infodata['author'])
            json_rig_version = str(infodata['rig_version'])
            json_base_rig = str(infodata['base_rig'])
            json_base_version = str(infodata['base_rig_vers'])
            json_rig_baked = str(infodata['has_baked'])

            b = box.row(align=True)
            b.label(text= "Select a preset to append!", icon='BLENDER')
            b = box.row(align=True)
            b.template_icon_view(wm, "my_previews_presets")
            b = box.row(align=True)
            b.prop(scene, "selected_rig_preset",text="")
            b.operator("refresh.rig_list",text="",icon='FILE_REFRESH')
            b = box.row(align=True)
            b.operator("append.preset", text = "Append Selected")
            b1 = b.row(align=True)
            if rig_baked == True:
                b1.operator("rig.bakedbutton", text= "Baked", icon= 'LAYER_ACTIVE')
                if json_rig_baked == "False":
                    rig_baked = False
            else:
                b1.operator("rig.bakedbutton", text= "Normal", icon= 'LAYER_USED')
            if json_rig_baked == "True":
                b1.enabled = True
            else:
                b1.enabled = False
                if properties.global_rig_baked == True:
                    properties.global_rig_baked = False
            b = box.row(align=True)
            b.operator("custom_presets.open", text = "DLC Folder")
            b.operator("template2.download", text = "Rig Template")
            box = layout.box()
            b = box.row(align=True)
            b.label(text="Rig Pack Info:", icon='INFO')
            try:
                row_labels = {
                               "Pack Name": json_pack_name,
                               "Author": json_pack_author,
                               "Version": json_pack_version
                            }
                for label in row_labels:
                    b = box.row(align = True)
                    b.label(text = f"{label}: {row_labels[label]}")
            except:
                b.label(text = "No Pack Selected!")

            box = layout.box()
            b = box.row(align=True)
            b.label(text="Current Rig Info:", icon='INFO')
            b = box.row(align=True)
            b = box.row(align=True)
            b.label(text="Name: " + json_rig_name)
            b = box.row(align=True)
            b.label(text="Author: " + json_rig_author)
            b = box.row(align=True)
            b.label(text="Version: " + json_rig_version)
            b = box.row(align=True)
            b.label(text="Base Rig: " + json_base_rig)
            b = box.row(align=True)
            b.label(text="Base Rig Version: " + json_base_version)
            b = box.row(align=True)
            b.label(text="Has \"BAKED\" version?: " + json_rig_baked)

    if obj.get("dlc_menu_switcher") is 1: #DOWNLOAD MENU
        dlc_folder_preset = root_folder+"/ice_cube_data/internal_files/user_packs/rigs"
        dlc_folder_asset = root_folder+"/ice_cube_data/internal_files/user_packs/inventory"

        box = layout.box()
        b = box.row(align=True)
        b.label(text = "DLC Manager",icon='IMPORT')
        b = box.row(align=True)

        b.prop(obj,"dlc_list",text="")
        b.operator("download.dlc", text="", icon= 'IMPORT')
        b.operator("refresh.dlc", text="", icon= 'FILE_REFRESH')
        b = box.row(align=True)
        
        #start of box
        box2 = b.box()
        b1 = box2.row(align=True)

        b1.label(text="Type:", icon ='FILE_BACKUP')
        b1.label(text="Author:")
        b1.label(text="Date:")
        b1 = box2.row(align=True)
        try:
            selected_dlc = getattr(obj,"dlc_list")
            dlc_number = GetListIndex(str(selected_dlc), dlc_id)
            
            b1.label(text=f"{dlc_type[dlc_number]}", icon ='FILE_BACKUP')
            b1.label(text=f"{dlc_author[dlc_number]}")
            b1.label(text=f"{dlc_date[dlc_number]}")
            b1 = box2.row(align=True)
        except:
            b1.label(text="REFRESH")
            b1 = box2.row(align=True)
        
        b = box.row(align=True)
        b.label(text = "Installed DLC:")
        b = box.row(align=True)
        #start of box
        box2 = b.box()
        b1 = box2.row(align=True)
        dlc_preset_scan = os.listdir(dlc_folder_preset)
        dlc_asset_scan = os.listdir(dlc_folder_asset)
        if len(dlc_preset_scan) + len(dlc_asset_scan) == 0:
            b1 = box2.row(align=True)
            b1.label(text = "NO DLC FOUND", icon = 'FILE_BACKUP')
        else:
            for dlc in getFiles(dlc_folder_asset):
                b1 = box2.row(align=True)
                b1.label(text = dlc, icon = 'FILE_BACKUP')
            for dlc in getFiles(dlc_folder_preset):
                b1 = box2.row(align=True)
                b1.label(text = dlc, icon = 'FILE_BACKUP')

    if obj.get("dlc_menu_switcher") is 2: #GENERATE MENU
        b.prop(obj,"ipaneltab6",text="")
        b = box.row(align=True)

        if obj.get("ipaneltab6") is 0: #ASSETS
            b.label(text="Generate Asset Pack")
            b1 = b.row(align=True)
            b1.prop(obj,"generate_thumbnail",text="Generate Thumbnail?")
            b1.enabled = False
            b = box.row(align=True)
            b.prop(obj, "target_thumbnail_generate", text="Thumbnail")
            b = box.row(align=True)
            b.prop(obj, "asset_pack_name", text="")
            b.prop(obj, "entry_name_asset", text="")
            b = box.row(align=True)
            b.prop(obj, "asset_author", text="")
            b.prop(obj, "asset_version", text="")
            b = box.row(align=True)
            b.operator("generate.asest_pack",text="Generate Pack")
        
        if obj.get("ipaneltab6") is 1: #PRESETS
            b.label(text="Generate Preset Pack")
            b.prop(obj,"generate_thumbnail",text="Generate Thumbnail?")
            b = box.row(align=True)
            b.prop(obj, "target_thumbnail_generate", text="Thumbnail")
            b = box.row(align=True)
            b.prop(obj, "has_baked_version", text="Has Baked?")
            b1 = b.row(align=True)
            b1.prop(obj,"baked_version_filepath",text="")
            if obj.get("has_baked_version") == False:
                b1.enabled = False
            b = box.row(align=True)
            b.prop(obj, "asset_pack_name", text="")
            b.prop(obj, "entry_name_asset", text="")
            b = box.row(align=True)
            b.prop(obj, "asset_author", text="")
            b.prop(obj, "asset_version", text="")
            b = box.row(align=True)
            b.operator("generate.asest_pack",text="Generate Pack")

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