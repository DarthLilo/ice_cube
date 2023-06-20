#Libraries
import bpy
import os
import bpy.utils.previews
from bpy.props import EnumProperty
from bpy.types import WindowManager
from sys import platform
import json

from ice_cube import root_folder, dlc_id,dlc_type,dlc_author, settings_file, cur_date, valid_dlcs

#Custom Files
from ice_cube_data.properties import properties
from ice_cube_data.operators import main_operators, os_management
from ice_cube_data.operators.web import check_for_updates_func, check_for_updates_auto
from ice_cube_data.systems import inventory_system, skin_downloader


#Custom Functions
from ice_cube_data.utils.selectors import isRigSelected, main_face
from ice_cube_data.utils.file_manage import getFiles, open_json
from ice_cube_data.utils.general_func import GetListIndex

#UI Panels
from ice_cube_data.ui import credits_info
from ice_cube_data.ui.main import bone_layers, general_settings
from ice_cube_data.ui.customization import custom_general, mesh, misc
from ice_cube_data.ui.materials import skin_material, eye_material, misc_material
from ice_cube_data.ui.advanced import dlc_ui, parenting, downloads, adv_misc

import ice_cube

#File Variables
rig_id = "ice_cube"

#InFileDefs
def presets_menu(self, context):
    """presets menu thing"""
    enum_items = []
    scene = context.scene

    if context is None:
        return enum_items
    
    cur_selected_rig = scene.selected_rig_preset

    if cur_selected_rig != "NONE":
        thumbnail_directory = root_folder+"/ice_cube_data/internal_files/user_packs/rigs/"+cur_selected_rig+"/thumbnails"
    else:
        thumbnail_directory = root_folder+"/ice_cube_data/internal_files/important/thumbnails"

    filepath  = thumbnail_directory


    wm = context.window_manager
    directory = filepath

    pcoll = preview_collections["main"]

    if directory == pcoll.my_previews_presets:
        return pcoll.my_previews_presets


    if directory and os.path.exists(directory):
        image_paths = []
        for img in os.listdir(directory):
            if img.lower().endswith(".png"):
                image_paths.append(img)

        for i, name in enumerate(image_paths):
            filepath = os.path.join(directory, name)
            icon = pcoll.get(name)
            if not icon:
                thumb = pcoll.load(name, filepath, 'IMAGE')
            else:
                thumb = pcoll[name]
            enum_items.append((name, name, "", thumb.icon_id, i))

    pcoll.my_previews_presets = enum_items
    pcoll.my_previews_presets_dir = directory
    return pcoll.my_previews_presets

def inventory_menu(self, context):
    """inventory menu thing"""
    enum_items = []
    cur_selected_asset = context.scene.selected_inv_asset

    if context is None:
        return enum_items


    if cur_selected_asset != "NONE":
        thumbnail_directory = root_folder+"/ice_cube_data/internal_files/user_packs/inventory/"+cur_selected_asset+"/thumbnails"
    else:
        thumbnail_directory = root_folder+"/ice_cube_data/internal_files/important/thumbnails"

    filepath  = thumbnail_directory


    wm = context.window_manager
    directory = filepath

    pcoll = preview_collections["main"]

    if directory == pcoll.inventory_preview:
        return pcoll.inventory_preview


    if directory and os.path.exists(directory):
        image_paths = []
        for img in os.listdir(directory):
            if img.lower().endswith(".png"):
                image_paths.append(img)

        for i, name in enumerate(image_paths):
            filepath = os.path.join(directory, name)
            icon = pcoll.get(name)
            if not icon:
                thumb = pcoll.load(name, filepath, 'IMAGE')
            else:
                thumb = pcoll[name]
            enum_items.append((name, name, "", thumb.icon_id, i))

    pcoll.inventory_preview = enum_items
    pcoll.inventory_preview_dir = directory
    return pcoll.inventory_preview

def skins_menu(self, context):
    """skins menu thing"""
    enum_items = []

    if context is None:
        return enum_items


    skin_path = root_folder+"/ice_cube_data/internal_files/skins"

    filepath  = skin_path

    wm = context.window_manager
    directory = filepath

    pcoll = preview_collections["main"]

    if directory == pcoll.skins_folder:
        return pcoll.skins_folder

    if directory and os.path.exists(directory):
        image_paths = []
        for img in os.listdir(directory):
            if img.lower().endswith(".png"):
                image_paths.append(img)

        for i, name in enumerate(image_paths):
            filepath = os.path.join(directory, name)
            icon = pcoll.get(name)
            if not icon:
                thumb = pcoll.load(name, filepath, 'IMAGE')
            else:
                thumb = pcoll[name]
            enum_items.append((name, name, "", thumb.icon_id, i))

    pcoll.skins_folder = enum_items
    pcoll.skins_folder_dir = directory
    return pcoll.skins_folder

