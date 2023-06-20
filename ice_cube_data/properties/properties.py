import bpy

from bpy.props import (StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        EnumProperty,
                        )


# classes



#Bool Prop

bpy.types.Object.r_arm_ik = BoolProperty(
name="r_arm_ik", description="Enables IK for the right arm", default=False)
    
bpy.types.Object.l_arm_ik = BoolProperty(
name="l_arm_ik", description="Enables IK for the left arm", default=False)
    
bpy.types.Object.r_leg_ik = BoolProperty(
name="r_leg_ik", description="Enables IK for the right leg", default=True)
    
bpy.types.Object.l_leg_ik = BoolProperty(
name="l_leg_ik", description="Enables IK for the left leg", default=True)
    
bpy.types.Object.ankle_r = BoolProperty(
name="ankle_r", description="Ankle Right", default=True)
    
bpy.types.Object.ankle_l = BoolProperty(
name="ankle_l", description="Ankle Left", default=True)
    
bpy.types.Object.stretch_leg_r = BoolProperty(
name="stretch_leg_r", description="Leg Stretch Right", default=True)
    
bpy.types.Object.stretch_leg_l = BoolProperty(
name="stretch_leg_l", description="Leg Stretch Left", default=True)
    
bpy.types.Object.stretch_arm_r = BoolProperty(
name="stretch_arm_r", description="Arm Stretch Right", default=False)
    
bpy.types.Object.stretch_arm_l = BoolProperty(
name="stretch_arm_l", description="Arm Stretch Left", default=False)
    
bpy.types.Object.fingers_r = BoolProperty(
name="fingers_r", description="Fingers Right", default=False)
    
bpy.types.Object.fingers_l = BoolProperty(
name="fingers_l", description="Fingers Left", default=False)

bpy.types.Object.wrist_lock_r = BoolProperty(
name="wrist_lock_r", description="Locks the right wrist", default=False)

bpy.types.Object.wrist_lock_l = BoolProperty(
name="wrist_lock_l", description="Locks the left wrist", default=False)

bpy.types.Object.eyelashes = BoolProperty(
name="eyelashes", description="Enables Eyelashes", default=False)

bpy.types.Object.wireframe = BoolProperty(
name="wireframe", description="Enables wireframe view", default=False)

bpy.types.Object.jaw = BoolProperty(
name="jaw", description="Enables the jaw", default=False)

bpy.types.Object.round_jaw = BoolProperty(
name="round_jaw", description="Rounds the jaw", default=False)

bpy.types.Object.bevelmouth = BoolProperty(
name="bevelmouth", description="Enables Bevel Mouth", default=False)

bpy.types.Object.teeth_cartoon = BoolProperty(
name="teeth_cartoon", description="Makes the teeth have bevel", default=False)

bpy.types.Object.antilag = BoolProperty(
name="antilag", description="Makes the rig run better", default=False)

bpy.types.Object.teeth_bool = BoolProperty(
name="teeth_bool", description="Booleans out the teeth past the head mesh", default=False)

bpy.types.Object.tongue = BoolProperty(
name="tongue", description="Enables the tongue", default=False)

bpy.types.Object.facerig = BoolProperty(
name="facerig", description="Enables the face rig", default=True)

bpy.types.Object.leg_deform = BoolProperty(
name="leg_deform", description="Enables leg deforms", default=False)

bpy.types.Object.body_deforms = BoolProperty(
name="body_deforms", description="Enables body deforms", default=False)

bpy.types.Object.dynamichair = BoolProperty(
name="dynamichair", description="Enables Dynamic Hair", default=False)

bpy.types.Object.eyebrowdeform = BoolProperty(
name="eyebrowdeform", description="Enables the eyebrow deforms", default=False)

bpy.types.Object.togglepupil = BoolProperty(
name="togglepupil", description="Toggle Pupil", default=True)

bpy.types.Object.togglegradient = BoolProperty(
name="togglegradient", description="Toggle Gradient", default=False)

bpy.types.Object.togglesparkle1 = BoolProperty(
name="togglesparkle1", description="Toggle Sparkle 1", default=True)

bpy.types.Object.togglesparkle2 = BoolProperty(
name="togglesparkle2", description="Toggle Sparkle 2", default=True)

bpy.types.Object.toggleemission = BoolProperty(
name="toggleemission", description="Toggle Emission", default=True)

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
name="breastswitch", description="Enables bones for controlling chest sizes", default=False)

bpy.types.Object.line_mouth = BoolProperty(
name="line_mouth", description="Show/Hides the cartoon line mouth", default=False)

bpy.types.Object.baked_rig = BoolProperty(
name="baked_rig", description="Decides if the imported rig should be baked or not", default=False)

bpy.types.Object.global_head_rotation = BoolProperty(
name="global_head_rotation", description="Enables/Disables global head rotation", default=False)

bpy.types.Object.prop_clipboard = BoolProperty(
name="prop_clipboard", description="Determines if the settings will be exported to the clipboard or a file", default=False)

