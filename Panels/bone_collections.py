import bpy

from ..constants import RIG_ID
from ..ice_cube_selectors import GetBoneCollection

class BoneCollectionManager():
    def new_bone_layer(self, context, layout, layer_id,text, icon="NONE"):
        collections = context.active_object.data.collections_all
        bone_collection = GetBoneCollection(collections, layer_id)
        if bone_collection:
            layout.prop(bone_collection, 'is_visible',toggle=True,text=text,icon=icon)

# Bone Collections
class ICECUBERIG_PT_BoneCollections(bpy.types.Panel):
    bl_label = "Bone Collections"
    bl_idname = "ICECUBERIG_PT_BoneCollections"
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
        self.layout.label(text="",icon='BONE_DATA')

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.prop(context.object, "responsive_bone_layers",text="Responsive Bone Layers",toggle=True)
        row = layout.row(align=True)


        # HEAD BONES
        head_col = row.column(align=True)
        head_row = head_col.row(align=True)
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.head',"Head")
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.facial',"Facial")
        head_row = head_col.row(align=True)
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.blink_pos',"Blink Pos")
        BoneCollectionManager.new_bone_layer(self,context,head_row,'ice_cube.facial_tweaks',"Tweak")
        row = layout.row(align=True)

        #ARM BONES
        row = layout.row(align=True)
        
        right_arm_col = row.column(align=True)
        left_arm_col = row.column(align=True)
        

        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_arm',"Left Arm")
        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_arm_fk',"FK Bones")
        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_arm_ik',"IK Bones")
        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_arm_tweak',"Tweaks")
        BoneCollectionManager.new_bone_layer(self,context,left_arm_col,'ice_cube.left_finger_tweaks',"Finger Tweaks")

        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_arm',"Right Arm")
        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_arm_fk',"FK Bones")
        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_arm_ik',"IK Bones")
        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_arm_tweak',"Tweaks")
        BoneCollectionManager.new_bone_layer(self,context,right_arm_col,'ice_cube.right_finger_tweaks',"Finger Tweaks")
        row = layout.row(align=True)


        #BODY BONES
        row = layout.row(align=True)
        body_col = row.column(align=True)
        body_row = body_col.row(align=True)
        BoneCollectionManager.new_bone_layer(self,context,body_row,'ice_cube.body',"Body")
        BoneCollectionManager.new_bone_layer(self,context,body_row,'ice_cube.body_tweak',"Tweak")
        body_row = body_col.row(align=True)
        BoneCollectionManager.new_bone_layer(self,context,body_row,'ice_cube.shoulders',"Shoulders")
        row = layout.row(align=True)

        # LEG BONES
        row = layout.row(align=True)
        right_leg_col = row.column(align=True)
        left_leg_col = row.column(align=True)
        row = layout.row(align=True)
        

        BoneCollectionManager.new_bone_layer(self,context,left_leg_col,'ice_cube.left_leg',"Left Leg")
        BoneCollectionManager.new_bone_layer(self,context,left_leg_col,'ice_cube.left_leg_ik',"IK Bones")
        BoneCollectionManager.new_bone_layer(self,context,left_leg_col,'ice_cube.left_leg_fk',"FK Bones")
        BoneCollectionManager.new_bone_layer(self,context,left_leg_col,'ice_cube.left_leg_tweak',"Tweak")

        BoneCollectionManager.new_bone_layer(self,context,right_leg_col,'ice_cube.right_leg',"Right Leg")
        BoneCollectionManager.new_bone_layer(self,context,right_leg_col,'ice_cube.right_leg_ik',"IK Bones")
        BoneCollectionManager.new_bone_layer(self,context,right_leg_col,'ice_cube.right_leg_fk',"FK Bones")
        BoneCollectionManager.new_bone_layer(self,context,right_leg_col,'ice_cube.right_leg_tweak',"Tweak")

        if GetBoneCollection(context.active_object.data.collections_all,'ice_cube.internal'):
            BoneCollectionManager.new_bone_layer(self,context,row,'ice_cube.internal','Internal')