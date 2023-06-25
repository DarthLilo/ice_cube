#Libraries
import bpy
import os
import json
from bpy.props import EnumProperty

from ice_cube import root_folder, dlc_id,dlc_type,dlc_author,dlc_date,cur_asset_id
from ice_cube_data.properties import properties
from ice_cube_data.systems import inventory_system

from ice_cube_data.utils.general_func import GetListIndex
from ice_cube_data.utils.file_manage import getFiles
from ice_cube_data.utils.selectors import isRigSelected







def dlc_menu(self, context, layout, rig_baked, menu_type,icon):
    scene = context.scene
    obj = context.object
    pcoll = icon["main"]
    has_entries = False

    #icons
    mat_icons = {
        "Amethyst" : pcoll["Amethyst"],
        "Copper" : pcoll["Copper"],
        "Diamond" : pcoll["Diamond"],
        "Emerald" : pcoll["Emerald"],
        "Gold" : pcoll["Gold"],
        "Iron" : pcoll["Iron"],
        "Lapis" : pcoll["Lapis"],
        "Netherite" : pcoll["Netherite"],
        "Quartz" : pcoll["Quartz"],
        "Redstone" : pcoll["Redstone"],
    }
    trim_icons = {
        "none" : pcoll["None"],
        "Coast" : pcoll["Coast"],
        "Dune" : pcoll["Dune"],
        "Eye" : pcoll["Eye"],
        "Host" : pcoll["Host"],
        "Raiser" : pcoll["Raiser"],
        "Rib" : pcoll["Rib"],
        "Sentry" : pcoll["Sentry"],
        "Shaper" : pcoll["Shaper"],
        "Silence" : pcoll["Silence"],
        "Snout" : pcoll["Snout"],
        "Spire" : pcoll["Spire"],
        "Tide" : pcoll["Tide"],
        "Vex" : pcoll["Vex"],
        "Ward" : pcoll["Ward"],
        "Wayfinder" : pcoll["Wayfinder"],
        "Wild" : pcoll["Wild"]
    }

    

    if menu_type is "IceCube":

        box = layout.box()
        b = box.row(align=True)
        b.prop(obj, "dlc_menu_switcher", text="")
        wm = context.window_manager

    

        if obj.get("dlc_menu_switcher") is 0: #APPEND MENU
            b.prop(obj,"ipaneltab6",text="")

            if obj.get("ipaneltab6") is 0: #ASSETS
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
                asset_json_asset_id = str(asset_infodata['asset_id'])
                asset_json_asset_author = str(asset_infodata['author'])
                asset_json_asset_version = str(asset_infodata['asset_version'])
                asset_json_customizable = bool(asset_infodata['customizable'])
                if asset_json_customizable:
                    asset_json_armor_trims = bool(asset_infodata['asset_settings']['supports_armor_trims']) #Armor Trim Support

                    try: #Checking For Entries
                        if list(asset_infodata['asset_settings']['entries']):
                            has_entries = True
                            entry_data = list(asset_infodata['asset_settings']['entries'])
                        else:
                            has_entries = False
                    except:
                        pass
                
                
                    

                #Updating Customization Panel

                b = box.row(align=True)
                b.label(text= "Select an asset to append!", icon='BLENDER')
                b = box.row(align=True)
                b.template_icon_view(wm, "inventory_preview")
                b = box.row(align=True)
                b.prop(scene, "selected_inv_asset",text="")
                b.operator("refresh.inv_list",text="",icon='FILE_REFRESH')
                b = box.row(align=True)
                b.operator("append.asset", text = "Append Selected")
                if asset_json_customizable:
                    b.operator("refresh.customizations", text="",icon ='BRUSH_DATA')
                b = box.row(align=True)
                b.operator("custom_presets.open", text = "DLC Folder")
                b.operator("template1.download", text = "Asset Template")
                
                if asset_json_customizable and cur_asset_id[0] == asset_json_asset_id:
                    if has_entries:
                            b = box.row(align=True)
                            b.prop(scene,"asset_entries",text="")
                    if asset_json_armor_trims:
                        b = box.row(align=True)
                        cur_asset_pattern = scene.armor_trim_pattern


                        b.prop(scene,"armor_trim_pattern",text="",icon_value=trim_icons[cur_asset_pattern].icon_id)
                        if scene.get("armor_trim_pattern") != None and scene.get("armor_trim_pattern") != 0:
                            cur_asset_material = scene.armor_trim_material
                            

                            b.prop(scene,"armor_trim_material",text="",icon_value=mat_icons[cur_asset_material].icon_id)

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

            if obj.get("ipaneltab6") is 1: #PRESETS
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
            box = layout.box()
            b = box.row(align=True)
            rig = isRigSelected(context)
            b.label(text = "DLC Manager",icon='IMPORT')
            b = box.row(align=True)
            b.template_icon_view(wm, "dlc_img_cache_folder")
            b = box.row(align=True)
            b.template_list("IC_DLC_available_list_i", "", rig, "ic_dlc_i", rig, "ic_dlc_active_index")
            colb = b.column()
            colb.operator("refresh_grab.dlc", text="", icon='FILE_REFRESH')
            colb.operator("download_selected.dlc", text="", icon='IMPORT')

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
                b1 = box.row(align=True)
                b1.prop(obj, "target_thumbnail_generate", text="Thumbnail")
                if obj.get("generate_thumbnail") == True:
                    b1.enabled = False
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

    elif menu_type is "ToolMenuAppend":
        box = layout.box()
        b = box.row(align=True)
        wm = context.window_manager
        b.prop(scene,"append_tab_global",text="")

        if scene.append_tab_global == 'two':
    
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
        
        elif scene.append_tab_global == 'one':
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
            asset_json_asset_id = str(asset_infodata['asset_id'])
            asset_json_asset_author = str(asset_infodata['author'])
            asset_json_asset_version = str(asset_infodata['asset_version'])
            asset_json_customizable = bool(asset_infodata['customizable'])
            if asset_json_customizable:
                asset_json_armor_trims = bool(asset_infodata['asset_settings']['supports_armor_trims']) #Armor Trim Support

                try: #Checking For Entries
                    if list(asset_infodata['asset_settings']['entries']):
                        has_entries = True
                        entry_data = list(asset_infodata['asset_settings']['entries'])
                    else:
                        has_entries = False
                except:
                    pass
            
            
                

            #Updating Customization Panel

            b = box.row(align=True)
            b.label(text= "Select an asset to append!", icon='BLENDER')
            b = box.row(align=True)
            b.template_icon_view(wm, "inventory_preview")
            b = box.row(align=True)
            b.prop(scene, "selected_inv_asset",text="")
            b.operator("refresh.inv_list",text="",icon='FILE_REFRESH')
            b = box.row(align=True)
            b.operator("append.asset", text = "Append Selected")
            if asset_json_customizable:
                b.operator("refresh.customizations", text="",icon ='BRUSH_DATA')
            b = box.row(align=True)
            b.operator("custom_presets.open", text = "DLC Folder")
            b.operator("template1.download", text = "Asset Template")
            
            if asset_json_customizable and cur_asset_id[0] == asset_json_asset_id:
                if has_entries:
                        b = box.row(align=True)
                        b.prop(scene,"asset_entries",text="")
                if asset_json_armor_trims:
                    b = box.row(align=True)
                    cur_asset_pattern = scene.armor_trim_pattern


                    b.prop(scene,"armor_trim_pattern",text="",icon_value=trim_icons[cur_asset_pattern].icon_id)
                    if scene.get("armor_trim_pattern") != None and scene.get("armor_trim_pattern") != 0:
                        cur_asset_material = scene.armor_trim_material
                        

                        b.prop(scene,"armor_trim_material",text="",icon_value=mat_icons[cur_asset_material].icon_id)

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
    elif menu_type is "ToolMenuGenerate":
        box = layout.box()
        b = box.row(align=True)
        b.label(text="Select Generator Type",icon='GEOMETRY_NODES')
        b = box.row(align=True)

        b = box.row(align=True)
        b.prop(scene, "target_thumbnail_generate", text="Thumbnail")
        b = box.row(align=True)
        b.prop(scene, "asset_pack_name", text="")
        b.prop(scene, "entry_name_asset", text="")
        b = box.row(align=True)
        b.prop(scene, "asset_author", text="")
        b.prop(scene, "asset_version", text="")
        b = box.row(align=True)
        newbox = box.box()
        b1 = newbox.row(align=True)
        b1.prop(scene,"asset_customizable",text="Customizable")
        if scene.asset_customizable:
            b1.prop(scene,"has_entries",text="Has Entries")
            b1 = newbox.row(align=True)
            b1.prop(scene,"supports_armor_trims",text="Armor Trims")
            b1.prop(scene,"leggings_half",text="Leggings Half")
            b1 = newbox.row(align=True)
            b1.prop(scene,"materialType",text="Material")
        b = box.row(align=True)
        b.operator("generate.asest_pack_global",text="Generate Pack")

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