import bpy

from bpy.props import (StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        EnumProperty,
                        )

from ice_cube_data.utils.selectors import isRigSelected
from ice_cube_data.utils.general_func import convertStringNumbers, selectBoneCollection, getLanguageTranslation

cur_blender_version = convertStringNumbers(list(bpy.app.version))


# classes

def r_fingers_update(self, context):
    if self.enable_control_linking:
        if cur_blender_version >= 400:
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Right Fingers")
            target_collection.is_visible = self.fingers_r
        else:
            bpy.data.objects[self.name].data.layers[5] = self.fingers_r

def l_fingers_update(self, context):
    if self.enable_control_linking:
        if cur_blender_version >= 400:
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Left Fingers")
            target_collection.is_visible = self.fingers_l
        else:
            bpy.data.objects[self.name].data.layers[21] = self.fingers_l

def r_arm_ik_update(self, context):
    if self.enable_control_linking:
        if cur_blender_version >= 400:
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Right Arm IK")
            target_collection.is_visible = self.r_arm_ik
        else:
            bpy.data.objects[self.name].data.layers[1] = self.r_arm_ik

def l_arm_ik_update(self, context):
    if self.enable_control_linking:
        if cur_blender_version >= 400:
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Left Arm IK")
            target_collection.is_visible = self.l_arm_ik
        else:
            bpy.data.objects[self.name].data.layers[2] = self.l_arm_ik

def r_leg_ik_update(self, context):
    if self.enable_control_linking:
        if cur_blender_version >= 400:
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Right Leg IK")
            target_collection.is_visible = self.r_leg_ik

            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Right Leg FK")
            target_collection.is_visible = not self.r_leg_ik
        else:
            bpy.data.objects[self.name].data.layers[3] = self.r_leg_ik
            bpy.data.objects[self.name].data.layers[19] = not self.r_leg_ik

def l_leg_ik_update(self, context):
    if self.enable_control_linking:
        if cur_blender_version >= 400:
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Left Leg IK")
            target_collection.is_visible = self.l_leg_ik

            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Left Leg FK")
            target_collection.is_visible = not self.l_leg_ik
        else:
            bpy.data.objects[self.name].data.layers[4] = self.l_leg_ik
            bpy.data.objects[self.name].data.layers[20] = not self.l_leg_ik

def dynamic_hair_update(self, context):
    if self.enable_control_linking:
        if cur_blender_version >= 400:
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Dynamic Hair")
            target_collection.is_visible = self.dynamichair
        else:
            bpy.data.objects[self.name].data.layers[6] = self.dynamichair

def face_rig_update(self, context):
    if self.enable_control_linking:
        if cur_blender_version >= 400:
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Face Panel Bones")
            target_collection.is_visible = self.facerig
            
            target_collection = selectBoneCollection(bpy.data.objects[self.name].data.collections,"Face Tweak")
            if target_collection.is_visible:
                target_collection.is_visible = self.facerig
        else:
            bpy.data.objects[self.name].data.layers[23] = self.facerig
            if bpy.data.objects[self.name].data.layers[16]:
                bpy.data.objects[self.name].data.layers[16] = self.facerig

def armtype_update(self,context):
    print(f"armtype_enum updated to {self.armtype_enum}")

#Bool Prop

bpy.types.Object.r_arm_ik = BoolProperty(
name="r_arm_ik", description="Enables IK for the right arm", default=False,update=r_arm_ik_update)
    
bpy.types.Object.l_arm_ik = BoolProperty(
name="l_arm_ik", description="Enables IK for the left arm", default=False,update=l_arm_ik_update)
    
bpy.types.Object.r_leg_ik = BoolProperty(
name="r_leg_ik", description="Enables IK for the right leg", default=True,update=r_leg_ik_update)
    
bpy.types.Object.l_leg_ik = BoolProperty(
name="l_leg_ik", description="Enables IK for the left leg", default=True,update=l_leg_ik_update)
    
bpy.types.Object.ankle_r = BoolProperty(
name="ankle_r", description="Toggles the ankle for the right leg, requires IK to be enabled", default=True)
    
bpy.types.Object.ankle_l = BoolProperty(
name="ankle_l", description="Toggles the ankle for the left leg, requires IK to be enabled", default=True)
    
bpy.types.Object.stretch_leg_r = BoolProperty(
name="stretch_leg_r", description="Allows the leg to stretch further than normal, requires IK to be enabled", default=True)
    
bpy.types.Object.stretch_leg_l = BoolProperty(
name="stretch_leg_l", description="Allows the leg to stretch further than normal, requires IK to be enabled", default=True)
    
bpy.types.Object.stretch_arm_r = BoolProperty(
name="stretch_arm_r", description="Allows the arm to stretch further than normal, requires IK to be enabled", default=False)
    
