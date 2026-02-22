import bpy

from ..constants import RIG_ID
from ..icons import ice_cube_icons_collection


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
        if obj.advanced_mode:
            row = layout.row(align=True)
            row.prop(obj,"ik_fk_keyframe",text="IK FK Keyframing",icon='DECORATE_KEYFRAME')

class ICECUBERIG_PT_FaceSettings(bpy.types.Panel):
    bl_label = "Face Settings"
    bl_idname = "ICECUBERIG_PT_FaceSettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_parent_id = "ICECUBERIG_PT_Workflow"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def draw_header(self, context):
        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        self.layout.label(text="",icon_value=pcoll['steve'].icon_id)

    def draw(self, context):
        layout = self.layout
        obj = context.object
        face_rig_row = layout.row(align=True)

        face_rig_row.prop(obj,"face_rig",text="Face Rig",toggle=True)

        if obj.face_rig:
            face_rig_row = layout.row(align=True)
            face_rig_row.prop(obj, "eye_toggle", text="Eyes",toggle=True)
            face_rig_row.prop(obj, "mouth_toggle", text="Mouth",toggle=True)
            if (obj.mouth_toggle or obj.eye_toggle):

                face_rig_box = layout.box()
                face_rig_row = face_rig_box.row(align=True)
                face_rig_row.prop(obj,"fluid_face_strength",text="Fluid Face Strength",slider=True)
                blink_toggle_row = face_rig_row.row(align=True)
                blink_toggle_row.prop(obj,"blink_position",text="Blink Position",slider=True)
                if not obj.eye_toggle:
                    blink_toggle_row.enabled = False
                face_rig_row = face_rig_box.row(align=True)
    
                if obj.advanced_mode:
                    face_rig_row.prop(obj,"eyetracker",text="Eyetracker",toggle=True,icon='TRACKER')
                    face_rig_row = face_rig_box.row(align=True)
                if not obj.mouth_toggle:
                    face_rig_row.enabled = False
                face_rig_row.prop(obj,"cartoon_mouth",text="Cartoon Mouth",toggle=True,icon='IPO_EASE_IN')
                face_rig_row.prop(obj,"o_mouth_shape",text="O Mouth Shape",toggle=True,icon='ONIONSKIN_OFF')
                face_rig_row.prop(obj,"teeth_bool",text="Teeth Boolean",icon='MOD_BOOLEAN')
                face_rig_row = face_rig_box.row(align=True)
                if not (obj.eye_toggle and obj.mouth_toggle):
                    face_rig_row.enabled = False
                face_rig_row.prop(obj,"texture_deform",text="Texture Deform",toggle=True,icon='TEXTURE')

