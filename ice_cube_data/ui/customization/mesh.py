#Libraries
import bpy

def custom_mesh_UI(self, context, layout, obj):
    box = layout.box()
    box.label(text= "Deforms", icon= 'OUTLINER_OB_MESH')
    box1 = box.box()
    box1.label(text= "Bulge", icon= 'MESH_ICOSPHERE')
    b = box1.row(align=True)
    if obj.get("bodybulge") == 0:
        b.prop(obj, "bodybulge", icon = "LAYER_USED", text = "Body Bulge")
    else:
        b.prop(obj, "bodybulge", icon = "LAYER_ACTIVE", text = "Body Bulge")
    b = box1.row(align=True)
    if obj.get("bulge_arm_r") == 0:
        b.prop(obj, "bulge_arm_r", icon = "LAYER_USED", text = "Right Arm Bulge")
    else:
        b.prop(obj, "bulge_arm_r", icon = "LAYER_ACTIVE", text = "Right Arm Bulge")
    if obj.get("bulge_arm_l") == 0:
        b.prop(obj, "bulge_arm_l", icon = "LAYER_USED", text = "Left Arm Bulge")
    else:
        b.prop(obj, "bulge_arm_l", icon = "LAYER_ACTIVE", text = "Left Arm Bulge")
    b = box1.row(align=True)
    if obj.get("bulge_leg_r") == 0:
        b.prop(obj, "bulge_leg_r", icon = "LAYER_USED", text = "Right Leg Bulge")
    else:
        b.prop(obj, "bulge_leg_r", icon = "LAYER_ACTIVE", text = "Right Leg Bulge")
    if obj.get("bulge_arm_l") == 0:
        b.prop(obj, "bulge_leg_l", icon = "LAYER_USED", text = "Left Leg Bulge")
    else:
        b.prop(obj, "bulge_leg_l", icon = "LAYER_ACTIVE", text = "Left Leg Bulge")
        
    box1 = box.box()
    box1.label(text= "Squish", icon= 'OUTLINER_OB_LATTICE')
    b = box1.row(align=True)
    if obj.get("squish_body") == 0:
        b.prop(obj, "squish_body", icon = "LAYER_USED", text = "Body Squish")
    else:
        b.prop(obj, "squish_body", icon = "LAYER_ACTIVE", text = "Body Squish")
    if obj.get("squish_head") == 0:
        b.prop(obj, "squish_head", icon = "LAYER_USED", text = "Head Squish")
    else:
        b.prop(obj, "squish_head", icon = "LAYER_ACTIVE", text = "Head Squish")
    b = box1.row(align=True)
    if obj.get("squish_arm_r") == 0:
        b.prop(obj, "squish_arm_r", icon = "LAYER_USED", text = "Right Arm Squish")
    else:
        b.prop(obj, "squish_arm_r", icon = "LAYER_ACTIVE", text = "Right Arm Squish")
    if obj.get("squish_arm_l") == 0:
        b.prop(obj, "squish_arm_l", icon = "LAYER_USED", text = "Left Arm Squish")
    else:
        b.prop(obj, "squish_arm_l", icon = "LAYER_ACTIVE", text = "Left Arm Squish")
    b = box1.row(align=True)
    if obj.get("squish_leg_r") == 0:
        b.prop(obj, "squish_leg_r", icon = "LAYER_USED", text = "Right Leg Squish")
    else:
        b.prop(obj, "squish_leg_r", icon = "LAYER_ACTIVE", text = "Right Leg Squish")
    if obj.get("squish_arm_l") == 0:
        b.prop(obj, "squish_leg_l", icon = "LAYER_USED", text = "Left Leg Squish")
    else:
        b.prop(obj, "squish_leg_l", icon = "LAYER_ACTIVE", text = "Left Leg Squish")
        
    box1 = box.box()
    box1.label(text= "Taper", icon= 'EDITMODE_HLT')
    b = box1.row(align=True)
    if obj.get("leg_deform") == 0:
        b.prop(obj, "leg_deform", icon = "RIGHTARROW", text = "Limb Deforms")
    else:
        b.prop(obj, "leg_deform", icon = "DOWNARROW_HLT", text = "Limb Deforms")
        b = box1.row(align=True)
        b.prop(obj, "armtaper", icon = "LAYER_USED", text = "Arm Taper Strength")
        b = box1.row(align=True)
        b.prop(obj, "leg_taper_strength", icon = "LAYER_USED", text = "Leg Taper Strength Lower")
        b = box1.row(align=True)
        b.prop(obj, "leg_taper_strength2", icon = "LAYER_USED", text = "Leg Taper Strength Upper")
    b = box1.row(align=True)
    if obj.get("body_deforms") == 0:
        b.prop(obj, "body_deforms", icon = "RIGHTARROW", text = "Body Deforms")
    else:
        b.prop(obj, "body_deforms", icon = "DOWNARROW_HLT", text = "Body Deforms")
        b = box1.row(align=True)
        if obj.get("breastswitch") == 0:
            b.prop(obj, "breastswitch", icon = "RIGHTARROW", text = "Chest")
        else:
            b.prop(obj, "breastswitch", icon = "DOWNARROW_HLT", text = "Chest")
            b = box1.row(align=True)
            b.prop(obj, "breastsize", text = "Size")
            b.prop(obj, "breastweight", text = "Weight")
            b = box1.row(align=True)
            b.prop(obj, "breastshape", text = "Shape")

        b = box1.row(align=True)
        if obj.get("hip") == 0:
            b.prop(obj, "hip", icon = "RIGHTARROW", text = "Hip")
        else:
            b.prop(obj, "hip", icon = "DOWNARROW_HLT", text = "Hip")
        b = box1.row(align=True)
        b.prop(obj, "upperbodywidth", icon = "DOWNARROW_HLT", text = "Upper Body Width")
        b = box1.row(align=True)
        if obj.get("lowerbodywidth") == 0:
            b.prop(obj, "lowerbodywidth", icon = "RIGHTARROW", text = "Normal")
        else:
            if obj.get("lowerbodywidth") == -1:
                b.prop(obj, "lowerbodywidth", icon = "RIGHTARROW", text = "Wider")
            else:
                b.prop(obj, "lowerbodywidth", icon = "DOWNARROW_HLT", text = "Thinner")
        b.prop(obj, "bodytopround", icon = "RIGHTARROW", text = "Rounded Body Top")
        b = box1.row(align=True)
        b.prop(obj, "breath", text = "Breath Slider",slider=True)
    b = box1.row(align=True)
    if obj.get("eyebrowdeform") == 0:
        b.prop(obj, "eyebrowdeform", icon = "RIGHTARROW", text = "Eyebrow Deforms")
    else:
        b.prop(obj, "eyebrowdeform", icon = "DOWNARROW_HLT", text = "Eyebrow Deforms")
        b = box1.row(align=True)
        if obj.get("eyebrowheight") == 0:
            b.prop(obj, "eyebrowheight", icon = "RIGHTARROW", text = "Eyebrow Height")
        else:
            b.prop(obj, "eyebrowheight", icon = "DOWNARROW_HLT", text = "Eyebrow Height")
        b = box1.row(align=True)
        if obj.get("eyebrowtaper1") == 0:
            b.prop(obj, "eyebrowtaper1", icon = "RIGHTARROW", text = "Taper 1")
        else:
            b.prop(obj, "eyebrowtaper1", icon = "DOWNARROW_HLT", text = "Taper 1")
        if obj.get("eyebrowtaper2") == 0:
            b.prop(obj, "eyebrowtaper2", icon = "RIGHTARROW", text = "Taper 2")
        else:
            b.prop(obj, "eyebrowtaper2", icon = "DOWNARROW_HLT", text = "Taper 2")
    box1 = box.box()
    box1.label(text= "Face", icon= 'CAMERA_STEREO')
    b = box1.row(align=True)
    b.prop(obj, "eyedepth", text = "Eye Depth")
    b = box1.row(align=True)
    b.prop(obj, "mouthdepth", text = "Mouth Depth")
    b.prop(obj, "innermouthdepth", text = "Inner Mouth Depth")

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