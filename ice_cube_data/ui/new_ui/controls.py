#Libraries
import bpy

from ice_cube_data.utils.ui_tools import button_toggle

def newEnum(layout,display,source,prop,expand):
    if display != "":
        layout.label(text=display)
    layout.prop(data=source,property=prop,expand=expand)

def newBoneLayer(context,layout,index,text):
    layers = context.active_object.data
    layout.prop(layers, 'layers', index=index, toggle=True, text=text)

def controls_ui(self,context,layout,obj,scale):
    box = layout.box()
    box.label(text= "Control/Workflow Settings", icon= 'NETWORK_DRIVE')
    b = box.row(align=True)
    b.scale_y=scale
    workflow_box_0 = b.box()
    workflow_box_0_row = workflow_box_0.row(align=True)
    workflow_box_0_row.label(text="Workflow Settings",icon='EMPTY_ARROWS')
    if button_toggle(obj,workflow_box_0_row,"workflow_settings"):
        workflow_box_0_row = workflow_box_0.row(align=True)
        workflow_box_1 = workflow_box_0_row.box()
        workflow_box_1.scale_y = 1.1
        workflow_box_1_row = workflow_box_1.row(align=True)
        workflow_box_1_row.prop(obj,"antilag",text="Anti-Lag")
        workflow_box_1_row.prop(obj,"wireframe",text="Wireframe")
        workflow_box_1_row = workflow_box_1.row(align=True)
        workflow_box_1_row.prop(obj,"global_head_rotation",text="Global Head")
        workflow_box_1_row.prop(obj,"eyetracker",text="Eye Tracker")
        workflow_box_1_row = workflow_box_1.row(align=True)
        workflow_box_1_row.prop(obj,"enable_control_linking",text="Control Linking")
        workflow_box_0_row = workflow_box_0.row(align=True)
        workflow_box_0_row.scale_y=scale
        workflow_box_2 = workflow_box_0.box()
        workflow_box_2.scale_y = 1.1
        workflow_box_2_row = workflow_box_2.row(align=True)
        workflow_box_2_row.prop(obj,"toggle_1",text="Toggle 1")
        workflow_box_2_row.prop(obj,"toggle_2",text="Toggle 2")
        workflow_box_2_row = workflow_box_2.row(align=True)
        workflow_box_2_row.prop(obj,"toggle_3",text="Toggle 3")
        workflow_box_2_row.prop(obj,"toggle_4",text="Toggle 4")
    b = box.row(align=True)
    b.scale_y=scale
    ik_box = b.box()
    ik_row = ik_box.row(align=True)
    ik_row.label(text="Inverse Kinematics",icon='CON_KINEMATIC')
    if button_toggle(obj,ik_row,"ik_settings"):
        ik_row = ik_box.row(align=True)
        ik_col = ik_row.column(align=True)
        #Right
        ik_col.scale_y = 1.2
        ik_col.prop(obj,"r_arm_ik",text="Right Arm",toggle=True)
        if obj.get("r_arm_ik"):
            smaller_scale = ik_col.row(align=True)
            smaller_scale.prop(obj,"stretch_arm_r",text="Stretch",toggle=True)
            smaller_scale.prop(obj,"wrist_lock_r",text="Wrist Lock",toggle=True)
            ik_col.prop(obj,"arm_ik_parent_r",text="")
        #Left
        ik_col = ik_row.column(align=True)
        ik_col.scale_y = 1.2
        ik_col.prop(obj,"l_arm_ik",text="Left Arm",toggle=True)
        if obj.get("l_arm_ik"):
            smaller_scale = ik_col.row(align=True)
            smaller_scale.prop(obj,"stretch_arm_l",text="Stretch",toggle=True)
            smaller_scale.prop(obj,"wrist_lock_l",text="Wrist Lock",toggle=True)
            ik_col.prop(obj,"arm_ik_parent_l",text="")
        
        
        ik_row = ik_box.row(align=True)
        ik_col = ik_row.column(align=True)
        #Right
        ik_col.scale_y = 1.2
        ik_col.prop(obj,"r_leg_ik",text="Right Leg",toggle=True)
        if obj.get("r_leg_ik"):
            smaller_scale = ik_col.row(align=True)
            smaller_scale.prop(obj,"stretch_leg_r",text="Stretch",toggle=True)
            smaller_scale.prop(obj,"ankle_r",text="Ankle",toggle=True)
        #Left
        ik_col = ik_row.column(align=True)
        ik_col.scale_y = 1.2
        ik_col.prop(obj,"l_leg_ik",text="Left Leg",toggle=True)
        if obj.get("l_leg_ik"):
            smaller_scale = ik_col.row(align=True)
            smaller_scale.prop(obj,"stretch_leg_l",text="Stretch",toggle=True)
            smaller_scale.prop(obj,"ankle_l",text="Ankle",toggle=True)
        
        ik_snapping_box = ik_box.box()
        ik_snapping_row = ik_snapping_box.row(align=True)
        ik_snapping_row.label(text="IK Snapping",icon='SNAP_ON')
        if button_toggle(obj,ik_snapping_row,"gen_set_snap"):
            ik_snapping_row = ik_snapping_box.row(align=True)
            ik_snapping_row.label(text="Right Arm",icon='EMPTY_SINGLE_ARROW')
            ik_snapping_row.label(text="Left Arm",icon='EMPTY_SINGLE_ARROW')
            ik_snapping_row = ik_snapping_box.row(align=True)
            ik_snapping_col = ik_snapping_row.column(align=True)
            ik_snapping_col.scale_y = 1
            ik_snapping_col.operator("fk_arm_r.snapping",text="IK > FK ")
            ik_snapping_col.operator("ik_arm_r.snapping",text="FK > IK")
            ik_snapping_col = ik_snapping_row.column(align=True) 
            ik_snapping_col.operator("fk_arm_l.snapping",text="IK > FK ")
            ik_snapping_col.operator("ik_arm_l.snapping",text="FK > IK")
            ik_snapping_row = ik_snapping_box.row(align=True)
            ik_snapping_row.label(text="Right Leg",icon='EMPTY_SINGLE_ARROW')
            ik_snapping_row.label(text="Left Leg",icon='EMPTY_SINGLE_ARROW')
            ik_snapping_row = ik_snapping_box.row(align=True)
            ik_snapping_col = ik_snapping_row.column(align=True)
            ik_snapping_col.scale_y = 1
            ik_snapping_col.operator("fk_leg_r.snapping",text="IK > FK ")
            ik_snapping_col.operator("ik_leg_r.snapping",text="FK > IK")
            ik_snapping_col = ik_snapping_row.column(align=True)
            ik_snapping_col.operator("fk_leg_l.snapping",text="IK > FK ")
            ik_snapping_col.operator("ik_leg_l.snapping",text="FK > IK")
    b = box.row(align=True)
    b.scale_y=scale
    if obj.get("facerig"):
        influence_box = b.box()
        influence_row = influence_box.row(align=True)
        influence_row.label(text="Influence Settings",icon='STICKY_UVS_DISABLE')
        if button_toggle(obj,influence_row,"influence_settings"):
            influence_row = influence_box.row(align=True)
            influence_col = influence_row.column(align=True)
            influence_col_row = influence_col.row(align=True)
            influence_col_row.prop(obj,"eye_influence",text="Eye",slider=True)
            influence_col_row.prop(obj,"eyebrow_influence",text="Eyebrow",slider=True)
            influence_col.prop(obj,"mouth_influence",text="Mouth",slider=True)
        b = box.row(align=True)
        b.scale_y=scale
    bonelayer_box = b.box()
    bonelayer_box.scale_y=1.1
    bonelayer_row = bonelayer_box.row(align=True)
    bonelayer_row.label(text="Bone Visibility",icon='CONSTRAINT_BONE')
    if button_toggle(obj,bonelayer_row,"bonelayer_settings"):
        bonelayer_row = bonelayer_box.row(align=True)
        face_box = bonelayer_row.box()
        face_row = face_box.row(align=True)
        face_row.label(text="Face",icon='GROUP_BONE')
        if button_toggle(obj,face_row,"bone_set_face"):
            face_row = face_box.row(align=True)
            newBoneLayer(context,face_row,0,'Main Rig')
            newBoneLayer(context,face_row,23,'Face Panel')
        
        bonelayer_row = bonelayer_box.row(align=True)
        arm_box = bonelayer_row.box()
        arm_row = arm_box.row(align=True)
        arm_row.label(text="Arms",icon='GROUP_BONE')
        if button_toggle(obj,arm_row,"bone_set_arm"):
            arm_row = arm_box.row(align=True)
            #right
            arm_col = arm_row.column(align=True)
            newBoneLayer(context,arm_col,1,'Right Arm IK')
            newBoneLayer(context,arm_col,17,'Right Arm FK')
            newBoneLayer(context,arm_col,5,'Right Fingers')
            #left
            arm_col = arm_row.column(align=True)
            newBoneLayer(context,arm_col,2,'Left Arm IK')
            newBoneLayer(context,arm_col,18,'Left Arm FK')
            newBoneLayer(context,arm_col,21,'Left Fingers')
        
        bonelayer_row = bonelayer_box.row(align=True)
        leg_box = bonelayer_row.box()
        leg_row = leg_box.row(align=True)
        leg_row.label(text="Legs",icon='GROUP_BONE')
        if button_toggle(obj,leg_row,"bone_set_leg"):
            leg_row = leg_box.row(align=True)
            #right
            leg_col = leg_row.column(align=True)
            newBoneLayer(context,leg_col,3,'Right Leg IK')
            newBoneLayer(context,leg_col,19,'Right Leg FK')
            #left
            leg_col = leg_row.column(align=True)
            newBoneLayer(context,leg_col,4,'Left Leg IK')
            newBoneLayer(context,leg_col,20,'Left Leg FK')
        
        bonelayer_row = bonelayer_box.row(align=True)
        tweak_box = bonelayer_row.box()
        tweak_row = tweak_box.row(align=True)
        tweak_row.label(text="Tweaks",icon='GROUP_BONE')
        if button_toggle(obj,tweak_row,"bone_set_tweak"):
            tweak_row = tweak_box.row(align=True)
            tweak_col = tweak_row.column(align=True)
            newBoneLayer(context,tweak_col,7,'Body Tweak')
            newBoneLayer(context,tweak_col,8,'Right Arm Tweak')
            newBoneLayer(context,tweak_col,24,'Right Leg Tweak')
            tweak_col = tweak_row.column(align=True)
            newBoneLayer(context,tweak_col,16,'Face Tweak')
            newBoneLayer(context,tweak_col,9,'Left Arm Tweak')
            newBoneLayer(context,tweak_col,25,'Left Leg Tweak')
        
        bonelayer_row = bonelayer_box.row(align=True)
        misc_box = bonelayer_row.box()
        misc_row = misc_box.row(align=True)
        misc_row.label(text="Misc",icon='GROUP_BONE')
        if button_toggle(obj,misc_row,"bone_set_misc"):
            misc_row = misc_box.row(align=True)
            misc_col = misc_row.column(align=True)

            newBoneLayer(context,misc_col,10,'Limb Twist')
            newBoneLayer(context,misc_col,6,'Dynamic Hair')
            misc_col = misc_row.column(align=True)
            newBoneLayer(context,misc_col,22,'Extras')
            newBoneLayer(context,misc_col,26,'Footroll')
            misc_col = misc_row.column(align=True)
            newBoneLayer(context,misc_col,15,'Emotion Bones')
            newBoneLayer(context,misc_col,27,'Cartoon Mouth')




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