import bpy
from bpy.props import (
    PointerProperty,
)

def check_for_armor_collections():
    valid_collections = []
    try:
        for collection in bpy.data.collections:
            if "ice_cube_collection" in collection and collection["ice_cube_collection"] == "armor":
                valid_collections.append(collection)
    except AttributeError:
        pass

    return valid_collections




def register():
    global IceCubeArmorCollectionTarget


    class IceCubeArmorCollectionTarget(bpy.types.PropertyGroup):
        armor_collection_target: PointerProperty(
            name="Armor Collection Target",
            type=bpy.types.Collection,
            poll=lambda self, obj: obj in check_for_armor_collections()
        )
    
    
    bpy.utils.register_class(IceCubeArmorCollectionTarget)
    bpy.types.Scene.ice_cube_remake = PointerProperty(type=IceCubeArmorCollectionTarget)

def unregister():

    bpy.utils.unregister_class(IceCubeArmorCollectionTarget)
    del bpy.types.Scene.ice_cube_remake