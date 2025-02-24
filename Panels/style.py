import bpy

from ..constants import RIG_ID
from ..ice_cube_selectors import GetMaterial
from ..icons import ice_cube_icons_collection

# Main panel

class ICECUBERIG_PT_Style(bpy.types.Panel):
    bl_label = "Style"
    bl_idname = "ICECUBERIG_PT_Style"
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
        self.layout.label(text="",icon='SOLO_ON')

    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        pcoll = ice_cube_icons_collection["ice_cube_remake"]
        icon_translation = {
            "1":"steve",
            "2":"alex",
            "3":"makena"
        }

        row = layout.row(align=True)
        row.label(text="",icon_value=pcoll[icon_translation[str(obj.arm_type)]].icon_id)
        row.prop(obj,"arm_type",text="Arm",expand=True)
        row.label(text="",icon_value=pcoll[icon_translation[str(obj.arm_type)]].icon_id)

        row = layout.row(align=True)
        row.prop(obj,"bend_smoothness",text="Bend Smoothness",slider=True)
        row.prop(obj,"body_bend_shape",text="Body Bend Shape",slider=True)
        row = layout.row(align=True)
        row.prop(obj,"arm_scale",text="Arm Scale",slider=True)
        row.prop(obj,"leg_scale",text="Leg Scale",slider=True)
        row = layout.row(align=True)

        right_arm_col = row.column(align=True)
        left_arm_col = row.column(align=True)
        

        left_arm_col.prop(obj,"left_fingers",text="Fingers",toggle=True)
        left_arm_thumbfill_col = left_arm_col.column(align=True)
        left_arm_thumbfill_col.enabled = obj.left_fingers
        left_arm_thumbfill_col.prop(obj,"left_thumbfill",text="Thumbfill",toggle=True)

        right_arm_col.prop(obj,"right_fingers",text="Fingers",toggle=True)
        right_arm_thumbfill_col = right_arm_col.column(align=True)
        right_arm_thumbfill_col.enabled = obj.right_fingers
        right_arm_thumbfill_col.prop(obj,"right_thumbfill",text="Thumbfill",toggle=True)

class ICECUBERIG_PT_StyleTaper(bpy.types.Panel):
    bl_label = "Taper"
    bl_idname = "ICECUBERIG_PT_StyleTaper"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_parent_id = "ICECUBERIG_PT_Style"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw_header(self, context):
        self.layout.label(text="",icon='MESH_CONE')
    
    def draw(self, context):
        layout = self.layout
        obj = context.object

        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(obj,"head_taper",text="Head Taper",slider=True)
        row.prop(obj,"hip",text="Hip",slider=True)
        row = col.row(align=True)
        row.prop(obj,"upper_body_width",text="Upper Body Taper",slider=True)
        row.prop(obj,"lower_body_width",text="Lower Body Taper",slider=True)
        row = col.row(align=True)
        row.prop(obj,"right_arm_taper_upper",text="Right Arm Taper Upper",slider=True)
        row.prop(obj,"left_arm_taper_upper",text="Left Arm Taper Upper",slider=True)
        row = col.row(align=True)
        row.prop(obj,"right_arm_taper_lower",text="Right Arm Taper Lower",slider=True)
        row.prop(obj,"left_arm_taper_lower",text="Left Arm Taper Lower",slider=True)
        row = col.row(align=True)
        row.prop(obj,"right_leg_taper_upper",text="Right Leg Taper Upper",slider=True)
        row.prop(obj,"left_leg_taper_upper",text="Left Leg Taper Upper",slider=True)
        row = col.row(align=True)
        row.prop(obj,"right_leg_taper_lower",text="Right Leg Taper Lower",slider=True)
        row.prop(obj,"left_leg_taper_lower",text="Left Leg Taper Lower",slider=True)

