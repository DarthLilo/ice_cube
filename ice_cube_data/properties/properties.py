import bpy

from bpy.props import (StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        EnumProperty,
                        )  
                 

#war crimewar crimewar crimewar crimewar crimewar crime fuck you

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

bpy.types.Object.squaremouth = BoolProperty(
name="squaremouth", description="Changes the mouth transforms to it more rounded on the edges.", default=False)

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

global_rig_baked = False
global_parent_half = False
update_available = False




#Sring Prop


#Int Prop

bpy.types.Object.squish_arm_r = IntProperty(
name="squish_arm_r", description="Right Arm Squish", default=0, min=0, max=1)

bpy.types.Object.squish_arm_l = IntProperty(
name="squish_arm_l", description="Left Arm Squish", default=0, min=0, max=1)

bpy.types.Object.squish_leg_r = IntProperty(
name="squish_leg_r", description="Right Leg Squish", default=0, min=0, max=1)

bpy.types.Object.squish_leg_l = IntProperty(
name="squish_leg_l", description="Left Leg Squish", default=0, min=0, max=1)

bpy.types.Object.squish_body = IntProperty(
name="squish_body", description="Body Squish", default=0, min=0, max=1)

bpy.types.Object.squish_head = IntProperty(
name="squish_head", description="Head Squish", default=0, min=0, max=1)

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
name="eyebrowheight", description="Changes the size of the eyebrows", default=0, min=-.5 ,max=1)

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

bpy.types.Object.breath = FloatProperty(
    name="breath", description="Deforms the body to look like its breathing", default=0, min=0, max=2)

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
             ('three', 'Downloads', 'A panel dedicated to managing downloads'),
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