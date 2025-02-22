import bpy

from ..icons import ice_cube_icons_collection

class ICECUBERIG_MT_3dview_add(bpy.types.Menu):
    bl_label = "Ice Cube"
    bl_idname = "ICECUBERIG_MT_3dview_add"

    def draw(self, context):
        layout = self.layout

        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        
        layout.operator("ice_cube.append_ice_cube_10px",text="Append Ice Cube (10px)",icon_value=pcoll['ice_cube_logo'].icon_id)
        layout.operator("ice_cube.append_ice_cube",text="Append Ice Cube (Default)",icon_value=pcoll['ice_cube_logo'].icon_id)
        layout.operator("ice_cube.append_ice_cube_14px",text="Append Ice Cube (14px)",icon_value=pcoll['ice_cube_logo'].icon_id)

def AddMenuFunction(self, context):
    layout = self.layout
    pcoll = ice_cube_icons_collection["ice_cube_remake"]
    layout.menu(ICECUBERIG_MT_3dview_add.bl_idname,icon_value=pcoll['ice_cube_logo'].icon_id)