class ICECUBERIG_PT_StyleBulge(bpy.types.Panel):
    bl_label = "Bulge"
    bl_idname = "ICECUBERIG_PT_StyleBulge"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_parent_id = "ICECUBERIG_PT_Style"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw_header(self, context):
        self.layout.label(text="",icon='SPHERE')
    
    def draw(self, context):
        layout = self.layout
        obj = context.object

        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(obj,"head_bulge",text="Head Bulge",slider=True)
        row.prop(obj,"eye_bulge",text="Eye Bulge",slider=True)
        row = col.row(align=True)
        row.prop(obj,"body_bulge",text="Body Bulge",slider=True)
        row = col.row(align=True)
        row.prop(obj,"right_arm_bulge",text="Right Arm Bulge",slider=True)
        row.prop(obj,"left_arm_bulge",text="Left Arm Bulge",slider=True)
        row = col.row(align=True)
        row.prop(obj,"right_leg_bulge",text="Right Leg Bulge",slider=True)
        row.prop(obj,"left_leg_bulge",text="Left Leg Bulge",slider=True)

class ICECUBERIG_PT_StyleCosmetics(bpy.types.Panel):
    bl_label = "Cosmetics"
    bl_idname = "ICECUBERIG_PT_StyleCosmetics"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_parent_id = "ICECUBERIG_PT_Style"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw_header(self, context):
        self.layout.label(text="",icon='MATCLOTH')
    
    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row(align=True)
        row.prop(obj,"breast_size",text="Breast Size",slider=True)
        row.prop(obj,"breast_angle",text="Breast Angle",slider=True)

        row = layout.row(align=True)
        row.prop(obj,"bevel_mouth_strength",text="Mouth Bevel",slider=True)
        row.prop(obj,"eye_bevel",text="Eye Bevel",slider=True)

        row = layout.row(align=True)
        row.prop(obj,"eyebrow_height",text="Eyebrow Height",slider=True)
        row.prop(obj,"eyebrow_taper",text="Eyebrow Taper",slider=True)

        row = layout.row(align=True)
        row.prop(obj,"eye_depth",text="Eye Depth",slider=True)
        row.prop(obj,"mouth_depth",text="Mouth Depth",slider=True)
        row.prop(obj,"inner_mouth_depth",text="Inner Mouth Depth",slider=True)

        row = layout.row(align=True)
        row.prop(obj,"lipstick",text="Lipstick",toggle=True,icon='MOD_OUTLINE')
        row.prop(obj,"lipstick_thickness",text="Thickness",slider=True)
        
        row = layout.row(align=True)
        row.prop(obj,"eyelashes",text="Eyelashes",icon='OUTLINER_DATA_GP_LAYER')
        row = layout.row(align=True)
        row.prop(obj,"eyelashes_lower",text="Eyelashes Lower",icon='OUTLINER_DATA_GP_LAYER')

class ICECUBERIG_PT_StyleEmotions(bpy.types.Panel):
    bl_label = "Emotions"
    bl_idname = "ICECUBERIG_PT_StyleEmotions"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_parent_id = "ICECUBERIG_PT_Style"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw_header(self, context):
        self.layout.label(text="",icon='HEART')
    
    def draw(self, context):
        layout = self.layout
        obj = context.object

        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(obj,"blush_strength",text="Blush",slider=True)
        row.prop(obj,"emotion_anger",text="Anger",toggle=True)
        row = col.row(align=True)
        row.prop(obj,"right_tear",text="Right Tear",slider=True)
        row.prop(obj,"left_tear",text="Left Tear",slider=True)
        row = col.row(align=True)
        row.prop(obj,"emotion_eye_shape",text="")

class ICECUBERIG_PT_StyleMouth(bpy.types.Panel):
    bl_label = "Mouth"
    bl_idname = "ICECUBERIG_PT_StyleMouth"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_parent_id = "ICECUBERIG_PT_Style"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw_header(self, context):
        self.layout.label(text="",icon='SURFACE_NSPHERE')
    
    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row(align=True)
        row.prop(obj,"round_jaw",text="Round Jaw",icon='SPHERECURVE')
        row.prop(obj,"jaw_strength",text="Jaw Strength",slider=True)
        row = layout.row(align=True)
        row.prop(obj,"jaw_shape",text="Jaw Shape",slider=True)
        row = layout.row(align=True)
        row.prop(obj,"tongue",text="Tongue",icon='PROP_PROJECTED')
        row.prop(obj,"teeth_curve",text="Teeth Curve",slider=True)
        