def dlc_img_cache(self, context):
    """dlc img cache thing"""
    enum_items = []

    if context is None:
        return enum_items

    filepath = root_folder+"/cache"

    wm = context.window_manager
    directory = filepath

    pcoll = preview_collections["main"]

    if directory == pcoll.dlc_img_cache_folder:
        return pcoll.dlc_img_cache_folder
    
    obj=context.object
    dlc_storage = obj.ic_dlc_i
    dlc_index = obj.ic_dlc_active_index
    dlc_data_list = []

    try:
        if directory and os.path.exists(directory):
            image_paths = []
            for img in os.listdir(directory):

                img_name = str(img).split(".png")[0]
                for i in dlc_storage:
                    dlc_data_list.append(str(i.name).split("|")[3])
                selected_dlc = dlc_data_list[dlc_index]
                cur_dlc_data = valid_dlcs[selected_dlc]['dlc_id']
                if img_name == cur_dlc_data:
                    image_paths.append(img)

            for i, name in enumerate(image_paths):
                filepath = os.path.join(directory, name)
                icon = pcoll.get(name)
                if not icon:
                    thumb = pcoll.load(name, filepath, 'IMAGE')
                else:
                    thumb = pcoll[name]
                enum_items.append((name, name, "", thumb.icon_id, i))
    except:
        pass

    pcoll.dlc_img_cache_folder = enum_items
    pcoll.dlc_img_cache_folder_dir = directory
    return pcoll.dlc_img_cache_folder

