#Libraries
import bpy
import os
from sys import platform
import json
from bpy.props import EnumProperty

from ice_cube import root_folder, dlc_id,dlc_type,dlc_author,dlc_date,cur_asset_id
from ice_cube_data.properties import properties
from ice_cube_data.systems import inventory_system

from ice_cube_data.utils.general_func import GetListIndex, getLanguageTranslation
from ice_cube_data.utils.file_manage import getFiles
from ice_cube_data.utils.selectors import isRigSelected
from ice_cube_data.utils.ui_tools import button_toggle

import ice_cube

def arrowIcon(obj,prop):
    if obj.get(prop):
        icon = 'SORT_ASC'
    else:
        icon = 'SORT_DESC'
    return icon

invalid_platform = "darwin"




def advanced_dlc_ui(self, context, layout, rig_baked, menu_type,icon,scale):
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

    

    if menu_type == "IceCube":

        box = layout.box()
        b = box.row(align=True)
        b.scale_y=scale
        b.prop(obj, "dlc_menu_switcher", text=getLanguageTranslation("ice_cube.ui.tabs.dlc_mode"))
        wm = context.window_manager

    

        if obj.get("dlc_menu_switcher") == 0: #APPEND MENU
            b = box.row(align=True)
            b.scale_y=scale
            b.prop(obj,"ipaneltab6",text=getLanguageTranslation("ice_cube.ui.tabs.dlc_type"))
            b = box.row(align=True)
            b.scale_y=scale
            dlc_sub_box = b.box()
            dlc_sub_row = dlc_sub_box.row(align=True)

            if obj.get("ipaneltab6") == 0: #ASSETS
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

                #if str(asset_infodata['asset_name']) == "MISSING FILE":
                #    bpy.data.window_managers["WinMan"].inventory_preview = str(asset_json_pack_default+".png")
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
                dlc_sub_row.label(text= getLanguageTranslation("ice_cube.ui.tabs.select_asset"), icon='BLENDER')
                dlc_sub_row = dlc_sub_box.row(align=True)
                dlc_sub_row.template_icon_view(wm, "inventory_preview")
                dlc_sub_row = dlc_sub_box.row(align=True)
                dlc_sub_row.prop(scene, "selected_inv_asset",text="")
                dlc_sub_row.operator("refresh.inv_list",text="",icon='FILE_REFRESH')
                dlc_sub_row = dlc_sub_box.row(align=True)
                dlc_sub_row.operator("append.asset", text = getLanguageTranslation("ice_cube.ops.append_selected"))
                if asset_json_customizable:
                    dlc_sub_row.operator("refresh.customizations", text="",icon ='BRUSH_DATA')
                dlc_sub_row = dlc_sub_box.row(align=True)
                dlc_sub_row.operator("custom_presets.open", text = getLanguageTranslation("ice_cube.ops.dlc_folder"))
                dlc_sub_row.operator("template1.download", text = getLanguageTranslation("ice_cube.ops.download_asset_template"))
                
                if asset_json_customizable and cur_asset_id[0] == asset_json_asset_id:
                    if has_entries:
                            dlc_sub_row = dlc_sub_box.row(align=True)
                            dlc_sub_row.prop(scene,"asset_entries",text="")
                    if asset_json_armor_trims:
                        dlc_sub_row = dlc_sub_box.row(align=True)
                        cur_asset_pattern = scene.armor_trim_pattern


                        dlc_sub_row.prop(scene,"armor_trim_pattern",text="",icon_value=trim_icons[cur_asset_pattern].icon_id)
                        if scene.get("armor_trim_pattern") != None and scene.get("armor_trim_pattern") != 0:
                            cur_asset_material = scene.armor_trim_material
                            

                            dlc_sub_row.prop(scene,"armor_trim_material",text="",icon_value=mat_icons[cur_asset_material].icon_id)

                box = layout.box()
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.tabs.asset_pack_info"), icon='INFO')
                try:
                    row_labels = {
                                   "ice_cube.ui.misc.pack_name": asset_json_pack_name,
                                   "ice_cube.ui.misc.pack_author": asset_json_pack_author,
                                   "ice_cube.ui.misc.pack_version": asset_json_pack_version
                                }
                    for label in row_labels:
                        b = box.row(align = True)
                        b.label(text = f"{getLanguageTranslation(label)}: {row_labels[label]}")
                except:
                    b.label(text = "Select a pack from the list")

                box = layout.box()
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.tabs.current_asset_info"), icon='INFO')
                b = box.row(align=True)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_name") + ": " + asset_json_asset_name)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_author") + ": " + asset_json_asset_author)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_version") + ": " + asset_json_asset_version)

            if obj.get("ipaneltab6") == 1: #PRESETS
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

                dlc_sub_row.label(text= getLanguageTranslation("ice_cube.ui.tabs.select_preset"), icon='BLENDER')
                dlc_sub_row = dlc_sub_box.row(align=True)
                dlc_sub_row.template_icon_view(wm, "my_previews_presets")
                dlc_sub_row = dlc_sub_box.row(align=True)
                dlc_sub_row.prop(scene, "selected_rig_preset",text="")
                dlc_sub_row.operator("refresh.rig_list",text="",icon='FILE_REFRESH')
                dlc_sub_row = dlc_sub_box.row(align=True)
                dlc_sub_row.operator("append.preset", text = getLanguageTranslation("ice_cube.ops.append_selected"))
                b1 = dlc_sub_row.row(align=True)
                if rig_baked == True:
                    b1.operator("rig.bakedbutton", text= getLanguageTranslation("ice_cube.ui.misc.baked"), icon= 'LAYER_ACTIVE')
                    if json_rig_baked == "False":
                        rig_baked = False
                else:
                    b1.operator("rig.bakedbutton", text= getLanguageTranslation("ice_cube.ui.misc.normal"), icon= 'LAYER_USED')
                if json_rig_baked == "True":
                    b1.enabled = True
                else:
                    b1.enabled = False
                    if properties.global_rig_baked == True:
                        properties.global_rig_baked = False
                dlc_sub_row = dlc_sub_box.row(align=True)
                dlc_sub_row.operator("custom_presets.open", text = getLanguageTranslation("ice_cube.ops.dlc_folder"))
                dlc_sub_row.operator("template2.download", text = getLanguageTranslation("ice_cube.ops.download_preset_template"))

                box = layout.box()
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.tabs.rig_pack_info"), icon='INFO')
                try:
                    row_labels = {
                                   "ice_cube.ui.misc.pack_name": json_pack_name,
                                   "ice_cube.ui.misc.pack_author": json_pack_author,
                                   "ice_cube.ui.misc.pack_version": json_pack_version
                                }
                    for label in row_labels:
                        b = box.row(align = True)
                        b.label(text = f"{getLanguageTranslation(label)}: {row_labels[label]}")
                except:
                    b.label(text = getLanguageTranslation("ice_cube.errors.no_pack_selected"))

                box = layout.box()
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.current_rig_info"), icon='INFO')
                b = box.row(align=True)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_name") + ": " + json_rig_name)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_author") + ": " + json_rig_author)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_version") + ": " + json_rig_version)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_base_rig") + ": " + json_base_rig)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_base_version") + ": " + json_base_version)
                b = box.row(align=True)
                b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_has_baked") + ": " + json_rig_baked)

        if obj.get("dlc_menu_switcher") == 1: #DOWNLOAD MENU
            box = layout.box()
            b = box.row(align=True)
            b.scale_y=scale
            rig = isRigSelected(context)
            b.label(text = getLanguageTranslation("ice_cube.ui.tabs.dlc_manager"),icon='IMPORT')
            b = box.row(align=True)
            b.scale_y=scale
            b.template_icon_view(wm, "dlc_img_cache_folder")
            b = box.row(align=True)
            b.scale_y=scale
            b.template_list("IC_DLC_UL_available_list_i", "", rig, "ic_dlc_i", rig, "ic_dlc_active_index")
            colb = b.column()
            colb.operator("refresh_grab.dlc", text="", icon='FILE_REFRESH')
            colb.operator("download_selected.dlc", text="", icon='IMPORT')
            b = box.row(align=True)
            b.operator("import.icpreset_file",text=getLanguageTranslation("ice_cube.ops.manually_import_icpreset"),icon='IMPORT')

        if obj.get("dlc_menu_switcher") == 2: #GENERATE MENU
            b.prop(obj,"ipaneltab6",text="")
            b = box.row(align=True)
            b.scale_y=scale

            if obj.get("ipaneltab6") == 0: #ASSETS
                b.label(text=getLanguageTranslation("ice_cube.errors.asset_generation_disabled")) #"Disabled, please use the in the main toolbar under \'Tool\'"
                #b = box.row(align=True)
                #b.enabled = False
                #b1 = b.row(align=True)
                #b1.scale_y=scale
                #b1.prop(obj,"generate_thumbnail",text="Generate Thumbnail?")
                #b1.enabled = False
                #b = box.row(align=True)
                #b.enabled = False
                #b.scale_y=scale
                #b.prop(obj, "target_thumbnail_generate", text="Thumbnail")
                #b = box.row(align=True)
                #b.enabled = False
                #b.scale_y=scale
                #b.prop(obj, "asset_pack_name", text="")
                #b.prop(obj, "entry_name_asset", text="")
                #b = box.row(align=True)
                #b.enabled = False
                #b.scale_y=scale
                #b.prop(obj, "asset_author", text="")
                #b.prop(obj, "asset_version", text="")
                #b = box.row(align=True)
                #b.enabled = False
                #b.scale_y=scale
                #b.operator("generate.asest_pack",text="Generate Pack")

            if obj.get("ipaneltab6") == 1: #PRESETS
                b.prop(obj,"export_to_icpreset",text=getLanguageTranslation("ice_cube.ui.props.use_icpreset"))
                b.prop(obj, "generate_baked", text=getLanguageTranslation("ice_cube.ui.props.generate_baked"))
                b = box.row(align=True)
                b.scale_y=scale
                b.prop(obj,"generate_thumbnail",text=getLanguageTranslation("ice_cube.ui.props.generate_thumbnail"))
                b1 = box.row(align=True)
                baking_box = b1.box()
                baking_bad = baking_box.row(align=True)
                baking_bad.scale_y=scale
                if not obj.generate_baked: baking_bad.enabled = False
                baking_bad.label(text=getLanguageTranslation("ice_cube.ui.tabs.baking_manager"),icon='FILE_ARCHIVE')
                if obj.generate_baked:
                    baking_bad = baking_box.row(align=True)
                    baking_bad.scale_y=scale
                    baking_bad.prop(obj,"bake_eye_textures",text=getLanguageTranslation("ice_cube.ui.props.bake_eyes"))
                    baking_bad.prop(obj,"bake_all_unused_features",text=getLanguageTranslation("ice_cube.ui.props.bake_unused"))
                    baking_bad = baking_box.row(align=True)
                    baking_bad.scale_y=scale
                    disable_row = baking_bad
                    if not obj.bake_eye_textures:
                        disable_row.enabled = False
                    disable_row.prop(obj,"split_eye_bakes",text=getLanguageTranslation("ice_cube.ui.props.split_baked_eyes"))
                    disable_row.prop(obj,"eye_bake_resolution",text=getLanguageTranslation("ice_cube.ui.props.eye_bake_resolution"))
                b1 = box.row(align=True)
                b1.scale_y=scale
                b1.prop(obj, "target_thumbnail_generate", text=getLanguageTranslation("ice_cube.ui.props.thumbnail_path"))
                if obj.get("generate_thumbnail") == True:
                    b1.enabled = False
                b = box.row(align=True)
                if obj.get("export_to_icpreset") == False:
                    b.scale_y=scale
                    b.prop(obj, "asset_pack_name", text="")
                    b.prop(obj, "entry_name_asset", text="")
                    b = box.row(align=True)
                    b.scale_y=scale
                    b.prop(obj, "asset_author", text="")
                    b.prop(obj, "asset_version", text="")
                    b = box.row(align=True)
                    b.scale_y=scale
                    b.operator("generate.asest_pack",text=getLanguageTranslation("ice_cube.ops.generate_pack"))
                else:
                    b.scale_y=scale
                    b.prop(obj,"export_icpreset_file",text="")
                    b = box.row(align=True)
                    b.prop(obj, "asset_pack_name", text="")
                    b.prop(obj, "entry_name_asset", text="")
                    b = box.row(align=True)
                    b.scale_y=scale
                    b.prop(obj, "asset_author", text="")
                    b.prop(obj, "asset_version", text="")
                    b = box.row(align=True)
                    b.scale_y=scale
                    b.operator("generate.asest_pack",text=getLanguageTranslation("ice_cube.ops.export_icpreset"))
                
                

    elif menu_type == "ToolMenuAppend":
        box = layout.box()
        b = box.row(align=True)
        b.scale_y=scale
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
            b.scale_y=scale
            b.label(text= getLanguageTranslation("ice_cube.ui.tabs.select_preset"), icon='BLENDER')
            b = box.row(align=True)
            b.scale_y=scale
            b.template_icon_view(wm, "my_previews_presets")
            b = box.row(align=True)
            b.scale_y=scale
            b.prop(scene, "selected_rig_preset",text="")
            b.operator("refresh.rig_list",text="",icon='FILE_REFRESH')
            b = box.row(align=True)
            b.scale_y=scale
            b.operator("append.preset", text = getLanguageTranslation("ice_cube.ops.append_selected"))
            b1 = b.row(align=True)
            if rig_baked == True:
                b1.operator("rig.bakedbutton", text= getLanguageTranslation("ice_cube.ui.misc.baked"), icon= 'LAYER_ACTIVE')
                if json_rig_baked == "False":
                    rig_baked = False
            else:
                b1.operator("rig.bakedbutton", text= getLanguageTranslation("ice_cube.ui.misc.normal"), icon= 'LAYER_USED')
            if json_rig_baked == "True":
                b1.enabled = True
            else:
                b1.enabled = False
                if properties.global_rig_baked == True:
                    properties.global_rig_baked = False
            b = box.row(align=True)
            b.scale_y=scale
            b.operator("custom_presets.open", text = getLanguageTranslation("ice_cube.ops.dlc_folder"))
            b.operator("template2.download", text = getLanguageTranslation("ice_cube.ops.download_preset_template"))
            box = layout.box()
            b = box.row(align=True)
            b.label(text="Rig Pack Info:", icon='INFO')
            try:
                row_labels = {
                               "ice_cube.ui.misc.pack_name": json_pack_name,
                               "ice_cube.ui.misc.pack_author": json_pack_author,
                               "ice_cube.ui.misc.pack_version": json_pack_version
                            }
                for label in row_labels:
                    b = box.row(align = True)
                    b.label(text = f"{getLanguageTranslation(label)}: {row_labels[label]}")
            except:
                b.label(text = "No Pack Selected!")

            box = layout.box()
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.current_rig_info"), icon='INFO')
            b = box.row(align=True)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_name") + ": " + json_rig_name)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_author") + ": " + json_rig_author)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_version") + ": " + json_rig_version)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_base_rig") + ": " + json_base_rig)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_base_version") + ": " + json_base_version)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_has_baked") + ": " + json_rig_baked)
        
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
            b.scale_y=scale
            b.label(text= getLanguageTranslation("ice_cube.ui.tabs.select_asset"), icon='BLENDER')
            b = box.row(align=True)
            b.scale_y=scale
            b.template_icon_view(wm, "inventory_preview")
            b = box.row(align=True)
            b.scale_y=scale
            b.prop(scene, "selected_inv_asset",text="")
            b.operator("refresh.inv_list",text="",icon='FILE_REFRESH')
            b = box.row(align=True)
            b.scale_y=scale
            b.operator("append.asset", text = getLanguageTranslation("ice_cube.ops.append_selected"))
            if asset_json_customizable:
                b.operator("refresh.customizations", text="",icon ='BRUSH_DATA')
            b = box.row(align=True)
            b.scale_y=scale
            b.operator("custom_presets.open", text = getLanguageTranslation("ice_cube.ops.dlc_folder"))
            b.operator("template1.download", text = getLanguageTranslation("ice_cube.ops.download_asset_template"))
            
            if asset_json_customizable and cur_asset_id[0] == asset_json_asset_id:
                if has_entries:
                        b = box.row(align=True)
                        b.scale_y=scale
                        b.prop(scene,"asset_entries",text="")
                if asset_json_armor_trims:
                    b = box.row(align=True)
                    b.scale_y=scale
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
                               "ice_cube.ui.misc.pack_name": asset_json_pack_name,
                               "ice_cube.ui.misc.pack_author": asset_json_pack_author,
                               "ice_cube.ui.misc.pack_version": asset_json_pack_version
                            }
                for label in row_labels:
                    b = box.row(align = True)
                    b.label(text = f"{getLanguageTranslation(label)}: {row_labels[label]}")
            except:
                b.label(text = "Select a pack from the list")

            box = layout.box()
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.tabs.current_asset_info"), icon='INFO')
            b = box.row(align=True)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_name") + ": " + asset_json_asset_name)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_author") + ": " + asset_json_asset_author)
            b = box.row(align=True)
            b.label(text=getLanguageTranslation("ice_cube.ui.misc.current_version") + ": " + asset_json_asset_version)
            
    elif menu_type == "ToolMenuGenerate":
        box = layout.box()
        b = box.row(align=True)
        b.scale_y=scale
        b.label(text=getLanguageTranslation("ice_cube.ui.tabs.select_generator"),icon='GEOMETRY_NODES')
        b = box.row(align=True)

        b = box.row(align=True)
        b.scale_y=scale
        b.prop(scene, "target_thumbnail_generate", text=getLanguageTranslation("ice_cube.ui.props.thumbnail_path"))
        b = box.row(align=True)
        b.scale_y=scale
        b.prop(scene, "asset_pack_name", text="")
        b.prop(scene, "entry_name_asset", text="")
        b = box.row(align=True)
        b.scale_y=scale
        b.prop(scene, "asset_author", text="")
        b.prop(scene, "asset_version", text="")
        b = box.row(align=True)
        b.scale_y=scale
        newbox = box.box()
        b1 = newbox.row(align=True)
        b1.prop(scene,"asset_customizable",text=getLanguageTranslation("ice_cube.ui.props.asset_customizable"))
        if scene.asset_customizable:
            b1.prop(scene,"has_entries",text=getLanguageTranslation("ice_cube.ui.props.asset_has_entries"))
            b1 = newbox.row(align=True)
            b1.prop(scene,"supports_armor_trims",text=getLanguageTranslation("ice_cube.ui.props.asset_supports_trims"))
            b1.prop(scene,"leggings_half",text=getLanguageTranslation("ice_cube.ui.props.asset_leggings_half"))
            b1 = newbox.row(align=True)
            b1.prop(scene,"materialType",text=getLanguageTranslation("ice_cube.ui.props.material"))
        b = box.row(align=True)
        b.scale_y=scale
        b.operator("generate.asest_pack_global",text=getLanguageTranslation("ice_cube.ops.generate_pack"))

