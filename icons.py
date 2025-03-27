import bpy, os, pathlib
from bpy.utils import previews

from .constants import ICONS

class IconLoaderMethod:
    
    @staticmethod
    def load_icons(pcoll) -> None:
        
        for icon in os.listdir(ICONS):
            path = os.path.join(ICONS,icon)
            pcoll.load(pathlib.Path(icon).stem, path, "IMAGE")

        pass
    
    @staticmethod
    def reload_icons() -> None:
        for pcoll in ice_cube_icons_collection.values():
            previews.remove(pcoll)
        
        pcoll = previews.new()
        IconLoaderMethod.load_icons(pcoll)
        ice_cube_icons_collection["ice_cube_remake"] = pcoll

ice_cube_icons_collection = {}

def register():
    IconLoaderMethod.reload_icons()

def unregister():
    del bpy.types.WindowManager.ice_cube_skin_library
    for pcoll in ice_cube_icons_collection.values():
        previews.remove(pcoll)

    ice_cube_icons_collection.clear()