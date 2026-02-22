import bpy

from ..constants import RIG_ID, ADDON_VERSION, INTERNAL_VERSION, LIBRARIES
from ..icons import ice_cube_icons_collection
from ..Operators.statistics import GetIceCubeVersion

class ICECUBERIG_PT_IceCubeMain(bpy.types.Panel):
    bl_label = ADDON_VERSION
    bl_idname = "ICECUBERIG_PT_IceCubeMain"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw_header(self, context):
        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        self.layout.label(text="",icon_value=pcoll['ice_cube_logo'].icon_id)




    def draw(self, context):
        layout = self.layout
        obj = context.object

        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        row = layout.row(align=True)
        rig_version = GetIceCubeVersion()
        if INTERNAL_VERSION == rig_version:
            vers_text = ""
        elif INTERNAL_VERSION > rig_version:
            vers_text = "Rig Outdated!"
            row.label(text=vers_text)
            row = layout.row(align=True)
        else:
            vers_text = "Addon Outdated!"
            row.label(text=vers_text)
            row = layout.row(align=True)
        

        row.operator("ice_cube.open_website",text="Website",icon='HOME')
        row.operator("ice_cube.open_discord",text="Support / Discord",icon_value=pcoll['discord_logo'].icon_id)
        row = layout.row(align=True)
        row.operator("ice_cube.open_wiki",text="Wiki",icon='TEXT')
        row.prop(obj,"advanced_mode",text="Advanced Mode",icon='MODIFIER')
        row = layout.row(align=True)
        row.operator("ice_cube.check_for_updates",text="Check for Updates",icon='INTERNET')
        open_library_folder = row.operator("ice_cube.open_folder",text="Manage Library", icon='FILE_FOLDER')
        open_library_folder.folder_path = LIBRARIES
        row = layout.row(align=True)
        row.operator("ice_cube.save_character",text="Save Character to Add Menu",icon='FILE_TICK')

        

        if rig_version <= (2,0,8) and not obj.data.get("ice_cube.converted_to_5_0"):
            row = layout.row(align=True)
            row.operator("ice_cube.blender_5_0_fix",text="Convert Rig",icon='INTERNET')