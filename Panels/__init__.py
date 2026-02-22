import bpy

from . import bone_collections
from . import workflow
from . import style
from . import add_menu
from . import ice_cube
from . import parenting

classes = (
    ice_cube.ICECUBERIG_PT_IceCubeMain,
    workflow.ICECUBERIG_PT_Workflow,
    workflow.ICECUBERIG_PT_FaceSettings,
    workflow.ICECUBERIG_PT_ArmSettings,
    workflow.ICECUBERIG_PT_LegSettings,
    workflow.ICECUBERIG_PT_BodySettings,
    bone_collections.ICECUBERIG_PT_BoneCollections,
    style.ICECUBERIG_PT_Style,
    style.ICECUBERIG_PT_StyleTaper,
    style.ICECUBERIG_PT_StyleBulge,
    style.ICECUBERIG_PT_StyleCosmetics,
    style.ICECUBERIG_PT_StyleEmotions,
    style.ICECUBERIG_PT_StyleMouth,
    style.ICECUBERIG_PT_StyleSkin,
    style.ICECUBERIG_PT_StyleMaterial,
    style.ICECUBERIG_PT_StyleMaterialEYES,
    style.ICECUBERIG_PT_StyleMaterialMISC,
    parenting.ICECUBERIG_PT_Parenting,
    add_menu.ICECUBERIG_MT_3dview_add,
    add_menu.ICECUBE_AppendChar,
    add_menu.ICECUBERIG_CUSTOMCHAR_MT_3dview_add
)

cls_register, cls_unregister = bpy.utils.register_classes_factory(classes)

def register():
    cls_register()
    bpy.types.VIEW3D_MT_add.append(add_menu.AddMenuFunction)
    add_menu.register()

def unregister():
    cls_unregister()

    bpy.types.VIEW3D_MT_add.remove(add_menu.AddMenuFunction)
    add_menu.unregister()