class ICECUBERIG_PT_ArmSettings(bpy.types.Panel):
    bl_label = "Arm Settings"
    bl_idname = "ICECUBERIG_PT_ArmSettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_parent_id = "ICECUBERIG_PT_Workflow"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def draw_header(self, context):
        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        self.layout.label(text="",icon_value=pcoll['arms'].icon_id)

    def draw(self, context):
        layout = self.layout
        obj = context.object
        pcoll = ice_cube_icons_collection["ice_cube_remake"]


        arm_settings_row = layout.row(align=False)

        # Arm Columns
        right_arm_col = arm_settings_row.column(align=True)
        left_arm_col = arm_settings_row.column(align=True)
        

        # --- Left Arm Box ---
        left_arm_box = left_arm_col.box()
        left_arm_col = left_arm_box.column(align=True)

        # --- Right Arm Box ---
        right_arm_box = right_arm_col.box()
        right_arm_col = right_arm_box.column(align=True)

        # --- Left Arm Icon ---
        left_arm_icon_row = left_arm_col.row()
        left_arm_icon_row.alignment = 'RIGHT'
        left_arm_icon_row.label(text="Left Arm")
        left_arm_icon_row.label(text="",icon_value=pcoll['left_arm'].icon_id)

        # --- Right Arm Icon ---
        right_arm_icon_row = right_arm_col.row()
        right_arm_icon_row.label(text="",icon_value=pcoll['right_arm'].icon_id)
        right_arm_icon_row.label(text="Right Arm")
        

        #Left Arm
        left_arm_col.prop(obj,"left_arm_ik",text="Left Arm IK",slider=True)
        left_arm_col.prop(obj,"left_arm_stretch",text="Stretch",slider=True)
        left_arm_col.prop(obj,"left_arm_wrist_lock",text="Wrist Lock",slider=True)
        if obj.advanced_mode:
            left_arm_col.operator('ice_cube.arm_l_ik_to_fk',text="Convert To IK",icon='RESTRICT_INSTANCED_OFF')
            left_arm_col.operator('ice_cube.arm_l_fk_to_ik',text="Convert To FK",icon='RESTRICT_INSTANCED_ON')
            left_arm_col.prop(obj,"left_arm_IK_parent",text="")

        #Right Arm
        right_arm_col.prop(obj,"right_arm_ik",text="Right Arm IK",slider=True)
        right_arm_col.prop(obj,"right_arm_stretch",text="Stretch",slider=True)
        right_arm_col.prop(obj,"right_arm_wrist_lock",text="Wrist Lock",slider=True)
        if obj.advanced_mode:
            right_arm_col.operator('ice_cube.arm_r_ik_to_fk',text="Convert To IK",icon='RESTRICT_INSTANCED_OFF')
            right_arm_col.operator('ice_cube.arm_r_fk_to_ik',text="Convert To FK",icon='RESTRICT_INSTANCED_ON')
            right_arm_col.prop(obj,"right_arm_IK_parent",text="")

        arm_settings_row = layout.row(align=False)

        arm_settings_row.prop(obj,"shoulder_deform",text="Shoulder Deform",toggle=True)

class ICECUBERIG_PT_LegSettings(bpy.types.Panel):
    bl_label = "Leg Settings"
    bl_idname = "ICECUBERIG_PT_LegSettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_parent_id = "ICECUBERIG_PT_Workflow"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def draw_header(self, context):
        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        self.layout.label(text="",icon_value=pcoll['legs'].icon_id)

    def draw(self, context):
        layout = self.layout
        obj = context.object
        pcoll = ice_cube_icons_collection["ice_cube_remake"]

        leg_settings_row = layout.row(align=False)

        # Leg Columns
        right_leg_col = leg_settings_row.column(align=True)
        left_leg_col = leg_settings_row.column(align=True)

        # --- Left Leg Box ---
        left_leg_box = left_leg_col.box()
        left_leg_col = left_leg_box.column(align=True)

        # --- Right Leg Box ---
        right_leg_box = right_leg_col.box()
        right_leg_col = right_leg_box.column(align=True)

        # --- Left Leg Icon ---
        left_leg_icon_row = left_leg_col.row()
        left_leg_icon_row.alignment = 'RIGHT'
        left_leg_icon_row.label(text="Left Leg")
        left_leg_icon_row.label(text="",icon_value=pcoll['left_leg'].icon_id)

        # --- Right Leg Icon ---
        right_leg_icon_row = right_leg_col.row()
        right_leg_icon_row.label(text="",icon_value=pcoll['right_leg'].icon_id)
        right_leg_icon_row.label(text="Right Leg")
        

        #Left Leg
        left_leg_col.prop(obj,"left_leg_ik",text="Left Leg IK",slider=True)
        left_leg_col.prop(obj,"left_leg_stretch",text="Stretch",slider=True)
        left_leg_col.prop(obj,"left_leg_ankle_lock",text="Ankle Lock",slider=True)
        if obj.advanced_mode:
            left_leg_col.operator('ice_cube.leg_l_ik_to_fk',text="Convert To IK",icon='RESTRICT_INSTANCED_OFF')
            left_leg_col.operator('ice_cube.leg_l_fk_to_ik',text="Convert To FK",icon='RESTRICT_INSTANCED_ON')
            left_leg_col.prop(obj,"left_leg_IK_parent",text="")
        #Right Leg
        right_leg_col.prop(obj,"right_leg_ik",text="Right Leg IK",slider=True)
        right_leg_col.prop(obj,"right_leg_stretch",text="Stretch",slider=True)
        right_leg_col.prop(obj,"right_leg_ankle_lock",text="Ankle Lock",slider=True)
        if obj.advanced_mode:
            right_leg_col.operator('ice_cube.leg_r_ik_to_fk',text="Convert To IK",icon='RESTRICT_INSTANCED_OFF')
            right_leg_col.operator('ice_cube.leg_r_fk_to_ik',text="Convert To FK",icon='RESTRICT_INSTANCED_ON')
            right_leg_col.prop(obj,"right_leg_IK_parent",text="")

