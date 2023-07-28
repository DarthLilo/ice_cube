#Libraries
import bpy

from ice_cube_data.utils.ui_tools import button_toggle
from ice_cube_data.utils.selectors import isRigSelected,mat_holder_func

def newEnum(layout,display,source,prop,expand):
    if display != "":
        layout.label(text=display)
    layout.prop(data=source,property=prop,expand=expand)


def material_skin_ui(self, context, layout, scale):
    obj = context.object
    scene = context.scene


    #getting valid materials

    #material codes
        # skin
        # eyes
        # eyewhites_l1
        # eyewhites_l2
        # eyewhites_r1
        # eyewhites_r2
        # tongue
        # teeth
        # mouth_inside
        # eyebrow_l1
        # eyebrow_l2
        # eyebrow_r1
        # eyebrow_r2
        # mouth_line
        # emotion_line

    material_list = {}
    rig = isRigSelected(context)
    mat_hold = mat_holder_func(rig)
    try:
        materials = mat_hold.data.materials
        for mat in materials:
            try:
                if mat["ice_cube_material"]:
                    material_list[mat["ice_cube_material"]] = mat
            except KeyError:
                pass
    except:
        materials = "OUTDATED"
        box = layout.box()
        box.label(text= "OUTDATED RIG, SKIN TAB DISABLED", icon= 'ERROR')
        return{'FINISHED'}
    


    box = layout.box()
    box.label(text= "Skin Materials", icon= 'MATERIAL')
    b = box.row(align=True)
    b.scale_y=scale
    try:

        material_list['skin'].node_tree.nodes['Skin Tex']

        textures_box = b.box()
        textures_row = textures_box.row(align=True)
        textures_row.label(text="Skin Texture",icon='TEXTURE')
        if button_toggle(obj,textures_row,"texture_settings"):
            textures_row = textures_box.row(align=True)
            textures_row.prop(scene,"minecraft_username",text="Username")
            textures_row.operator("skin.download", text="", icon='IMPORT')
            textures_row = textures_box.row(align=True)
            textures_row.context_pointer_set("edit_image",material_list['skin'].node_tree.nodes['Skin Tex'].image)
            textures_row.operator("image.unpack" if material_list['skin'].node_tree.nodes['Skin Tex'].image.packed_file else "image.pack",
                    text="", icon="PACKAGE" if material_list['skin'].node_tree.nodes['Skin Tex'].image.packed_file else "UGLYPACKAGE")
            textures_row.prop(material_list['skin'].node_tree.nodes['Skin Tex'].image, "filepath", text="")
            textures_row.operator("image.reload", text="", icon='FILE_REFRESH')
            textures_row = textures_box.row(align=True)
            textures_row.label(text="Downloaded Skins:")
            textures_row = textures_box.row(align=True)
            wm = context.window_manager
            textures_row.template_icon_view(wm, "skins_folder")
            textures_row = textures_box.row(align=True)
            textures_row.operator("skin.apply", text="Apply Skin")
            textures_row.operator("skin.reset", text="Reset Skin")
            textures_row = textures_box.row(align=True)
            textures_row.operator("skin.delete", text="Delete Skin")
    except:
        pass
    b = box.row(align=True)
    b.scale_y=scale
    
    try:
        material_list['skin'].node_tree.nodes['color']

        sss_box = b.box()
        sss_row = sss_box.row(align=True)
        sss_row.label(text="SSS Options",icon='COLOR')
        if button_toggle(obj,sss_row,"sss_settings"):
            sss_row = sss_box.row(align=True)
            sss_col = sss_row.column(align=True)
            sss_col.prop(material_list['skin'].node_tree.nodes['color'].inputs[1], 'default_value', text="Auto SSS", slider=True)
            sss_col.prop(material_list['skin'].node_tree.nodes['color'].inputs[3], 'default_value', text="Sensitivity", slider=True)
            sss_col.prop(material_list['skin'].node_tree.nodes['color'].inputs[4], 'default_value', text="SSS", slider=True)  
            sss_col.prop(material_list['skin'].node_tree.nodes['color'].inputs[7], 'default_value', text="Radius", slider=False)
            sss_col.prop(material_list['skin'].node_tree.nodes['color'].inputs[2], 'default_value', text="Skin Color", slider=True)
            sss_col.prop(material_list['skin'].node_tree.nodes['color'].inputs[5], 'default_value', text="SSS Color", slider=True)
    except:
        pass

