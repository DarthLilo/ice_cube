import bpy

from ..constants import RIG_ID

# Main panel

class ICECUBERIG_PT_Parenting(bpy.types.Panel):
    bl_label = "Parenting"
    bl_idname = "ICECUBERIG_PT_Parenting"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def draw_header(self, context):
        self.layout.label(text="",icon='ORIENTATION_PARENT')

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene

        layout.operator("ice_cube.update_parenting",text="Update Parenting",icon='ORIENTATION_PARENT')

        armor_box = layout.box()
        armor_row = armor_box.row(align=True)
        armor_row.label(text="Armor Parenting",icon='MOD_CLOTH')
        armor_row = armor_box.row(align=True)
        armor_row.prop(scene.ice_cube_remake,"armor_collection_target",text="",placeholder="Armor Collection")
        armor_row.operator("ice_cube.parent_armor")
        