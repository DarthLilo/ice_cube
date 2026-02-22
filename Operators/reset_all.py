import bpy

from ..ice_cube_selectors import GetMaterial
from ..constants import DEFAULT_SKIN
from ..utils import UnpackImage

def get_default(holder, prop_name):
    prop = holder.bl_rna.properties[prop_name]

    return prop.default

ice_cube_properties = [
            "arm_type",
            "advanced_mode",
            "left_fingers",
            "left_thumbfill",
            "right_fingers",
            "right_thumbfill",
            "face_rig",
            "eyetracker",
            "global_head_rotation",
            "cartoon_mouth",
            "o_mouth_shape",
            "lipstick",
            "round_jaw",
            "tongue",
            "texture_deform",
            "teeth_bool",
            "body_squish",
            "head_squish",
            "shoulder_deform",
            "lock_limb_rotation",
            "eyelashes",
            "left_arm_ik",
            "left_arm_stretch",
            "left_arm_wrist_lock",
            "right_arm_ik",
            "right_arm_stretch",
            "right_arm_wrist_lock",
            "left_leg_ik",
            "left_leg_stretch",
            "left_leg_ankle_lock",
            "right_leg_ik",
            "right_leg_stretch",
            "right_leg_ankle_lock",
            "fluid_face_strength",
            "blink_position",
            "lipstick_thickness",
            "head_taper",
            "left_arm_taper_upper",
            "right_arm_taper_upper",
            "left_leg_taper_upper",
            "right_leg_taper_upper",
            "left_arm_taper_lower",
            "right_arm_taper_lower",
            "left_leg_taper_lower",
            "right_leg_taper_lower",
            "head_bulge",
            "eye_bulge",
            "body_bulge",
            "left_arm_bulge",
            "right_arm_bulge",
            "left_leg_bulge",
            "right_leg_bulge",
            "bevel_mouth_strength",
            "eye_bevel",
            "breast_size",
            "breast_angle",
            "eyebrow_height",
            "eyebrow_taper",
            "hip",
            "upper_body_width",
            "lower_body_width",
            "bend_smoothness",
            "arm_scale",
            "leg_scale",
            "jaw_strength",
            "teeth_curve",
            "minecraft_accurate_scaling",
            "eye_depth",
            "mouth_depth",
            "inner_mouth_depth",
            "performance_mode",
            "jaw_shape",
            "emotion_eye_shape",
            "emotion_anger",
            "blush_strength",
            "left_tear",
            "right_tear",
            "eyelashes_lower",
            "mouth_toggle",
            "eye_toggle",
            "emotion_eyebags",
            "emotion_eyebrow_point_L",
            "emotion_eyebrow_line_L",
            "emotion_eyebrow_line_U_L",
            "emotion_eyebrow_shocked_L",
            "emotion_eye_line_L",
            "emotion_eye_point_L",
            "emotion_eye_shocked_L",
            "emotion_eyebrow_point_R",
            "emotion_eyebrow_line_R",
            "emotion_eyebrow_line_U_R",
            "emotion_eyebrow_shocked_R",
            "emotion_eye_line_R",
            "emotion_eye_point_R",
            "emotion_eye_shocked_R",
            "left_arm_IK_parent",
            "right_arm_IK_parent",
            "left_leg_IK_parent",
            "right_leg_IK_parent",
            "bevel_toggle_viewport",
            "bevel_toggle_render",
        ]

def get_modified_settings():
    modified_properties = {}
    for property in ice_cube_properties:
        cur_value = getattr(bpy.context.object, property)
        default_value = get_default(bpy.context.object,property)

        if cur_value != default_value:
            modified_properties[property] = cur_value
    
    return(modified_properties)

class ICECUBE_Reset(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}
    bl_idname = 'ice_cube.reset_all'
    bl_label = "Reset All"

    def execute(self, context):

        obj = context.object

        #Reset Properties
        for prop in ice_cube_properties:
            default = get_default(obj,prop)
            setattr(obj,prop,default)

        current_skin = GetMaterial(context, 'skin').node_tree.nodes['Skin Texture'].image
        UnpackImage(current_skin)
        current_skin.filepath = DEFAULT_SKIN

        for bone in obj.pose.bones:
            bone.location = (0,0,0)
            bone.rotation_quaternion = [1,0,0,0]
            bone.rotation_euler = [0,0,0]
            bone.scale = (1,1,1)

        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self,title="Reset rig confirmation?",confirm_text="Reset")