class ICECUBERIG_PT_StyleSkin(bpy.types.Panel):
    bl_label = "Skin"
    bl_idname = "ICECUBERIG_PT_StyleSkin"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_parent_id = "ICECUBERIG_PT_Style"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False

    def draw_header(self, context):
        self.layout.label(text="",icon='TEXTURE_DATA')

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene

        row = layout.row(align=True)

        row.prop(scene,"ice_cube_minecraft_username",text="Username")
        row.operator("ice_cube.download_skin",text="",icon='IMPORT')
        row = layout.row(align=True)

        # Skin Path Stuff
        skin_texture_node = GetMaterial(context,'skin').node_tree.nodes['Skin Texture']
        skin_texture_packed = skin_texture_node.image.packed_file
        row.context_pointer_set("edit_image",skin_texture_node.image)
        row.operator("image.unpack" if skin_texture_packed else "image.pack",text="", icon='PACKAGE' if skin_texture_packed else "UGLYPACKAGE")
        row.prop(skin_texture_node.image, "filepath", text="")
        row.operator("image.reload", text="",icon='FILE_REFRESH')

        row = layout.row(align=True)
        row.template_icon_view(context.window_manager.ice_cube_skin_library,"skin_library")
        row = layout.row(align=True)
        row.operator("ice_cube.apply_skin",text="Apply Skin", icon='IMAGE_DATA')
        row.operator("ice_cube.delete_skin",text="Delete Skin",icon='TRASH')
        row.operator("ice_cube.reset_skin",text="Reset Skin", icon='LOOP_BACK')

