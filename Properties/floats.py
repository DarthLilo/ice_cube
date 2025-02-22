import bpy
from bpy.props import (
    FloatProperty,
)

# Arm Settings
class ArmSettings():
    bpy.types.Object.left_arm_ik = FloatProperty(
        name = "Left Arm IK",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_arm_stretch = FloatProperty(
        name = "Left Arm Stretch",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_arm_wrist_lock = FloatProperty(
        name = "Left Arm Wrist Lock",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_arm_ik = FloatProperty(
        name = "Right Arm IK",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_arm_stretch = FloatProperty(
        name = "Right Arm Stretch",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_arm_wrist_lock = FloatProperty(
        name = "Right Arm Wrist Lock",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

# Leg Settings
class LegSettings():
    bpy.types.Object.left_leg_ik = FloatProperty(
        name = "Left Leg IK",
        default=1,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_leg_stretch = FloatProperty(
        name = "Left Leg Stretch",
        default=1,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_leg_ankle_lock = FloatProperty(
        name = "Left Leg Ankle Lock",
        default=1,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_leg_ik = FloatProperty(
        name = "Right Leg IK",
        default=1,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_leg_stretch = FloatProperty(
        name = "Right Leg Stretch",
        default=1,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_leg_ankle_lock = FloatProperty(
        name = "Right Leg Ankle Lock",
        default=1,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

#Face Settings
class FaceSettings():
    bpy.types.Object.fluid_face_strength = FloatProperty(
        name = "Fluid Face Strength",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.blink_position = FloatProperty(
        name = "Blink Position",
        default=0.2,
        min=0, max=0.5,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.lipstick_thickness = FloatProperty(
        name = "Lipstick Thickness",
        default=0,
        min=0, max=2,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.eye_depth = FloatProperty(
        name = "Eye Depth",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )
    
    bpy.types.Object.mouth_depth = FloatProperty(
        name = "Mouth Depth",
        default=0,
        min=-0.65, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.inner_mouth_depth = FloatProperty(
        name = "Inner Mouth Depth",
        default=1,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.jaw_shape = FloatProperty(
        name = "Jaw Shape",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.blush_strength = FloatProperty(
        name = "Blush Strength",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )
    
    bpy.types.Object.right_tear = FloatProperty(
        name = "Right Tear",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_tear = FloatProperty(
        name = "Left Tear",
        default=0,
        min=0, max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )
    

#Taper Settings
class TaperSettings():
    bpy.types.Object.head_taper = FloatProperty(
        name="Head Taper",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_arm_taper_upper = FloatProperty(
        name="Left Arm Taper Upper",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )
    bpy.types.Object.right_arm_taper_upper = FloatProperty(
        name="Left Arm Taper Upper",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_arm_taper_lower = FloatProperty(
        name="Left Arm Taper Lower",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )
    bpy.types.Object.right_arm_taper_lower = FloatProperty(
        name="Left Arm Taper Lower",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_leg_taper_upper = FloatProperty(
        name="Left Leg Taper Upper",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_leg_taper_upper = FloatProperty(
        name="Left Leg Taper Upper",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_leg_taper_lower = FloatProperty(
        name="Left Leg Taper Lower",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_leg_taper_lower = FloatProperty(
        name="Left Leg Taper Lower",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

class BulgeSettings():
    bpy.types.Object.head_bulge = FloatProperty(
        name="Head Bulge",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.eye_bulge = FloatProperty(
        name="Eye Bulge",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.body_bulge = FloatProperty(
        name="Body Bulge",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_arm_bulge = FloatProperty(
        name="Left Arm Bulge",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_arm_bulge = FloatProperty(
        name="Left Arm Bulge",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.left_leg_bulge = FloatProperty(
        name="Left Arm Bulge",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.right_leg_bulge = FloatProperty(
        name="Left Arm Bulge",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

class BevelSettings():
    bpy.types.Object.bevel_mouth_strength = FloatProperty(
        name="Mouth Bevel",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.eye_bevel = FloatProperty(
        name="Eye Bevel",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

class BreastSettings():
    bpy.types.Object.breast_size = FloatProperty(
        name="Breast Size",
        default=0,
        min=0,max=2,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.breast_angle = FloatProperty(
        name="Breast Angle",
        default=0,
        min=0,max=1.5,
        override={"LIBRARY_OVERRIDABLE"}
    )

class CosmeticSettings():
    bpy.types.Object.eyebrow_height = FloatProperty(
        name="Eyebrow Height",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.eyebrow_taper = FloatProperty(
        name="Eyebrow Taper",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

class BodyDeforms():
    bpy.types.Object.hip = FloatProperty(
        name="Hip",
        default=0,
        min=0,max=2,
        override={"LIBRARY_OVERRIDABLE"}
    )
    bpy.types.Object.upper_body_width = FloatProperty(
        name="Upper Body Width",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )
    bpy.types.Object.lower_body_width = FloatProperty(
        name="Lower Body Width",
        default=0,
        min=-1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )
    bpy.types.Object.body_bend_shape = FloatProperty(
        name="Body Bend Shape",
        default=1,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

class GenericSettings():
    bpy.types.Object.bend_smoothness = FloatProperty(
        name="Bend Smoothness",
        default=0,
        min=-0.1,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.arm_scale = FloatProperty(
        name="Arm Scale",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.leg_scale = FloatProperty(
        name="Leg Scale",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )

    bpy.types.Object.jaw_strength = FloatProperty(
        name="Jaw Strength",
        default=0.3,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )
    
    bpy.types.Object.teeth_curve = FloatProperty(
        name="Teeth Curve",
        default=0,
        min=0,max=1,
        override={"LIBRARY_OVERRIDABLE"}
    )