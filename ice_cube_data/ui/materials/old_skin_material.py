#Libraries
import bpy
from sys import platform

def skin_material_UI(self, context, layout, skin_mat, face):
    box = layout.box()
    box.label(text= "Skin Texture", icon= 'IMAGE_DATA')
    b = box.row(align=True)
    b.label(text= "Username:")
    b = box.row(align=True)
    if platform == "darwin":
        b2 = b.row(align=True)
        b2.prop(context.scene, "minecraft_username", text="", icon='URL')
        b2.operator("skin.download", text="", icon='IMPORT')
        b2.enabled = False
    else:
        b2 = b.row(align=True)
        b2.prop(context.scene, "minecraft_username", text="", icon='URL')
        b2.operator("skin.download", text="", icon='IMPORT')
        b2.enabled = True
    b = box.row(align=True)
    b = box.row(align=True)
    b.label(text= "Texture Path:")
    b = box.row(align=True)
    b.context_pointer_set("edit_image",skin_mat.image)
    b.operator("image.unpack" if skin_mat.image.packed_file else "image.pack",
                text="", icon="PACKAGE" if skin_mat.image.packed_file else "UGLYPACKAGE")
    b.prop(skin_mat.image, "filepath", text="")
    b.operator("image.reload", text="", icon='FILE_REFRESH')
    
    b = box.row(align=True)
    b.prop(face.material_slots[0].material.node_tree.nodes['color'].inputs[1], 'default_value', text="Auto SSS", slider=True)
    b = box.row(align=True)
    b.prop(face.material_slots[0].material.node_tree.nodes['color'].inputs[3], 'default_value', text="Sensitivity", slider=True)
    b = box.row(align=True)
    b.prop(face.material_slots[0].material.node_tree.nodes['color'].inputs[4], 'default_value', text="SSS", slider=True)
    b = box.row(align=True)
    b.prop(face.material_slots[0].material.node_tree.nodes['color'].inputs[7], 'default_value', text="Radius", slider=False)
    b = box.row(align=True)
    b.prop(face.material_slots[0].material.node_tree.nodes['color'].inputs[2], 'default_value', text="Skin Color", slider=True)
    b = box.row(align=True)
    b.prop(face.material_slots[0].material.node_tree.nodes['color'].inputs[5], 'default_value', text="SSS Color", slider=True)
    b = box.row(align=True)

    b.label(text = "Downloaded Skins:")
    b = box.row(align=True)
    wm = context.window_manager
    b.template_icon_view(wm, "skins_folder")
    b = box.row(align=True)
    b.operator("skin.apply", text="Apply Skin")
    b.operator("skin.reset", text="Reset Skin")
    b = box.row(align=True)
    b.operator("skin.delete", text="Delete Skin")  

classes = [
           ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__=="__main__":
    register()