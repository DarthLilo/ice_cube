import bpy

from ..constants import RIG_ID, RIG_VERSION
from ..icons import ice_cube_icons_collection

class ICECUBERIG_PT_IceCubeMain(bpy.types.Panel):
    bl_label = RIG_VERSION
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
        row.operator("ice_cube.open_website",text="Website",icon='HOME')
        row.operator("ice_cube.open_discord",text="Support / Discord",icon_value=pcoll['discord_logo'].icon_id)
        row = layout.row(align=True)
        row.operator("ice_cube.open_wiki",text="Wiki",icon='TEXT')
        row.prop(obj,"advanced_mode",text="Advanced Mode",icon='MODIFIER')