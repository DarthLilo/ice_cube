import bpy, os, pathlib
import bpy.utils.previews

from .constants import SKIN_STORAGE, ICONS

class IconLoaderMethod:
    
    @staticmethod
    def load_icons(pcoll) -> None:
        
        for icon in os.listdir(ICONS):
            path = os.path.join(ICONS,icon)
            pcoll.load(pathlib.Path(icon).stem, path, "IMAGE")

        pass

    def load_skins():
        skins_pcoll = ice_cube_icons_collection["ice_cube_remake"]
        skin_items = []

        skin_path = SKIN_STORAGE
        os.makedirs(skin_path,exist_ok=True)

        wm = bpy.context.window_manager
        image_paths = []

        for img in os.listdir(SKIN_STORAGE):
            if img.lower().endswith(".png"):
                image_paths.append(img)
        
        for i, name in enumerate(image_paths):
            img_path = os.path.join(SKIN_STORAGE,name)
            icon = skins_pcoll.get(name)
            
            if not icon:
                thumb = skins_pcoll.load(name,img_path,'IMAGE')
            else:
                thumb = skins_pcoll[name]

            skin_items.append((name,name,"",thumb.icon_id,i))

        return skin_items
    
    @staticmethod
    def reload_icons() -> None:
        for pcoll in ice_cube_icons_collection.values():
            bpy.utils.previews.remove(pcoll)
        
        pcoll = bpy.utils.previews.new()
        IconLoaderMethod.load_icons(pcoll)
        ice_cube_icons_collection["ice_cube_remake"] = pcoll

ice_cube_icons_collection = {}

def register():

    def update_skin_items(self, context):
        return IconLoaderMethod.load_skins()

    bpy.types.WindowManager.ice_cube_skin_library = bpy.props.EnumProperty(
        items = update_skin_items
    )

    IconLoaderMethod.reload_icons()

def unregister():

    del bpy.types.WindowManager.ice_cube_skin_library

    for pcoll in ice_cube_icons_collection.values():
        bpy.utils.previews.remove(pcoll)

    ice_cube_icons_collection.clear()