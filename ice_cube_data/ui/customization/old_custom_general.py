#Libraries
import bpy

def customization_general_UI(self, context, layout, obj):
    box = layout.box()
    box.label(text= "General", icon= 'SETTINGS')
    b = box.row(align=True)
    if obj.get("eyelashes") == 0:
        b.prop(obj, "eyelashes", icon = "LAYER_USED", text = "Eyelashes")
    else:
        b.prop(obj, "eyelashes", icon = "LAYER_ACTIVE", text = "Eyelashes")
    b = box.row(align=True)
    if obj.get("jaw") == 0:
        b.prop(obj, "jaw", icon = "RIGHTARROW", text = "Jaw")
    else:
        b.prop(obj, "jaw", icon = "DOWNARROW_HLT", text = "Jaw Settings")
        if obj.get("round_jaw") == 0:
            b.prop(obj, "round_jaw", icon = "LAYER_USED", text = "Flat")
        else:
            b.prop(obj, "round_jaw", icon = "LAYER_ACTIVE", text = "Round")
        b = box.row(align=True)
        b.prop(obj, "jaw_strength", text = "Strength", slider = True)
    b = box.row(align=True)
    if obj.get("bevelmouth") == 0:
        b.prop(obj, "bevelmouth", icon = "RIGHTARROW", text = "Bevels")
    else:
        b.prop(obj, "bevelmouth", icon = "DOWNARROW_HLT", text = "Bevels")
        b = box.row(align=True)
        b.prop(obj, "bevelmouthstrength", text = "Mouth Strength", slider = True)
    b = box.row(align=True)
    if obj.get("teeth_cartoon") == 0:
        b.prop(obj, "teeth_cartoon", icon = "LAYER_USED", text = "Teeth Cartoon")
    else:
        b.prop(obj, "teeth_cartoon", icon = "LAYER_ACTIVE", text = "Teeth Cartoon")

    if obj.get("teeth_bool") == 0:
        b.prop(obj, "teeth_bool", icon = "LAYER_USED", text = "Teeth Bool")
    else:
        b.prop(obj, "teeth_bool", icon = "LAYER_ACTIVE", text = "Teeth Bool")
    b = box.row(align=True)

    if obj.get("teeth_curve") == 0:
        b.prop(obj, "teeth_curve", icon = "LAYER_USED", text = "Teeth Curve", slider = True)
    else:
        b.prop(obj, "teeth_curve", icon = "LAYER_ACTIVE", text = "Teeth Curve", slider = True)

    b = box.row(align=True)
    if obj.get("tongue") == 0:
        b.prop(obj, "tongue", icon = "LAYER_USED", text = "Tongue")
    else:
        b.prop(obj, "tongue", icon = "LAYER_ACTIVE", text = "Tongue")
    if obj.get("dynamichair") == 0:
        b.prop(obj, "dynamichair", icon = "LAYER_USED", text = "Dynamic Hair")
    else:
        b.prop(obj, "dynamichair", icon = "LAYER_ACTIVE", text = "Dynamic Hair")
    
    b = box.row(align=True)
    b.prop(obj,"eye_influence",text="Eye Influence",slider=True)
    b.prop(obj,"eyebrow_influence",text="Eyebrow Influence",slider=True)
    b = box.row(align=True)
    b.prop(obj,"mouth_influence",text="Mouth Influence",slider=True)

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