bpy.types.Object.stretch_arm_l = BoolProperty(
name="stretch_arm_l", description="Allows the arm to stretch further than normal, requires IK to be enabled", default=False)
    
bpy.types.Object.fingers_r = BoolProperty(
name="fingers_r", description="Enables fingers on the rig, if the bones don't appear check the bone layer section",default=False,update=r_fingers_update)
    
bpy.types.Object.fingers_l = BoolProperty(
name="fingers_l", description="Enables fingers on the rig, if the bones don't appear check the bone layer section", default=False,update=l_fingers_update)

bpy.types.Object.wrist_lock_r = BoolProperty(
name="wrist_lock_r", description="Locks the right wrist to world space, requires IK", default=False)

bpy.types.Object.wrist_lock_l = BoolProperty(
name="wrist_lock_l", description="Locks the left wrist to world space, requires IK", default=False)

bpy.types.Object.eyelashes = BoolProperty(
name="eyelashes", description="Enables eyelashes on the character", default=False)

bpy.types.Object.wireframe = BoolProperty(
name="wireframe", description="Enables a wireframe view", default=False)

bpy.types.Object.jaw = BoolProperty(
name="jaw", description="Enables the jaw", default=False)

bpy.types.Object.round_jaw = BoolProperty(
name="round_jaw", description="Decides whether to use a square or rounded jaw", default=False)

bpy.types.Object.bevelmouth = BoolProperty(
name="bevelmouth", description="Bevels the mouth inwards to create the appearance of lips", default=False)

bpy.types.Object.teeth_cartoon = BoolProperty(
name="teeth_cartoon", description="Creates a cartoon like look with the teeth", default=False)

bpy.types.Object.antilag = BoolProperty(
name="antilag", description="Disables certain features to allow the rig to run better", default=False)

bpy.types.Object.teeth_bool = BoolProperty(
name="teeth_bool", description="Fixes the teeth sticking outside of the head, disabled by default for performance reasons", default=False)

bpy.types.Object.tongue = BoolProperty(
name="tongue", description="Enables a tongue inside of the rig", default=False)

bpy.types.Object.facerig = BoolProperty(
name="facerig", description="Toggles the entire face rig and its controls", default=True,update=face_rig_update)

bpy.types.Object.leg_deform = BoolProperty(
name="leg_deform", description="Enables leg deforms", default=False)

bpy.types.Object.body_deforms = BoolProperty(
name="body_deforms", description="Enables body deforms", default=False)

bpy.types.Object.dynamichair = BoolProperty(
name="dynamichair", description="Enables dynamic hair, extra faces will appear along the body that can be used to cut out hair", default=False,update=dynamic_hair_update)

bpy.types.Object.eyebrowdeform = BoolProperty(
name="eyebrowdeform", description="Enables the eyebrow deforms", default=False)

bpy.types.Object.togglepupil = BoolProperty(
name="togglepupil", description="Toggles the pupil on the eye", default=True)

bpy.types.Object.togglegradient = BoolProperty(
name="togglegradient", description="Toggle Gradient", default=False)

bpy.types.Object.togglesparkle1 = BoolProperty(
name="togglesparkle1", description="Toggles the first eye sparkle", default=True)

bpy.types.Object.togglesparkle2 = BoolProperty(
name="togglesparkle2", description="Toggles the second eye sparkle", default=True)

bpy.types.Object.toggleemission = BoolProperty(
name="toggleemission", description="Toggles eye emission", default=True)

bpy.types.Object.toggle_1 = BoolProperty(
name="Toggle 1", description="Toggle one, on by default.", default=True)

bpy.types.Object.toggle_2 = BoolProperty(
name="Toggle 2", description="Toggle two, off by default.", default=False)

bpy.types.Object.mouthrotate = BoolProperty(
name="mouthrotate", description="Rotates the mouthe edges based on position", default=False)

bpy.types.Object.toggle_3 = BoolProperty(
name="Toggle 3", description="Toggle three, off by default.", default=False)

bpy.types.Object.toggle_4 = BoolProperty(
name="Toggle 4", description="Toggle four, off by default.", default=False)

bpy.types.Object.breastswitch = BoolProperty(
name="breastswitch", description="Toggles a bone for controlling the position of the breasts", default=False)

bpy.types.Object.line_mouth = BoolProperty(
name="line_mouth", description="Show/Hides the cartoon line mouth", default=False)

bpy.types.Object.baked_rig = BoolProperty(
name="baked_rig", description="Decides if the imported rig should be baked or not", default=False)

bpy.types.Object.global_head_rotation = BoolProperty(
name="global_head_rotation", description="Enables/Disables global head rotation", default=False)

bpy.types.Object.prop_clipboard = BoolProperty(
name="prop_clipboard", description="Determines if the settings will be exported to the clipboard or a file", default=False)

