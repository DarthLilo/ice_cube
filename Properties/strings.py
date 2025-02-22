import bpy
from bpy.props import (
    StringProperty,
)

bpy.types.Scene.ice_cube_minecraft_username = StringProperty(
    name="Minecraft Username",
    default=""
)
