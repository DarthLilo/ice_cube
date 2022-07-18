#Libraries
import bpy

def eye_material_UI(self, context, layout, obj, face):
    box = layout.box()
    box.label(text= "Eye Materials", icon= 'NODETREE')
    box1 = box.box()
    box1.label(text= "Eye Colors", icon= 'NODE_MATERIAL')
    b = box1.column(align=True)
    b1 = b.row(align=True)
    b1.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[0], 'default_value', text="", slider=True)
    b1.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[2], 'default_value', text="", slider=True)
    b1 = b.row(align=True)
    b1.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[1], 'default_value', text="", slider=True)
    b1.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[3], 'default_value', text="", slider=True)
    b1 = b.row(align=True)
    
    boxlayout = box1.box().column()
    boxlayout.label(text= "Right Eye Gradient", icon= 'MATERIAL_DATA')
    reg1 = face.material_slots[1].material.node_tree.nodes['Gradient Right']
    boxlayout.template_color_ramp(reg1, "color_ramp", expand=True)
    boxlayout = box1.box().column()
    boxlayout.label(text= "Left Eye Gradient", icon= 'MATERIAL_DATA')
    leg1 = face.material_slots[1].material.node_tree.nodes['Gradient Left']
    boxlayout.template_color_ramp(leg1, "color_ramp", expand=True)
    
    box1 = box.box()
    box1.label(text= "Secondary Colors", icon= 'NODE_MATERIAL')
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[11], 'default_value', text="", slider=True)
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[16], 'default_value', text="", slider=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[20], 'default_value', text="", slider=True)
    
    box1 = box.box()
    box1.label(text= "Eye Settings", icon= 'NODE_MATERIAL')
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[4], 'default_value', text="Specular", slider=True)
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[5], 'default_value', text="Roughness", slider=True)
    b = box1.row(align=True)
    if obj.get("togglegradient") == 0:
        b.prop(obj, "togglegradient", icon = "LAYER_USED", text = "Toggle Gradient")
    else:
        b.prop(obj, "togglegradient", icon = "LAYER_ACTIVE", text = "Toggle Gradient")
    b = box1.row(align=True)
    if obj.get("togglepupil") == 0:
        b.prop(obj, "togglepupil", icon = "LAYER_USED", text = "Toggle Pupil")
    else:
        b.prop(obj, "togglepupil", icon = "LAYER_ACTIVE", text = "Toggle Pupil")
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[10], 'default_value', text="Pupil Size")
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[12], 'default_value', text="Pupil Bright", slider=True)
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[25], 'default_value', text="Flip Pupil Bright", slider=True)
    bc = box1.column(align=True)
    bc.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[24], 'default_value', text="Pupil Size 2", slider=False)
    b = box1.row(align=True)
    if obj.get("togglesparkle1") == 0:
        b.prop(obj, "togglesparkle1", icon = "LAYER_USED", text = "Toggle Sparkle 1")
    else:
        b.prop(obj, "togglesparkle1", icon = "LAYER_ACTIVE", text = "Toggle Sparkle 1")
    if obj.get("togglesparkle2") == 0:
        b.prop(obj, "togglesparkle2", icon = "LAYER_USED", text = "Toggle Sparkle 2")
    else:
        b.prop(obj, "togglesparkle2", icon = "LAYER_ACTIVE", text = "Toggle Sparkle 2")
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[14], 'default_value', text="Sparkle 1 Size", slider=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[18], 'default_value', text="Sparkle 2 Size", slider=True)
    split = box1.split(factor=0.5, align=True)
    bc = split.column(align=True)
    bc.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[15], 'default_value', text="Sparkle 1 POS", slider=False)
    bc = split.column(align=True)
    bc.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[19], 'default_value', text="Sparkle 2 POS", slider=False)
    
    
    b = box1.row(align=True)
    if obj.get("toggleemission") == 0:
        b.prop(obj, "toggleemission", icon = "LAYER_USED", text = "Toggle Emission")
    else:
        b.prop(obj, "toggleemission", icon = "LAYER_ACTIVE", text = "Toggle Emission")
    b = box1.row(align=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[22], 'default_value', text="Real Light", slider=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[23], 'default_value', text="Texture Light", slider=True)

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