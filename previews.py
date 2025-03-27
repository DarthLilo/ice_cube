import bpy, os
from bpy.utils import previews

from .constants import SKIN_STORAGE

ice_cube_skin_collections = {}

class PreviewsClass(bpy.types.PropertyGroup):

    def load_skins(self, context, dir, entry):
        skin_items = []
        
        if context is None:
            return skin_items
        
        skins_pcoll = ice_cube_skin_collections["ice_cube_skin_library"]

        if dir and os.path.exists(dir):
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
        
        setattr(skins_pcoll, entry, skin_items)
        return skin_items

    def get_skins_items(self, context):
        return self.load_skins(context, SKIN_STORAGE, "skin_library")
    
    skin_library : bpy.props.EnumProperty(items = get_skins_items )


def register():
    bpy.utils.register_class(PreviewsClass)
    bpy.types.WindowManager.ice_cube_skin_library = bpy.props.PointerProperty(type=PreviewsClass)

    pcoll = previews.new()
    pcoll.skin_library = ()
    ice_cube_skin_collections['ice_cube_skin_library'] = pcoll

def unregister():
    del bpy.types.WindowManager.ice_cube_skin_library

    for pcoll in ice_cube_skin_collections.values():
        previews.remove(pcoll)
    ice_cube_skin_collections.clear()

    bpy.utils.unregister_class(PreviewsClass)