#Libraries
import bpy

def eye_mat_UI(self, context, face):
    layout = self.layout
    obj = context.object
    box = layout.box()
    box.label(text= "Eye Materials", icon= 'NODETREE')
    box1 = box.box()
    b = box1.row(align=True)
    b.label(text= "Iris Settings", icon= 'NODE_MATERIAL')
    b = box1.row(align=True)
    b = b.column(align=True)

    #Iris Settings
    b1 = b.row(align=True)
    b1.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[0], 'default_value', text="", slider=True)
    b1.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[2], 'default_value', text="", slider=True)
    b1 = b.row(align=True)
    b1.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[1], 'default_value', text="", slider=True)
    b1.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[3], 'default_value', text="", slider=True)
    b = box1.row(align=True)
    
    #Gradients
    
    b.prop(obj, "togglegradient", toggle=True, text = "Toggle Gradient")

    if obj.get("togglegradient") == True:
        boxlayout = box1.box().column(align=True)
        boxlayout.label(text= "Right Eye Gradient", icon= 'MATERIAL_DATA')
        reg1 = face.material_slots[1].material.node_tree.nodes['Gradient Right']
        boxlayout.template_color_ramp(reg1, "color_ramp", expand=True)
        boxlayout = box1.box().column(align=True)
        boxlayout.label(text= "Left Eye Gradient", icon= 'MATERIAL_DATA')
        leg1 = face.material_slots[1].material.node_tree.nodes['Gradient Left']
        boxlayout.template_color_ramp(leg1, "color_ramp", expand=True)
    
    b = box1.row(align=True)
    
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[4], 'default_value', text="Specular", slider=True)
    b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[5], 'default_value', text="Roughness", slider=True)
    
    b = box1.row(align=True)

    b.prop(obj, "toggleemission", icon = "LAYER_USED", text = "Toggle Emission")
    if obj.get("toggleemission") == True:
        b = box1.row(align=True)
        b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[22], 'default_value', text="Real Light", slider=True)
        b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[23], 'default_value', text="Texture Light", slider=True)


    #Pupil Settings
    box1 = box.box()
    b = box1.row(align=True)
    b.label(text= "Pupil Settings", icon= 'NODE_MATERIAL')
    b = box1.row(align=True)
    b.prop(obj, "togglepupil", toggle=True, text = "Toggle Pupil")
    if obj.get("togglepupil") == True:
        b = box1.row(align=True)
        b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[11], 'default_value', text="", slider=True)
        b = box1.row(align=True)
        b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[10], 'default_value', text="Pupil Size")
        b = box1.row(align=True)
        b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[12], 'default_value', text="Pupil Bright", slider=True)
        b.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[25], 'default_value', text="Flip Pupil Bright", slider=True)
        bc = box1.column(align=True)
        bc.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[24], 'default_value', text="Pupil Size 2", slider=False)
        b = box1.row(align=True)
    
    #Sparkle Settings
    box1 = box.box()
    b = box1.row(align=True)
    b.label(text= "Sparkle Settings", icon= 'NODE_MATERIAL')
    b = box1.row(align=True)
    b.prop(obj, "togglesparkle1", toggle = True, text = "Toggle Sparkle 1")
    b.prop(obj, "togglesparkle2", toggle = True, text = "Toggle Sparkle 2")
    split = box1.split(factor=0.5, align=True)
    if obj.get("togglesparkle1") is True or obj.get("togglesparkle2") is True:
        b = box1.row(align=True)
    bc = split.column(align=True)
    if obj.get("togglesparkle1") == True:
        bc.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[14], 'default_value', text="Sparkle 1 Size", slider=True)
    if obj.get("togglesparkle2") == True:
        bc = split.column(align=True)
        bc.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[18], 'default_value', text="Sparkle 2 Size", slider=True)
    split = box1.split(factor=0.5, align=True)
    if obj.get("togglesparkle1") is True or obj.get("togglesparkle2") is True:
        bc.row(align=True)
    bc = split.column(align=True)
    if obj.get("togglesparkle1") == True:
        bc.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[15], 'default_value', text="Sparkle 1 POS", slider=False)
    if obj.get("togglesparkle2") == True:
        bc = split.column(align=True)
        bc.prop(face.material_slots[1].material.node_tree.nodes['eyenode'].inputs[19], 'default_value', text="Sparkle 2 POS", slider=False)


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