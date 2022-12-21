#Libraries
import bpy

def general_settings_main_UI(self, context, layout, obj, icon):
    box = layout.box()
    pcoll = icon["main"]
    box.label(text= "General Settings", icon= 'TOOL_SETTINGS')
    
    box1 = box.box()
    box1.label(text= "Misc", icon= 'FILE_CACHE')
    b = box1.row(align=True)
    b.prop(obj, "bendstyle", expand=True, text = "Sharp Bends")
    b = box1.row(align=True)
    b.prop(obj, "mouthtypes", expand=True)
    b = box1.row(align=True)
    b.prop(obj, "facerig", toggle=True, text = "Face Rig")
    b = box1.row(align=True)
    b.prop(obj, "antilag", text = "Anti Lag")
    b.prop(obj, "wireframe", text = "Wireframe")
    b = box1.row(align=True)
    b.prop(obj, "mouthrotate", text = "Mouth Rotate")
    b.prop(obj, "global_head_rotation", text = "Global Head Rot")
    b = box1.row(align=True)
    preset = box1.box()
    b = preset.row(align=True)
    b.prop(obj, "toggle_1", text = "Toggle 1")
    b.prop(obj, "toggle_2", text = "Toggle 2")
    b = preset.row(align=True)
    b.prop(obj, "toggle_3", text = "Toggle 3")
    b.prop(obj, "toggle_4", text = "Toggle 4")
    
    box1 = box.box()
    my_icon = pcoll["Steve"]
    if obj.get("armtype_enum") == 0:
        box1.label(text= "Arms", icon_value=my_icon.icon_id)
    my_icon = pcoll["Alex"]
    if obj.get("armtype_enum") == 1:
        box1.label(text= "Arms", icon_value=my_icon.icon_id)
    my_icon = pcoll["DarthLilo"]
    if obj.get("armtype_enum") == 2:
        box1.label(text= "Arms", icon_value=my_icon.icon_id)
    b = box1.row(align=True)
    b.prop(obj, "armtype_enum", expand=True)
    b = box1.row(align=True)
    b.prop(obj, "r_arm_ik", toggle=True, text = "Right Arm IK")
    b.prop(obj, "l_arm_ik", toggle=True, text = "Left Arm IK")
    b = box1.row(align=True)
    if obj.get("r_arm_ik") == 1:
        stretchR = b.row(align=True)
        stretchR.prop(obj, "stretch_arm_r", toggle=True, text = "Arm Stretch R")
    else:
        stretchR = b.row(align=True)
        stretchR.prop(obj, "stretch_arm_r", toggle=True, text = "Arm Stretch R")
        stretchR.enabled = False
    

    if obj.get("l_arm_ik") == 1:
        stretchL = b.row(align=True)
        stretchL.prop(obj, "stretch_arm_l", toggle=True, text = "Arm Stretch L")
    else:
        stretchL = b.row(align=True)
        stretchL.prop(obj, "stretch_arm_l", toggle=True, text = "Arm Stretch L")
        stretchL.enabled = False
    
    b = box1.row(align=True)
    b.prop(obj, "fingers_r", toggle=True, text = "Fingers R")
    
    b.prop(obj, "fingers_l", toggle=True, text = "Fingers L")
    b = box1.row(align=True)
    b.prop(obj, "thumbfill_R", text = "Thumbfill R",toggle=True)
    b.prop(obj, "thumbfill_L", text = "Thumbfill L",toggle=True)
    b = box1.row(align=True)
    b.prop(obj, "wrist_lock_r", toggle=True, text = "Wrist Lock R")
    b.prop(obj, "wrist_lock_l", toggle=True, text = "Wrist Lock L")
    b = box1.row(align=True)
    b.prop(obj, "arm_ik_parent_r", text = "")
    b.prop(obj, "arm_ik_parent_l", text = "")
    
    box1 = box.box()
    box1.label(text= "Legs", icon= 'FILE_CACHE')
    b = box1.row(align=True)
    b.prop(obj, "r_leg_ik", toggle=True, text = "Right Leg IK")
    b.prop(obj, "l_leg_ik", toggle=True, text = "Left Leg IK")
    b = box1.row(align=True)
    b.prop(obj, "ankle_r", toggle=True, text = "Ankle R")
    b.prop(obj, "ankle_l", toggle=True, text = "Ankle L")
    b = box1.row(align=True)
    if obj.get("r_leg_ik") == 1:
        stretchRL = b.row(align=True)
        stretchRL.prop(obj, "stretch_leg_r", toggle=True, text = "Leg Stretch R")
    else:
        stretchRL = b.row(align=True)
        stretchRL.prop(obj, "stretch_leg_r", toggle=True, text = "Leg Stretch R")
        stretchRL.enabled=False
    if obj.get("l_leg_ik") == 1:
        stretchLL = b.row(align=True)
        stretchLL.prop(obj, "stretch_leg_l", toggle=True, text = "Leg Stretch L")
    else:
        stretchLL = b.row(align=True)
        stretchLL.prop(obj, "stretch_leg_l", toggle=True, text = "Leg Stretch L")
        stretchLL.enabled=False

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