class ICECUBERIG_PT_StyleMaterial(bpy.types.Panel):
    bl_label = "Materials"
    bl_idname = "ICECUBERIG_PT_StyleMaterial"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "Ice Cube v2"
    bl_parent_id = "ICECUBERIG_PT_Style"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        active_object = bpy.context.active_object
        try:
            return (active_object.data.get("rig_id") == RIG_ID)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def draw_header(self, context):
        self.layout.label(text="",icon='NODE_MATERIAL')

    def draw(self, context):
        layout = self.layout
        obj = context.object
        scene = context.scene
        eye_material = GetMaterial(context,'eyes')
        eye_node = eye_material.node_tree.nodes['Ice_Cube_Eyes']
        eye_texture_node = eye_material.node_tree.nodes['Ice_Cube_Eye_Texture']

        row = layout.row(align=True)

        eyes_box = row.box()
        eyes_row = eyes_box.row(align=True)
        eyes_row.label(text="Eyes",icon='NODE_MATERIAL')
        eyes_row = eyes_box.row(align=True)

        left_eye_col = eyes_row.column(align=True)
        right_eye_col = eyes_row.column(align=True)

        left_eye_col.prop(eye_node.inputs[0], 'default_value', text="")
        left_eye_col.prop(eye_node.inputs[1], 'default_value', text="")
        right_eye_col.prop(eye_node.inputs[2], 'default_value', text="")
        right_eye_col.prop(eye_node.inputs[3], 'default_value', text="")

        eyes_row = eyes_box.row(align=True)
        eyes_row.prop(eye_node.inputs[4],'default_value',text="Gradient")
        eyes_row.prop(eye_node.inputs[5],'default_value',text="Image Texture")
        eyes_row = eyes_box.row(align=True)
        if eye_node.inputs[5].default_value:
            eyes_row.context_pointer_set("edit_image",eye_texture_node.image)
            eye_texture_packed = eye_texture_node.image.packed_file
            eyes_row.operator("image.unpack" if eye_texture_packed else "image.pack",text="", icon='PACKAGE' if eye_texture_packed else "UGLYPACKAGE")
            eyes_row.prop(eye_texture_node.image, "filepath", text="")
            eyes_row = eyes_box.row(align=True)
            eyes_row.prop(eye_node.inputs[7],'default_value',text="")
            eyes_row.prop(eye_node.inputs[8],'default_value',text="")
            eyes_row = eyes_box.row(align=True)

        else:
            eyes_row.prop(eye_node.inputs[9],'default_value',text="Toggle Pupil",toggle=True)
            eyes_row = eyes_box.row(align=True)
            if eye_node.inputs[9].default_value:
                eyes_row.prop(eye_node.inputs[11],'default_value',text="Right Scale")
                eyes_row.prop(eye_node.inputs[10],'default_value',text="Left Scale")
                eyes_row = eyes_box.row(align=True)
                eyes_row.prop(eye_node.inputs[12],'default_value',text="Roundness",slider=True)
                eyes_row.prop(eye_node.inputs[13],'default_value',text="Rotation")
                eyes_row = eyes_box.row(align=True)
                pupil_loc_col = eyes_row.column(align=True)
                pupil_loc_col.prop(eye_node.inputs[14],'default_value',text="Location X",index=1)
                pupil_loc_col.prop(eye_node.inputs[14],'default_value',text="Location Y",index=0)
                pupil_rot_col = eyes_row.column(align=True)
                pupil_rot_col.prop(eye_node.inputs[15],'default_value',text="Scale X",index=1)
                pupil_rot_col.prop(eye_node.inputs[15],'default_value',text="Scale Y",index=0)
                eyes_row = eyes_box.row(align=True)
                eyes_row.prop(eye_node.inputs[16],'default_value',text="")
                eyes_row.prop(eye_node.inputs[17],'default_value',text="")
                eyes_row = eyes_box.row(align=True)

            eyes_row.prop(eye_node.inputs[18],'default_value',text="Toggle Sparkle 1",toggle=True)
            eyes_row = eyes_box.row(align=True)
            if eye_node.inputs[18].default_value:
                eyes_row.prop(eye_node.inputs[20],'default_value',text="Scale")
                eyes_row.prop(eye_node.inputs[21],'default_value',text="Roundness",slider=True)
                eyes_row.prop(eye_node.inputs[22],'default_value',text="Rotation")
                eyes_row = eyes_box.row(align=True)
                sparkle_loc_col = eyes_row.column(align=True)
                sparkle_loc_col.prop(eye_node.inputs[23],'default_value',text="Location X",index=1)
                sparkle_loc_col.prop(eye_node.inputs[23],'default_value',text="Location Y",index=0)
                sparkle_rot_col = eyes_row.column(align=True)
                sparkle_rot_col.prop(eye_node.inputs[24],'default_value',text="Scale X",index=1)
                sparkle_rot_col.prop(eye_node.inputs[24],'default_value',text="Scale Y",index=0)
                eyes_row = eyes_box.row(align=True)
                eyes_row.prop(eye_node.inputs[19],'default_value',text="")
                eyes_row = eyes_box.row(align=True)

            eyes_row.prop(eye_node.inputs[25],'default_value',text="Toggle Sparkle 2",toggle=True)
            eyes_row = eyes_box.row(align=True)
            if eye_node.inputs[25].default_value:
                eyes_row.prop(eye_node.inputs[27],'default_value',text="Scale")
                eyes_row.prop(eye_node.inputs[28],'default_value',text="Roundness",slider=True)
                eyes_row.prop(eye_node.inputs[29],'default_value',text="Rotation")
                eyes_row = eyes_box.row(align=True)
                sparkle_loc_col = eyes_row.column(align=True)
                sparkle_loc_col.prop(eye_node.inputs[30],'default_value',text="Location X",index=1)
                sparkle_loc_col.prop(eye_node.inputs[30],'default_value',text="Location Y",index=0)
                sparkle_rot_col = eyes_row.column(align=True)
                sparkle_rot_col.prop(eye_node.inputs[31],'default_value',text="Scale X",index=1)
                sparkle_rot_col.prop(eye_node.inputs[31],'default_value',text="Scale Y",index=0)
                eyes_row = eyes_box.row(align=True)
                eyes_row.prop(eye_node.inputs[26],'default_value',text="")
                eyes_row = eyes_box.row(align=True)

            eyes_row.prop(eye_node.inputs[32],'default_value',text="Toggle Highlight",toggle=True)
            eyes_row = eyes_box.row(align=True)
            if eye_node.inputs[32].default_value:
                eyes_row.prop(eye_node.inputs[33],'default_value',text="Scale")
                eyes_row.prop(eye_node.inputs[34],'default_value',text="Roundness",slider=True)
                eyes_row.prop(eye_node.inputs[35],'default_value',text="Rotation")
                eyes_row = eyes_box.row(align=True)
                sparkle_loc_col = eyes_row.column(align=True)
                sparkle_loc_col.prop(eye_node.inputs[36],'default_value',text="Location X",index=1)
                sparkle_loc_col.prop(eye_node.inputs[36],'default_value',text="Location Y",index=0)
                sparkle_rot_col = eyes_row.column(align=True)
                sparkle_rot_col.prop(eye_node.inputs[37],'default_value',text="Scale X",index=1)
                sparkle_rot_col.prop(eye_node.inputs[37],'default_value',text="Scale Y",index=0)
                eyes_row = eyes_box.row(align=True)
                eyes_row.prop(eye_node.inputs[38],'default_value',text="")
                eyes_row.prop(eye_node.inputs[39],'default_value',text="")
                eyes_row = eyes_box.row(align=True)
        
        eyes_row.prop(eye_node.inputs[42],'default_value',text="Emission R",toggle=True)
        eyes_row.prop(eye_node.inputs[43],'default_value',text="Emission L",toggle=True)
        eyes_row = eyes_box.row(align=True)
        if eye_node.inputs[42].default_value or eye_node.inputs[43].default_value :
            eyes_row.prop(eye_node.inputs[44],'default_value',text="Real Light (Cycles Only)")
            eyes_row.prop(eye_node.inputs[45],'default_value',text="Visual Strength")
            eyes_row = eyes_box.row(align=True)
        
        eyes_row.prop(eye_node.inputs[40],'default_value',text="Roughness")
        eyes_row.prop(eye_node.inputs[41],'default_value',text="Specular")
        
        row = layout.row(align=True)

        misc_box = row.box()
        misc_row = misc_box.row(align=True)
        misc_row.label(text="Misc",icon='MATERIAL')
        misc_row = misc_box.row(align=True)

        right_eyebrow_1 = GetMaterial(context,'right_eyebrow_1')
        right_eyebrow_2 = GetMaterial(context,'right_eyebrow_2')
        left_eyebrow_1 = GetMaterial(context,'left_eyebrow_1')
        left_eyebrow_2 = GetMaterial(context,'left_eyebrow_2')
        
        misc_row.label(text="Eyebrow Colors")
        misc_row = misc_box.row(align=True)
        misc_row.prop(right_eyebrow_2.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        misc_row.prop(right_eyebrow_1.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        misc_row.prop(left_eyebrow_1.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        misc_row.prop(left_eyebrow_2.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")

        misc_row = misc_box.row(align=True)
        misc_row.label(text="Eyewhite Colors")
        misc_row = misc_box.row(align=True)
        right_eyewhite_upper = GetMaterial(context,'eyewhite_right_upper')
        right_eyewhite_lower = GetMaterial(context,'eyewhite_right_lower')
        left_eyewhite_upper = GetMaterial(context,'eyewhite_left_upper')
        left_eyewhite_lower = GetMaterial(context,'eyewhite_left_lower')
        right_eyewhite_col = misc_row.column(align=True)
        left_eyewhite_col = misc_row.column(align=True)

        right_eyewhite_col.prop(right_eyewhite_upper.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        right_eyewhite_col.prop(right_eyewhite_lower.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        left_eyewhite_col.prop(left_eyewhite_upper.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        left_eyewhite_col.prop(left_eyewhite_lower.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")

        misc_row = misc_box.row(align=True)
        misc_row.label(text="Cartoon Mouth Color")
        misc_row = misc_box.row(align=True)
        cartoon_mouth = GetMaterial(context,'cartoon_mouth')
        misc_row.prop(cartoon_mouth.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")

        misc_row = misc_box.row(align=True)
        misc_row.label(text="Eyelashes")
        misc_row = misc_box.row(align=True)
        left_eyelash = GetMaterial(context,'left_eyelash')
        right_eyelash = GetMaterial(context,'right_eyelash')
        misc_row.prop(right_eyelash.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        misc_row.prop(left_eyelash.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        

        misc_row = misc_box.row(align=True)
        misc_row.label(text="Lipstick")
        misc_row = misc_box.row(align=True)
        lipstick_top = GetMaterial(context,'lipstick_top')
        lipstick_bottom = GetMaterial(context,'lipstick_bottom')
        misc_row.prop(lipstick_top.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")
        misc_row = misc_box.row(align=True)
        misc_row.prop(lipstick_bottom.node_tree.nodes['Principled BSDF'].inputs[0],'default_value',text="")