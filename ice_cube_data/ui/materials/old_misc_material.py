#Libraries
import bpy

def misc_material_UI(self, context, layout, face):
    box = layout.box()
    box.label(text= "Misc Materials", icon= 'MATERIAL')
    b = box.row(align=True)
    box.label(text= "Eyewhites")
    b = box.column(align=True)
    b1 = b.row(align=True)
    b1.prop(face.material_slots[10].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
    b1.prop(face.material_slots[2].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
    b1 = b.row(align=True)
    b1.prop(face.material_slots[11].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
    b1.prop(face.material_slots[9].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
    b1 = b.row(align=True)
    b1.prop(face.material_slots[2].material.node_tree.nodes['Principled BSDF'].inputs[7], 'default_value', text="Specular", slider=True)
    b1.prop(face.material_slots[2].material.node_tree.nodes['Principled BSDF'].inputs[9], 'default_value', text="Roughness", slider=True)
    b = box.row(align=True)
    box.label(text= "Eyebrows")
    b = box.column(align=True)
    b1 = b.row(align=True)
    b1.prop(face.material_slots[14].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
    b1.prop(face.material_slots[13].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
    b1 = b1.column(align=False)
    b1 = b1.row(align=True)
    b1.prop(face.material_slots[6].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
    b1.prop(face.material_slots[12].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
    b = box.row(align=True)
    b.prop(face.material_slots[3].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="Tongue", slider=True)
    b.enabled = False
    b = box.row(align=True)
    b.prop(face.material_slots[4].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="Teeth", slider=True)
    b = box.row(align=True)
    b.prop(face.material_slots[5].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="Mouth Inside", slider=True)
    b = box.row(align=True)
    b.prop(face.material_slots[15].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="Cartoon Mouth", slider=True)
    b = box.row(align=True)
    b.prop(face.material_slots[16].material.node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="Emotion Line", slider=True)
    b = box.row(align=True)

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