bpy.types.Object.export_to_icpreset = BoolProperty(
    name = "export_to_icpreset", description="Decides whether to export the finished product to an icpreset file or an asset pack",default=False)

bpy.types.Object.generate_thumbnail = BoolProperty(
    name = "generate_thumbnail", description="Decides whether to generate a thumbnail in the current scene",default=False)

bpy.types.Object.generate_baked = BoolProperty(
    name = "generate_baked", description="Decides whether to generate a baked version of the rig",default=False)

bpy.types.Object.has_baked_version = BoolProperty(
    name = "has_baked_version", description="Decides whether to put True or False in the baked part of info.json",default=False)

bpy.types.Object.thumbfill_L = BoolProperty(
    name = "thumbfill_L", description="Toggles the thumbfill on the left hand",default=True)

bpy.types.Object.thumbfill_R = BoolProperty(
    name = "thumbfill_R", description="Toggles the thumbfill on the right hand",default=True)

bpy.types.Object.eyetracker = BoolProperty(
    name = "eyetracker", description="Toggles an eye tracker that will operate in global space",default=False)

bpy.types.Object.teeth_follow = BoolProperty(
    name = "teeth_follow", description="Teeth will follow and rotate with the mouth control",default=True)

bpy.types.Object.teeth_settings = BoolProperty(
    name = "teeth_settings", description="Shows/Hides teeth settings in the panel",default=True)

bpy.types.Object.bevel_settings = BoolProperty(
    name = "bevel_settings", description="Shows/Hides bevel settings in the panel",default=False)

bpy.types.Object.jaw_settings = BoolProperty(
    name = "jaw_settings", description="Shows/Hides jaw settings in the panel",default=False)

bpy.types.Object.depth_settings = BoolProperty(
    name = "depth_settings", description="Shows/Hides depth settings in the panel",default=False)

bpy.types.Scene.asset_customizable = BoolProperty(
    name = "asset_customizable", description="Determines whether the asset can be customized or not",default=False)

bpy.types.Scene.supports_armor_trims = BoolProperty(
    name = "supports_armor_trims", description="Determines whether the asset can use armor trims",default=False)

bpy.types.Scene.leggings_half = BoolProperty(
    name = "leggings_half", description="Decides whether the rig will use the main or legs armor texture",default=False)

bpy.types.Scene.has_entries = BoolProperty(
    name = "has_entries", description="Determines whether the asset has entries in it. (Will add each major collection as a valid entry)",default=False)

bpy.types.Object.upgraded_ui = BoolProperty(
    name = "upgraded_ui", description="internal property to decide whether to disable/enable broken features",default=False)

bpy.types.Object.baked_rig = BoolProperty(
    name = "baked_rig", description="internal property that indicates the rig has been baked",default=False)

bpy.types.Object.baked_rig_unused_features = BoolProperty(
    name = "baked_rig_unused_features", description="internal property that indicates the rig has been baked removing unused features",default=False)

bpy.types.Object.baked_rig_eyes = BoolProperty(
    name = "baked_rig_eyes", description="internal property that indicates the rig has been baked removing the eyenode",default=False)

bpy.types.Object.baked_rig_squish = BoolProperty(
    name = "baked_rig_squish", description="internal property that indicates the rig has been baked removing the squish deforms",default=False)

#menu props
ckbox = bpy.types.Object

ckbox.bonelayer_settings = BoolProperty(
    name = "bonelayer_settings",
    default=True
)

ckbox.bone_set_face = BoolProperty(
    name = "bone_set_face",
    default=True
)

ckbox.bone_set_arm = BoolProperty(
    name = "bone_set_arm",
    default=True
)

ckbox.bone_set_leg = BoolProperty(
    name = "bone_set_leg",
    default=True
)

ckbox.bone_set_tweak = BoolProperty(
    name = "bone_set_tweak",
    default=True
)

ckbox.bone_set_misc = BoolProperty(
    name = "bone_set_misc",
    default=False
)

ckbox.gen_set_main = BoolProperty(
    name = "gen_set_main",
    default=True
)

ckbox.gen_set_arm = BoolProperty(
    name = "gen_set_arm",
    default=True
)

ckbox.gen_set_leg = BoolProperty(
    name = "gen_set_leg",
    default=True
)

ckbox.gen_set_snap = BoolProperty(
    name = "gen_set_snap",
    default=False
)

ckbox.mesh_set_bulge = BoolProperty(
    name = "mesh_set_bulge",
    default=True
)

ckbox.mesh_set_squish = BoolProperty(
    name = "mesh_set_squish",
    default=True
)

ckbox.mesh_set_taper = BoolProperty(
    name = "mesh_set_taper",
    default=True
)

ckbox.mesh_set_face = BoolProperty(
    name = "mesh_set_face",
    default=True
)