def material_eyes_ui(self,context,layout,face,scale):
    obj = context.object

    material_list = {}
    rig = isRigSelected(context)
    mat_hold = mat_holder_func(rig)
    try:
        materials = mat_hold.data.materials
        for mat in materials:
            try:
                if mat["ice_cube_material"]:
                    material_list[mat["ice_cube_material"]] = mat
            except KeyError:
                pass
    except:
        materials = "OUTDATED"
        box = layout.box()
        box.label(text= "OUTDATED RIG, EYE TAB DISABLED", icon= 'ERROR')
        return{'FINISHED'}

    
    box = layout.box()
    box.label(text= "Eye Materials", icon= 'MATERIAL')
    b = box.row(align=True)
    b.scale_y=scale
    try:
        material_list['eyes'].node_tree.nodes['eyenode']


        iris_box = b.box()
        iris_row = iris_box.row(align=True)
        iris_row.label(text="Iris",icon='NODE_MATERIAL')
        if button_toggle(obj,iris_row,"mat_set_iris"):
            iris_row = iris_box.row(align=True)
            gradient_thing = iris_row
            gradient_thing.prop(obj,"gradient_color_eye",expand=True)
            if obj.get("upgraded_ui"):
                gradient_thing.enabled = False
            if obj.get("gradient_color_eye") == 0:
                iris_row = iris_box.row(align=True)
                iris_col = iris_row.column(align=True)
                iris_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[0], 'default_value', text="", slider=True)
                iris_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[1], 'default_value', text="", slider=True)
                iris_col = iris_row.column(align=True)
                iris_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[2], 'default_value', text="", slider=True)
                iris_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[3], 'default_value', text="", slider=True)


            elif obj.get("gradient_color_eye") == 1:
                iris_row = iris_box.row(align=True)
                boxlayout = iris_row.box().column(align=True)
                boxlayout.label(text= "Right Eye Gradient", icon= 'MATERIAL_DATA')
                reg1 = material_list['eyes'].node_tree.nodes['Gradient Right']
                boxlayout.template_color_ramp(reg1, "color_ramp", expand=True)
                iris_row = iris_box.row(align=True)
                boxlayout = iris_row.box().column(align=True)
                boxlayout.label(text= "Left Eye Gradient", icon= 'MATERIAL_DATA')
                leg1 = material_list['eyes'].node_tree.nodes['Gradient Left']
                boxlayout.template_color_ramp(leg1, "color_ramp", expand=True)


            elif obj.get("gradient_color_eye") == 2:
                iris_row = iris_box.row(align=True)
                iris_sub_box = iris_row.box()
                iris_col = iris_sub_box.column(align=False)
                iris_col.template_node_view(material_list['eyes'].node_tree,material_list['eyes'].node_tree.nodes['image_eyes_overlay_1'],material_list['eyes'].node_tree.nodes['image_eyes_overlay_1'].inputs[6])
                iris_col.prop(material_list['eyes'].node_tree.nodes['image_eyes_overlay_1'].inputs[7],'default_value',text="Overlay Color R",slider=True)
                iris_col.prop(material_list['eyes'].node_tree.nodes['image_eyes_overlay_2'].inputs[7],'default_value',text="Overlay Color L",slider=True)

            
            iris_row = iris_box.row(align=True)
            iris_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[4], 'default_value', text="Specular", slider=True)
            iris_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[5], 'default_value', text="Roughness", slider=True)
            iris_row = iris_box.row(align=True)
            iris_row.prop(obj, "toggleemission", text = "Toggle Emission",toggle=True)
            if obj.get("toggleemission") == True:
                iris_row = iris_box.row(align=True)
                iris_row.prop(obj, "emissioneye", text = "")
                iris_row = iris_box.row(align=True)
                iris_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[22], 'default_value', text="Real Light", slider=True)
                iris_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[23], 'default_value', text="Texture Light", slider=True)
        b = box.row(align=True)
        b.scale_y=scale
        pupil_box = b.box()
        pupil_row = pupil_box.row(align=True)
        pupil_row.label(text="Pupil",icon='NODE_MATERIAL')
        if button_toggle(obj,pupil_row,"mat_set_pupil"):
            pupil_row = pupil_box.row(align=True)
            pupil_row.prop(obj, "togglepupil", toggle=True, text = "Toggle Pupil")
            if obj.get("togglepupil"):
                pupil_row = pupil_box.row(align=True)
                pupil_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[11], 'default_value', text="", slider=True)
                pupil_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[26], 'default_value', text="", slider=True)
                pupil_row = pupil_box.row(align=True)
                pupil_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[10], 'default_value', text="Pupil Size",slider=True)
                pupil_row = pupil_box.row(align=True)
                pupil_upgraded = pupil_row
                pupil_upgraded.prop(obj,"pupil_bright",text="Pupil Bright")
                pupil_upgraded.prop(obj,"flip_pupil_bright",text="Flip Pupil Bright")
                if obj.get("upgraded_ui"):
                    pupil_upgraded.enabled = False
                pupil_row = pupil_box.row(align=True)
                pupil_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[24], 'default_value',index=0, text="Pupil Size X", slider=False)
                pupil_row.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[24], 'default_value',index=1, text="Pupil Size Y", slider=False)
        b = box.row(align=True)
        b.scale_y=scale
        sparkle_box = b.box()
        sparkle_row = sparkle_box.row(align=True)
        sparkle_row.label(text="Sparkles",icon='NODE_MATERIAL')
        if button_toggle(obj,sparkle_row,"mat_set_sparkle"):
            material_list = {}
            rig = isRigSelected(context)
            mat_hold = mat_holder_func(rig)
            materials = mat_hold.data.materials
            for mat in materials:
                try:
                    if mat["ice_cube_material"]:
                        material_list[mat["ice_cube_material"]] = mat
                except KeyError:
                    pass

            sparkle_row = sparkle_box.row(align=True)
            sparkle_col = sparkle_row.column(align=True)
            sparkle_col.prop(obj, "togglesparkle1", toggle = True, text = "Toggle Sparkle 1")
            sparkle_1_sub = sparkle_col.row(align=True)
            sparkle_col = sparkle_row.column(align=True)
            sparkle_col.prop(obj, "togglesparkle2", toggle = True, text = "Toggle Sparkle 2")
            sparkle_2_sub = sparkle_col.row(align=True)
            if obj.get("togglesparkle1"):
                sparkle_1_sub_col = sparkle_1_sub.column(align=True)
                sparkle_1_sub_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[14], 'default_value', text="Sparkle 1 Size", slider=True)
                sparkle_1_sub_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[15], 'default_value',index=0, text="X", slider=False)
                sparkle_1_sub_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[15], 'default_value',index=1, text="Y", slider=False)
            sparkle_col = sparkle_row.column(align=True)
            if obj.get("togglesparkle2"):
                sparkle_2_sub_col = sparkle_2_sub.column(align=True)
                sparkle_2_sub_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[18], 'default_value', text="Sparkle 2 Size", slider=True)
                sparkle_2_sub_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[19], 'default_value',index=0, text="X", slider=False)
                sparkle_2_sub_col.prop(material_list['eyes'].node_tree.nodes['eyenode'].inputs[19], 'default_value',index=1, text="Y", slider=False)
    except:
        pass

