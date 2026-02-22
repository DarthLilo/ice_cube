import bpy

from . import icons
from . import constants
from . import Operators
from . import Panels
from . import Properties
from . import previews


bl_info = {
    "name": "Ice Cube Rig",
    "author": "DarthLilo",
    "version": (2, 1, 0),
    "blender": (4, 2, 0)
}

modules = (
    "icons",
    "previews",
    "Operators",
    "Panels",
    "Properties"
)

register, unregister = bpy.utils.register_submodule_factory(module_name=__name__, submodule_names=modules)