ckbox.mesh_set_deform = BoolProperty(
    name = "mesh_set_deform",
    default=True
)

ckbox.mat_set_iris = BoolProperty(
    name = "mat_set_iris",
    default=True
)

ckbox.mat_set_pupil = BoolProperty(
    name = "mat_set_iris",
    default=True
)

ckbox.mat_set_sparkle = BoolProperty(
    name = "mat_set_sparkle",
    default=True
)

ckbox.face_style_settings = BoolProperty(
    name="face_style_settings",
    default=True
)

ckbox.workflow_settings = BoolProperty(
    name="workflow_settings",
    default=True
)

ckbox.ik_settings = BoolProperty(
    name="ik_settings",
    default=True
)

ckbox.influence_settings = BoolProperty(
    name="influence_settings",
    default=True
)

ckbox.texture_settings = BoolProperty(
    name="texture_settings",
    default=True
)

ckbox.sss_settings = BoolProperty(
    name="sss_settings",
    default=True
)

ckbox.pupil_bright = BoolProperty(
    name="pupil_bright",
    description="Adds a brigher section to the pupil",
    default=True
)

ckbox.flip_pupil_bright = BoolProperty(
    name="flip_pupil_bright",
    description="Flips the brighter section added to the pupil",
    default=False
)

ckbox.advanced_button_settings = BoolProperty(
    name="advanced_button_settings",
    default=False
)

ckbox.advanced_guide = BoolProperty(
    name="advanced_guide",
    default=False
)

ckbox.update_manager = BoolProperty(
    name="update_manager",
    default=False
)

ckbox.setting_data_manager = BoolProperty(
    name="setting_data_manager",
    default=False
)

ckbox.backup_data_manager = BoolProperty(
    name="backup_data_manager",
    default=False
)

ckbox.confirm_ice_cube_reset = BoolProperty(
    name="confirm_ice_cube_reset",
    description="Enables the ability to completely reset Ice Cube to default",
    default=False
)

ckbox.enable_control_linking = BoolProperty(
    name="enable_control_linking",
    description="Links certain bone layers and their respective controls such as fingers, enabled by default",
    default=True
)

ckbox.baking_data_manager = BoolProperty(
    name="baking_data_manager",
    default=False
)

ckbox.confirm_rig_bake = BoolProperty(
    name="confirm_rig_bake",
    description="Enables the ability to bake the rig, EXTREMELY DESTRUCTIVE",
    default=False
)

ckbox.bake_all_unused_features = BoolProperty(
    name="bake_all_unused_features",
    description="Bakes all unused features on the rig, recommended for performance BUT locks you out of customizing the rig more in the future",
    default=False
)

ckbox.bake_eye_textures = BoolProperty(
    name="bake_eye_textures",
    description="Bakes the eye textures removing the eye node and converting it into an image file, requires a save location",
    default=False
)

ckbox.split_eye_bakes = BoolProperty(
    name="split_eye_bakes",
    description="Used if you have multi colored eyes, will use two images for baking instead of just one",
    default=False
)

global_rig_baked = False
global_parent_half = False
update_available = False




#Sring Prop


#Int Prop

bpy.types.Object.breastshape = IntProperty(
name="breast_shape", description="Extends the chest down one pixel", default=0, min=0, max=1)

bpy.types.Object.eye_bake_resolution = IntProperty(
name="eye_bake_resolution", description="Final resolution for the baked eye texture", default=512, min=256, max=1024)

#Float Prop

bpy.types.Object.jaw_strength = FloatProperty(
name="jaw_strength", description="Changes the influence of the jaw", default=1, min=0, max=1)

bpy.types.Object.bevelmouthstrength = FloatProperty(
name="bevelmouthstrength", description="Changes the strength of the bevel", default=1, min=0, max=1)

bpy.types.Object.leg_taper_strength = FloatProperty(
name="leg_taper_strength", description="Changes the strength of leg taper", default=0, min=-1, max=1)

bpy.types.Object.hip = FloatProperty(
name="hip", description="Changes the hip size", default=0, min=0 ,max=1.5)

bpy.types.Object.upperbodywidth = FloatProperty(
name="upperbodywidth", description="Enables body deforms", default=0, min=0 ,max=1)

bpy.types.Object.lowerbodywidth = FloatProperty(
name="lowerbodywidth", description="Enables body deforms", default=0, min=-1 ,max=1)

bpy.types.Object.bulge_arm_r = FloatProperty(
name="bulge_arm_r", description="Rounds out the limb to give a smoother look", default=0, min=0, max=1)

bpy.types.Object.bulge_arm_l = FloatProperty(
name="bulge_arm_l", description="Rounds out the limb to give a smoother look", default=0, min=0, max=1)

bpy.types.Object.bulge_leg_r = FloatProperty(
name="bulge_leg_r", description="Rounds out the limb to give a smoother look", default=0, min=0, max=1)

