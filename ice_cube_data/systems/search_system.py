import bpy
from bpy.props import StringProperty
import re
from ice_cube_data.utils.general_func import selectBoneCollection, getLanguageTranslation




matching_props = []

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
    sep(getLanguageTranslation("ice_cube.search.terms.bendstyle"),"bendstyle",getLanguageTranslation("ice_cube.search.display.bendstyle")), #Smooth Bend Sharp Bend Type Style
    sep(getLanguageTranslation("ice_cube.search.terms.armtype_enum"),"armtype_enum"), #Arm Type Style Steve Alex Thin ModelArm Type Style Steve Alex Thin Model
    sep(getLanguageTranslation("ice_cube.search.terms.fingers_r"),"fingers_r"), #Right Fingers
    sep(getLanguageTranslation("ice_cube.search.terms.fingers_l"),"fingers_l"), #Left Fingers
    sep(getLanguageTranslation("ice_cube.search.terms.facerig"),"facerig",getLanguageTranslation("ice_cube.search.display.facerig")), #Face Rig Enable Hide
    sep(getLanguageTranslation("ice_cube.search.terms.mouthtypes"),"mouthtypes",getLanguageTranslation("ice_cube.search.display.mouth_style")), #Mouth Type Style Square Mouth Mine-imator Mouth Mineimator Mouth
    sep(getLanguageTranslation("ice_cube.search.terms.eyelashes"),"eyelashes",getLanguageTranslation("ice_cube.search.display.eyelashes"),toggle=False), #Eyelashes Female Woman Girl
    sep(getLanguageTranslation("ice_cube.search.terms.mouthrotate"),"mouthrotate",toggle=False), #Mouth Rotate
    sep(getLanguageTranslation("ice_cube.search.terms.tongue"),"tongue","Tongue",toggle=False), #Tongue Mouth
    sep(getLanguageTranslation("ice_cube.search.terms.line_mouth"),"line_mouth",getLanguageTranslation("ice_cube.search.display.cartoon_mouth"),toggle=False), #Cartoon Line Lips Mouth
    sep(getLanguageTranslation("ice_cube.search.terms.dynamichair"),"dynamichair",toggle=False), #Dynamic Hair
    sep(getLanguageTranslation("ice_cube.search.terms.teeth_cartoon"),"teeth_cartoon",getLanguageTranslation("ice_cube.search.display.cartoon_teeth")), #Cartoon Teeth Mouth
    sep(getLanguageTranslation("ice_cube.search.terms.teeth_bool"),"teeth_bool",getLanguageTranslation("ice_cube.search.display.teeth_bool")),  #Boolean Teeth Clipping Head
    sep(getLanguageTranslation("ice_cube.search.terms.teeth_curve"),"teeth_curve",getLanguageTranslation("ice_cube.search.display.teeth_curve")), #Teeth Curve Cartoon
    sep(getLanguageTranslation("ice_cube.search.terms.teeth_follow"),"teeth_follow",getLanguageTranslation("ice_cube.search.display.teeth_follow")), #Teeth Follow Mouth
    sep(getLanguageTranslation("ice_cube.search.terms.bevelmouth"),"bevelmouth",getLanguageTranslation("ice_cube.search.display.mouth_bevel")), #Mouth Bevel Lip
    sep(getLanguageTranslation("ice_cube.search.terms.bevel_mouth_strength"),"bevelmouthstrength",getLanguageTranslation("ice_cube.search.display.mouth_bevel_strength")), #Mouth Bevel Lip Strength
    sep(getLanguageTranslation("ice_cube.search.terms.jaw"),"jaw",getLanguageTranslation("ice_cube.search.display.jaw")), #Jaw Enable Disable
    sep(getLanguageTranslation("ice_cube.search.terms.round_jaw"),"round_jaw",getLanguageTranslation("ice_cube.search.display.round_jaw")), #Jaw Round Smooth Curve
    sep(getLanguageTranslation("ice_cube.search.terms.jaw_strength"),"jaw_strength",getLanguageTranslation("ice_cube.search.display.jaw_strength")), #Jaw Strength Length
    sep(getLanguageTranslation("ice_cube.search.terms.eye_depth"),"eyedepth",getLanguageTranslation("ice_cube.search.display.eye_depth")), #Eye Depth 2D
    sep(getLanguageTranslation("ice_cube.search.terms.mouth_depth"),"mouthdepth",getLanguageTranslation("ice_cube.search.display.mouth_depth")), #Mouth Depth 2D
    sep(getLanguageTranslation("ice_cube.search.terms.inner_mouth_depth"),"innermouthdepth",getLanguageTranslation("ice_cube.search.display.inner_mouth_depth")), #Inner Mouth Depth 2D Clipping Inside
    sep(getLanguageTranslation("ice_cube.search.terms.thumbfill_R"),"thumbfill_R"), #Thumbfill Right
    sep(getLanguageTranslation("ice_cube.search.terms.thumbfill_L"),"thumbfill_L"), #Thumbfill Left

    #mesh style
    sep(getLanguageTranslation("ice_cube.search.terms.bodybulge"),"bodybulge",getLanguageTranslation("ice_cube.search.display.body_bulge")), #Body Bulge Round Deform
    sep(getLanguageTranslation("ice_cube.search.terms.bulge_arm_r"),"bulge_arm_r",getLanguageTranslation("ice_cube.search.display.bulge_arm_r")), #Arm Right Bulge Round Deform
    sep(getLanguageTranslation("ice_cube.search.terms.bulge_arm_l"),"bulge_arm_l",getLanguageTranslation("ice_cube.search.display.bulge_arm_l")), #Arm Left Bulge Round Deform
    sep(getLanguageTranslation("ice_cube.search.terms.bulge_leg_r"),"bulge_leg_r",getLanguageTranslation("ice_cube.search.display.bulge_leg_r")), #Leg Right Bulge Round Deform
    sep(getLanguageTranslation("ice_cube.search.terms.bulge_leg_l"),"bulge_leg_l",getLanguageTranslation("ice_cube.search.display.bulge_leg_l")), #Leg Left Bulge Round Deform
    sep(getLanguageTranslation("ice_cube.search.terms.squish_head"),"squish_head",getLanguageTranslation("ice_cube.search.display.squish_head")), #Head Squish Deform
    sep(getLanguageTranslation("ice_cube.search.terms.squish_body"),"squish_body",getLanguageTranslation("ice_cube.search.display.squish_body")), #Body Squish Deform
    sep(getLanguageTranslation("ice_cube.search.terms.squish_arm_r"),"squish_arm_r",getLanguageTranslation("ice_cube.search.display.squish_arm_r")), #Right Arm Squish Deform
    sep(getLanguageTranslation("ice_cube.search.terms.squish_arm_l"),"squish_arm_l",getLanguageTranslation("ice_cube.search.display.squish_arm_l")), #Left Arm Squish Deform
    sep(getLanguageTranslation("ice_cube.search.terms.squish_leg_r"),"squish_leg_r",getLanguageTranslation("ice_cube.search.display.squish_leg_r")), #Right Leg Squish Deform
    sep(getLanguageTranslation("ice_cube.search.terms.squish_leg_l"),"squish_leg_l",getLanguageTranslation("ice_cube.search.display.squish_leg_l")), #Left Leg Squish Deform
    sep(getLanguageTranslation("ice_cube.search.terms.arm_taper"),"armtaper",getLanguageTranslation("ice_cube.search.display.arm_taper")), #Upper Arm Taper Deform
    sep(getLanguageTranslation("ice_cube.search.terms.arm_taper_lower"),"armtaperlower",getLanguageTranslation("ice_cube.search.display.arm_taper_lower")), #Lower Arm Taper Deform
    sep(getLanguageTranslation("ice_cube.search.terms.leg_taper_strength2"),"leg_taper_strength2",getLanguageTranslation("ice_cube.search.display.leg_taper_strength2")), #Upper Leg Taper Deform
    sep(getLanguageTranslation("ice_cube.search.terms.leg_taper_strength"),"leg_taper_strength",getLanguageTranslation("ice_cube.search.display.leg_taper_strength")), #Lower Leg Taper Female Woman Girl Deform
    sep(getLanguageTranslation("ice_cube.search.terms.hip"),"hip",getLanguageTranslation("ice_cube.search.display.hip")), #Hips Female Woman Girl Deform
    sep(getLanguageTranslation("ice_cube.search.terms.upper_body_width"),"upperbodywidth",getLanguageTranslation("ice_cube.search.display.upper_body_width")), #Upper Body Female Woman Girl Deform
    sep(getLanguageTranslation("ice_cube.search.terms.body_top_round"),"bodytopround",getLanguageTranslation("ice_cube.search.display.body_top_round")), #Rounded Body Top Deform
    sep(getLanguageTranslation("ice_cube.search.terms.lower_body_width"),"lowerbodywidth",getLanguageTranslation("ice_cube.search.display.lower_body_width")), #Lower Body Width Fat Deform
    sep(getLanguageTranslation("ice_cube.search.terms.breast_size"),"breastsize",getLanguageTranslation("ice_cube.search.display.breast_size")), #Chest Size Boobs Breasts Female Woman Girl Deform
    sep(getLanguageTranslation("ice_cube.search.terms.breast_weight"),"breastweight",getLanguageTranslation("ice_cube.search.display.breast_weight")), #Chest Weight Boobs Breasts Female Woman Girl Deform
    sep(getLanguageTranslation("ice_cube.search.terms.breast_shape"),"breastshape",getLanguageTranslation("ice_cube.search.display.breast_shape")), #Chest Shape Boobs Breasts Female Woman Girl Deform
    sep(getLanguageTranslation("ice_cube.search.terms.eyebrow_height"),"eyebrowheight"), #Eyebrow Height
    sep(getLanguageTranslation("ice_cube.search.terms.eyebrow_length"),"eyebrowlength"), #Eyebrow Length
    sep(getLanguageTranslation("ice_cube.search.terms.eyebrow_taper_1"),"eyebrowtaper1"), #Inner Taper Eyebrow
    sep(getLanguageTranslation("ice_cube.search.terms.eyebrow_taper_2"),"eyebrowtaper2"), #Outer Taper Eyebrow

    #controls
    sep(getLanguageTranslation("ice_cube.search.terms.antilag"), "antilag", getLanguageTranslation("ice_cube.search.display.antilag"),toggle=False), #Anti Lag Laggy Slow Performance Stutter
    sep(getLanguageTranslation("ice_cube.search.terms.wireframe"),"wireframe",toggle=False), #Wireframe
    sep(getLanguageTranslation("ice_cube.search.terms.global_head_rotation"),"global_head_rotation",getLanguageTranslation("ice_cube.search.display.global_head_rotation"),toggle=False), #Global Head Rotation Animation
    sep(getLanguageTranslation("ice_cube.search.terms.eyetracker"),"eyetracker",getLanguageTranslation("ice_cube.search.display.eye_tracker"),toggle=False), #Eye Tracker Control
    sep(getLanguageTranslation("ice_cube.search.terms.toggle_1"),"toggle_1",getLanguageTranslation("ice_cube.search.display.toggle_1"),toggle=False), #Toggle Custom 1
    sep(getLanguageTranslation("ice_cube.search.terms.toggle_2"),"toggle_2",getLanguageTranslation("ice_cube.search.display.toggle_2"),toggle=False), #Toggle Custom 2
    sep(getLanguageTranslation("ice_cube.search.terms.toggle_3"),"toggle_3",getLanguageTranslation("ice_cube.search.display.toggle_3"),toggle=False), #Toggle Custom 3
    sep(getLanguageTranslation("ice_cube.search.terms.toggle_4"),"toggle_4",getLanguageTranslation("ice_cube.search.display.toggle_4"),toggle=False), #Toggle Custom 4
    sep(getLanguageTranslation("ice_cube.search.terms.r_arm_ik"),"r_arm_ik",getLanguageTranslation("ice_cube.search.display.r_arm_ik")), #Right Arm IK Inverse Kinematics
    sep(getLanguageTranslation("ice_cube.search.terms.l_arm_ik"),"l_arm_ik",getLanguageTranslation("ice_cube.search.display.l_arm_ik")), #Left Arm IK Inverse Kinematics
    sep(getLanguageTranslation("ice_cube.search.terms.r_leg_ik"),"r_leg_ik",getLanguageTranslation("ice_cube.search.display.r_leg_ik")), #Right Leg IK Inverse Kinematics
    sep(getLanguageTranslation("ice_cube.search.terms.l_leg_ik"),"l_leg_ik",getLanguageTranslation("ice_cube.search.display.l_leg_ik")), #Left Leg IK Inverse Kinematics
    sep(getLanguageTranslation("ice_cube.search.terms.stretch_arm_r"),"stretch_arm_r",getLanguageTranslation("ice_cube.search.display.stretch_arm_r")), #IK Stretch Arm Right
    sep(getLanguageTranslation("ice_cube.search.terms.stretch_arm_l"),"stretch_arm_l",getLanguageTranslation("ice_cube.search.display.stretch_arm_l")), #IK Stretch Arm Left
    sep(getLanguageTranslation("ice_cube.search.terms.stretch_leg_r"),"stretch_leg_r",getLanguageTranslation("ice_cube.search.display.stretch_leg_r")), #IK Stretch Leg Right
    sep(getLanguageTranslation("ice_cube.search.terms.stretch_leg_l"),"stretch_leg_l",getLanguageTranslation("ice_cube.search.display.stretch_leg_l")), #IK Stretch Leg Left
    sep(getLanguageTranslation("ice_cube.search.terms.wrist_lock_r"),"wrist_lock_r",getLanguageTranslation("ice_cube.search.display.wrist_lock_r")), #Wrist Lock IK Right
    sep(getLanguageTranslation("ice_cube.search.terms.wrist_lock_l"),"wrist_lock_l",getLanguageTranslation("ice_cube.search.display.wrist_lock_l")), #Wrist Lock IK Left
    sep(getLanguageTranslation("ice_cube.search.terms.ankle_r"),"ankle_r",getLanguageTranslation("ice_cube.search.display.ankle_r")), #Ankle IK Right
    sep(getLanguageTranslation("ice_cube.search.terms.ankle_l"),"ankle_l",getLanguageTranslation("ice_cube.search.display.ankle_l")), #Ankle IK Left
    sep(getLanguageTranslation("ice_cube.search.terms.arm_ik_parent_r"),"arm_ik_parent_r",getLanguageTranslation("ice_cube.search.display.arm_ik_parent_r"),expand=False), #Arm IK Parent Right
    sep(getLanguageTranslation("ice_cube.search.terms.arm_ik_parent_l"),"arm_ik_parent_l",getLanguageTranslation("ice_cube.search.display.arm_ik_parent_l"),expand=False), #Arm IK Parent Left
    sep(getLanguageTranslation("ice_cube.search.terms.eye_influence"),"eye_influence",getLanguageTranslation("ice_cube.search.display.eye_influence")), #Eye Influence Controls
    sep(getLanguageTranslation("ice_cube.search.terms.eyebrow_influence"),"eyebrow_influence",getLanguageTranslation("ice_cube.search.display.eyebrow_influence")), #Eyebrow Influence Controls
    sep(getLanguageTranslation("ice_cube.search.terms.mouth_influence"),"mouth_influence",getLanguageTranslation("ice_cube.search.display.mouth_influence")), #Mouth Influence Controls

    #bone layers
    if bpy.app.version >= (4, 0, 0):
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.main"),"is_visible",source="bone_collection",prop_tag="Main Bones"), #Main Rig Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.face"),"is_visible",source="bone_collection",prop_tag="Face Panel Bones"), #Face Panel Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armRIK"),"is_visible",source="bone_collection",prop_tag="Right Arm IK"), #Right Arm IK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armLIK"),"is_visible",source="bone_collection",prop_tag="Left Arm IK"), #Left Arm IK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armRFK"),"is_visible",source="bone_collection",prop_tag="Right Arm FK"), #Right Arm FK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armLFK"),"is_visible",source="bone_collection",prop_tag="Left Arm FK"), #Left Arm FK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.rFingers"),"is_visible",source="bone_collection",prop_tag="Right Fingers"), #Right Fingers Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.lFingers"),"is_visible",source="bone_collection",prop_tag="Left Fingers"), #Left Fingers Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legRIK"),"is_visible",source="bone_collection",prop_tag="Right Leg IK"), #Right Leg IK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legLIK"),"is_visible",source="bone_collection",prop_tag="Left Leg IK"), #Left Leg IK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legRFK"),"is_visible",source="bone_collection",prop_tag="Right Leg FK"), #Right Leg FK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legLFK"),"is_visible",source="bone_collection",prop_tag="Left Leg FK"), #Left Leg FK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.bodytweak"),"is_visible",source="bone_collection",prop_tag="Body Tweak"), #Body Tweak Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.facetweak"),"is_visible",source="bone_collection",prop_tag="Face Tweak"), #Face Tweak Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armRTweak"),"is_visible",source="bone_collection",prop_tag="Right Arm Tweak"), #Right Arm Tweak Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armLTweak"),"is_visible",source="bone_collection",prop_tag="Left Arm Tweak"), #Left Arm Tweak Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legRTweak"),"is_visible",source="bone_collection",prop_tag="Right Leg Tweak"), #Right Leg Tweak Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legLTweak"),"is_visible",source="bone_collection",prop_tag="Left Leg Tweak"), #Left Leg Tweak Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.twist"),"is_visible",source="bone_collection",prop_tag="Twist"), #Limb Twist Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.extra"),"is_visible",source="bone_collection",prop_tag="Extra"), #Extras Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.emotion"),"is_visible",source="bone_collection",prop_tag="Emotion Bones"), #Emotion Bones Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.hair"),"is_visible",source="bone_collection",prop_tag="Dynamic Hair"), #Dynamic Hair Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.footroll"),"is_visible",source="bone_collection",prop_tag="Footroll"), #Footroll Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.cartoon"),"is_visible",source="bone_collection",prop_tag="Cartoon Mouth"), #Cartoon Mouth Bone Layer
    else:
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.main"),"layers",source=layers,index=0), #Main Rig Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.face"),"layers",source=layers,index=23), #Face Panel Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armRIK"),"layers",source=layers,index=1), #Right Arm IK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armLIK"),"layers",source=layers,index=2), #Left Arm IK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armRFK"),"layers",source=layers,index=17), #Right Arm FK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armLFK"),"layers",source=layers,index=18), #Left Arm FK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.rFingers"),"layers",source=layers,index=5), #Right Fingers Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.lFingers"),"layers",source=layers,index=21), #Left Fingers Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legRIK"),"layers",source=layers,index=3), #Right Leg IK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legLIK"),"layers",source=layers,index=4), #Left Leg IK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legRFK"),"layers",source=layers,index=19), #Right Leg FK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legLFK"),"layers",source=layers,index=20), #Left Leg FK Bone Layer
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.bodytweak"),"layers",source=layers,index=7), #Body Tweak
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.facetweak"),"layers",source=layers,index=16), #Face Tweak
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armRTweak"),"layers",source=layers,index=8), #Right Arm Tweak
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.armLTweak"),"layers",source=layers,index=9), #Left Arm Tweak
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legRTweak"),"layers",source=layers,index=24), #Right Leg Tweak
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.legLTweak"),"layers",source=layers,index=25), #Left Leg Tweak
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.twist"),"layers",source=layers,index=10), #Limb Twist
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.extra"),"layers",source=layers,index=22), #Extras
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.emotion"),"layers",source=layers,index=15), #Emotion Bones
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.hair"),"layers",source=layers,index=6), #Dynamic Hair
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.footroll"),"layers",source=layers,index=26), #Footroll
        sep(getLanguageTranslation("ice_cube.search.terms.bonelayer.cartoon"),"layers",source=layers,index=27), #Cartoon Mouth

    #skins
    sep(getLanguageTranslation("ice_cube.search.terms.minecraft_username"),"minecraft_username",getLanguageTranslation("ice_cube.search.display.minecraft_username"),source=context.scene), # Minecraft Skin Downloader Username Downloader Skin Search NameMC
    seo(getLanguageTranslation("ice_cube.search.terms.skin"),"skin.download",getLanguageTranslation("ice_cube.search.display.skin")), # Minecraft Skin Downloader Username Downloader Skin Search NameMC Button
    sem(getLanguageTranslation("ice_cube.search.terms.auto_sss"),"color",0,2,"skin",getLanguageTranslation("ice_cube.search.display.auto_sss")), #Auto SSS Skin
    sem(getLanguageTranslation("ice_cube.search.terms.sss_senstivity"),"color",0,3,"skin",getLanguageTranslation("ice_cube.search.display.sss_senstivity")), #Auto SSS Sensitivity Skin
    sem(getLanguageTranslation("ice_cube.search.terms.sss_strength"),"color",0,4,"skin",getLanguageTranslation("ice_cube.search.display.sss_strength")), #Auto SSS Value Skin
    sem(getLanguageTranslation("ice_cube.search.terms.sss_radius"),"color",0,9,"skin",getLanguageTranslation("ice_cube.search.display.sss_radius")), #Auto SSS Radius Skin
    sem(getLanguageTranslation("ice_cube.search.terms.skin_color"),"color",0,5,"skin",getLanguageTranslation("ice_cube.search.display.skin_color")), #Base Skin Color Colour SSS
    sem(getLanguageTranslation("ice_cube.search.terms.sss_color"),"color",0,1,"skin",getLanguageTranslation("ice_cube.search.display.sss_color")), #SSS Color Colour

    #eyes
    sep(getLanguageTranslation("ice_cube.search.terms.gradient_eyes"),"gradient_color_eye",getLanguageTranslation("ice_cube.search.display.gradient_eyes")), #Gradient Eyes Color Colour Switch Eye Type Texture Eyes
    sem(getLanguageTranslation("ice_cube.search.terms.eye_color_1"),"eyenode",1,0,"eyes",getLanguageTranslation("ice_cube.search.display.eye_color_1")), #Eye Color Colour 1 Iris
    sem(getLanguageTranslation("ice_cube.search.terms.eye_color_2"),"eyenode",1,2,"eyes",getLanguageTranslation("ice_cube.search.display.eye_color_2")), #Eye Color Colour 3 Iris
    sem(getLanguageTranslation("ice_cube.search.terms.eye_color_3"),"eyenode",1,1,"eyes",getLanguageTranslation("ice_cube.search.display.eye_color_3")), #Eye Color Colour 2 Iris
    sem(getLanguageTranslation("ice_cube.search.terms.eye_color_4"),"eyenode",1,3,"eyes",getLanguageTranslation("ice_cube.search.display.eye_color_4")), #Eye Color Colour 4 Iris
    sem(getLanguageTranslation("ice_cube.search.terms.eye_specular"),"eyenode",1,4,"eyes",getLanguageTranslation("ice_cube.search.display.eye_specular")), #Specular Eye Color Colour
    sem(getLanguageTranslation("ice_cube.search.terms.eye_roughness"),"eyenode",1,5,"eyes",getLanguageTranslation("ice_cube.search.display.eye_roughness")), #Roughness Eye Color Colour
    sep(getLanguageTranslation("ice_cube.search.terms.eye_emission"),"toggleemission",getLanguageTranslation("ice_cube.search.display.eye_emission")), #Emission Toggle Eye
    sep(getLanguageTranslation("ice_cube.search.terms.toggle_pupil"),"togglepupil",getLanguageTranslation("ice_cube.search.display.toggle_pupil")), #Emission Toggle Pupil
    sem(getLanguageTranslation("ice_cube.search.terms.pupil_color_1"),"eyenode",1,11,"eyes",getLanguageTranslation("ice_cube.search.display.pupil_color_1")), #Pupil Color Colour 1 Iris
    sem(getLanguageTranslation("ice_cube.search.terms.pupil_color_2"),"eyenode",1,26,"eyes",getLanguageTranslation("ice_cube.search.display.pupil_color_2")), #Pupil Color Colour 2 Iris
    sep(getLanguageTranslation("ice_cube.search.terms.pupil_bright"),"pupil_bright",getLanguageTranslation("ice_cube.search.display.pupil_bright")), #Pupil Bright Eye Iris
    sep(getLanguageTranslation("ice_cube.search.terms.flip_pupil_bright"),"flip_pupil_bright",getLanguageTranslation("ice_cube.search.display.flip_pupil_bright")) #,Pupil Flip Bright Eye Iris
    sem(getLanguageTranslation("ice_cube.search.terms.pupil_size_2"),"eyenode",1,24,"eyes"), #Pupil Size 2 Iris
    sep(getLanguageTranslation("ice_cube.search.terms.toggle_sparkle_1"),"togglesparkle1",getLanguageTranslation("ice_cube.search.display.toggle_sparkle_1")), #Toggle Sparkle Eye 1
    sep(getLanguageTranslation("ice_cube.search.terms.toggle_sparkle_2"),"togglesparkle2",getLanguageTranslation("ice_cube.search.display.toggle_sparkle_2")), #Toggle Sparkle Eye 2
    sem(getLanguageTranslation("ice_cube.search.terms.sparkle_1_size"),"eyenode",1,14,"eyes"), #Sparkle 1 Size
    sem(getLanguageTranslation("ice_cube.search.terms.sparkle_1_pos"),"eyenode",1,15,"eyes"), #Sparkle 1 Pos
    sem(getLanguageTranslation("ice_cube.search.terms.sparkle_2_size"),"eyenode",1,18,"eyes"), #Sparkle 2 Size
    sem(getLanguageTranslation("ice_cube.search.terms.sparkle_2_pos"),"eyenode",1,19,"eyes"), #Sparkle 2 Pos

    #misc mats
    sem(getLanguageTranslation("ice_cube.search.terms.eyewhite_1"),"Principled BSDF",10,0,"eyewhites_r1",getLanguageTranslation("ice_cube.search.display.eyewhite_1")), #Eyewhites Color Colour Eye R1
    sem(getLanguageTranslation("ice_cube.search.terms.eyewhite_2"),"Principled BSDF",2,0,"eyewhites_l1",getLanguageTranslation("ice_cube.search.display.eyewhite_2")), #Eyewhites Color Colour Eye L1
    sem(getLanguageTranslation("ice_cube.search.terms.eyewhite_3"),"Principled BSDF",11,0,"eyewhites_r2",getLanguageTranslation("ice_cube.search.display.eyewhite_3")), #Eyewhites Color Colour Eye R2
    sem(getLanguageTranslation("ice_cube.search.terms.eyewhite_4"),"Principled BSDF",9,0,"eyewhites_l2",getLanguageTranslation("ice_cube.search.display.eyewhite_4")), #Eyewhites Color Colour Eye L2
    sem(getLanguageTranslation("ice_cube.search.terms.eyewhite_specular"),"Principled BSDF",2,7,"eyewhites_l1",getLanguageTranslation("ice_cube.search.display.eyewhite_specular")), #Eyewhites Specular Color Colour Reflection
    sem(getLanguageTranslation("ice_cube.search.terms.eyewhite_roughness"),"Principled BSDF",2,9,"eyewhites_l1",getLanguageTranslation("ice_cube.search.display.eyewhite_roughness")), #Eyewhites Roughness Color Colour Reflection
    sem(getLanguageTranslation("ice_cube.search.terms.eyebrow_color_1"),"Principled BSDF",13,0,"eyebrow_r1", getLanguageTranslation("ice_cube.search.display.eyebrow_color_1")), #Eyebrow Color Colour R1
    sem(getLanguageTranslation("ice_cube.search.terms.eyebrow_color_2"),"Principled BSDF",6,0,"eyebrow_l1", getLanguageTranslation("ice_cube.search.display.eyebrow_color_2")), #Eyebrow Color Colour L1
    sem(getLanguageTranslation("ice_cube.search.terms.eyebrow_color_3"),"Principled BSDF",14,0,"eyebrow_r2", getLanguageTranslation("ice_cube.search.display.eyebrow_color_3")), #Eyebrow Color Colour R2
    sem(getLanguageTranslation("ice_cube.search.terms.eyebrow_color_4"),"Principled BSDF",12,0,"eyebrow_l2", getLanguageTranslation("ice_cube.search.display.eyebrow_color_4")), #Eyebrow Color Colour L2
    sem(getLanguageTranslation("ice_cube.search.terms.tongue_color"),"Principled BSDF",3,0,"tongue",getLanguageTranslation("ice_cube.search.display.tongue_color")), #Tongue Color Colour
    sem(getLanguageTranslation("ice_cube.search.terms.teeth_color"),"Principled BSDF",4,0,"teeth",getLanguageTranslation("ice_cube.search.display.teeth_color")), #Teeth Color Colour
    sem(getLanguageTranslation("ice_cube.search.terms.mouth_inside_color"),"Principled BSDF",5,0,"mouth_inside",getLanguageTranslation("ice_cube.search.display.mouth_inside_color")), #Mouth Inside Color Colour
    sem(getLanguageTranslation("ice_cube.search.terms.cartoon_mouth_color"),"Principled BSDF",15,0,"mouth_line",getLanguageTranslation("ice_cube.search.display.cartoon_mouth_color")), #Cartoon Mouth Color Colour
    sem(getLanguageTranslation("ice_cube.search.terms.emotion_line_color"),"Principled BSDF",16,0,"emotion_line",getLanguageTranslation("ice_cube.search.display.emotion_line_color")), #Emotion Line Color Colour

    #adv
    sep(getLanguageTranslation("ice_cube.search.terms.confirm_reset"),"confirm_ice_cube_reset",getLanguageTranslation("ice_cube.search.display.confirm_reset")), #Confirm Reset Ice Cube

    #operators
    seo(getLanguageTranslation("ice_cube.search.terms.append_emtion"),"append.emotion"), #Append Emotion Line
    seo(getLanguageTranslation("ice_cube.search.terms.fk_arm_r"),"fk_arm_r.snapping",getLanguageTranslation("ice_cube.search.display.fk_arm_r")), #IK To FK Snapping Arm Right        #R Arm IK > FK
    seo(getLanguageTranslation("ice_cube.search.terms.fk_arm_l"),"fk_arm_l.snapping",getLanguageTranslation("ice_cube.search.display.fk_arm_l")), #IK To FK Snapping Arm Left         #L Arm IK > FK
    seo(getLanguageTranslation("ice_cube.search.terms.ik_arm_r"),"ik_arm_r.snapping",getLanguageTranslation("ice_cube.search.display.ik_arm_r")), #FK To IK Snapping Arm Right        #R Arm FK > IK
    seo(getLanguageTranslation("ice_cube.search.terms.ik_arm_l"),"ik_arm_l.snapping",getLanguageTranslation("ice_cube.search.display.ik_arm_l")), #FK To IK Snapping Arm Left         #L Arm FK > IK
    seo(getLanguageTranslation("ice_cube.search.terms.fk_leg_r"),"fk_leg_r.snapping",getLanguageTranslation("ice_cube.search.display.fk_leg_r")), #IK To FK Snapping Leg Right        #R Leg IK > FK
    seo(getLanguageTranslation("ice_cube.search.terms.fk_leg_l"),"fk_leg_l.snapping",getLanguageTranslation("ice_cube.search.display.fk_leg_l")), #IK To FK Snapping Leg Left         #L Leg IK > FK
    seo(getLanguageTranslation("ice_cube.search.terms.ik_leg_r"),"ik_leg_r.snapping",getLanguageTranslation("ice_cube.search.display.ik_leg_r")), #FK To IK Snapping Leg Right        #R Leg FK > IK
    seo(getLanguageTranslation("ice_cube.search.terms.ik_leg_l"),"ik_leg_l.snapping",getLanguageTranslation("ice_cube.search.display.ik_leg_l")), #FK To IK Snapping Leg Left         #L Leg FK > IK
    seo(getLanguageTranslation("ice_cube.search.terms.check_updates"),"ice_cube_check.updates",getLanguageTranslation("ice_cube.search.display.check_updates")), #Updates Release New Ice Cube Download
    seo(getLanguageTranslation("ice_cube.search.terms.reset_ice_cube"),"reset_to_default.icecube",getLanguageTranslation("ice_cube.search.display.reset_ice_cube")), #Reset Ice Cube

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

    seo(getLanguageTranslation("ice_cube.search.terms.jump.rigstyle"),"jump_to_panel.rigstyle",getLanguageTranslation("ice_cube.search.display.jump.rigstyle")), #Rig Bends Arm Type Fingers Face Mouth Rotate Eyelashes Tongue Dynamic Hair Teeth Bevels Jaw Depth Shortcut
    seo(getLanguageTranslation("ice_cube.search.terms.jump.meshstyle"),"jump_to_panel.meshstyle",getLanguageTranslation("ice_cube.search.display.jump.meshstyle")), #Bulge Squish Deform Taper Hip Chest Boob Women Girl Body Eyebrow Shortcut Men Boy
    seo(getLanguageTranslation("ice_cube.search.terms.jump.controls"),"jump_to_panel.controls",getLanguageTranslation("ice_cube.search.display.jump.controls")), #Controls IK Inverse Kinematics Influence Bone Layers Snapping Lag Wireframe Tracker Global Shortcut
    seo(getLanguageTranslation("ice_cube.search.terms.jump.skins"),"jump_to_panel.skins",getLanguageTranslation("ice_cube.search.display.jump.skins")), #Skin Username Auto SSS Radius SSS Color Colour Shortcut
    seo(getLanguageTranslation("ice_cube.search.terms.jump.eyes"),"jump_to_panel.eyes",getLanguageTranslation("ice_cube.search.display.jump.eyes")), #Eyes Eye Color Pupil Eye Colour Gradient Eye Texture Emission Roughness Specular Sparkle Size Bright Face Shortcut Iris
    seo(getLanguageTranslation("ice_cube.search.terms.jump.misc"),"jump_to_panel.misc",getLanguageTranslation("ice_cube.search.display.jump.misc")), #Eyewhite Specular Roughness Eyebrow Tongue Teeth Mouth Inside Cartoon Emotion Line Shortcut
    seo(getLanguageTranslation("ice_cube.search.terms.jump.dlc"),"jump_to_panel.dlc",getLanguageTranslation("ice_cube.search.display.jump.dlc")), #Armor DLC Asset Download Rig Append Create Free Preset Generate Template Shortcut
    seo(getLanguageTranslation("ice_cube.search.terms.jump.parenting"),"jump_to_panel.parenting",getLanguageTranslation("ice_cube.search.display.jump.parenting")), #Parenting Children Parent Connect Attach Follow Shortcut
    seo(getLanguageTranslation("ice_cube.search.terms.jump.system"),"jump_to_panel.system",getLanguageTranslation("ice_cube.search.display.jump.system")) #System Memory Lag Update Settings Data Export Import Backup Reload Reset Shortcut


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
