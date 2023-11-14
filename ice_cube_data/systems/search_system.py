import bpy
from bpy.props import StringProperty
import re
from ice_cube_data.utils.general_func import convertStringNumbers,selectBoneCollection




matching_props = []

cur_blender_version = convertStringNumbers(list(bpy.app.version))

bpy.types.Object.ice_cube_search_filter = StringProperty(
    name="ice_cube_search_filter",
    description="Search filter for Ice Cube",
    default="",
    options={'TEXTEDIT_UPDATE'}
    )

def ic_search_ui(self,context,scale):
    obj = context.object
    search_input = obj.ice_cube_search_filter
    layers = context.active_object.data

    material_list = {}
    materials = bpy.data.materials
    for mat in materials:
        try:
            if mat["ice_cube_material"]:
                material_list[mat["ice_cube_material"]] = mat
        except KeyError:
            pass
    
    layout = self.layout
    box = layout.box()
    b = box.row(align=True)
    b.scale_y = scale
    b.label(text="Search Results")
    b = box.row(align=True)
    b.scale_y = scale
    search_results_box = b.box()

    search_reference = {
    }

    def sep(search_name,property_name,display_name="",index=0,expand=True,toggle=True,slider=True,source=obj,prop_tag=None):
        if source == "bone_collection":
            collections = context.active_object.data.collections
            target_collection = selectBoneCollection(collections,prop_tag)
            if target_collection != None:
                search_reference[search_name] = {"display_name": display_name if display_name else search_name, "property_name": property_name, "expand": expand, "toggle": toggle, "slider": slider, "index": index, "source": target_collection, "type":"prop"}
        else:
            search_reference[search_name] = {"display_name": display_name if display_name else search_name, "property_name": property_name, "expand": expand, "toggle": toggle, "slider": slider, "index": index, "source": source, "type":"prop"}
        
    def seo(search_name,op_name,display_name=""):

        search_reference[search_name] = {"display_name": display_name if display_name else search_name,"op_name":op_name, "type":"op"}
    
    def sem(search_name,node,material_slot,input,mat_id,display_name=""):

        search_reference[search_name] = {"display_name": display_name if display_name else search_name,"node":node, "material_slot": material_slot, "input": input, "mat_id":mat_id, "type":"mat"}
    
    # Search Entries
    #rig style props
    sep("Smooth Bend Sharp Bend Type Style","bendstyle","Bend Type"),
    sep("Arm Type Style Steve Alex Thin Model","armtype_enum"),
    sep("Right Fingers","fingers_r"),
    sep("Left Fingers","fingers_l"),
    sep("Face Rig Enable Hide","facerig","Face Rig"),
    sep("Mouth Type Style Square Mouth Mine-imator Mouth Mineimator Mouth","mouthtypes","Mouth Style"),
    sep("Eyelashes Female Woman Girl","eyelashes","Eyelashes",toggle=False),
    sep("Mouth Rotate","mouthrotate",toggle=False),
    sep("Tongue Mouth","tongue","Tongue",toggle=False),
    sep("Cartoon Line Lips Mouth","line_mouth","Cartoon Mouth",toggle=False),
    sep("Dynamic Hair","dynamichair",toggle=False),
    sep("Cartoon Teeth Mouth","teeth_cartoon","Cartoon Teeth"),
    sep("Boolean Teeth Clipping Head","teeth_bool","Teeth Boolean"),
    sep("Teeth Curve Cartoon","teeth_curve","Teeth Curve"),
    sep("Teeth Follow Mouth","teeth_follow","Teeth Follow"),
    sep("Mouth Bevel Lip","bevelmouth","Mouth Bevel"),
    sep("Mouth Bevel Lip Strength","bevelmouthstrength","Mouth Bevel Strength"),
    sep("Jaw Enable Disable","jaw","Jaw Toggle"),
    sep("Jaw Round Smooth Curve","round_jaw","Round Jaw"),
    sep("Jaw Strength Length","jaw_strength","Jaw Strength"),
    sep("Eye Depth 2D","eyedepth","Eye Depth"),
    sep("Mouth Depth 2D","mouthdepth","Mouth Depth"),
    sep("Inner Mouth Depth 2D Clipping Inside","innermouthdepth","Inner Mouth Depth"),
    sep("Thumbfill Right","thumbfill_R"),
    sep("Thumbfill Left","thumbfill_L"),

    #mesh style
    sep("Body Bulge Round Deform","bodybulge","Body Bulge"),
    sep("Arm Right Bulge Round Deform","bulge_arm_r","Right Arm Bulge"),
    sep("Arm Left Bulge Round Deform","bulge_arm_l","Left Arm Bulge"),
    sep("Leg Right Bulge Round Deform","bulge_leg_r","Right Leg Bulge"),
    sep("Leg Left Bulge Round Deform","bulge_leg_l","Left Leg Bulge"),
    sep("Head Squish Deform","squish_head","Head Squish"),
    sep("Body Squish Deform","squish_body","Body Squish"),
    sep("Right Arm Squish Deform","squish_arm_r","Right Arm Squish"),
    sep("Left Arm Squish Deform","squish_arm_l","Left Arm Squish"),
    sep("Right Leg Squish Deform","squish_leg_r","Right Leg Squish"),
    sep("Left Leg Squish Deform","squish_leg_l","Left Leg Squish"),
    sep("Upper Arm Taper Deform","armtaper","Upper Arms"),
    sep("Lower Arm Taper Deform","armtaperlower","Lower Arms"),
    sep("Upper Leg Taper Deform","leg_taper_strength2","Upper Legs"),
    sep("Lower Leg Taper Female Woman Girl Deform","leg_taper_strength","Lower Legs"),
    sep("Hips Female Woman Girl Deform","hip","Hip"),
    sep("Upper Body Female Woman Girl Deform","upperbodywidth","Upper Width"),
    sep("Rounded Body Top Deform","bodytopround","Rounded Body Top"),
    sep("Lower Body Width Fat Deform","lowerbodywidth","Lower Body Width"),
    sep("Chest Size Boobs Breasts Female Woman Girl Deform","breastsize","Chest Size"),
    sep("Chest Weight Boobs Breasts Female Woman Girl Deform","breastweight","Chest Weight"),
    sep("Chest Shape Boobs Breasts Female Woman Girl Deform","breastshape","Chest Shape"),
    sep("Eyebrow Height","eyebrowheight"),
    sep("Eyebrow Length","eyebrowlength"),
    sep("Inner Taper Eyebrow","eyebrowtaper1"),
    sep("Outer Taper Eyebrow","eyebrowtaper2"),

    #controls
    sep("Anti Lag Laggy Slow Performance Stutter", "antilag", "Anti-Lag",toggle=False),
    sep("Wireframe","wireframe",toggle=False),
    sep("Global Head Rotation Animation","global_head_rotation","Global Head Rotation",toggle=False),
    sep("Eye Tracker Control","eyetracker","Eye Tracker",toggle=False),
    sep("Toggle Custom 1","toggle_1","Toggle 1",toggle=False),
    sep("Toggle Custom 2","toggle_2","Toggle 2",toggle=False),
    sep("Toggle Custom 3","toggle_3","Toggle 3",toggle=False),
    sep("Toggle Custom 4","toggle_4","Toggle 4",toggle=False),
    sep("Right Arm IK Inverse Kinematics","r_arm_ik","Right Arm IK"),
    sep("Left Arm IK Inverse Kinematics","l_arm_ik","Left Arm IK"),
    sep("Right Leg IK Inverse Kinematics","r_leg_ik","Right Leg IK"),
    sep("Left Leg IK Inverse Kinematics","l_leg_ik","Left Leg IK"),
    sep("IK Stretch Arm Right","stretch_arm_r","Right Arm Stretch"),
    sep("IK Stretch Arm Left","stretch_arm_l","Left Arm Stretch"),
    sep("IK Stretch Leg Right","stretch_leg_r","Right Leg Stretch"),
    sep("IK Stretch Leg Left","stretch_leg_l","Left Leg Stretch"),layers
    sep("Wrist Lock IK Right","wrist_lock_r","Right Wrist Lock"),
    sep("Wrist Lock IK Left","wrist_lock_l","Left Wrist Lock"),
    sep("Ankle IK Right","ankle_r","Right Ankle"),
    sep("Ankle IK Left","ankle_l","Left Ankle"),
    sep("Arm IK Parent Right","arm_ik_parent_r","IK Parent R",expand=False),
    sep("Arm IK Parent Left","arm_ik_parent_l","IK Parent L",expand=False),
    sep("Eye Influence Controls","eye_influence","Eye Influence"),
    sep("Eyebrow Influence Controls","eyebrow_influence","Eyebrow Influence"),
    sep("Mouth Influence Controls","mouth_influence","Mouth Influence"),



    #bone layers
    if cur_blender_version >= 400:
        sep("Main Rig Bone Layer","is_visible",source="bone_collection",prop_tag="Main Bones"),
        sep("Face Panel Bone Layer","is_visible",source="bone_collection",prop_tag="Face Panel Bones"),
        sep("Right Arm IK Bone Layer","is_visible",source="bone_collection",prop_tag="Right Arm IK"),
        sep("Left Arm IK Bone Layer","is_visible",source="bone_collection",prop_tag="Left Arm IK"),
        sep("Right Arm FK Bone Layer","is_visible",source="bone_collection",prop_tag="Right Arm FK"),
        sep("Left Arm FK Bone Layer","is_visible",source="bone_collection",prop_tag="Left Arm FK"),
        sep("Right Fingers Bone Layer","is_visible",source="bone_collection",prop_tag="Right Fingers"),
        sep("Left Fingers Bone Layer","is_visible",source="bone_collection",prop_tag="Left Fingers"),
        sep("Right Leg IK Bone Layer","is_visible",source="bone_collection",prop_tag="Right Leg IK"),
        sep("Left Leg IK Bone Layer","is_visible",source="bone_collection",prop_tag="Left Leg IK"),
        sep("Right Leg FK Bone Layer","is_visible",source="bone_collection",prop_tag="Right Leg FK"),
        sep("Left Leg FK Bone Layer","is_visible",source="bone_collection",prop_tag="Left Leg FK"),
        sep("Body Tweak Bone Layer","is_visible",source="bone_collection",prop_tag="Body Tweak"),
        sep("Face Tweak Bone Layer","is_visible",source="bone_collection",prop_tag="Face Tweak"),
        sep("Right Arm Tweak Bone Layer","is_visible",source="bone_collection",prop_tag="Right Arm Tweak"),
        sep("Left Arm Tweak Bone Layer","is_visible",source="bone_collection",prop_tag="Left Arm Tweak"),
        sep("Right Leg Tweak Bone Layer","is_visible",source="bone_collection",prop_tag="Right Leg Tweak"),
        sep("Left Leg Tweak Bone Layer","is_visible",source="bone_collection",prop_tag="Left Leg Tweak"),
        sep("Limb Twist Bone Layer","is_visible",source="bone_collection",prop_tag="Twist"),
        sep("Extras Bone Layer","is_visible",source="bone_collection",prop_tag="Extra"),
        sep("Emotion Bones Bone Layer","is_visible",source="bone_collection",prop_tag="Emotion Bones"),
        sep("Dynamic Hair Bone Layer","is_visible",source="bone_collection",prop_tag="Dynamic Hair"),
        sep("Footroll Bone Layer","is_visible",source="bone_collection",prop_tag="Footroll"),
        sep("Cartoon Mouth Bone Layer","is_visible",source="bone_collection",prop_tag="Cartoon Mouth"),
    else:
        sep("Main Rig Bone Layer","layers",source=layers,index=0),
        sep("Face Panel Bone Layer","layers",source=layers,index=23),
        sep("Right Arm IK Bone Layer","layers",source=layers,index=1),
        sep("Left Arm IK Bone Layer","layers",source=layers,index=2),
        sep("Right Arm FK Bone Layer","layers",source=layers,index=17),
        sep("Left Arm FK Bone Layer","layers",source=layers,index=18),
        sep("Right Fingers Bone Layer","layers",source=layers,index=5),
        sep("Left Fingers Bone Layer","layers",source=layers,index=21),
        sep("Right Leg IK Bone Layer","layers",source=layers,index=3),
        sep("Left Leg IK Bone Layer","layers",source=layers,index=4),
        sep("Right Leg FK Bone Layer","layers",source=layers,index=19),
        sep("Left Leg FK Bone Layer","layers",source=layers,index=20),
        sep("Left Leg FK Bone Layer","layers",source=layers,index=20),
        sep("Body Tweak","layers",source=layers,index=7),
        sep("Face Tweak","layers",source=layers,index=16),
        sep("Right Arm Tweak","layers",source=layers,index=8),
        sep("Left Arm Tweak","layers",source=layers,index=9),
        sep("Right Leg Tweak","layers",source=layers,index=24),
        sep("Left Leg Tweak","layers",source=layers,index=25),
        sep("Limb Twist","layers",source=layers,index=10),
        sep("Extras","layers",source=layers,index=22),
        sep("Emotion Bones","layers",source=layers,index=15),
        sep("Dynamic Hair","layers",source=layers,index=6),
        sep("Footroll","layers",source=layers,index=26),
        sep("Cartoon Mouth","layers",source=layers,index=27),

    #skins
    sep("Minecraft Skin Downloader Username Downloader Skin Search NameMC","minecraft_username","Username",source=context.scene),
    seo("Minecraft Skin Downloader Username Downloader Skin Search NameMC Button","skin.download","Download From Username"),
    sem("Auto SSS Skin","color",0,1,"skin","Auto SSS"),
    sem("Auto SSS Sensitivity Skin","color",0,3,"skin","Auto SSS Sensitivity"),
    sem("Auto SSS Value Skin","color",0,4,"skin","SSS"),
    sem("Auto SSS Radius Skin","color",0,7,"skin","SSS Radius"),
    sem("Base Skin Color Colour SSS","color",0,2,"skin","Skin Color"),
    sem("SSS Color Colour","color",0,5,"skin","SSS Color"),

    #eyes
    sep("Gradient Eyes Color Colour Switch Eye Type Texture Eyes","gradient_color_eye","Eye Type"),
    sem("Eye Color Colour 1 Iris","eyenode",1,0,"eyes","Eye Color 1"),
    sem("Eye Color Colour 3 Iris","eyenode",1,2,"eyes","Eye Color 2"),
    sem("Eye Color Colour 2 Iris","eyenode",1,1,"eyes","Eye Color 3"),
    sem("Eye Color Colour 4 Iris","eyenode",1,3,"eyes","Eye Color 4"),
    sem("Specular Eye Color Colour","eyenode",1,4,"eyes","Eye Specular"),
    sem("Roughness Eye Color Colour","eyenode",1,5,"eyes","Eye Roughness"),
    sep("Emission Toggle Eye","toggleemission","Toggle Emission"),
    sep("Emission Toggle Pupil","togglepupil","Toggle Pupil"),
    sem("Pupil Color Colour 1 Iris","eyenode",1,11,"eyes","Pupil Color 1"),
    sem("Pupil Color Colour 2 Iris","eyenode",1,26,"eyes","Pupil Color 2"),
    sem("Pupil Size Iris","eyenode",1,10,"eyes"),
    sep("Pupil Bright Eye Iris","pupil_bright","Pupil Bright"),
    sep("Pupil Flip Bright Eye Iris","flip_pupil_bright","Flip Pupil Bright"),
    sem("Pupil Size 2 Iris","eyenode",1,24,"eyes"),
    sep("Toggle Sparkle Eye 1","togglesparkle1","Toggle Sparkle 1"),
    sep("Toggle Sparkle Eye 2","togglesparkle2","Toggle Sparkle 2"),
    sem("Sparkle 1 Size","eyenode",1,14,"eyes"),
    sem("Sparkle 1 Pos","eyenode",1,15,"eyes"),
    sem("Sparkle 2 Size","eyenode",1,18,"eyes"),
    sem("Sparkle 2 Pos","eyenode",1,19,"eyes"),

    #misc mats
    sem("Eyewhites Color Colour Eye R1","Principled BSDF",10,0,"eyewhites_r1","Eyewhite Color 1"),
    sem("Eyewhites Color Colour Eye L1","Principled BSDF",2,0,"eyewhites_l1","Eyewhite Color 2"),
    sem("Eyewhites Color Colour Eye R2","Principled BSDF",11,0,"eyewhites_r2","Eyewhite Color 3"),
    sem("Eyewhites Color Colour Eye L2","Principled BSDF",9,0,"eyewhites_l2","Eyewhite Color 4"),
    sem("Eyewhites Specular Color Colour Reflection","Principled BSDF",2,7,"eyewhites_l1","Eyewhite Specular"),
    sem("Eyewhites Roughness Color Colour Reflection","Principled BSDF",2,9,"eyewhites_l1","Eyewhite Rougness"),
    sem("Eyebrow Color Colour R1","Principled BSDF",13,0,"eyebrow_r1", "Eyebrow Color 1"),
    sem("Eyebrow Color Colour L1","Principled BSDF",6,0,"eyebrow_l1", "Eyebrow Color 2"),
    sem("Eyebrow Color Colour R2","Principled BSDF",14,0,"eyebrow_r2", "Eyebrow Color 3"),
    sem("Eyebrow Color Colour L2","Principled BSDF",12,0,"eyebrow_l2", "Eyebrow Color 4"),
    sem("Tongue Color Colour","Principled BSDF",3,0,"tongue","Tongue Color"),
    sem("Teeth Color Colour","Principled BSDF",4,0,"teeth","Teeth Color"),
    sem("Mouth Inside Color Colour","Principled BSDF",5,0,"mouth_inside","Mouth Inside Color"),
    sem("Cartoon Mouth Color Colour","Principled BSDF",15,0,"mouth_line","Cartoon Mouth Color"),
    sem("Emotion Line Color Colour","Principled BSDF",16,0,"emotion_line","Emotion Line Color"),

    #adv
    sep("Confirm Reset Ice Cube","confirm_ice_cube_reset","Confirm Ice Cube Reset"),

    #operators
    seo("Append Emotion Line","append.emotion"),
    seo("IK To FK Snapping Arm Right","fk_arm_r.snapping","R Arm IK > FK"),
    seo("IK To FK Snapping Arm Left","fk_arm_l.snapping","L Arm IK > FK"),
    seo("FK To IK Snapping Arm Right","fk_arm_r.snapping","R Arm FK > IK"),
    seo("FK To IK Snapping Arm Left","fk_arm_l.snapping","L Arm FK > IK"),
    seo("IK To FK Snapping Leg Right","fk_leg_r.snapping","R Leg IK > FK"),
    seo("IK To FK Snapping Leg Left","fk_leg_l.snapping","L Leg IK > FK"),
    seo("FK To IK Snapping Leg Right","fk_leg_r.snapping","R Leg FK > IK"),
    seo("FK To IK Snapping Leg Left","fk_arm_l.snapping","L Leg FK > IK"),
    seo("Updates Release New Ice Cube Download","ice_cube_check.updates","Check for Updates"),
    seo("Reset Ice Cube","reset_to_default.icecube","FULL ICE CUBE RESET"),

    #panel jumps 

    # IC_Jump_To_Panel_RigStyle,
    # IC_Jump_To_Panel_MeshStyle,
    # IC_Jump_To_Panel_Controls,
    # IC_Jump_To_Panel_Skins,
    # IC_Jump_To_Panel_Eyes,
    # IC_Jump_To_Panel_Misc,
    # IC_Jump_To_Panel_DLC,
    # IC_Jump_To_Panel_Parenting,
    # IC_Jump_To_Panel_System,

    seo("Rig Bends Arm Type Fingers Face Mouth Rotate Eyelashes Tongue Dynamic Hair Teeth Bevels Jaw Depth Shortcut","jump_to_panel.rigstyle","Jump to Rig Style"),
    seo("Bulge Squish Deform Taper Hip Chest Boob Women Girl Body Eyebrow Shortcut","jump_to_panel.meshstyle","Jump to Mesh Style"),
    seo("Controls IK Inverse Kinematics Influence Bone Layers Snapping Lag Wireframe Tracker Global Shortcut","jump_to_panel.controls","Jump to Controls"),
    seo("Skin Username Auto SSS Radius SSS Color Colour Shortcut","jump_to_panel.skins","Jump to Skins"),
    seo("Eyes Eye Color Pupil Eye Colour Gradient Eye Texture Emission Roughness Specular Sparkle Size Bright Face Shortcut Iris","jump_to_panel.eyes","Jump to Eyes"),
    seo("Eyewhite Specular Roughness Eyebrow Tongue Teeth Mouth Inside Cartoon Emotion Line Shortcut","jump_to_panel.misc","Jump to Misc"),
    seo("Armor DLC Asset Download Rig Append Create Free Preset Generate Template Shortcut","jump_to_panel.dlc","Jump to DLC"),
    seo("Parenting Children Parent Connect Attach Follow Shortcut","jump_to_panel.parenting","Jump to Parenting"),
    seo("System Memory Lag Update Settings Data Export Import Backup Reload Reset Shortcut","jump_to_panel.system","Jump to System")


    for entry in sorted(search_reference):
        if re.search(search_input,entry,re.IGNORECASE):
            if entry not in matching_props:
                matching_props.append(entry)

    for prop in matching_props:
        ref = search_reference[prop]
        ptype = ref['type']
        if ptype == 'prop':
            search_results_row = search_results_box.row(align=True)
            search_results_row.prop(data=ref['source'],property=str(ref['property_name']),text=str(ref['display_name']),expand=ref['expand'],toggle=ref['toggle'],index=ref['index'])
        elif ptype == 'op':
            search_results_row = search_results_box.row(align=True)
            search_results_row.operator(ref['op_name'],text=str(ref['display_name']))
        elif ptype == 'mat':
            try:
                material_list[ref['mat_id']].node_tree.nodes[ref['node']]

                search_results_row = search_results_box.row(align=True)
                search_results_row.prop(material_list[ref['mat_id']].node_tree.nodes[ref['node']].inputs[ref['input']], 'default_value', text=ref['display_name'],slider=True)
            except KeyError:
                pass
    
    if matching_props:
        pass
    else:
        search_results_row = search_results_box.row(align=True)
        search_results_row.label(text='No Results')
    
    matching_props.clear()

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