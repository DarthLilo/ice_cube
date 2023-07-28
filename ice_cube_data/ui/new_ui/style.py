#Libraries
import bpy

from ice_cube_data.utils.ui_tools import button_toggle

def newEnum(layout,display,source,prop,expand):
    if display != "":
        layout.label(text=display)
    layout.prop(data=source,property=prop,expand=expand)

def rig_style_ui(self, context, layout, obj, icon,scale):
    box = layout.box()
    pcoll = icon["main"]
    box.label(text= "Rig Style Options", icon= 'GREASEPENCIL')
    b = box.row(align=True)
    b.scale_y=scale
    style_box_1 = b.box()
    sb1_row = style_box_1.row(align=True)
    sb1_row.scale_y = 1.1
    newEnum(sb1_row,"",obj,"bendstyle",True)
    if obj.baked_rig: sb1_row.enabled = False
    sb1_row = style_box_1.row(align=True)
    sb1_row.scale_y = 1.1
    if obj.get("armtype_enum") == 0:
        armtype_icon = pcoll["Steve"]
    elif obj.get("armtype_enum") == 1:
        armtype_icon = pcoll["Alex"]
    elif obj.get("armtype_enum") == 2:
        armtype_icon = pcoll["DarthLilo"]
    sb1_row.label(text="",icon_value=armtype_icon.icon_id)
    sb1_row.prop(data=obj,property="armtype_enum",expand=True)
    sb1_row.label(text="",icon_value=armtype_icon.icon_id)
    if obj.baked_rig: sb1_row.enabled = False
    sb1_row = style_box_1.row(align=True)
    sb1_row.scale_y = 1.2
    fingers_col = sb1_row.column(align=True)
    fingers_col.prop(obj,"fingers_r",text="Fingers R",toggle=True)
    thumbfill_r = fingers_col.row(align=True)
    thumbfill_r.scale_y=1
    fingers_col = sb1_row.column(align=True)
    fingers_col.prop(obj,"fingers_l",text="Fingers L",toggle=True)
    thumbfill_l = fingers_col.row(align=True)
    thumbfill_l.scale_y=1
    if obj.get("fingers_r"):
        thumbfill_r.prop(obj,"thumbfill_R",text="Thumbfill",toggle=True)
    if obj.get("fingers_l"):
        thumbfill_l.prop(obj,"thumbfill_L",text="Thumbfill",toggle=True)
    sb1_row = style_box_1.row(align=True)
    sb1_row.scale_y = 1.3
    sb1_row.prop(obj,"facerig",text="Face Rig",toggle=True)
    if obj.get("facerig"):
        sb1_row = style_box_1.row(align=True)
        facestyle = sb1_row.box()
        sb2_row = facestyle.row(align=True)
        face_style_box = sb2_row.box()
        face_style_row = face_style_box.row(align=True)
        face_style_row.label(text="Face Style Settings",icon='USER')
        if button_toggle(obj,face_style_row,"face_style_settings"):
            face_style_row = face_style_box.row(align=True)
            newEnum(face_style_row,"",obj,"mouthtypes",True)
            face_style_row = face_style_box.row(align=True)

            checkbox_box = face_style_row.box()
            cbb_row = checkbox_box.row(align=True)
            cbb_row.scale_y=1.3
            cbb_row_eyelash = cbb_row.row(align=True)
            cbb_row_eyelash.prop(obj,"eyelashes",text="Eyelashes")
            if obj.baked_rig: cbb_row_eyelash.enabled = False
            cbb_row.prop(obj,"mouthrotate",text="Mouth Rotate")
            cbb_row = checkbox_box.row(align=True)
            cbb_row.scale_y=1.3
            cbb_row.prop(obj,"tongue",text="Tongue")
            cbb_row.prop(obj,"line_mouth",text="Cartoon Mouth")
            cbb_row = checkbox_box.row(align=True)
            cbb_row.scale_y=1.3
            cbb_row.prop(obj,"dynamichair",text="Dynamic Hair")
            if obj.baked_rig: cbb_row.enabled = False
        
        sb2_row = facestyle.row(align=True)
        sb2_row = facestyle.row(align=True)
        sb2_row.scale_y = 0.9
        teeth_box = sb2_row.box()
        teeth_row=teeth_box.row(align=True)
        teeth_row.label(text="Teeth",icon='NOCURVE')
        if button_toggle(obj,teeth_row,"teeth_settings"):
            teeth_row=teeth_box.row(align=True)
            teeth_col = teeth_row.column(align=True)
            teeth_col.scale_y=1.35
            teeth_col.prop(obj,"teeth_cartoon",text="Cartoon",toggle=True)
            teeth_col.prop(obj,"teeth_curve",text="Curvature",slider=True)
            teeth_col = teeth_row.column(align=True)
            teeth_col.scale_y=1.35
            teeth_col.prop(obj,"teeth_bool",text="Boolean",toggle=True)
            teeth_col.prop(obj,"teeth_follow",text="Follow",toggle=True)
        sb2_row = facestyle.row(align=True)
        sb2_row = facestyle.row(align=True)
        sb2_row.scale_y = 0.9
        bevel_box = sb2_row.box()
        bevel_row = bevel_box.row(align=True)
        bevel_row.label(text="Bevels",icon='MOD_BEVEL')
        if button_toggle(obj,bevel_row,"bevel_settings"):
            bevel_row=bevel_box.row(align=True)
            bevel_col = bevel_row.column(align=True)
            bevel_col.scale_y=1.2
            bevel_col.prop(obj,"bevelmouth",text="Mouth",toggle=True)
            bevel_col = bevel_row.column(align=True)
            bevel_col.scale_y=1.2
            bevel_col.prop(obj,"bevelmouthstrength",text="Strength",slider=True)
            
        sb2_row = facestyle.row(align=True)
        sb2_row = facestyle.row(align=True)
        sb2_row.scale_y = 0.9
        jaw_box = sb2_row.box()
        jaw_row = jaw_box.row(align=True)
        jaw_row.label(text="Jaw",icon='MESH_MONKEY')
        if button_toggle(obj,jaw_row,"jaw_settings"):
            jaw_row = jaw_box.row(align=True)
            jaw_row.scale_y=1.35
            if obj.get("jaw"):
                jawtext = "Enabled"
            else:
                jawtext = "Disabled"
            jaw_row.prop(obj,"jaw",text=jawtext,toggle=True)
            jaw_row.prop(obj,"round_jaw",text="Round",toggle=True)
            jaw_row = jaw_box.row(align=True)
            jaw_row.prop(obj,"jaw_strength",text="Strength",slider=True)
        sb2_row = facestyle.row(align=True)
        sb2_row = facestyle.row(align=True)
        sb2_row.scale_y = 0.9
        depth_box = sb2_row.box()
        depth_row = depth_box.row(align=True)
        depth_row.label(text="Depth",icon='NODE_TEXTURE')
        if button_toggle(obj,depth_row,"depth_settings"):
            depth_row = depth_box.row(align=True)
            depth_col = depth_row.column(align=True)
            depth_col.scale_y=1.1
            depth_col.prop(obj,"eyedepth",text="Eye",slider=True)
            depth_col.prop(obj,"mouthdepth",text="Mouth",slider=True)
            depth_col.prop(obj,"innermouthdepth",text="Inner Mouth",slider=True)
        sb2_row = facestyle.row(align=True)
        sb2_row = facestyle.row(align=True)
        sb2_row.scale_y = 1.2
        sb2_row.operator("append.emotion")

