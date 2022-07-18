#Libraries
import bpy
import os
import json

from ice_cube import root_folder
from ice_cube_data.properties import properties

def dlc_assets_UI(self, context, layout, inv_system):
    #window setup
    obj = context.scene
    thumbnail = bpy.data.window_managers["WinMan"].inventory_preview
    thumbnailnopng = thumbnail.split(".")[0]
    
    #json loader
    try:
        asset_selected_file = inv_system[context.scene.get("selected_inv_asset")]
        asset_settings_directory = root_folder+"/ice_cube_data/internal_files/user_packs/inventory/"+asset_selected_file+"/settings.json"
            
            
    except:
        asset_settings_directory = root_folder+"/ice_cube_data/internal_files/important/settings.json"
    
            
    try:
        asset_selected_file = inv_system[context.scene.get("selected_inv_asset")]
        asset_info_directory = root_folder+"/ice_cube_data/internal_files/user_packs/inventory/"+asset_selected_file+"/assets/"+thumbnailnopng+"/info.json"
            
    except:
        asset_info_directory = root_folder+"/ice_cube_data/internal_files/important/info_asset.json"
            
    
            
            
    asset_missing_file_dir_set = root_folder+"/ice_cube_data/internal_files/important/missing_settings.json"
    asset_missing_file_dir_inf = root_folder+"/ice_cube_data/internal_files/important/missing_info.json"
    
    #read json file
    try:
        with open(asset_settings_directory, 'r') as myfile:
            asset_data = myfile.read()
    except:
        with open(asset_missing_file_dir_set, 'r') as myfile:
            asset_data = myfile.read()
    
    try:
        with open(asset_info_directory, 'r') as notmyfile:
            asset_data_inf = notmyfile.read()
    except:
        with open(asset_missing_file_dir_inf, 'r') as notmyfile:
            asset_data_inf = notmyfile.read()
    asset_packdata = json.loads(asset_data)
    
    asset_json_pack_name = str(asset_packdata['pack_name'])
    asset_json_pack_author = str(asset_packdata['author'])
    asset_json_pack_version = str(asset_packdata['version'])
    asset_json_pack_default = str(asset_packdata['default'])
    asset_infodata = json.loads(asset_data_inf)
            
    if str(asset_infodata['asset_name']) == "MISSING FILE":
        bpy.data.window_managers["WinMan"].inventory_preview = str(asset_json_pack_default+".png")
    asset_json_asset_name = str(asset_infodata['asset_name'])
    asset_json_asset_author = str(asset_infodata['author'])
    asset_json_asset_version = str(asset_infodata['asset_version'])
    
    #drawing the menu
    box = layout.box()
    b = box.row(align=True)
    b.label(text= "Select an asset to append!", icon='BLENDER')
    b = box.row(align=True)
    wm = context.window_manager
    b.template_icon_view(wm, "inventory_preview")
    b = box.row(align=True)
    b.prop(context.scene, "selected_inv_asset")
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

def dlc_presets_UI(self, context, layout, files_list, rig_baked):
    #window setup
    thumbnail = bpy.data.window_managers["WinMan"].my_previews_presets
    thumbnailnopng = thumbnail.split(".")[0]

    #json loader
    try:
        selected_file = files_list[context.scene.get("selected_asset")]
        settings_directory = root_folder+"/ice_cube_data/internal_files/user_packs/rigs/"+selected_file+"/settings.json"


    except:
        settings_directory = root_folder+"/ice_cube_data/internal_files/important/settings.json"


    try:
        selected_file = files_list[context.scene.get("selected_asset")]
        info_directory = root_folder+"/ice_cube_data/internal_files/user_packs/rigs/"+selected_file+"/rigs/"+thumbnailnopng+"/info.json"

    except:
        info_directory = root_folder+"/ice_cube_data/internal_files/important/info.json"




    missing_file_dir_set = root_folder+"/ice_cube_data/internal_files/important/missing_settings.json"
    missing_file_dir_inf = root_folder+"/ice_cube_data/internal_files/important/missing_info.json"

    #read json file
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

    json_pack_name = str(packdata['pack_name'])
    json_pack_author = str(packdata['author'])
    json_pack_version = str(packdata['version'])
    json_pack_default = str(packdata['default'])
    infodata = json.loads(data_inf)

    if str(infodata['rig_name']) == "MISSING FILE":
        bpy.data.window_managers["WinMan"].my_previews_presets = str(json_pack_default+".png")
    json_rig_name = str(infodata['rig_name'])
    json_rig_author = str(infodata['author'])
    json_rig_version = str(infodata['rig_version'])
    json_base_rig = str(infodata['base_rig'])
    json_base_version = str(infodata['base_rig_vers'])
    json_rig_baked = str(infodata['has_baked'])
    scene = context.scene

    #drawing the menu
    box = layout.box()
    b = box.row(align=True)
    b.label(text= "Select a preset to append!", icon='BLENDER')
    b = box.row(align=True)
    wm = context.window_manager
    b.template_icon_view(wm, "my_previews_presets")
    b = box.row(align=True)
    b.prop(scene, "selected_asset")
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