import bpy

from ..constants import RIG_ID

class UI_Chunks():
    def ArmSettings(layout, obj):
        arm_settings_box = layout.box()
        arm_settings_row = arm_settings_box.row(align=True)
        arm_settings_row.label(text="Arm Settings",icon='BONE_DATA')
        arm_settings_row = arm_settings_box.row(align=True)

        # Arm Columns
        right_arm_col = arm_settings_row.column(align=True)
        left_arm_col = arm_settings_row.column(align=True)
        

        #Left Arm
        left_arm_col.prop(obj,"left_arm_ik",text="Left Arm IK",slider=True)
        left_arm_col.prop(obj,"left_arm_stretch",text="Stretch",slider=True)
        left_arm_col.prop(obj,"left_arm_wrist_lock",text="Wrist Lock",slider=True)
        if obj.advanced_mode:
            left_arm_col.operator('ice_cube.arm_l_ik_to_fk',text="Convert To IK",icon='RESTRICT_INSTANCED_OFF')
            left_arm_col.operator('ice_cube.arm_l_fk_to_ik',text="Convert To FK",icon='RESTRICT_INSTANCED_ON')

        #Right Arm
        right_arm_col.prop(obj,"right_arm_ik",text="Right Arm IK",slider=True)
        right_arm_col.prop(obj,"right_arm_stretch",text="Stretch",slider=True)
        right_arm_col.prop(obj,"right_arm_wrist_lock",text="Wrist Lock",slider=True)
        if obj.advanced_mode:
            right_arm_col.operator('ice_cube.arm_r_ik_to_fk',text="Convert To IK",icon='RESTRICT_INSTANCED_OFF')
            right_arm_col.operator('ice_cube.arm_r_fk_to_ik',text="Convert To FK",icon='RESTRICT_INSTANCED_ON')

    def LegSettings(layout, obj):
        leg_settings_box = layout.box()
        leg_settings_row = leg_settings_box.row(align=True)
        leg_settings_row.label(text="Leg Settings",icon='BONE_DATA')
        leg_settings_row = leg_settings_box.row(align=True)

        # Leg Columns
        right_leg_col = leg_settings_row.column(align=True)
        left_leg_col = leg_settings_row.column(align=True)
        

        #Left Leg
        left_leg_col.prop(obj,"left_leg_ik",text="Left Leg IK",slider=True)
        left_leg_col.prop(obj,"left_leg_stretch",text="Stretch",slider=True)
        left_leg_col.prop(obj,"left_leg_ankle_lock",text="Ankle Lock",slider=True)
        if obj.advanced_mode:
            left_leg_col.operator('ice_cube.leg_l_ik_to_fk',text="Convert To IK",icon='RESTRICT_INSTANCED_OFF')
            left_leg_col.operator('ice_cube.leg_l_fk_to_ik',text="Convert To FK",icon='RESTRICT_INSTANCED_ON')
        #Right Leg
        right_leg_col.prop(obj,"right_leg_ik",text="Right Leg IK",slider=True)
        right_leg_col.prop(obj,"right_leg_stretch",text="Stretch",slider=True)
        right_leg_col.prop(obj,"right_leg_ankle_lock",text="Ankle Lock",slider=True)
        if obj.advanced_mode:
            right_leg_col.operator('ice_cube.leg_r_ik_to_fk',text="Convert To IK",icon='RESTRICT_INSTANCED_OFF')
            right_leg_col.operator('ice_cube.leg_r_fk_to_ik',text="Convert To FK",icon='RESTRICT_INSTANCED_ON')


