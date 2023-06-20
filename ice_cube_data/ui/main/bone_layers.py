#Libraries
import bpy

from ice_cube_data.utils.ui_tools import button_toggle

def bone_layers_UI(self, context, layout, obj):
    layers = context.active_object.data
    box = layout.box()
    box.label(text= "Bone Layers", icon= 'RENDERLAYERS')
    box1 = box.box()
    rowb = box1.row(align=True)
    rowb.label(text= "Face", icon= 'MODIFIER')
    if button_toggle(obj,rowb,"bone_set_face"):
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=0, toggle=True, text='Main Rig') 
        b.prop(layers, 'layers', index=23, toggle=True, text='Face Panel')

    row = layout.row()
    split = row.split(factor=0.5, align=True)
    c = split.column()
    box1 = box.box()
    rowb = box1.row(align=True)
    rowb.label(text= "Arms", icon= 'MODIFIER')
    if button_toggle(obj,rowb,"bone_set_arm"):
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=1, toggle=True, text='Right Arm IK')
    
        b.prop(layers, 'layers', index=2, toggle=True, text='Left Arm IK')
    
        b = box1.row(align=True)
    
        b.prop(layers, 'layers', index=17, toggle=True, text='Right Arm FK')
    
        b.prop(layers, 'layers', index=18, toggle=True, text='Left Arm FK')
    
        b = box1.row(align=True)
    
        b.prop(layers, 'layers', index=5, toggle=True, text='Right Fingers')
    
        b.prop(layers, 'layers', index=21, toggle=True, text='Left Fingers')

    box1 = box.box()
    rowb = box1.row(align=True)
    rowb.label(text= "Legs", icon= 'MODIFIER')
    if button_toggle(obj,rowb,"bone_set_leg"):
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=3, toggle=True, text='Right Leg IK')
        b.prop(layers, 'layers', index=4, toggle=True, text='Left Leg IK')
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=19, toggle=True, text='Right Leg FK')
        b.prop(layers, 'layers', index=20, toggle=True, text='Left Leg FK')

    box1 = box.box()
    rowb = box1.row(align=True)
    rowb.label(text= "Tweak Bones", icon= 'MODIFIER')
    if button_toggle(obj,rowb,"bone_set_tweak"):
        b = box1.row(align=True)

        b.prop(layers, 'layers', index=7, toggle=True, text='Body Tweak')
        b.prop(layers, 'layers', index=16, toggle=True, text='Face Tweak')
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=8, toggle=True, text='Right Arm Tweak')
        b.prop(layers, 'layers', index=9, toggle=True, text='Left Arm Tweak')
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=24, toggle=True, text='Right Leg Tweak')
        b.prop(layers, 'layers', index=25, toggle=True, text='Left Leg Tweak')

    box1 = box.box()
    rowb = box1.row(align=True)
    rowb.label(text= "Misc", icon= 'MODIFIER')
    if button_toggle(obj,rowb,"bone_set_misc"):
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=10, toggle=True, text='Limb Twist')
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=6, toggle=True, text='Dynamic Hair')
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=22, toggle=True, text='Extras')
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=26, toggle=True, text='Footroll')
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=15, toggle=True, text='Emotion Bones')
        b = box1.row(align=True)
        b.prop(layers, 'layers', index=27, toggle=True, text='Cartoon Mouth')

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