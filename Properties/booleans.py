import bpy
from bpy.props import (
    BoolProperty,
)


bpy.types.Object.advanced_mode = BoolProperty(
    name="Advanced Mode",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

# Finger Bools
bpy.types.Object.left_fingers = BoolProperty(
    name = "Left Fingers",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)
bpy.types.Object.left_thumbfill = BoolProperty(
    name = "Left Thumbfill",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.right_fingers = BoolProperty(
    name = "Right Fingers",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)
bpy.types.Object.right_thumbfill = BoolProperty(
    name = "Right Thumbfill",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

# Face Bools
bpy.types.Object.face_rig = BoolProperty(
    name="Face Rig",
    default=True,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.eyetracker = BoolProperty(
    name="Eyetracker",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.global_head_rotation = BoolProperty(
    name="Global Head Rot",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.cartoon_mouth = BoolProperty(
    name="Cartoon Mouth",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.o_mouth_shape = BoolProperty(
    name="O Mouth Shape",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.lipstick = BoolProperty(
    name="Lipstick",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.round_jaw = BoolProperty(
    name="Round Jaw",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.tongue = BoolProperty(
    name="Tongue",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.texture_deform = BoolProperty(
    name="Texture Deform",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.teeth_bool = BoolProperty(
    name="Teeth Bool",
    default=True,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.emotion_anger = BoolProperty(
    name="Anger",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)


# Body
bpy.types.Object.body_squish = BoolProperty(
    name="Body Squish",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.head_squish = BoolProperty(
    name="Head Squish",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.shoulder_deform = BoolProperty(
    name="Shoulder Deform",
    default=False,
    override={"LIBRARY_OVERRIDABLE"}
)

#general bools

bpy.types.Object.lock_limb_rotation = BoolProperty(
    name="Limb Rotation Lock",
    default=True,
    description="Allows the arms/legs to rotate freely in FK mode, WILL cause issues with IK/FK conversion!",
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.minecraft_accurate_scaling = BoolProperty(
    name="Minecraft Accurate Scaling",
    default=True,
    description="Scales the rig to fit to most minecraft scenes!",
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.ik_fk_keyframe = BoolProperty(
    name="IK FK Keyframe",
    default=False,
    description="Turns on keyframing for the IK FK conversion buttons",
    override={"LIBRARY_OVERRIDABLE"}
)