class IC_Panel(bpy.types.Panel):
    bl_label = "Ice Cube"
    bl_idname = "ice_cube_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Ice Cube'
    
    @classmethod
    def poll(self, context):
        rig = isRigSelected(context)
        try:
            return (rig.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        obj = context.object
        row = layout.row()

        if ice_cube.has_checked_for_updates == False:
            check_for_updates_auto()
        
        

        #custom variables
        rig = isRigSelected(context)
        face = main_face(rig)
        skin_nodes = face.material_slots[0].material.node_tree
        skin_mat = skin_nodes.nodes['Skin Tex']

        #Draw the panel
        credits_info.credits_ui_panel(self,context,preview_collections)

        #tab switcher
        box = layout.box() #UNCOMMENTING WILL DRAW BOX
        b = box.row(align=True)
        b.label(text= "Settings Tab", icon= 'EVENT_TAB')
        b = box.row(align=True)
        b.prop(obj, "ipaneltab1", text = "the funny", expand=True)
        b = box.row(align=True)
        for i in range(0,4):
            if obj.get("ipaneltab1") == i:
                b.prop(obj, f"ipaneltab{str(i + 2)}", text = "the funny", expand=True)
        
        #tabs/Main
        if obj.get("ipaneltab1") == 0: #Main
            if obj.get("ipaneltab2") == 0: #Bone Layers
                bone_layers.bone_layers_UI(self, context, layout, obj)
            if obj.get("ipaneltab2") == 1: #General Settings
                general_settings.general_settings_main_UI(self, context, layout, obj, preview_collections)
        #tabs/Customization
        if obj.get("ipaneltab1") == 1: #Customization
            if obj.get("ipaneltab3") == 0: #General
                custom_general.customization_general_UI(self, context, layout, obj)
            if obj.get("ipaneltab3") == 1: #Mesh
                mesh.custom_mesh_UI(self, context, layout, obj)
            if obj.get("ipaneltab3") == 2: #Misc
                misc.custom_misc_UI(self, context, layout, obj)
        #tabs/Materials
        if obj.get("ipaneltab1") == 2: #Materials
            if obj.get("ipaneltab4") == 0: #Skin
                skin_material.skin_material_UI(self, context, layout, skin_mat, face)
            if obj.get("ipaneltab4") == 1: #Eyes
                eye_material.eye_mat_UI(self, context, face)
            if obj.get("ipaneltab4") == 2: #Misc
                misc_material.misc_material_UI(self, context, layout, face)
        #tabs/Advanced
        if obj.get("ipaneltab1") == 3: #Advanced
            if obj.get("ipaneltab5") == 0: #DLC
                dlc_ui.dlc_menu(self,context,layout, properties.global_rig_baked, True, preview_collections)
            if obj.get("ipaneltab5") == 1: #Parenting
                parenting.parenting_UI(self, context, layout, properties.global_rig_baked)
            if obj.get("ipaneltab5") == 2: #Downloads
                downloads.downloads_UI(self, context, layout, obj)
            if obj.get("ipaneltab5") == 3: #Misc
                adv_misc.advanced_misc_UI(self, context, layout, obj)

def menu_function_thing(self, context):
    layout = self.layout
    pcoll = preview_collections["main"]
    my_icon = pcoll["Ice_Cube"]
    layout.operator("append.defaultrig", icon_value = my_icon.icon_id)

class ToolsAppendMenu(bpy.types.Panel):
    bl_label = "Append Preset"
    bl_idname = "ToolsAppendIceCube"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        obj = context.object
        row = layout.row()

        dlc_ui.dlc_menu(self,context,layout, properties.global_rig_baked, False)



#Register

classes = [IC_Panel,
           ToolsAppendMenu
           ]

preview_collections = {}

def register():
    WindowManager.my_previews_presets = EnumProperty(
        items=presets_menu)

    WindowManager.skins_folder = EnumProperty(
        items=skins_menu)

    WindowManager.dlc_img_cache_folder = EnumProperty(
        items=dlc_img_cache)
    
    WindowManager.inventory_preview = EnumProperty(
       items=inventory_menu)

    pcoll = bpy.utils.previews.new()
    
    my_icons_dir = os.path.normpath(f"{root_folder}/ice_cube_data/internal_files/icons")
    pcoll.load("DarthLilo", os.path.join(my_icons_dir, "DarthLilo.png"), 'IMAGE')
    pcoll.load("Alex", os.path.join(my_icons_dir, "Alex.png"), 'IMAGE')
    pcoll.load("Steve", os.path.join(my_icons_dir, "Steve.png"), 'IMAGE')
    pcoll.load("Ice_Cube", os.path.join(my_icons_dir, "ice_cube.png"), 'IMAGE')
    #mat icons
    pcoll.load("Amethyst", os.path.join(my_icons_dir,"amethyst_shard.png"), 'IMAGE')
    pcoll.load("Copper", os.path.join(my_icons_dir,"copper_ingot.png"), 'IMAGE')
    pcoll.load("Diamond", os.path.join(my_icons_dir,"diamond.png"), 'IMAGE')
    pcoll.load("Emerald", os.path.join(my_icons_dir,"emerald.png"), 'IMAGE')
    pcoll.load("Gold", os.path.join(my_icons_dir,"gold_ingot.png"), 'IMAGE')
    pcoll.load("Iron", os.path.join(my_icons_dir,"iron_ingot.png"), 'IMAGE')
    pcoll.load("Lapis", os.path.join(my_icons_dir,"lapis_lazuli.png"), 'IMAGE')
    pcoll.load("Netherite", os.path.join(my_icons_dir,"netherite_ingot.png"), 'IMAGE')
    pcoll.load("Quartz", os.path.join(my_icons_dir,"quartz.png"), 'IMAGE')
    pcoll.load("Redstone", os.path.join(my_icons_dir,"redstone.png"), 'IMAGE')
    #trim icons
    pcoll.load("None", os.path.join(my_icons_dir,"Empty.png"), 'IMAGE')
    pcoll.load("Coast", os.path.join(my_icons_dir,"Coast.png"), 'IMAGE')
    pcoll.load("Dune", os.path.join(my_icons_dir,"Dune.png"), 'IMAGE')
    pcoll.load("Eye", os.path.join(my_icons_dir,"Eye.png"), 'IMAGE')
    pcoll.load("Host", os.path.join(my_icons_dir,"Host.png"), 'IMAGE')
    pcoll.load("Raiser", os.path.join(my_icons_dir,"Raiser.png"), 'IMAGE')
    pcoll.load("Rib", os.path.join(my_icons_dir,"Rib.png"), 'IMAGE')
    pcoll.load("Sentry", os.path.join(my_icons_dir,"Sentry.png"), 'IMAGE')
    pcoll.load("Shaper", os.path.join(my_icons_dir,"Shaper.png"), 'IMAGE')
    pcoll.load("Silence", os.path.join(my_icons_dir,"Silence.png"), 'IMAGE')
    pcoll.load("Snout", os.path.join(my_icons_dir,"Snout.png"), 'IMAGE')
    pcoll.load("Spire", os.path.join(my_icons_dir,"Spire.png"), 'IMAGE')
    pcoll.load("Tide", os.path.join(my_icons_dir,"Tide.png"), 'IMAGE')
    pcoll.load("Vex", os.path.join(my_icons_dir,"Vex.png"), 'IMAGE')
    pcoll.load("Ward", os.path.join(my_icons_dir,"Ward.png"), 'IMAGE')
    pcoll.load("Wayfinder", os.path.join(my_icons_dir,"Wayfinder.png"), 'IMAGE')
    pcoll.load("Wild", os.path.join(my_icons_dir,"Wild.png"), 'IMAGE')

    
    
    pcoll.my_previews_presets = ""
    pcoll.my_previews_presets = ()

    pcoll.skins_folder = ""
    pcoll.skins_folder= ()

    pcoll.dlc_img_cache_folder = ""
    pcoll.dlc_img_cache_folder= ()

    pcoll.inventory_preview = ""
    pcoll.inventory_preview = ()
    
    preview_collections["main"] = pcoll
    
    from bpy.utils import register_class
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_add.append(menu_function_thing)

def unregister():
    from bpy.types import WindowManager
    
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    
    from bpy.utils import unregister_class
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_add.remove(menu_function_thing)
    
if __name__=="__main__":
    register()