class ICECUBERIG_PT_Workflow(bpy.types.Panel):
    bl_label = "Workflow"
    bl_idname = "ICECUBERIG_PT_Workflow"
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
        self.layout.label(text="",icon='PROPERTIES')

    def draw(self, context):
        layout = self.layout
        obj = context.object


        #Main Layout
        row = layout.row(align=True)
        row.prop(obj,"performance_mode",text="Performance Mode",icon='TIME',expand=True)
        row = layout.row(align=True)

        #Arm Settings
        UI_Chunks.ArmSettings(row,obj)

        row = layout.row(align=True)

        UI_Chunks.LegSettings(row,obj)

        row = layout.row(align=True)

        face_rig_box = row.box()
        face_rig_row = face_rig_box.row(align=True)
        face_rig_row.label(text="Misc Settings", icon='MONKEY')
        face_rig_row = face_rig_box.row(align=True)
        face_rig_row.prop(obj,"face_rig",text="Face Rig",toggle=True)
        face_rig_row = face_rig_box.row(align=True)
        if obj.face_rig:
            face_rig_row.prop(obj,"fluid_face_strength",text="Fluid Face Strength",slider=True)
            face_rig_row.prop(obj,"blink_position",text="Blink Position",slider=True)
            face_rig_row = face_rig_box.row(align=True)
        
        if obj.advanced_mode:

            if obj.face_rig:
                face_rig_row.prop(obj,"eyetracker",text="Eyetracker")
                face_rig_row.prop(obj,"global_head_rotation",text="Global Head Rot")
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.prop(obj,"head_squish",text="Head Squish")
                face_rig_row.prop(obj,"body_squish",text="Body Squish")
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.prop(obj,"cartoon_mouth",text="Cartoon Mouth")
                face_rig_row.prop(obj,"o_mouth_shape",text="O Mouth Shape")
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.prop(obj,"shoulder_deform",text="Shoulder Deform")
                face_rig_row.prop(obj,"texture_deform",text="Texture Deform")
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.prop(obj,"lock_limb_rotation",text="Lock Limb Rotation",toggle=True,icon='DECORATE_LOCKED')
                face_rig_row.prop(obj,"teeth_bool",text="Teeth Boolean",icon='MOD_BOOLEAN')
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.operator("ice_cube.set_custom_default_pose",text="Update Rest Pose",icon='ARMATURE_DATA')
                face_rig_row.operator("ice_cube.reset_custom_default_pose",text="Reset Rest Pose",icon='LOOP_BACK')
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.prop(obj,"minecraft_accurate_scaling",text="Minecraft Scale",icon='CON_TRANSFORM')
                face_rig_row.operator("ice_cube.bake_rig",text="Bake Rig",icon='ERROR')
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.operator("ice_cube.reset_all",text="Reset All",icon='ERROR')
            else:
                face_rig_row.prop(obj,"global_head_rotation",text="Global Head Rot")
                face_rig_row.prop(obj,"shoulder_deform",text="Shoulder Deform")
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.prop(obj,"head_squish",text="Head Squish")
                face_rig_row.prop(obj,"body_squish",text="Body Squish")
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.prop(obj,"lock_limb_rotation",text="Lock Limb Rotation",toggle=True,icon='DECORATE_LOCKED')
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.operator("ice_cube.set_custom_default_pose",text="Update Rest Pose",icon='ARMATURE_DATA')
                face_rig_row.operator("ice_cube.reset_custom_default_pose",text="Reset Rest Pose",icon='LOOP_BACK')
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.operator("ice_cube.bake_rig",text="Bake Rig",icon='ERROR')
                face_rig_row.operator("ice_cube.reset_all",text="Reset All",icon='ERROR')
        else:
            face_rig_row.prop(obj,"global_head_rotation",text="Global Head Rot",toggle=True,icon='DRIVER_ROTATIONAL_DIFFERENCE')
            if obj.face_rig:
                face_rig_row.prop(obj,"cartoon_mouth",text="Cartoon Mouth",toggle=True,icon='IPO_LINEAR')
            face_rig_row = face_rig_box.row(align=True)
            if obj.face_rig:
                face_rig_row.prop(obj,"texture_deform",text="Texture Deform",toggle=True,icon='UV')
            face_rig_row.prop(obj,"lock_limb_rotation",text="Lock Limb Rotation",toggle=True,icon='DECORATE_LOCKED')
            face_rig_row = face_rig_box.row(align=True)
            face_rig_row.operator("ice_cube.set_custom_default_pose",text="Update Rest Pose",icon='ARMATURE_DATA')
            face_rig_row.operator("ice_cube.reset_custom_default_pose",text="Reset Rest Pose",icon='LOOP_BACK')
