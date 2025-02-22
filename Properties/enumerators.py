import bpy
from bpy.props import (
    EnumProperty,
)

#-------------------------------------------------#
#                     Updates
#-------------------------------------------------#
def generic_update(self, context):
    pass


# Arm Types
bpy.types.Object.arm_type = EnumProperty(
    name = "Arm Type Selection",
    default='1',
    items=[
        ('1', 'Steve', '4x4 Arms'),
        ('2', 'Alex', '4x3 Arms'),
        ('3', 'Thin', '3x3 Arms')
    ],
    update=generic_update,
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.eyelashes = EnumProperty(
    name = "Eyelash Type",
    default='1',
    items=[
        ('1', 'None', 'No Eyelashes'),
        ('2', 'Standard', 'Standard Ice Cube Eyelashes'),
        ('3', 'Andromeda', 'Andromeda Styled Eyelashes'),
        ('4', 'Bushy', 'Bushy Eyelashes')
    ],
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.eyelashes_lower = EnumProperty(
    name = "Eyelash Lower Type",
    default='1',
    items=[
        ('1', 'None', 'No Eyelashes'),
        ('2', 'Standard', 'Standard Ice Cube Eyelashes'),
        ('3', 'Bushy', 'Bushy Eyelashes')
    ],
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.performance_mode = EnumProperty(
    name="Animation Mode",
    default='2',
    items=[
        ('1', 'Performance','Displays graybox meshes ONLY'),
        ('2', 'High Quality','Full quality mesh display')
    ],
    override={"LIBRARY_OVERRIDABLE"}
)

bpy.types.Object.emotion_eye_shape = EnumProperty(
    name="Eye Shape",
    default='0',
    items=[
        ('0', 'None','No eyeshape'),
        ('1', 'Dizzy','Dizzy Eyeshape'),
        ('2', 'X','X Eyeshape'),
        ('3', 'Happy','Happy Eyeshape'),
        ('4', 'Money','Dollar Eyeshape'),
        ('5', 'Star','Star Eyeshape'),
        ('6', 'Heart','Heart Eyeshape')
    ],
    override={"LIBRARY_OVERRIDABLE"}
)