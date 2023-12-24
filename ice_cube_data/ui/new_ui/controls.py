#Libraries
import bpy

from ice_cube_data.utils.ui_tools import button_toggle
from ice_cube_data.utils.general_func import selectBoneCollection, getLanguageTranslation

def newEnum(layout,display,source,prop,expand):
    if display != "":
        layout.label(text=display)
    layout.prop(data=source,property=prop,expand=expand)






def newBoneLayer(context,layout,index,text,prop_tag,cur_blender_version):
    if cur_blender_version >= 400:
        collections = context.active_object.data.collections
        target_collection = selectBoneCollection(collections,prop_tag)
        if target_collection != None:
            layout.prop(target_collection,'is_visible',toggle=True,text=getLanguageTranslation(text))
    else:
        layers = context.active_object.data
        layout.prop(layers, 'layers', index=index, toggle=True, text=getLanguageTranslation(text))

def controls_ui(self,context,layout,obj,scale,cur_blender_version):
    box = layout.box()
    box.label(text= getLanguageTranslation("ice_cube.ui.tabs.control_settings"), icon= 'NETWORK_DRIVE')
    b = box.row(align=True)
    b.scale_y=scale
    workflow_box_0 = b.box()
    workflow_box_0_row = workflow_box_0.row(align=True)
    workflow_box_0_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.workflow_settings"),icon='EMPTY_ARROWS')
    if button_toggle(obj,workflow_box_0_row,"workflow_settings"):
        workflow_box_0_row = workflow_box_0.row(align=True)
        workflow_box_1 = workflow_box_0_row.box()
        workflow_box_1.scale_y = 1.1
        workflow_box_1_row = workflow_box_1.row(align=True)
        workflow_box_1_row.prop(obj,"antilag",text=getLanguageTranslation("ice_cube.ui.props.antilag"))
        workflow_box_1_row.prop(obj,"wireframe",text=getLanguageTranslation("ice_cube.ui.props.wireframe"))
        workflow_box_1_row = workflow_box_1.row(align=True)
        workflow_box_1_row.prop(obj,"global_head_rotation",text=getLanguageTranslation("ice_cube.ui.props.global_head_rotation"))
        workflow_box_1_row.prop(obj,"eyetracker",text=getLanguageTranslation("ice_cube.ui.props.eyetracker"))
        workflow_box_1_row = workflow_box_1.row(align=True)
        workflow_box_1_row.prop(obj,"enable_control_linking",text=getLanguageTranslation("ice_cube.ui.props.control_linking"))

        workflow_box_0_row = workflow_box_0.row(align=True)
        workflow_box_0_row.scale_y=scale
        workflow_box_3 = workflow_box_0.box()
        workflow_box_3.scale_y = 1.1
        workflow_box_3_row = workflow_box_3.row(align=True)
        workflow_box_3_row.operator("ice_cube.updaterestpose",text=getLanguageTranslation("ice_cube.ops.update_rest_pose"))
        workflow_box_3_row.operator("ice_cube.resetrestpose",text=getLanguageTranslation("ice_cube.ops.reset_rest_pose"))


        workflow_box_0_row = workflow_box_0.row(align=True)
        workflow_box_0_row.scale_y=scale
        workflow_box_2 = workflow_box_0.box()
        workflow_box_2.scale_y = 1.1
        workflow_box_2_row = workflow_box_2.row(align=True)
        workflow_box_2_row.prop(obj,"toggle_1",text=getLanguageTranslation("ice_cube.ui.props.toggle_1"))
        workflow_box_2_row.prop(obj,"toggle_2",text=getLanguageTranslation("ice_cube.ui.props.toggle_2"))
        workflow_box_2_row = workflow_box_2.row(align=True)
        workflow_box_2_row.prop(obj,"toggle_3",text=getLanguageTranslation("ice_cube.ui.props.toggle_3"))
        workflow_box_2_row.prop(obj,"toggle_4",text=getLanguageTranslation("ice_cube.ui.props.toggle_4"))
    b = box.row(align=True)
    b.scale_y=scale
    ik_box = b.box()
    ik_row = ik_box.row(align=True)
    ik_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.ik"),icon='CON_KINEMATIC')
    if button_toggle(obj,ik_row,"ik_settings"):
        ik_row = ik_box.row(align=True)
        ik_col = ik_row.column(align=True)
        #Right
        ik_col.scale_y = 1.2
        ik_col.prop(obj,"r_arm_ik",text=getLanguageTranslation("ice_cube.ui.props.right_arm_ik"),toggle=True)
        if obj.get("r_arm_ik"):
            smaller_scale = ik_col.row(align=True)
            smaller_scale.prop(obj,"stretch_arm_r",text=getLanguageTranslation("ice_cube.ui.props.right_arm_stretch"),toggle=True)
            smaller_scale.prop(obj,"wrist_lock_r",text=getLanguageTranslation("ice_cube.ui.props.right_arm_wrist"),toggle=True)
            ik_col.prop(obj,"arm_ik_parent_r",text="")
        #Left
        ik_col = ik_row.column(align=True)
        ik_col.scale_y = 1.2
        ik_col.prop(obj,"l_arm_ik",text=getLanguageTranslation("ice_cube.ui.props.left_arm_ik"),toggle=True)
        if obj.get("l_arm_ik"):
            smaller_scale = ik_col.row(align=True)
            smaller_scale.prop(obj,"stretch_arm_l",text=getLanguageTranslation("ice_cube.ui.props.left_arm_stretch"),toggle=True)
            smaller_scale.prop(obj,"wrist_lock_l",text=getLanguageTranslation("ice_cube.ui.props.left_arm_wrist"),toggle=True)
            ik_col.prop(obj,"arm_ik_parent_l",text="")
        
        
        ik_row = ik_box.row(align=True)
        ik_col = ik_row.column(align=True)
        #Right
        ik_col.scale_y = 1.2
        ik_col.prop(obj,"r_leg_ik",text=getLanguageTranslation("ice_cube.ui.props.right_leg_ik"),toggle=True)
        if obj.get("r_leg_ik"):
            smaller_scale = ik_col.row(align=True)
            smaller_scale.prop(obj,"stretch_leg_r",text=getLanguageTranslation("ice_cube.ui.props.right_leg_stretch"),toggle=True)
            smaller_scale.prop(obj,"ankle_r",text=getLanguageTranslation("ice_cube.ui.props.right_leg_ankle"),toggle=True)
        #Left
        ik_col = ik_row.column(align=True)
        ik_col.scale_y = 1.2
        ik_col.prop(obj,"l_leg_ik",text=getLanguageTranslation("ice_cube.ui.props.left_leg_ik"),toggle=True)
        if obj.get("l_leg_ik"):
            smaller_scale = ik_col.row(align=True)
            smaller_scale.prop(obj,"stretch_leg_l",text=getLanguageTranslation("ice_cube.ui.props.left_leg_stretch"),toggle=True)
            smaller_scale.prop(obj,"ankle_l",text=getLanguageTranslation("ice_cube.ui.props.left_leg_ankle"),toggle=True)
        
        ik_snapping_box = ik_box.box()
        ik_snapping_row = ik_snapping_box.row(align=True)
        ik_snapping_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.ik_snapping"),icon='SNAP_ON')
        if button_toggle(obj,ik_snapping_row,"gen_set_snap"):
            ik_snapping_row = ik_snapping_box.row(align=True)
            ik_snapping_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.right_arm_snap"),icon='EMPTY_SINGLE_ARROW')
            ik_snapping_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.left_arm_snap"),icon='EMPTY_SINGLE_ARROW')
            ik_snapping_row = ik_snapping_box.row(align=True)
            ik_snapping_col = ik_snapping_row.column(align=True)
            ik_snapping_col.scale_y = 1
            ik_snapping_col.operator("fk_arm_r.snapping",text="IK > FK")
            ik_snapping_col.operator("ik_arm_r.snapping",text="FK > IK")
            ik_snapping_col = ik_snapping_row.column(align=True) 
            ik_snapping_col.operator("fk_arm_l.snapping",text="IK > FK")
            ik_snapping_col.operator("ik_arm_l.snapping",text="FK > IK")
            ik_snapping_row = ik_snapping_box.row(align=True)
            ik_snapping_row.label(text=getLanguageTranslation("ice_cube.ui.props.right_leg_snap"),icon='EMPTY_SINGLE_ARROW')
            ik_snapping_row.label(text=getLanguageTranslation("ice_cube.ui.props.left_leg_snap"),icon='EMPTY_SINGLE_ARROW')
            ik_snapping_row = ik_snapping_box.row(align=True)
            ik_snapping_col = ik_snapping_row.column(align=True)
            ik_snapping_col.scale_y = 1
            ik_snapping_col.operator("fk_leg_r.snapping",text="IK > FK")
            ik_snapping_col.operator("ik_leg_r.snapping",text="FK > IK")
            ik_snapping_col = ik_snapping_row.column(align=True)
            ik_snapping_col.operator("fk_leg_l.snapping",text="IK > FK")
            ik_snapping_col.operator("ik_leg_l.snapping",text="FK > IK")
    b = box.row(align=True)
    b.scale_y=scale
    if obj.get("facerig"):
        influence_box = b.box()
        influence_row = influence_box.row(align=True)
        influence_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.influence"),icon='STICKY_UVS_DISABLE')
        if button_toggle(obj,influence_row,"influence_settings"):
            influence_row = influence_box.row(align=True)
            influence_col = influence_row.column(align=True)
            influence_col_row = influence_col.row(align=True)
            influence_col_row.prop(obj,"eye_influence",text=getLanguageTranslation("ice_cube.ui.props.eye_influence"),slider=True)
            influence_col_row.prop(obj,"eyebrow_influence",text=getLanguageTranslation("ice_cube.ui.props.eyebrow_influence"),slider=True)
            influence_col.prop(obj,"mouth_influence",text=getLanguageTranslation("ice_cube.ui.props.mouth_influence"),slider=True)
        b = box.row(align=True)
        b.scale_y=scale
    bonelayer_box = b.box()
    bonelayer_box.scale_y=1.1
    bonelayer_row = bonelayer_box.row(align=True)
    bonelayer_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.bone_visibility"),icon='CONSTRAINT_BONE')
    if button_toggle(obj,bonelayer_row,"bonelayer_settings"):
        bonelayer_row = bonelayer_box.row(align=True)
        face_box = bonelayer_row.box()
        face_row = face_box.row(align=True)
        face_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.face_bones"),icon='GROUP_BONE')
        if button_toggle(obj,face_row,"bone_set_face"):
            face_row = face_box.row(align=True)
            newBoneLayer(context,face_row,0,'ice_cube.ui.bone_layers.main','Main Bones',cur_blender_version)
            newBoneLayer(context,face_row,23,'ice_cube.ui.bone_layers.face_panel','Face Panel Bones',cur_blender_version)
        
        bonelayer_row = bonelayer_box.row(align=True)
        arm_box = bonelayer_row.box()
        arm_row = arm_box.row(align=True)
        arm_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.arm_bones"),icon='GROUP_BONE')
        if button_toggle(obj,arm_row,"bone_set_arm"):
            arm_row = arm_box.row(align=True)
            #right
            arm_col = arm_row.column(align=True)
            newBoneLayer(context,arm_col,1,'ice_cube.ui.bone_layers.right_arm_ik','Right Arm IK',cur_blender_version)
            newBoneLayer(context,arm_col,17,'ice_cube.ui.bone_layers.right_arm_fk','Right Arm FK',cur_blender_version)
            newBoneLayer(context,arm_col,5,'ice_cube.ui.bone_layers.right_fingers','Right Fingers',cur_blender_version)
            #left
            arm_col = arm_row.column(align=True)
            newBoneLayer(context,arm_col,2,'ice_cube.ui.bone_layers.left_arm_ik','Left Arm IK',cur_blender_version)
            newBoneLayer(context,arm_col,18,'ice_cube.ui.bone_layers.left_arm_fk','Left Arm FK',cur_blender_version)
            newBoneLayer(context,arm_col,21,'ice_cube.ui.bone_layers.left_fingers','Left Fingers',cur_blender_version)
        
        bonelayer_row = bonelayer_box.row(align=True)
        leg_box = bonelayer_row.box()
        leg_row = leg_box.row(align=True)
        leg_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.leg_bones"),icon='GROUP_BONE')
        if button_toggle(obj,leg_row,"bone_set_leg"):
            leg_row = leg_box.row(align=True)
            #right
            leg_col = leg_row.column(align=True)
            newBoneLayer(context,leg_col,3,'ice_cube.ui.bone_layers.right_leg_ik','Right Leg IK',cur_blender_version)
            newBoneLayer(context,leg_col,19,'ice_cube.ui.bone_layers.right_leg_fk','Right Leg FK',cur_blender_version)
            #left
            leg_col = leg_row.column(align=True)
            newBoneLayer(context,leg_col,4,'ice_cube.ui.bone_layers.left_leg_ik','Left Leg IK',cur_blender_version)
            newBoneLayer(context,leg_col,20,'ice_cube.ui.bone_layers.left_leg_fk','Left Leg FK',cur_blender_version)
        
        bonelayer_row = bonelayer_box.row(align=True)
        tweak_box = bonelayer_row.box()
        tweak_row = tweak_box.row(align=True)
        tweak_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.tweak_bones"),icon='GROUP_BONE')
        if button_toggle(obj,tweak_row,"bone_set_tweak"):
            tweak_row = tweak_box.row(align=True)
            tweak_col = tweak_row.column(align=True)
            newBoneLayer(context,tweak_col,7,'ice_cube.ui.bone_layers.body_tweak','Body Tweak',cur_blender_version)
            newBoneLayer(context,tweak_col,8,'ice_cube.ui.bone_layers.right_arm_tweak','Right Arm Tweak',cur_blender_version)
            newBoneLayer(context,tweak_col,24,'ice_cube.ui.bone_layers.right_leg_tweak','Right Leg Tweak',cur_blender_version)
            tweak_col = tweak_row.column(align=True)
            newBoneLayer(context,tweak_col,16,'ice_cube.ui.bone_layers.face_tweak','Face Tweak',cur_blender_version)
            newBoneLayer(context,tweak_col,9,'ice_cube.ui.bone_layers.left_arm_tweak','Left Arm Tweak',cur_blender_version)
            newBoneLayer(context,tweak_col,25,'ice_cube.ui.bone_layers.left_leg_tweak','Left Leg Tweak',cur_blender_version)
        
        bonelayer_row = bonelayer_box.row(align=True)
        misc_box = bonelayer_row.box()
        misc_row = misc_box.row(align=True)
        misc_row.label(text=getLanguageTranslation("ice_cube.ui.tabs.misc_bones"),icon='GROUP_BONE')
        if button_toggle(obj,misc_row,"bone_set_misc"):
            misc_row = misc_box.row(align=True)
            misc_col = misc_row.column(align=True)

            newBoneLayer(context,misc_col,10,'ice_cube.ui.bone_layers.twist','Twist',cur_blender_version)
            newBoneLayer(context,misc_col,6,'ice_cube.ui.bone_layers.dynamic_hair','Dynamic Hair',cur_blender_version)
            misc_col = misc_row.column(align=True)
            newBoneLayer(context,misc_col,22,'ice_cube.ui.bone_layers.extras','Extra',cur_blender_version)
            newBoneLayer(context,misc_col,26,'ice_cube.ui.bone_layers.footroll','Footroll',cur_blender_version)
            misc_col = misc_row.column(align=True)
            newBoneLayer(context,misc_col,15,'ice_cube.ui.bone_layers.emotion_bones','Emotion Bones',cur_blender_version)
            newBoneLayer(context,misc_col,27,'ice_cube.ui.bone_layers.cartoon_mouth','Cartoon Mouth',cur_blender_version)




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