bpy.types.Object.bulge_leg_l = FloatProperty(
name="bulge_leg_l", description="Rounds out the limb to give a smoother look", default=0, min=0, max=1)

bpy.types.Object.eyebrowheight = FloatProperty(
name="eyebrowheight", description="Changes the height of the eyebrows", default=0, min=-.5 ,max=1)

bpy.types.Object.eyebrowlength = FloatProperty(
name="eyebrowlength", description="Changes the length of the eyebrows", default=0, min=-1 ,max=1)

bpy.types.Object.eyebrowtaper1 = FloatProperty(
name="eyebrowtaper1", description="Changes the taper of the eyebrows", default=0, min=-.5 ,max=1)

bpy.types.Object.eyebrowtaper2 = FloatProperty(
name="eyebrowtaper2", description="Changes the taper of the eyebrows", default=0, min=-.5 ,max=1)

bpy.types.Object.leg_taper_strength2 = FloatProperty(
name="leg_taper_strength2", description="Changes the strength of leg taper upper", default=0, min=-1, max=1)

bpy.types.Object.armtaper = FloatProperty(
name="armtaper", description="Changes the strength of arm upper", default=0, min=-1, max=1)

bpy.types.Object.armtaperlower = FloatProperty(
name="armtaperlower", description="Changes the strength of arm lower", default=0, min=-1, max=1)

bpy.types.Object.bodybulge = FloatProperty(
    name="bodybulge", description="Rounds out the body to give a smoother look", default=0, min=0, max=1)

bpy.types.Object.eyedepth = FloatProperty(
    name="eyedepth", description="Controls how much of a 2D/3D effect the eyes have", default=0, min=-1, max=1)

bpy.types.Object.mouthdepth = FloatProperty(
    name="mouthdepth", description="Controls how much of a 2D/3D effect the mouth has", default=0, min=-1, max=1)

bpy.types.Object.innermouthdepth = FloatProperty(
    name="innermouthdepth", description="Used to fix clipping with the inner mouth and the body", default=0, min=0, max=1)

bpy.types.Object.breastsize = FloatProperty(
    name="breastsize", description="Controls the chest size", default=0, min=0, max=2)
    
bpy.types.Object.breastweight = FloatProperty(
    name="breastweight", description="Moves the point of the chest downwards to look more natural", default=0, min=0, max=1)

bpy.types.Object.bodytopround = FloatProperty(
    name="bodytopround", description="Rounds the top of the body", default=0, min=0, max=2)

bpy.types.Object.eye_influence = FloatProperty(
    name="eye_influence", description="Controls how much the eyes should be influenced by the eye controls", default=0, min=0, max=1)

bpy.types.Object.eyebrow_influence = FloatProperty(
    name="eyebrow_influence", description="Controls how much the eyes should be influenced by the eyebrow controls", default=0, min=0, max=1)

bpy.types.Object.mouth_influence = FloatProperty(
    name="mouth_influence", description="Controls how much the eyes should be influenced by the mouth controls", default=0, min=0, max=1)

bpy.types.Object.squish_arm_r = FloatProperty(
name="squish_arm_r", description="Allows the limb to sqaush and stretch in a cartoony way", default=0, min=0, max=1)

bpy.types.Object.squish_arm_l = FloatProperty(
name="squish_arm_l", description="Allows the limb to sqaush and stretch in a cartoony way", default=0, min=0, max=1)

bpy.types.Object.squish_leg_r = FloatProperty(
name="squish_leg_r", description="Allows the limb to sqaush and stretch in a cartoony way", default=0, min=0, max=1)

bpy.types.Object.squish_leg_l = FloatProperty(
name="squish_leg_l", description="Allows the limb to sqaush and stretch in a cartoony way", default=0, min=0, max=1)

bpy.types.Object.squish_body = FloatProperty(
name="squish_body", description="Allows the body to sqaush and stretch in a cartoony way", default=0, min=0, max=1)

bpy.types.Object.squish_head = FloatProperty(
name="squish_head", description="Allows the head to sqaush and stretch in a cartoony way", default=0, min=0, max=1)

bpy.types.Object.teeth_curve = FloatProperty(
name="teeth_curve", description="Curves the teeth inwards to create a nicer shade", default=0, min=0, max=1)

bpy.types.Object.UI_Scale = FloatProperty(
name="UI_Scale", description="Scales the main UI", default=1, min=0.8, max=3)

#Enum Prop 