bpy.types.Object.R_A_Half = BoolProperty(
    name = "R_A_Half", description="Determines which half of the Right Arm the mesh should be parented to",default=False)

bpy.types.Object.L_A_Half = BoolProperty(
    name = "L_A_Half", description="Determines which half of the Left Arm the mesh should be parented to",default=False)

bpy.types.Object.R_L_Half = BoolProperty(
    name = "R_L_Half", description="Determines which half of the Right Leg the mesh should be parented to",default=False)

bpy.types.Object.L_L_Half = BoolProperty(
    name = "L_L_Half", description="Determines which half of the Left Leg the mesh should be parented to",default=False)

bpy.types.Object.Body_Bend_Half = BoolProperty(
    name = "Body_Bend_Half", description="Determines which half of the Body the mesh should be parented to",default=False)

bpy.types.Object.generate_thumbnail = BoolProperty(
    name = "generate_thumbnail", description="Decides whether to generate a thumbnail in the current scene",default=False)

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


#menu props
ckbox = bpy.types.Object

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


global_rig_baked = False
global_parent_half = False
update_available = False




#Sring Prop


#Int Prop

bpy.types.Object.breastshape = IntProperty(
name="breast_shape", description="Extends the chest down one pixel", default=0, min=0, max=1)

#Float Prop

bpy.types.Object.jaw_strength = FloatProperty(
name="jaw_strength", description="Changes the influence of the jaw", default=1, min=0, max=1)

bpy.types.Object.bevelmouthstrength = FloatProperty(
name="bevelmouthstrength", description="Changes the strength of the bevel", default=1, min=0, max=1)

bpy.types.Object.leg_taper_strength = FloatProperty(
name="leg_taper_strength", description="Changes the strength of leg taper", default=0, min=-1, max=1)

bpy.types.Object.hip = FloatProperty(
name="hip", description="Changes hip strength", default=0, min=0 ,max=1.5)

bpy.types.Object.upperbodywidth = FloatProperty(
name="upperbodywidth", description="Enables body deforms", default=0, min=0 ,max=1)

bpy.types.Object.lowerbodywidth = FloatProperty(
name="lowerbodywidth", description="Enables body deforms", default=0, min=-1 ,max=1)

bpy.types.Object.bulge_arm_r = FloatProperty(
name="bulge_arm_r", description="Right Arm Bulge", default=0, min=0, max=1)

bpy.types.Object.bulge_arm_l = FloatProperty(
name="bulge_arm_l", description="Left Arm Bulge", default=0, min=0, max=1)

bpy.types.Object.bulge_leg_r = FloatProperty(
name="bulge_leg_r", description="Right Leg Bulge", default=0, min=0, max=1)

bpy.types.Object.bulge_leg_l = FloatProperty(
name="bulge_leg_l", description="Left Leg Bulge", default=0, min=0, max=1)

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

bpy.types.Object.bodybulge = FloatProperty(
    name="bodybulge", description="Body Bulge", default=0, min=0, max=1)

bpy.types.Object.eyedepth = FloatProperty(
    name="eyedepth", description="Eye Depth", default=0, min=-1, max=1)

bpy.types.Object.mouthdepth = FloatProperty(
    name="mouthdepth", description="Mouth Depth", default=0, min=-1, max=1)

bpy.types.Object.innermouthdepth = FloatProperty(
    name="innermouthdepth", description="Inner Mouth Depth", default=0, min=0, max=1)

bpy.types.Object.breastsize = FloatProperty(
    name="breastsize", description="Chest Size", default=0, min=0, max=2)
    
bpy.types.Object.breastweight = FloatProperty(
    name="breastweight", description="Chest Weight", default=0, min=0, max=1)

bpy.types.Object.bodytopround = FloatProperty(
    name="bodytopround", description="Rounded Body Top", default=0, min=0, max=2)

bpy.types.Object.eye_influence = FloatProperty(
    name="eye_influence", description="Controls how much the eyes should be influenced by the eye controls", default=0, min=0, max=1)

bpy.types.Object.eyebrow_influence = FloatProperty(
    name="eyebrow_influence", description="Controls how much the eyes should be influenced by the eyebrow controls", default=0, min=0, max=1)

bpy.types.Object.mouth_influence = FloatProperty(
    name="mouth_influence", description="Controls how much the eyes should be influenced by the mouth controls", default=0, min=0, max=1)

bpy.types.Object.squish_arm_r = FloatProperty(
name="squish_arm_r", description="Right Arm Squish", default=0, min=0, max=1)

bpy.types.Object.squish_arm_l = FloatProperty(
name="squish_arm_l", description="Left Arm Squish", default=0, min=0, max=1)

bpy.types.Object.squish_leg_r = FloatProperty(
name="squish_leg_r", description="Right Leg Squish", default=0, min=0, max=1)

