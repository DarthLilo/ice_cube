#Libraries
import bpy
import os
import bpy.utils.previews
from bpy.props import EnumProperty
from bpy.types import WindowManager
from sys import platform

from ice_cube import root_folder, dlc_id,dlc_type,dlc_author

#Custom Files
from ice_cube_data.properties import properties
from ice_cube_data.operators import main_operators
from ice_cube_data.systems import inventory_system, skin_downloader


#Custom Functions
from ice_cube_data.utils.selectors import isRigSelected, main_face
from ice_cube_data.utils.file_manage import getFiles
from ice_cube_data.utils.general_func import GetListIndex

#UI Panels
from ice_cube_data.ui import credits_info
from ice_cube_data.ui.main import bone_layers, general_settings
from ice_cube_data.ui.customization import custom_general, mesh, misc
from ice_cube_data.ui.materials import skin_material, eye_material, misc_material
from ice_cube_data.ui.advanced import dlc_ui, parenting, downloads, adv_misc



#File Variables
RIG_ID = "ice_cube"

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
            return (rig.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        obj = context.object
        row = layout.row()

        #custom variables
        rig = isRigSelected(context)
        face = main_face(rig)
        skin_nodes = face.material_slots[0].material.node_tree
        skin_mat = skin_nodes.nodes['Skin Tex']

        #Draw the panel
        credits_info.credits_ui_panel(self,context)

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
                bone_layers.bone_layers_UI(self, context, layout)
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
                eye_material.eye_material_UI(self, context, layout, obj, face)
            if obj.get("ipaneltab4") == 2: #Misc
                misc_material.misc_material_UI(self, context, layout, face)
        #tabs/Advanced
        if obj.get("ipaneltab1") == 3: #Advanced
            if obj.get("ipaneltab5") == 0: #DLC
                dlc_ui.dlc_menu(self,context,layout, properties.global_rig_baked, True)
            if obj.get("ipaneltab5") == 1: #Parenting
                parenting.parenting_UI(self, context, layout, properties.global_rig_baked)
            if obj.get("ipaneltab5") == 2: #Downloads
                downloads.downloads_UI(self, context, layout, obj)
            if obj.get("ipaneltab5") == 3: #Misc
                adv_misc.advanced_misc_UI(self, context, layout, obj)

def menu_function_thing(self, context):
    pcoll = preview_collections["main"]
    my_icon = pcoll["DarthLilo"]
    self.layout.menu("IceCubeAppendMenu", text = "Ice Cube Rig", icon_value = my_icon.icon_id)

class IceCubeAppendMenu(bpy.types.Menu):
        bl_label = "Append Rig"
        bl_idname = "IceCubeAppendMenu"
        bl_options = bl_options = {'REGISTER', 'UNDO'}
        
        def draw(self, context):
        
            layout = self.layout
            
            pcoll = preview_collections["main"]
            
            my_icon = pcoll["Steve"]
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
           ToolsAppendMenu,
           IceCubeAppendMenu
           ]
           
modules = (
            main_operators,
          )

preview_collections = {}

def register():
    WindowManager.my_previews_presets = EnumProperty(
        items=presets_menu)

    WindowManager.skins_folder = EnumProperty(
        items=skins_menu)
    
    WindowManager.inventory_preview = EnumProperty(
       items=inventory_menu)

    pcoll = bpy.utils.previews.new()
    
    my_icons_dir = os.path.normpath(f"{root_folder}/ice_cube_data/internal_files/icons")
    pcoll.load("DarthLilo", os.path.join(my_icons_dir, "DarthLilo.png"), 'IMAGE')
    pcoll.load("Alex", os.path.join(my_icons_dir, "Alex.png"), 'IMAGE')
    pcoll.load("Steve", os.path.join(my_icons_dir, "Steve.png"), 'IMAGE')
    
    
    
    pcoll.my_previews_presets = ""
    pcoll.my_previews_presets = ()

    pcoll.skins_folder = ""
    pcoll.skins_folder= ()

    pcoll.inventory_preview = ""
    pcoll.inventory_preview = ()
    
    preview_collections["main"] = pcoll
    
    
    for m in modules:
        m.register()
    
    from bpy.utils import register_class
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_add.append(menu_function_thing)

def unregister():
    from bpy.types import WindowManager
    
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
    
    for m in modules:
        m.unregister()
    
    from bpy.utils import unregister_class
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_add.remove(menu_function_thing)
    
if __name__=="__main__":
    register()