def advanced_parenting_ui(self, context, layout,scale):
    obj = context.object
    box = layout.box()
    if obj.upgraded_ui:
        box.label(text= "OUTDATED RIG", icon= 'ERROR')
        return{'FINISHED'}
    box.label(text= "Parenting", icon= 'FILE_PARENT')
    b = box.row(align=True)
    b.scale_y=scale
    parenting_box = b.box()
    parenting_row = parenting_box.row(align=True)
    parenting_row.operator("parent.allcollections",text=getLanguageTranslation("ice_cube.ops.update_parenting"))
        

    b = box.row(align=True)
    b.scale_y=scale
    guide_box = b.box()
    guide_row = guide_box.row(align=True)
    guide_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.advanced_guide"),icon='HELP')
    if button_toggle(obj,guide_row,"advanced_guide"):
        guide_row = guide_box.row(align=True)
        guide_row.label(text= getLanguageTranslation("ice_cube.ui.misc.advanced_guide_1")) #"To parent something to the rig and make it"
        guide_row = guide_box.row(align=True)
        guide_row.label(text= getLanguageTranslation("ice_cube.ui.misc.advanced_guide_2")) #"follow the bends, drag your object into the correct"
        guide_row = guide_box.row(align=True)
        guide_row.label(text= getLanguageTranslation("ice_cube.ui.misc.advanced_guide_3")) #"collection under Ice Cube > Main Mesh"