bpy.types.Object.squish_leg_l = FloatProperty(
name="squish_leg_l", description="Left Leg Squish", default=0, min=0, max=1)

bpy.types.Object.squish_body = FloatProperty(
name="squish_body", description="Body Squish", default=0, min=0, max=1)

bpy.types.Object.squish_head = FloatProperty(
name="squish_head", description="Head Squish", default=0, min=0, max=1)

bpy.types.Object.teeth_curve = FloatProperty(
name="teeth_curve", description="Teeth Curve", default=0, min=0, max=1)

#Enum Prop 

bpy.types.Object.armtype_enum = EnumProperty(
    name = "Changes the arm width",
    default = 'one',
    items = [('one', 'Steve', '4x4'),
             ('two', 'Alex', '4x3'),
             ('three', 'Thin', '3x3')
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
    name = "haha tab",
    default = 'one',
    items = [('one', 'Assets', 'Asset appending menu'),
             ('two', 'Presets', 'Preset appending menu')
             ])

bpy.types.Object.ipaneltab7 = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', 'Exporting', 'Export Settings'),
             ('two', 'Importing', 'Import Settings')
             ])

bpy.types.Object.bendstyle = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('one', 'Sharp', 'Sharp bends on arms and legs'),
             ('two', 'Smooth', 'Smooth bends on arms and legs')
             ])
             
bpy.types.Object.arm_ik_parent_r = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('zero', 'NONE', 'IK PARENT'),
             ('one', 'Root', 'IK PARENT'),
             ('two', 'Waist', 'IK PARENT'),
             ('three', 'Torso', 'IK PARENT')
             ])

bpy.types.Object.arm_ik_parent_l = EnumProperty(
    name = "haha tab",
    default = 'one',
    items = [('zero', 'NONE', 'IK PARENT'),
             ('one', 'Root', 'IK PARENT'),
             ('two', 'Waist', 'IK PARENT'),
             ('three', 'Torso', 'IK PARENT')
             ])

bpy.types.Object.dlc_menu_switcher = EnumProperty(
    name = "DLC Menu Switcher",
    default = 'one',
    items = [
             ('one', 'Append', 'Append Downloaded Asset'),
             ('two', 'Download', 'Download New Asset'),
             ('three', 'Generate', 'Generate Asset Pack')
             ])

bpy.types.Object.emissioneye = EnumProperty(
    name = "emissioneye",
    default= 'one',
    items = [
             ('one', 'Both', 'Both'),
             ('two', 'Right', 'Right Eye'),
             ('three', 'Left', 'Left Eye')
             ]
)

bpy.types.Object.mouthtypes = EnumProperty(
    name = "mouthtypes",
    default= 'one',
    items = [
             ('one', 'Ice Cube', 'Ice Cube'),
             ('two', 'Mine-Imator', 'Mine-Imator'),
             ('three', 'Square', 'Square')
             ]
)

bpy.types.Object.armor_trim_pattern = EnumProperty(
        name = "Asset Entries",
        default= 'none',
        items = [
            ('none', 'none','description none'),
            ('Coast', 'Coast','Applies the Coast trim'),
            ('Dune', 'Dune','Applies the Dune trim'),
            ('Eye', 'Eye','Applies the Eye trim'),
            ('Host', 'Host','Applies the Host trim'),
            ('Raiser', 'Raiser','Applies the Raiser trim'),
            ('Rib', 'Rib','Applies the Rib trim'),
            ('Sentry', 'Sentry','Applies the Sentry trim'),
            ('Shaper', 'Shaper','Applies the Shaper trim'),
            ('Silence', 'Silence','Applies the Silence trim'),
            ('Snout', 'Snout','Applies the Snout trim'),
            ('Spire', 'Spire','Applies the Spire trim'),
            ('Tide', 'Tide','Applies the Tide trim'),
            ('Vex', 'Vex','Applies the Vex trim'),
            ('Ward', 'Ward','Applies the Ward trim'),
            ('Wayfinder', 'Wayfinder','Applies the Wayfinder trim'),
            ('Wild', 'Wild','Applies the Wild trim')
            ]
        )

bpy.types.Object.armor_trim_material = EnumProperty(
        name = "Asset Entries",
        default= 'Amethyst',
        items = [
            ('Amethyst', 'Amethyst','Sets the trim material to Amethyst'),
            ('Copper', 'Copper','Sets the trim material to Copper'),
            ('Diamond', 'Diamond','Sets the trim material to Diamond'),
            ('Emerald', 'Emerald','Sets the trim material to Emerald'),
            ('Gold', 'Gold','Sets the trim material to Gold'),
            ('Iron', 'Iron','Sets the trim material to Iron'),
            ('Lapis', 'Lapis','Sets the trim material to Lapis'),
            ('Netherite', 'Netherite','Sets the trim material to Netherite'),
            ('Quartz', 'Quartz','Sets the trim material to Quartz'),
            ('Redstone', 'Redstone','Sets the trim material to Redstone')
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