bpy.types.Object.armtype_enum = EnumProperty(
    name = "Changes the arm width",
    default = 'one',
    items = [('one', getLanguageTranslation("ice_cube.ui.props.enum.steve"), '4x4'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.alex"), '4x3'),
             ('three', getLanguageTranslation("ice_cube.ui.props.enum.thin"), '3x3')
             ],
    update=armtype_update)

bpy.types.Object.main_panel_switcher = EnumProperty(
    name = "main_panel_switcher",
    default = 'style',
    items = [('style', getLanguageTranslation("ice_cube.ui.props.enum.style"), 'Main Style Settings'),
             ('controls', getLanguageTranslation("ice_cube.ui.props.enum.controls"), 'Control Settings'),
             ('materials', getLanguageTranslation("ice_cube.ui.props.enum.materials"), 'Material Settings'),
             ('advanced',getLanguageTranslation("ice_cube.ui.props.enum.advanced"),'Advanced Settings')
             ])

bpy.types.Object.style_menu_switcher = EnumProperty(
    name = "style_menu_switcher",
    default = 'rig',
    items = [('rig', getLanguageTranslation("ice_cube.ui.props.enum.rig_style"), 'Rig Style Settings'),
             ('mesh', getLanguageTranslation("ice_cube.ui.props.enum.mesh_style"), 'Mesh Style Settings')
             ])

bpy.types.Object.material_menu_switcher = EnumProperty(
    name = "material_menu_switcher",
    default = 'skin',
    items = [('skin', getLanguageTranslation("ice_cube.ui.props.enum.skin"), 'Skin Material Settings'),
             ('eyes', getLanguageTranslation("ice_cube.ui.props.enum.eyes"), 'Eye Material Settings'),
             ('misc', getLanguageTranslation("ice_cube.ui.props.enum.misc"), 'Misc Material Settings')
             ])

bpy.types.Object.advanced_menu_switcher = EnumProperty(
    name = "advanced_menu_switcher",
    default = 'dlc',
    items = [('dlc', getLanguageTranslation("ice_cube.ui.props.enum.dlc"), 'DLC Settings'),
             ('parenting', getLanguageTranslation("ice_cube.ui.props.enum.parenting"), 'Parenting Settings'),
             ('system', getLanguageTranslation("ice_cube.ui.props.enum.system"), 'System Settings')
             ])

bpy.types.Object.gradient_color_eye = EnumProperty(
    name = "gradient_color_eye",
    default = 'color',
    items = [('color', getLanguageTranslation("ice_cube.ui.props.enum.colors"), 'Uses the default 4 color options for eyes'),
             ('gradient', getLanguageTranslation("ice_cube.ui.props.enum.gradient"), 'Uses a gradient for the eyes'),
             ('texture', getLanguageTranslation("ice_cube.ui.props.enum.texture"), 'Uses a texture for the eyes')
             ])
             
bpy.types.Object.ipaneltab1 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', 'Main', 'Contains general settings'),
             ('two', 'Customization', 'Contains customizations settings'),
             ('three', 'Materials', 'Material Customization'),
             ('four', 'Advanced', 'Only for advanced users')
             ])
             
bpy.types.Object.ipaneltab2 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', 'Bone Layers', 'Toggles bone visibility based on layer'),
             ('two', 'General Settings', 'Basic settings for the rig')
             ])
             
bpy.types.Object.ipaneltab3 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', 'General', 'General Customizations'),
             ('two', 'Mesh', 'Mesh Customizations'),
             ('three', 'Misc', 'Misc page')
             ])
             
bpy.types.Object.ipaneltab4 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', 'Skin', 'Skin Materials'),
             ('two', 'Eyes', 'Eye Materials'),
             ('three', 'Misc', 'Misc')
             ])
             
bpy.types.Object.ipaneltab5 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', 'DLC', 'The DLC management menu'),
             ('two', 'Parenting', 'The advanced parenting panel'),
             ('three', 'Updates', 'A panel dedicated to managing downloads'),
             ('four', 'Misc', 'The misc functions panel')
             ])

bpy.types.Object.ipaneltab6 = EnumProperty(
    name = "Asset/Preset Switcher",
    default = 'two',
    items = [('one', getLanguageTranslation("ice_cube.ui.props.enum.assets"), 'Asset appending menu'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.presets"), 'Preset appending menu')
             ])

bpy.types.Scene.append_tab_global = EnumProperty(
    name = "Append Type",
    default = 'two',
    items = [('one', getLanguageTranslation("ice_cube.ui.props.enum.assets"), 'Asset appending menu'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.presets"), 'Preset appending menu')
             ])

bpy.types.Object.ipaneltab7 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', getLanguageTranslation("ice_cube.ui.props.enum.exporting"), 'Export Settings'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.importing"), 'Import Settings')
             ])

bpy.types.Object.bendstyle = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', getLanguageTranslation("ice_cube.ui.props.enum.sharp_bends"), 'Sharp bends on arms and legs'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.smooth_bends"), 'Smooth bends on arms and legs')
             ])
             