class ICECUBERIG_PT_BodySettings(bpy.types.Panel):
    bl_label = "Body Settings"
    bl_idname = "ICECUBERIG_PT_BodySettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_parent_id = "ICECUBERIG_PT_Workflow"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def draw_header(self, context):
        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        self.layout.label(text="",icon_value=pcoll['body'].icon_id)

    def draw(self, context):
        layout = self.layout
        obj = context.object

        face_rig_row = layout.row(align=True)
        
        if obj.advanced_mode:
            
            face_rig_row.prop(obj,"global_head_rotation",text="Global Head Rot",toggle=True,icon='DRIVER_ROTATIONAL_DIFFERENCE')
            face_rig_row.prop(obj,"lock_limb_rotation",text="Lock Limb Rotation",toggle=True,icon='DECORATE_LOCKED')
            face_rig_row = layout.row(align=True)
            face_rig_row.operator("ice_cube.set_custom_default_pose",text="Update Rest Pose",icon='ARMATURE_DATA')
            face_rig_row.operator("ice_cube.reset_custom_default_pose",text="Reset Rest Pose",icon='LOOP_BACK')
            face_rig_row = layout.row(align=True)
            face_rig_row.prop(obj,"head_squish",text="Head Squish",toggle=True,icon='MOD_LENGTH')
            face_rig_row.prop(obj,"body_squish",text="Body Squish",toggle=True,icon='MOD_LENGTH')
            face_rig_row = layout.row(align=True)
            face_rig_row.prop(obj,"minecraft_accurate_scaling",text="Minecraft Scale",icon='CON_TRANSFORM')
            face_rig_row = layout.row(align=True)
            face_rig_row.operator("ice_cube.bake_rig",text="Bake Rig",icon='ERROR')
            face_rig_row.operator("ice_cube.reset_all",text="Reset All",icon='ERROR')
            face_rig_row = layout.row(align=True)
            face_rig_row.operator("ice_cube.statsexport",text="Export Debug",icon='EXPORT')
            face_rig_row.operator("ice_cube.statsimport",text="Import Debug",icon='IMPORT')

        else:
            face_rig_row.prop(obj,"global_head_rotation",text="Global Head Rot",toggle=True,icon='DRIVER_ROTATIONAL_DIFFERENCE')
            face_rig_row.prop(obj,"lock_limb_rotation",text="Lock Limb Rotation",toggle=True,icon='DECORATE_LOCKED')
            face_rig_row = layout.row(align=True)
            face_rig_row.prop(obj,"bevel_toggle_viewport",text="Viewport Bevel",toggle=True, icon='MOD_BEVEL')
            face_rig_row.prop(obj,"bevel_toggle_render",text="Render Bevel",toggle=True,icon='RENDER_STILL')
            face_rig_row = layout.row(align=True)
            face_rig_row.operator("ice_cube.set_custom_default_pose",text="Update Rest Pose",icon='ARMATURE_DATA')
            face_rig_row.operator("ice_cube.reset_custom_default_pose",text="Reset Rest Pose",icon='LOOP_BACK')