def material_misc_ui(self,context,layout,face,scale):
    obj = context.object

    material_list = {}
    rig = isRigSelected(context)
    mat_hold = mat_holder_func(rig)
    try:
        materials = mat_hold.data.materials
        for mat in materials:
            try:
                if mat["ice_cube_material"]:
                    material_list[mat["ice_cube_material"]] = mat
            except KeyError:
                pass
    except:
        materials = "OUTDATED"
        box = layout.box()
        box.label(text= "OUTDATED RIG, MISC TAB DISABLED", icon= 'ERROR')
        return{'FINISHED'}

    
    box.label(text= "Misc Materials", icon= 'MATERIAL')
    b = box.row(align=True)
    b.scale_y=scale
    main_box = b.box()
    main_row = main_box.row(align=True)
    try:

        material_list['eyewhites_r1'].node_tree.nodes['Principled BSDF']
        material_list['eyewhites_r2'].node_tree.nodes['Principled BSDF']
        material_list['eyewhites_l1'].node_tree.nodes['Principled BSDF']
        material_list['eyewhites_l2'].node_tree.nodes['Principled BSDF']

        main_row.label(text="Eyewhites:")
        main_row = main_box.row(align=True)
        main_col = main_row.column(align=True)
        main_col.prop(material_list['eyewhites_r1'].node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
        main_col.prop(material_list['eyewhites_r2'].node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
        main_col.prop(material_list['eyewhites_l1'].node_tree.nodes['Principled BSDF'].inputs[7], 'default_value', text="Specular", slider=True)
        main_col = main_row.column(align=True)
        main_col.prop(material_list['eyewhites_l1'].node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
        main_col.prop(material_list['eyewhites_l2'].node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
        main_col.prop(material_list['eyewhites_l1'].node_tree.nodes['Principled BSDF'].inputs[9], 'default_value', text="Roughness", slider=True)
        main_row = main_box.row(align=True)
        main_row = main_box.row(align=True)
    except:
        pass
    try:
        material_list['eyebrow_r1'].node_tree.nodes['Principled BSDF']
        material_list['eyebrow_r2'].node_tree.nodes['Principled BSDF']
        material_list['eyebrow_l1'].node_tree.nodes['Principled BSDF']
        material_list['eyebrow_l2'].node_tree.nodes['Principled BSDF']


        main_row.label(text="Eyebrows:")
        main_row = main_box.row(align=True)
        main_col = main_row.column(align=True)
        main_col_row = main_col.row(align=True)
        main_col_row.prop(material_list['eyebrow_r2'].node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
        main_col_row.prop(material_list['eyebrow_r1'].node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
        main_col = main_row.column(align=False)
        main_col_row = main_col.row(align=True)
        main_col_row.prop(material_list['eyebrow_l1'].node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
        main_col_row.prop(material_list['eyebrow_l2'].node_tree.nodes['Principled BSDF'].inputs[0], 'default_value', text="", slider=True)
        main_row = main_box.row(align=True)
        main_row = main_box.row(align=True)
    except:
        pass
    main_row.label(text="Misc Face:")
    main_row = main_box.row(align=True)
    main_col_text = main_row.column(align=True)
    main_col = main_row.column(align=True)
    misc_mats = ['tongue','teeth','mouth_inside','mouth_line','emotion_line']
    misc_mats_names = {
        'tongue': {"name":"Tongue:","node":"Tongue Color","input":7},
        'teeth': {"name":"Teeth:","node":"Principled BSDF","input":0},
        'mouth_inside': {"name":"Mouth Inside:","node":"Principled BSDF","input":0},
        'mouth_line': {"name":"Cartoon Mouth:","node":"Principled BSDF","input":0},
        'emotion_line': {"name":"Emotion Line:","node":"Principled BSDF","input":0}
    }
    for mat in misc_mats:
        try:
            main_col.prop(material_list[mat].node_tree.nodes[misc_mats_names[mat]['node']].inputs[misc_mats_names[mat]['input']], 'default_value', text="", slider=True)
            main_col_text.label(text=misc_mats_names[mat]['name'])
        except:
            pass


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