bpy.types.Object.arm_ik_parent_r = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('zero', getLanguageTranslation("ice_cube.ui.props.enum.none"), 'IK PARENT'),
             ('one', getLanguageTranslation("ice_cube.ui.props.enum.root"), 'IK PARENT'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.waist"), 'IK PARENT'),
             ('three', getLanguageTranslation("ice_cube.ui.props.enum.torso"), 'IK PARENT')
             ])

bpy.types.Object.arm_ik_parent_l = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('zero', getLanguageTranslation("ice_cube.ui.props.enum.none"), 'IK PARENT'),
             ('one', getLanguageTranslation("ice_cube.ui.props.enum.root"), 'IK PARENT'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.waist"), 'IK PARENT'),
             ('three', getLanguageTranslation("ice_cube.ui.props.enum.torso"), 'IK PARENT')
             ])

bpy.types.Object.dlc_menu_switcher = EnumProperty(
    name = "DLC Menu Switcher",
    default = 'one',
    items = [
             ('one', getLanguageTranslation("ice_cube.ui.props.enum.append"), 'Append Downloaded Asset'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.download"), 'Download New Asset'),
             ('three', getLanguageTranslation("ice_cube.ui.props.enum.generate"), 'Generate Asset Pack')
             ])

bpy.types.Object.emissioneye = EnumProperty(
    name = "emissioneye",
    default= 'one',
    items = [
             ('one', getLanguageTranslation("ice_cube.ui.props.enum.both_eyes"), 'Gives both eyes emission'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.right_eye"), 'Only the right eye glows'),
             ('three', getLanguageTranslation("ice_cube.ui.props.enum.left_eye"), 'Only the left eye glows')
             ]
)

bpy.types.Object.mouthtypes = EnumProperty(
    name = "mouthtypes",
    default= 'one',
    items = [
             ('one', getLanguageTranslation("ice_cube.ui.props.enum.ice_cube"), 'Uses the default Ice Cube mouth shape'),
             ('two', getLanguageTranslation("ice_cube.ui.props.enum.mineimator"), 'Uses a \'Skibbz\' like mouth shape from Mine-Imator'),
             ('three', getLanguageTranslation("ice_cube.ui.props.enum.square"), 'Uses a classical Zamination styled square mouth')
             ]
)

bpy.types.Object.icecube_menu_version = EnumProperty(
    name = "icecube_menu_version",
    default= 'new',
    items = [
             ('new', getLanguageTranslation("ice_cube.ui.props.enum.new_ui"), '1.5.2+'),
             ('classic', getLanguageTranslation("ice_cube.ui.props.enum.classic_ui"), '-1.5.1')
             ]
)

bpy.types.Scene.armor_trim_pattern = EnumProperty(
        name = "Asset Entries",
        default= 'none',
        items = [
            ('none', getLanguageTranslation("ice_cube.ui.props.enum.none"),'description none'),
            ('Coast', getLanguageTranslation("ice_cube.ui.props.enum.trim_coast"),'Applies the Coast trim'),
            ('Dune', getLanguageTranslation("ice_cube.ui.props.enum.trim_dune"),'Applies the Dune trim'),
            ('Eye', getLanguageTranslation("ice_cube.ui.props.enum.trim_eye"),'Applies the Eye trim'),
            ('Host', getLanguageTranslation("ice_cube.ui.props.enum.trim_host"),'Applies the Host trim'),
            ('Raiser', getLanguageTranslation("ice_cube.ui.props.enum.trim_raiser"),'Applies the Raiser trim'),
            ('Rib', getLanguageTranslation("ice_cube.ui.props.enum.trim_rib"),'Applies the Rib trim'),
            ('Sentry', getLanguageTranslation("ice_cube.ui.props.enum.trim_sentry"),'Applies the Sentry trim'),
            ('Shaper', getLanguageTranslation("ice_cube.ui.props.enum.trim_shaper"),'Applies the Shaper trim'),
            ('Silence', getLanguageTranslation("ice_cube.ui.props.enum.trim_silence"),'Applies the Silence trim'),
            ('Snout', getLanguageTranslation("ice_cube.ui.props.enum.trim_snout"),'Applies the Snout trim'),
            ('Spire', getLanguageTranslation("ice_cube.ui.props.enum.trim_spire"),'Applies the Spire trim'),
            ('Tide', getLanguageTranslation("ice_cube.ui.props.enum.trim_tide"),'Applies the Tide trim'),
            ('Vex', getLanguageTranslation("ice_cube.ui.props.enum.trim_vex"),'Applies the Vex trim'),
            ('Ward', getLanguageTranslation("ice_cube.ui.props.enum.trim_ward"),'Applies the Ward trim'),
            ('Wayfinder', getLanguageTranslation("ice_cube.ui.props.enum.trim_wayfinder"),'Applies the Wayfinder trim'),
            ('Wild', getLanguageTranslation("ice_cube.ui.props.enum.trim_wild"),'Applies the Wild trim')
            ]
        )

bpy.types.Scene.armor_trim_material = EnumProperty(
        name = "Asset Entries",
        default= 'Amethyst',
        items = [
            ('Amethyst', getLanguageTranslation("ice_cube.ui.props.enum.mat_amethyst"),'Sets the trim material to Amethyst'),
            ('Copper', getLanguageTranslation("ice_cube.ui.props.enum.mat_copper"),'Sets the trim material to Copper'),
            ('Diamond', getLanguageTranslation("ice_cube.ui.props.enum.mat_diamond"),'Sets the trim material to Diamond'),
            ('Emerald', getLanguageTranslation("ice_cube.ui.props.enum.mat_emerald"),'Sets the trim material to Emerald'),
            ('Gold', getLanguageTranslation("ice_cube.ui.props.enum.mat_gold"),'Sets the trim material to Gold'),
            ('Iron', getLanguageTranslation("ice_cube.ui.props.enum.mat_iron"),'Sets the trim material to Iron'),
            ('Lapis', getLanguageTranslation("ice_cube.ui.props.enum.mat_lapis"),'Sets the trim material to Lapis'),
            ('Netherite', getLanguageTranslation("ice_cube.ui.props.enum.mat_netherite"),'Sets the trim material to Netherite'),
            ('Quartz', getLanguageTranslation("ice_cube.ui.props.enum.mat_quartz"),'Sets the trim material to Quartz'),
            ('Redstone', getLanguageTranslation("ice_cube.ui.props.enum.mat_redstone"),'Sets the trim material to Redstone')
            ]
        )

#string properties
bpy.types.Scene.minecraft_username = StringProperty(name="username", description="username slot", default="")

bpy.types.Object.backup_name = StringProperty(name="backup_name", description="Backup Name", default="")

bpy.types.Object.dlc_name_load = StringProperty(name="dlc_name_load", description="DLC Name Load", default="")

bpy.types.Object.export_settings_filepath = StringProperty(
    name="export_settings_filepath",
    description="Defines a location to export settings to",
    subtype='DIR_PATH',
    default="")

bpy.types.Object.import_settings_filepath = StringProperty(
    name="export_settings_filepath",
    description="Defines a location to export settings to",
    subtype='FILE_PATH',
    default="")

bpy.types.Object.export_settings_name = StringProperty(
    name="export_settings_name",
    description="Defines a name for the export settings",
    default="")

bpy.types.Object.target_thumbnail_generate = StringProperty(
    name="target_thumbnail_generate",
    description="Defines a png file to generate an asset pack from",
    subtype='FILE_PATH',
    default="")

bpy.types.Object.asset_pack_name = StringProperty(
    name="asset_pack_name",
    description="Defines a name to use when generating the asset pack",
    default="Pack Name")

bpy.types.Object.entry_name_asset = StringProperty(
    name="entry_name_asset",
    description="Defines a name for the asset pack entry",
    default="Entry Name")

bpy.types.Object.asset_author = StringProperty(
    name="asset_author",
    description="Defines a name for the author in settings.json",
    default="Your Name")

bpy.types.Object.asset_version = StringProperty(
    name="asset_version",
    description="Defines a version number in settings.json",
    default="1.0.0")

bpy.types.Object.baked_version_filepath = StringProperty(
    name="baked_version_filepath",
    description="Defines a filepath for the baked version",
    subtype='FILE_PATH',
    default="")

bpy.types.Object.import_icpreset_file = StringProperty(
    name="import_icpreset_file",
    description="Targets a .icpreset file to import",
    subtype='FILE_PATH',
    default="")

bpy.types.Object.export_icpreset_file = StringProperty(
    name="export_icpreset_file",
    description="Targets a location to generate the .icpreset file",
    subtype='DIR_PATH',
    default="")

bpy.types.Scene.target_thumbnail_generate = StringProperty(
    name="target_thumbnail_generate",
    description="Defines a png file to generate an asset pack from",
    subtype='FILE_PATH',
    default="")

bpy.types.Scene.asset_pack_name = StringProperty(
    name="asset_pack_name",
    description="Defines a name to use when generating the asset pack",
    default="Pack Name")

bpy.types.Scene.entry_name_asset = StringProperty(
    name="entry_name_asset",
    description="Defines a name for the asset pack entry",
    default="Entry Name")

bpy.types.Scene.asset_author = StringProperty(
    name="asset_author",
    description="Defines a name for the author in settings.json",
    default="Your Name")

bpy.types.Scene.asset_version = StringProperty(
    name="asset_version",
    description="Defines a version number in settings.json",
    default="1.0.0")

bpy.types.Scene.materialType = StringProperty(
    name="materialType",
    description="Defines which material the asset is (Leave default unless you know what you're doing)",
    default="default")




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