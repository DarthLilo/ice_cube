import bpy

from . import constants
from . import Operators
from . import Panels
from . import Properties
from . import icons

bl_info = {
    "name": "Ice Cube Rig",
    "author": "DarthLilo",
    "version": (2, 0, 0),
    "blender": (4, 2, 0)
}

modules = (
    "Operators",
    "Panels",
    "Properties",
    "icons"
)

register, unregister = bpy.utils.register_submodule_factory(module_name=__name__, submodule_names=modules)