def advanced_system_ui(self, context, layout, obj,scale):
    obj = context.object
    box = layout.box()
    box.label(text= "System", icon= 'SYSTEM')
    b = box.row(align=True)
    b.scale_y=scale
    update_box = b.box()
    update_row = update_box.row(align=True)
    update_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.update_manager"),icon='URL')
    if button_toggle(obj,update_row,"update_manager"):
        if platform == invalid_platform:
            update_row = update_box.row(align=True)
            update_row.label(text= getLanguageTranslation("ice_cube.errors.macos_not_available"), icon='ERROR') #"UPDATE MANAGER NOT SUPPORTED ON MACOS!"
        else:
            update_row = update_box.row(align=True)
            update_row.label(text=getLanguageTranslation("ice_cube.errors.do_not_restart_install"),icon='ERROR') #"WARNING: DO NOT RESTART WHEN INSTALLING"
            update_row = update_box.row(align=True)
            if ice_cube.update_available == True:
                update_row.operator("install.update", text=getLanguageTranslation("ice_cube.ops.install_update"), icon='MOD_WAVE')
            else:
                update_row.operator("ice_cube_check.updates", text=getLanguageTranslation("ice_cube.ops.check_for_updates"), icon='FILE_REFRESH')
    b = box.row(align=True)
    b.scale_y=scale
    settings_box = b.box()
    settings_row = settings_box.row(align=True)
    settings_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.settings_manager"),icon='TOOL_SETTINGS')
    if button_toggle(obj,settings_row,"setting_data_manager"):
        if platform == invalid_platform:
            settings_row = settings_box.row(align=True)
            settings_row.label(text= getLanguageTranslation("ice_cube.errors.macos_not_available"), icon='ERROR')
            settings_row = settings_box.row(align=True)
        else:
            settings_row = settings_box.row(align=True)

            clipboard = settings_row
            clipboard.prop(obj,"prop_clipboard",text=getLanguageTranslation("ice_cube.ui.props.use_clipboard"))
            settings_row.prop(obj,"ipaneltab7",text="")
            if obj.get("ipaneltab7") == 0:
                if obj.get("prop_clipboard") == 0:
                    settings_row = settings_box.row(align=True)
                    settings_row.prop(obj,"export_settings_filepath",text=getLanguageTranslation("ice_cube.ui.props.export_location"),icon='EXPORT')
                    settings_row = settings_box.row(align=True)
                    settings_row.prop(obj,"export_settings_name",text=getLanguageTranslation("ice_cube.ui.props.export_filename"),icon='INFO')
                    export_name = "ice_cube.ops.export_to_file"
                else:
                    export_name = "ice_cube.ops.export_to_clipboard"
                settings_row = settings_box.row(align=True)
                settings_row.operator("export.settings",text=getLanguageTranslation(export_name))
                settings_row = settings_box.row(align=True)
            else:
                settings_row = settings_box.row(align=True)
                settings_row.prop(obj,"import_settings_filepath",text=getLanguageTranslation("ice_cube.ui.props.import_location"),icon='IMPORT')
                settings_row = settings_box.row(align=True)
                settings_row.operator("import.settings", text=getLanguageTranslation("ice_cube.ops.import_from_clipboard") if obj.get("prop_clipboard") else getLanguageTranslation("ice_cube.ops.import_from_file"))
                settings_row = settings_box.row(align=True)
        
        settings_row.operator("ice_cube.updatedefaultrig",text=getLanguageTranslation("ice_cube.ops.update_default_rig"))
        settings_row.operator("ice_cube.resetdefaultrig",text=getLanguageTranslation("ice_cube.ops.reset_default_rig"))

        settings_row = settings_box.row(align=True)
        settings_row.operator("reset.settings",text=getLanguageTranslation("ice_cube.ops.reset_ice_cube_settings"))
        settings_row = settings_box.row(align=True)
        settings_row.operator("reset_to_default.icecube",text=getLanguageTranslation("ice_cube.ops.full_ice_cube_reset"))
        settings_row.prop(obj, "confirm_ice_cube_reset", toggle=True, text="", icon="ERROR")
        
    b = box.row(align=True)
    b.scale_y=scale
    backup_box = b.box()
    backup_row = backup_box.row(align=True)
    backup_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.backup_manager"),icon='TEMP')
    if button_toggle(obj,backup_row,"backup_data_manager"):
        backup_row = backup_box.row(align=True)
        backups_folder = root_folder+"/backups"
        backup_folder_scan = os.listdir(backups_folder)
        if platform == invalid_platform:
            backup_row = backup_box.row(align=True)
            backup_row.label(text= getLanguageTranslation("ice_cube.errors.macos_not_available"), icon='ERROR')
        else:
            virtual_ice_cube = root_folder+""
            virtual_ice_cube = os.path.normpath(virtual_ice_cube)
            if os.path.exists(backups_folder):
                pass
            else:
                os.mkdir(backups_folder)

            backup_row_box = backup_row.box()
            rig = isRigSelected(context)
            backup_row_box_row = backup_row_box.row(align=True)
            backup_row_box_row.prop(obj, "backup_name", text=getLanguageTranslation("ice_cube.ui.misc.name"), icon='FILE_BACKUP')
            backup_row_box_row = backup_row_box.row(align=True)
            backup_row_box_row.template_list("IC_BACKUP_UL_list_i", "", rig, "ic_backups_i", rig, "ic_backups_active_index")
            colb = backup_row_box_row.column(align=True)
            colb.operator("create.backup", text="", icon='ADD')
            colb.operator("delete.backup", text="", icon='REMOVE')
            colb.operator("refresh.backup", text="", icon='FILE_REFRESH')
            colb.operator("load.backup", text="", icon='IMPORT')
    
    b = box.row(align=True)
    b.scale_y=scale
    if obj.upgraded_ui:
        b.label(text=getLanguageTranslation("ice_cube.errors.outdated_rig_baking"),icon='ERROR')
    else:
        baking_box = b.box()
        baking_bad = baking_box.row(align=True)
        baking_bad.label(text=getLanguageTranslation("ice_cube.ui.tabs.baking_manager"),icon='FILE_ARCHIVE')
        if button_toggle(obj,baking_bad,"baking_data_manager"):
            baking_bad = baking_box.row(align=True)
            baking_bad.prop(obj,"bake_eye_textures",text=getLanguageTranslation("ice_cube.ui.props.bake_eyes"))
            baking_bad.prop(obj,"bake_all_unused_features",text=getLanguageTranslation("ice_cube.ui.props.bake_unused"))
            baking_bad = baking_box.row(align=True)
            disable_row = baking_bad
            if not obj.bake_eye_textures:
                disable_row.enabled = False
            disable_row.prop(obj,"split_eye_bakes",text=getLanguageTranslation("ice_cube.ui.props.split_baked_eyes"))
            disable_row.prop(obj,"eye_bake_resolution",text=getLanguageTranslation("ice_cube.ui.props.eye_bake_resolution"))
            baking_bad = baking_box.row(align=True)
            baking_bad.operator("ice_cube.bake_rig",text=getLanguageTranslation("ice_cube.ops.bake_rig"),icon='FILE_TICK')
            baking_bad.prop(obj,"confirm_rig_bake",text="",icon='ERROR')

            

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