def mesh_style_ui(self,context,layout,obj,icon,scale):
    box = layout.box()
    pcoll = icon["main"]
    box.label(text= "Mesh Style Options", icon= 'MESH_ICOSPHERE')
    b = box.row(align=True)
    b.scale_y=scale
    style_box_1 = b.box()
    sb1_row = style_box_1.row(align=True)
    bulge_box = sb1_row.box()
    if obj.baked_rig_unused_features: bulge_box.enabled = False
    bulge_row = bulge_box.row(align=True)
    bulge_row.label(text="Bulge",icon='MESH_CYLINDER')
    if button_toggle(obj,bulge_row,"mesh_set_bulge"):
        bulge_row = bulge_box.row(align=True)
        bulge_row.prop(obj,"bodybulge",text="👕 Body",slider=True)
        bulge_row = bulge_box.row(align=True)
        bulge_col = bulge_row.column(align=True)
        bulge_col.prop(obj,"bulge_arm_r",text="🦾 Right Arm",slider=True)
        bulge_col.prop(obj,"bulge_leg_r",text="🦿 Right Leg",slider=True)
        bulge_col = bulge_row.column(align=True)
        bulge_col.prop(obj,"bulge_arm_l",text="🦾 Left Arm",slider=True)
        bulge_col.prop(obj,"bulge_leg_l",text="🦿 Left Leg",slider=True)
    sb1_row = style_box_1.row(align=True)
    squish_box = sb1_row.box()
    if obj.baked_rig_squish: squish_box.enabled = False
    squish_row = squish_box.row(align=True)
    squish_row.label(text="Squish",icon='CON_STRETCHTO')
    if button_toggle(obj,squish_row,"mesh_set_squish"):
        squish_row = squish_box.row(align=True)
        squish_row.prop(obj,"squish_head",text="😑 Head",slider=True)
        squish_row.prop(obj,"squish_body",text="👕 Body",slider=True)
        squish_row = squish_box.row(align=True)
        squish_col = squish_row.column(align=True)
        squish_col.prop(obj,"squish_arm_r",text="🦾 Right Arm",slider=True)
        squish_col.prop(obj,"squish_leg_r",text="🦿 Right Leg",slider=True)
        squish_col = squish_row.column(align=True)
        squish_col.prop(obj,"squish_arm_l",text="🦾 Left Arm",slider=True)
        squish_col.prop(obj,"squish_leg_l",text="🦿 Left Leg",slider=True)
    sb1_row = style_box_1.row(align=True)
    deform_box = sb1_row.box()
    if obj.baked_rig_unused_features: deform_box.enabled = False
    deform_row = deform_box.row(align=True)
    deform_row.label(text="Deforms",icon='MOD_SIMPLEDEFORM')
    if button_toggle(obj,deform_row,"mesh_set_deform"):
        deform_row = deform_box.row(align=True)
        deform_row.label(text="Taper:",icon='MOD_DECIM')
        deform_row = deform_box.row(align=True)
        deform_col = deform_row.column(align=True)
        deform_col_row = deform_col.row(align=True)
        deform_col_row.prop(obj,"armtaper",text="🦾 Upper Arms",slider=True)
        deform_col_row.prop(obj,"armtaperlower",text="🦾 Lower Arms",slider=True)
        deform_col_row = deform_col.row(align=True)
        deform_col_row.prop(obj,"leg_taper_strength",text="🦿 Lower Legs",slider=True)
        deform_col_row.prop(obj,"leg_taper_strength2",text="🦿 Upper Legs",slider=True)
        deform_row = deform_box.row(align=True)
        deform_row = deform_box.row(align=True)
        deform_row.label(text="Body Mods:",icon='MOD_REMESH')
        deform_row = deform_box.row(align=True)
        deform_col = deform_row.column(align=True)
        deform_col.prop(obj,"hip",text="Hip",slider=True)
        deform_col.prop(obj,"bodytopround",text="Round Top",slider=True)
        deform_col = deform_row.column(align=True)
        deform_col.prop(obj,"upperbodywidth",text="Upper Width",slider=True)
        deform_col.prop(obj,"lowerbodywidth",text="Lower Width",slider=True)
        deform_row = deform_box.row(align=True)
        deform_row = deform_box.row(align=True)
        deform_row.label(text="Chest Settings:",icon='SPHERE')
        deform_row = deform_box.row(align=True)
        deform_col = deform_row.column(align=True)
        deform_col_row = deform_col.row(align=True)
        deform_col_row.prop(obj,"breastsize",text="Size",slider=True)
        deform_col_row.prop(obj,"breastweight",text="Weight",slider=True)
        deform_col_row = deform_col.row(align=True)
        deform_col_row.prop(obj,"breastshape",text="Shape",slider=True)
        deform_col_row.prop(obj,"breastswitch",text="Position Bone",toggle=True)
        if obj.get("facerig"):
            deform_row = deform_box.row(align=True)
            deform_row = deform_box.row(align=True)
            deform_row.label(text="Eyebrow Settings:",icon='OUTLINER_OB_CURVES')
            deform_row = deform_box.row(align=True)
            deform_col = deform_row.column(align=True)
            deform_col.prop(obj,"eyebrowheight",text="Height",slider=True)
            deform_col.prop(obj,"eyebrowtaper1",text="Inner Taper",slider=True)
            deform_col = deform_row.column(align=True)
            deform_col.prop(obj,"eyebrowlength",text="Length",slider=True)
            deform_col.prop(obj,"eyebrowtaper2",text="Outer Taper",slider=True)

        
    

    


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